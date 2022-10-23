import gspread 
import time 
from datetime import datetime 
import re 
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import pandas as pd


datos = pd.read_csv('set_datos\set1.csv', header= 0)
#PATH = '../Scrapeo/chromedriver' #driver = webdriver.Chrome(PATH) #driver.get("https://www.google.com") 
class ScrapearGMaps: 
    data = {} 
    worksheet = {} 
    def __init__(self): 
        # Ruta de ChromeDriver 
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\LENOVO\OneDrive\Documents\Nueva carpeta (4)\chromedriver_win32\chromedriver.exe") 
       

        now = datetime.now() 
        today = now.strftime("%Y-%m-%d") 
        gc = gspread.service_account(filename='qualitytech-366208-8a5676b951dc.json') 
        # Abrir por titulo 
        sh = gc.open("dataset1") 

        # Seleccionar primera hoja 
        self.worksheet = sh.get_worksheet(0) 
    def scroll_the_page(self, i): 
        try: 
            # section_loading = self.driver.find_element_by_class_name("section-loading") 
            section_loading = self.driver.find_element(By.CLASS_NAME, "section-loading") 
            while True: 
                # if i >= len(self.driver.find_elements(By.CLASS_NAME, "place-result-container-place-link")): 
                if i >= len(self.driver.find_elements(By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')): 
                    actions = ActionChains(self.driver) 
                    actions.move_to_element(section_loading).perform() 
                    time.sleep(2) 
                else: 
                    break 
        except: 
            pass 
    
      
        
        
        
    def get_name(self): 
        try: 
            return self.driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1").text 
        except: return "NULL" 
    def get_address(self): 
        try: 
            return self.driver.find_element(By.CSS_SELECTOR, "[data-tooltip='Copiar la dirección']").text 
            # return self.driver.find_element(By.CSS_SELECTOR, "[data-item-id='address']").text 
        except: 
            return "NULL" 
    def get_phone(self): 
        try: 
            return self.driver.find_element(By.CSS_SELECTOR, "[data-tooltip='Copiar el número de teléfono']").text 
        except: return "NULL" 
    def get_website(self): 
        try: 
            return self.driver.find_element(By.CSS_SELECTOR, "[data-tooltip='Abrir el sitio web']").text 
        except: 
            return "NULL" 
    def get_review_number(self): 
        try: 
            return self.driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[2]").text 
        except: 
            return "NULL" 
    def get_qualification(self): 
        try: 
            return self.driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[1]").text 
        except: 
            return "NULL" 
    def get_category(self): 
        try: 
            return self.driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/span[1]").text 
        except: 
            return "NULL" 
    def get_geocoder(self, url_location): # gets geographical lat/long coordinate
        
        try: 
            time.sleep(4)
            coords = re.search(r"!3d-?\d\d?\.\d{4,8}!4d-?\d\d?\.\d{4,8}", url_location).group() 
            coord = coords.split('!3d')[1] 
            return tuple(coord.split('!4d')) 
        except (TypeError, AttributeError): 
            return ("NULL", "NULL") 
   
    
    def scrape(self, url): 
        try: 
            self.driver.get(url) 
           
            name = self.get_name() 
            address = self.get_address() 
            phone_number = self.get_phone() 
            website = self.get_website() 
            review_number = self.get_review_number() 
            qualificacion = self.get_qualification() 
            category = self.get_category() 
            time.sleep(4) 
            coords = self.get_geocoder(self.driver.current_url) 
            email = "NULL" 
            
            print([name, address, phone_number, coords[0], coords[1], website, email, review_number, qualificacion, category]) 
            
            
            row_index = len(self.worksheet.col_values(1)) + 1 
            self.worksheet.update('A'+str(row_index), name) 
            self.worksheet.update('B'+str(row_index), address) 
            self.worksheet.update('C'+str(row_index), phone_number) 
            self.worksheet.update('D'+str(row_index), coords[0]) 
            self.worksheet.update('E'+str(row_index), coords[1]) 
            self.worksheet.update('F'+str(row_index), website) 
            self.worksheet.update('G'+str(row_index), email) 
            self.worksheet.update('H'+str(row_index), review_number) 
            self.worksheet.update('I'+str(row_index), qualificacion) 
            self.worksheet.update('J'+str(row_index), category) 
            # element = self.driver.find_element(By.XPATH, "//button[.//span[text()='Volver a los resultados']]") 
            # time.sleep(2) 
            # element.click() 
            time.sleep(3) 
                
        except Exception as e: 
            print(e) 
         #self.driver.quit() 
        Delete =self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/a")
        Delete.click()
        time.sleep(2)
        return(self.data) 
    



datos['name_dir']= datos['NombComp']+', '+datos['Estado']+', '+datos['MunicipioDel']
dir = ""
for i in range(len(datos['name_dir'])):
    dir = datos['name_dir'].iloc[i]
    url = "https://www.google.es/maps/search/"+dir.replace(" ", "+")+"/"
    print(gmaps.scrape(url))
    
    


