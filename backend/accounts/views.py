from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from .decorators import unauthenticated_user, admin_only
from accounts.models import UserProfile
from booking.models import Booking, Room
from django.contrib.auth.models import User
from .serializer import AccountSerializer
from rest_framework.permissions import IsAuthenticated
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
    bookings_count = Booking.objects.count()
    rooms_count = Room.objects.count()
    upcoming_revenue = 0
    package_types = {"Delux": 0, "Suite": 0, "Studio": 0}
    for booking in Booking.objects.all():
        if booking.booking_room_type in package_types:
            package_types[booking.booking_room_type] += 1
        else:
            package_types[booking.booking_room_type] = 1

        upcoming_revenue += int(booking.amount)

    context = {"bookings_count": bookings_count,
               "rooms_count": rooms_count,
               "upcoming_revenue": upcoming_revenue,
               "Studio": package_types["Studio"],
               "StudioCount": int(package_types["Studio"] / rooms_count),
               "Suite": package_types["Suite"],
               "SuiteCount": int(package_types["Suite"] / rooms_count),
               "Delux": package_types["Delux"],
               "DeluxCount": int(package_types["Delux"] / rooms_count),
               }
    return render(request, 'hotel/dashboard.html', context)


@login_required(login_url='login')
@admin_only
def bookings_list(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'hotel/booking_list.html', context)


@login_required(login_url='login')
@admin_only
def create_booking(request):
    context = {}
    return render(request, 'hotel/booking_create.html', context)


@login_required(login_url='login')
@admin_only
def edit_booking(request, pk):
    context = {}
    return render(request, 'hotel/booking_edit.html', context)


@login_required(login_url='login')
@admin_only
def delete_booking(request, pk):
    context = {}
    return render(request, 'hotel/booking_delete.html', context)


@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'hotel/user_page.html', context)


########################################################################################################################
# API Views

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
                status=status.HTTP_200_OK)


class UsersProfileAPI(APIView):
    @staticmethod
    def post(request):
        user_name = request.POST.get('username')
        if user_name:
            user_detail = User.objects.filter(username=user_name)[0]
            user_profile = UserProfile.objects.filter(user=user_detail)[0]
            user_record = {
                "username": user_profile.user.username,
                "total_bookings": user_profile.total_bookings,
                "total_reward_points": user_profile.total_rewards,
                "level": user_profile.user_level
            }
            return Response({
                "status": "success",
                "data": user_record},
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "message": "username is required"},
                status=status.HTTP_400_BAD_REQUEST)


class ManageHotelAccountView(APIView):
    # permission_classes = (IsAuthenticated,)
    @staticmethod
    def post(request, *args, **kwargs):
        try:
            user_name = request.POST.get('username')
            reward_points_booking = request.POST.get('reward_points')
            user_detail = User.objects.filter(username=user_name)[0]
            user_profile = UserProfile.objects.filter(user=user_detail)[0]
            user_profile.total_bookings += 1
            user_profile.total_rewards += int(reward_points_booking)

            if 5 < user_profile.total_bookings < 10:
                user_profile.user_level = "Gold"
            elif user_profile.total_bookings > 10:
                user_profile.user_level = "Diamond"

            user_profile.save()

            return Response({
                "status": "success",
                "message": "Account Details Added Successfully"},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)
