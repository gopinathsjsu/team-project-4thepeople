from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Room, Booking
from accounts.models import UserProfile
from .decorators import DynamicPricing, holidayPricing, weekendPricing, weekdayPricing
import datetime
import holidays
from django.contrib.auth.models import User


# Room API
class RoomDetails(APIView):
    def get(self, request, datestring):
        try:
            us_holidays = holidays.US()
            room_details = Room.objects.all().values()
            api_response = {}
            date_time_obj = datetime.datetime.strptime(datestring, '%Y-%m-%d')
            day = date_time_obj.weekday()
            context = DynamicPricing()
            if datestring in us_holidays:
                context.setStrategy(holidayPricing())
            elif 0 <= day < 4:
                context.setStrategy(weekdayPricing())
            else:
                context.setStrategy(weekendPricing())
            dynamic_pricing_percentage = context.executeStrategy()
            for objects in room_details:
                if objects['is_available']:
                    objects['price'] = objects['price'] + (objects['price'] * dynamic_pricing_percentage * 0.01)
                    api_response[objects['room_no']] = {
                        'room_no': objects['room_no'],
                        'room_type': objects['room_type'],
                        'base_price': objects['price'],
                        'room_location': objects['room_location'],
                        'is_available': objects['is_available'],
                        'no_of_days_advance': objects['no_of_days_advance'],
                        'room_image': objects['room_image'],
                        'start_date': objects['start_date'],
                        'room_amenities': objects['room_amenities']
                    }
            return Response({"status": "success",
                             "room_detail": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Error",
                             "room_detail": e},
                            status=status.HTTP_400_BAD_REQUEST)


class BookRoom(APIView):
    # Search room type, location, date and price range
    def post(self, request):
        try:
            request_room_no = request.POST.get('room_no')
            request_room_id = Room.objects.get(room_no=request_room_no)

            user_name = request.POST.get('username')
            request_user_id = User.objects.get(username=user_name)

            request_number_of_guests = request.POST.get('number_of_guests')
            request_booking_amenities = request.POST.get('booking_amenities')

            request_start_day = request.POST.get('start_day')
            request_end_day = request.POST.get('end_day')
            total_amount = request.POST.get('room_price')

            if Booking.objects.filter(room_no=request_room_id).count()==0:
                booking_record = Booking(room_no=request_room_id,
                                         user_id=request_user_id,
                                         number_of_guests=int(request_number_of_guests),
                                         booking_amenities=request_booking_amenities,
                                         start_day=request_start_day,
                                         end_day=request_end_day,
                                         amount=total_amount
                                         )
                booking_record.save()
                return Response({
                    "status": "error",
                    "message": "room is already booked by other customer"},
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "message": "room is already booked by other customer"},
                    status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)


class SearchRoom(APIView):
    # Search room type, location, date and price range
    @staticmethod
    def post(request):
        try:
            user_name = request.POST.get('username')
            location = request.POST.get('location')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            price_range_first = request.POST.get('price_start')
            price_range_end = request.POST.get('price_end')

            room_records = {}
            all_room_records = Room.objects.all()
            context = DynamicPricing()

            if location:
                all_room_records = all_room_records.filter(room_location=location)


            if start_date:
                all_room_records = all_room_records.filter(start_date__lte=start_date)

                date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                us_holidays = holidays.US()
                day = date_time_obj.weekday()

                if start_date in us_holidays:
                    context.setStrategy(holidayPricing())
                elif 0 <= day < 4:
                    context.setStrategy(weekdayPricing())
                else:
                    context.setStrategy(weekendPricing())

                dynamic_pricing_percentage = context.executeStrategy()
                for room in all_room_records:
                    room.price = room.price + (room.price * dynamic_pricing_percentage * 0.01)

            if price_range_first and price_range_end:
                all_room_records = all_room_records.filter(price__gte=price_range_first, price__lte=price_range_end)
            elif price_range_first:
                all_room_records = all_room_records.filter(price__gte=price_range_first)

            if user_name:
                user_detail = User.objects.filter(username=user_name)[0]
                user_profile = UserProfile.objects.filter(user=user_detail)[0]
                print(user_profile)
                print(user_profile.user_level)

                if user_profile.user_level == "Diamond":
                    for room in all_room_records:
                        room.price = room.price - 50
                elif user_profile.user_level == "Gold":
                    for room in all_room_records:
                        room.price = room.price - 30

            for room in all_room_records:
                room_records[room.room_no] = {
                    "room_no": room.room_no,
                    "room_type": room.room_type,
                    "room_amenities": room.room_amenities,
                    "price": room.price,
                    "start_date": room.start_date,
                    "room_location": room.room_location,
                    "room_image": room.room_image
                }

            return Response({
                "status": "success",
                "data": room_records},
                status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)
