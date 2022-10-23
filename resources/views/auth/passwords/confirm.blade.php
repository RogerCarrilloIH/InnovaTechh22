@extends('layouts.signInUp')

@section('content')

<h2>{{ __('Confirm Password') }}</h2>

<div class="inputForm">
    {{ __('Please confirm your password before continuing.') }}
</div>

<form method="POST" action="{{ route('password.confirm') }}">
    @csrf

    <div class="inputForm">
        <label for="password">{{ __('Password') }}</label>
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
        <button type="submit">{{ __('Confirm Password') }}</button>
    </div>
</form>

@endsection
