@extends('layouts.signInUp')

@section('content')

<h2>Regístrate</h2>
<form method="POST" action="{{ route('register') }}">
    @csrf
    <div class="inputForm">
        <label for="name">{{ __('Name') }}</label>
        <input id="name" type="text" class="@error('name') is-invalid @enderror"
                name="name" value="{{ old('name') }}" required autocomplete="name" autofocus>
        @error('name')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
        @enderror
    </div>
    <div class="inputForm">
        <label for="email">{{ __('E-Mail Address') }}</label>
        <input id="email" type="email" class="@error('email') is-invalid @enderror"
                name="email" value="{{ old('email') }}" required autocomplete="email">
        @error('email')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
        @enderror
    </div>
    <div class="inputForm">
        <label for="password">{{ __('Password') }}</label>
        <input id="password" type="password" class="@error('password') is-invalid @enderror"
                name="password" required autocomplete="new-password">
        @error('password')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
        @enderror
    </div>
    <div class="inputForm">
        <label for="password-confirm">{{ __('Confirm Password') }}</label>
        <input id="password-confirm" type="password" name="password_confirmation"
                required autocomplete="new-password">
    </div>
    <div class="inputForm">
        <button type="submit">{{ __('Register') }}</button>
    </div>
    <div class="inputForm">
        <p>¿Ya tienes una cuenta? <a href="{{ route('login') }}"> Inicia sesión</a></p>
    </div>
</form>

@endsection
