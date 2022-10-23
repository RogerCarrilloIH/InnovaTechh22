@extends('layouts.signInUp')

@section('content')

<h2>{{ __('Reset Password') }}</h2>

<form method="POST" action="{{ route('password.update') }}">
    @csrf

    <input type="hidden" name="token" value="{{ $token }}">
    <div class="inputForm">
        <label for="email">{{ __('E-Mail Address') }}</label>
        <input id="email" type="email" class="@error('email') is-invalid @enderror"
                name="email" value="{{ $email ?? old('email') }}" required autocomplete="email" autofocus>
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
        <button type="submit">{{ __('Reset Password') }}</button>
    </div>
</form>

@endsection
