from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from login_module.models import Customer


# API View here
class UsersSignupAPI(APIView):
    @staticmethod
    def post(request):
        user_name = request.POST["user_name"]
        email_address = request.POST["email_address"]

        # account check
        if Customer.objects.filter(username=user_name) or Customer.objects.filter(email=email_address):
            return Response({
                "status": "error",
                "message": "Account already exist, please Login to continue"},
                status=status.HTTP_409_CONFLICT)
        else:
            try:
                password = request.POST['password']
                contact_number = request.POST['contact']
                password_hash = make_password(password)

                customer = Customer(username=user_name,
                                    password=password_hash,
                                    email=email_address,
                                    contact=contact_number)
                customer.save()
                return Response({
                    "status": "success",
                    "message": "Account Created Successfully, please Login to continue"},
                    status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "status": "error",
                    "message": e},
                    status=status.HTTP_401_UNAUTHORIZED)


class UsersSigninAPI(APIView):
    @staticmethod
    def post(request):
        username = request.POST['user_name']
        password = request.POST['password']

        if not len(username):
            return Response(
                {"status": "error",
                 "data": "Username Field is Empty"
                 }, status=status.HTTP_401_UNAUTHORIZED)
        elif not len(password):
            return Response(
                {"status": "error",
                 "data": "Password Field is Empty"
                 }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            pass

        if Customer.objects.filter(username=username):
            user = Customer.objects.filter(username=username)[0]
            password_hash = user.password
            res = check_password(password, password_hash)

            if res == 1:
                return Response({
                    "status": "success",
                    "message": "Valid"},
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "message": "Username or Password is Incorrect"},
                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                "status": "error",
                "message": "No Account exist for the given Username"},
                status=status.HTTP_401_UNAUTHORIZED)







