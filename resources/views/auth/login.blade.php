@extends('layouts.signInUp')

@section('content')

<h2>Iniciar sesión</h2>
<form method="POST" action="{{ route('login') }}">
    @csrf
    <div class="inputForm">
        <label for="email">{{ __('E-Mail Address') }}</label>
        <input id="email" type="email" class="@error('email') is-invalid @enderror"
                name="email" value="{{ old('email') }}" required autocomplete="email" autofocus>
        @error('email')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
        @enderror
    </div>
    <div class="inputForm">
        <label for="password">{{__('Password') }}</label>
        <input id="password" type="password" class="@error('password') is-invalid @enderror"
                name="password" required autocomplete="current-password">
        @error('password')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
        @enderror
    </div>
    <div class="inputForm">
        @if (Route::has('password.request'))
            <a class="btn btn-link" href="{{ route('password.request') }}">
                {{ __('Forgot Your Password?') }}
            </a>
        @endif
    </div>
    <div class="inputForm">
        <button type="submit">{{ __('Login') }}</button>
    </div>
    <div class="inputForm">
        <p>¿No tienes una cuenta? <a href="{{ route('register') }}"> Regístrate aquí</a></p>
    </div>
</form>

@endsection
