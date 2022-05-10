from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from .decorators import unauthenticated_user, admin_only
from accounts.models import UserProfile
from accounts.forms import CreateUserForm
from booking.models import Booking, Room
from booking.forms import BookingForm, RoomForm
from django.contrib.auth.models import User
from django.db.models import Q
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


########################################################################################################################

@login_required(login_url='login')
@admin_only
def home(request):
    bookings_count = Booking.objects.count()
    rooms_count = Room.objects.count()
    upcoming_revenue = 0
    package_types = {"Deluxe": 0, "Suite": 0, "Studio": 0}
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
               "Suite": package_types["Suite"],
               "Deluxe": package_types["Deluxe"],
               }
    return render(request, 'hotel/dashboard.html', context)


########################################################################################################################
# Bookings

@login_required(login_url='login')
@admin_only
def bookings_list(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    bookings = Booking.objects.filter(
        Q(booking_location__contains=search_query),
        Q(booking_room_type__contains=search_query)
    )

    context = {
        'bookings': bookings,
        'search_query': search_query,
    }
    return render(request, 'hotel/booking_list.html', context)


@login_required(login_url='login')
@admin_only
def create_booking(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bookings_list')
        else:
            print(form.errors)
            messages.info(request, str(form.errors))

    context = {
        'form': form,
    }

    return render(request, 'hotel/booking_create.html', context)


@login_required(login_url='login')
@admin_only
def edit_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')

    context = {
        'booking': booking,
        'form': form,
    }

    return render(request, 'hotel/booking_edit.html', context)


@login_required(login_url='login')
@admin_only
def delete_booking(request, pk):
    booking = Booking.objects.get(id=pk)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')

    context = {
        'booking': booking,
    }
    return render(request, 'hotel/booking_delete.html', context)


########################################################################################################################
# Rooms

@login_required(login_url='login')
@admin_only
def rooms_list(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    rooms = Room.objects.filter(
        Q(room_no__contains=search_query),
        Q(room_type__contains=search_query)
    )

    context = {
        'rooms': rooms,
        'search_query': search_query,
    }
    return render(request, 'hotel/room_list.html', context)


@login_required(login_url='login')
@admin_only
def create_room(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('room_list')

    context = {
        'form': form,
    }

    return render(request, 'hotel/room_create.html', context)


@login_required(login_url='login')
@admin_only
def edit_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')

    context = {
        'rooms': room,
        'form': form,
    }

    return render(request, 'hotel/room_edit.html', context)


@login_required(login_url='login')
@admin_only
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('room_list')

    context = {
        'room': room,
    }
    return render(request, 'hotel/room_delete.html', context)


########################################################################################################################
# Customers

@login_required(login_url='login')
@admin_only
def customers_list(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    customers = UserProfile.objects.filter(
        Q(user_level__contains=search_query),
        Q(total_rewards__contains=search_query)
    )

    context = {
        'customers': customers,
        'search_query': search_query,
    }
    return render(request, 'hotel/customer_list.html', context)


@login_required(login_url='login')
@admin_only
def create_customer(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer_list')

    context = {
        'form': form,
    }

    return render(request, 'hotel/customer_create.html', context)


@login_required(login_url='login')
@admin_only
def edit_customer(request, pk):
    user_id = User.objects.get(id=pk)
    user = UserProfile.objects.get(id=user_id.id)
    form = RoomForm(instance=user)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('room_list')

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'hotel/customer_edit.html', context)


@login_required(login_url='login')
@admin_only
def delete_customer(request, pk):
    customer = User.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    context = {
        'customer': customer,
    }

    return render(request, 'hotel/customer_delete.html', context)


########################################################################################################################
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
    def delete(request, *args, **kwargs):
        try:
            user_name = request.POST.get('username')
            reward_points_booking = request.POST.get('reward_points')
            user_detail = User.objects.filter(username=user_name)[0]
            user_profile = UserProfile.objects.filter(user=user_detail)[0]
            user_profile.total_bookings -= 1
            user_profile.total_rewards -= int(reward_points_booking)

            if 5 < user_profile.total_bookings < 10:
                user_profile.user_level = "Gold"
            elif user_profile.total_bookings > 10:
                user_profile.user_level = "Diamond"

            user_profile.save()

            return Response({
                "status": "success",
                "message": "Account Details Modified Successfully"},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)

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
