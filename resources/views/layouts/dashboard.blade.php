<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>{{ config('app.name', 'Laravel') }}</title>

    <!-- plugins:css -->
    <link rel="stylesheet" href="{{ asset('dashboard/vendors/materialdesignicons/css/materialdesignicons.min.css') }}">
    <link rel="stylesheet" href="{{ asset('assets/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ asset('dashboard/vendors/datatables/css/dataTables.bootstrap5.min.css') }}">

    <!-- Layout styles -->
    <link rel="stylesheet" href="{{ asset('dashboard/css/style.css') }}">
    <link rel="stylesheet" href="{{ asset('dashboard/css/styleCustom.css') }}">
    @stack('styles')

    <link rel="shortcut icon" href="{{ asset('dashboard/images/favicon.ico') }}" />
</head>
<body>

    <div class="container-scroller">
        @include('layouts.inc.dashboard.navbar')
        
        <div class="container-fluid page-body-wrapper">
            @include('layouts.inc.dashboard.sidebar')
            <div class="main-panel">
                <div class="content-wrapper">
                    @yield('content')
                </div>
            </div>
        </div>
    </div>

    <!-- plugins:js -->
    <script src="{{ asset('assets/js/bootstrap.bundle.min.js') }}"></script>
    <script src="{{ asset('assets/js/jquery-3.6.1.min.js') }}"></script>
    <script src="{{ asset('dashboard/vendors/datatables/js/jquery.dataTables.min.js') }}"></script>
    <script src="{{ asset('dashboard/vendors/datatables/js/dataTables.bootstrap5.min.js') }}"></script>
    <script src="{{ asset('dashboard/vendors/sweetalert2/sweetalert2.all.min.js') }}"></script>
    <!-- Plugin js for this page -->
    <script src="{{ asset('dashboard/js/misc.js') }}"></script>
    <script src="{{ asset('dashboard/js/hoverable-collapse.js') }}"></script>
    <script src="{{ asset('dashboard/js/off-canvas.js') }}"></script>
    <!-- Custom js for this page -->
    <script src="{{ asset('dashboard/js/file-upload.js') }}"></script>
    <script src="{{ asset('dashboard/js/scriptCustom.js') }}"></script>
    @stack('script')
</body>
</html>