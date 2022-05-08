from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from accounts.models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login_page.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            add_to_group(form.cleaned_data.get('username'),
                         form.cleaned_data.get('password1'))
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register_page.html', context)


def add_to_group(username, password):
    user = authenticate(username=username, password=password)
    group = Group.objects.get(name='customer')
    user.groups.add(group)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    context = {}
    return render(request, 'hotel/dashboard.html', context)


@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'hotel/user_page.html', context)


# API View here
class UsersRegistrationAPI(APIView):
    @staticmethod
    def post(request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            add_to_group(form.cleaned_data.get('username'),
                         form.cleaned_data.get('password1'))

            return Response({
                "status": "success",
                "message": "Account Created Successfully, please Login to continue"},
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "message": form.errors},
                status=status.HTTP_400_BAD_REQUEST)


# API View here
class UsersSigninAPI(APIView):
    @staticmethod
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            user_profile = UserProfile.objects.filter(user=user)[0]
            return Response({
                "status": "success",
                "data": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "total_bookings": user_profile.total_bookings,
                    "total_rewards": user_profile.total_rewards,
                    "user_level": user_profile.user_level
                },
                "message": "AUTHORIZED"},
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "message": "UNAUTHORIZED"},
                status=status.HTTP_401_UNAUTHORIZED)
