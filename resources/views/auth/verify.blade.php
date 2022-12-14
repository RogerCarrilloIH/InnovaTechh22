@extends('layouts.signInUp')

@section('content')

<h2>{{ __('Verify Your Email Address') }}</h2>

@if (session('resent'))
    <div class="alert alert-success" role="alert">
        {{ __('A fresh verification link has been sent to your email address.') }}
    </div>
@endif

<div class="inputForm">
    {{ __('Before proceeding, please check your email for a verification link.') }}
    {{ __('If you did not receive the email') }},
    <form class="d-inline" method="POST" action="{{ route('verification.resend') }}">
        @csrf
        <a type="submit" class="btn btn-link p-0 m-0 align-baseline">{{ __('click here to request another') }}</a>.
    </form>
</div>

@endsection