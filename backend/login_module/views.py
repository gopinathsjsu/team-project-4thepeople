from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Customer


def user_signup(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        email_address = request.POST["email_address"]

        # account check
        if Customer.objects.filter(username=user_name) or Customer.objects.filter(email=email_address):
            messages.warning(request, "Account already exist, please Login to continue")
            redirect('user_signin')
        else:
            password = request.POST['password']
            contact_number = request.POST['contact']
            password_hash = make_password(password)

            customer = Customer(username=user_name,
                                password=password_hash,
                                email=email_address,
                                contact=contact_number)
            customer.save()
            messages.info(request, "Account Created Successfully, please Login to continue")
            redirect('user_signin')

    return render(request, 'login/user_signup.html', {})


def user_sigin(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        if not len(username):
            messages.warning(request, "Username field is empty")
            redirect('user_signin')
        elif not len(password):
            messages.warning(request, "Password field is empty")
            redirect('user_signin')
        else:
            pass

        if Customer.objects.filter(username=username):
            user = Customer.objects.filter(username=username)[0]
            password_hash = user.password
            res = check_password(password, password_hash)

            if res == 1:
                request.session['username'] = username
                request.session['type'] = 'user'
                return render(request, 'hotel/hotel_dashboard.html', {})
            else:
                messages.warning(request, "Username or password is incorrect")
                redirect('user_signin')
        else:
            messages.warning(request, "No, Account exist for the given Username")
            redirect('user_signin')

    return render(request, 'login/user_signin.html', {})


def manager_signin(request):
    return render(request, "login/logout.html", {})


def logout(request):
    if request.session.get('username', None):
        del request.session['username']
        del request.session['type']
        return render(request, "login/logout.html", {})
    else:
        return render(request, "login/user_signup.html", {})
