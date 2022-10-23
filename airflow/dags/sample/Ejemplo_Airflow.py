from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "Airflow",
    "email": ["your.email@domain.com"],
    "start_date": days_ago(1),
    "email_on_failure": False,
}

with DAG(
    dag_id="data_pipeline-dag",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    schedule_interval=None,
    tags=["sample"],
) as dag:

    
    def _extract_process():
        from pyspark.sql import SparkSession
        from pyspark.sql import functions as F
        from pyspark.sql.types import StructType,StructField, StringType, IntegerType
        schema = StructType([ \
                StructField("package_id",IntegerType(),True), \
                StructField("package_name",StringType(),True), \
                StructField("date",StringType(),True), 
            ])
        spark = (
            SparkSession.builder.master("local[*]")
            .appName("airflow_app")
            .config("spark.executor.memory", "6g")
            .config("spark.driver.memory", "6g")
            .config("spark.driver.maxResultSize", "1048MB")
            .config("spark.port.maxRetries", "100")
            .getOrCreate()
        )

        df = spark.read.options(inferSchema="true", header="true").csv(
            "/home/airflow/data/CAT_TYPE_PACKAGE.csv"
        )
        
        df.write.option("schema",schema).parquet("/home/airflow/datalake/bronze_layer/extract_process.parquet")
        
        spark.stop()
        
    def _transform_process():

        from pyspark.sql import SparkSession
        from pyspark.sql import functions as F

        spark = (
            SparkSession.builder.master("local[*]")
            .appName("airflow_app")
            .config("spark.executor.memory", "6g")
            .config("spark.driver.memory", "6g")
            .config("spark.driver.maxResultSize", "1048MB")
            .config("spark.port.maxRetries", "100")
            .getOrCreate()
        )

        df = spark.read.load("/home/airflow/datalake/bronze_layer/*")

        df = df.select("package_name").dropDuplicates()

        df.write.parquet("/home/airflow/datalake/silver_layer/transform_process.parquet")

        spark.stop()
        

    
    extract_task = PythonOperator(task_id="extract_process", python_callable=_extract_process)
    
    
    flag_task = BashOperator(
    task_id='flag_task',
    bash_command='echo Done',)
    

    transform_task = PythonOperator(task_id="transform_process", python_callable=_transform_process)

    extract_task >> flag_task  >> transform_task
