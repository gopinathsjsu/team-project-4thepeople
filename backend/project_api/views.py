from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Room, Booking
from accounts.models import UserProfile
from .decorators import DynamicPricing, holidayPricing, weekendPricing, weekdayPricing
import datetime
import holidays
import copy
from django.contrib.auth.models import User


class BookRoom(APIView):
    @staticmethod
    def put(request):
        try:
            user_name = request.POST.get('username')
            request_room_no = request.POST.get('room_no')
            request_user_id = User.objects.get(username=user_name)

            # booking update details
            request_number_of_guests = request.POST.get('number_of_guests')
            request_booking_amenities = request.POST.get('booking_amenities')
            request_start_day = request.POST.get('start_day')
            request_end_day = request.POST.get('end_day')
            request_price = request.POST.get('room_price')

            if Booking.objects.count() != 0:
                # filtering results
                room_record = Room.objects.filter(room_no=request_room_no)
                booking_record = Booking.objects.filter(user_id=request_user_id).filter(room_no=room_record[0])

                if booking_record:
                    for record in booking_record:
                        record.number_of_guests = request_number_of_guests
                        record.booking_amenities = request_booking_amenities
                        record.amount = request_price
                        record.start_day = request_start_day
                        record.end_day = request_end_day
                        record.save()

                    return Response({
                        "status": "success",
                        "message": "Booking Successfully Updated"},
                        status=status.HTTP_200_OK)
                else:
                    return Response({
                        "status": "error",
                        "message": "No Booking Details Found"},
                        status=status.HTTP_200_OK)

            return Response({
                "status": "error",
                "message": "No Booking Details Found"},
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        try:
            user_name = request.POST.get('username')
            request_room_no = request.POST.get('room_no')
            request_user_id = User.objects.get(username=user_name)

            if Booking.objects.count() != 0:
                # filtering results
                room_record = Room.objects.filter(room_no=request_room_no)
                booking_record = Booking.objects.filter(user_id=request_user_id).filter(room_no=room_record[0])

                if booking_record:
                    booking_record.delete()
                    return Response({
                        "status": "success",
                        "message": "Booking Successfully Deleted"},
                        status=status.HTTP_200_OK)
                else:
                    return Response({
                        "status": "error",
                        "message": "No Booking Details Found"},
                        status=status.HTTP_200_OK)

            return Response({
                "status": "error",
                "message": "No Booking Details Found"},
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        try:
            request_room_no = request.POST.get('room_no')
            user_name = request.POST.get('username')
            request_user_id = User.objects.get(username=user_name)

            request_number_of_guests = request.POST.get('number_of_guests')
            request_booking_amenities = request.POST.get('booking_amenities')

            request_start_day = request.POST.get('start_day')
            request_end_day = request.POST.get('end_day')
            total_amount = request.POST.get('room_price')

            requested_booking_location = request.POST.get('booking_location')
            requested_room_type = request.POST.get('booking_room_type')

            booking_flag = False

            if Booking.objects.count() != 0:
                # filtering results
                room_record = Room.objects.filter(room_no=request_room_no)
                booking_record = Booking.objects.filter(room_no=room_record[0])

                for book_record in booking_record:
                    requested_start_date = datetime.datetime.strptime(request_start_day, '%Y-%m-%d')
                    requested_end_date = datetime.datetime.strptime(request_end_day, '%Y-%m-%d')

                    if book_record.start_day <= requested_start_date.date() <= book_record.end_day:
                        booking_flag = True

                    if book_record.start_day <= requested_end_date.date() <= book_record.end_day:
                        booking_flag = True

            if not booking_flag:
                request_room_id = Room.objects.get(room_no=request_room_no)
                booking_record = Booking(room_no=request_room_id,
                                         user_id=request_user_id,
                                         number_of_guests=int(request_number_of_guests),
                                         booking_location=requested_booking_location,
                                         booking_room_type=requested_room_type,
                                         booking_amenities=request_booking_amenities,
                                         start_day=request_start_day,
                                         end_day=request_end_day,
                                         amount=total_amount
                                         )
                booking_record.save()

                return Response({
                    "status": "success",
                    "message": "Booking Successfully Done"},
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "message": "Booking Already Exist for Room Number"},
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)


class BookingDetails(APIView):
    @staticmethod
    def post(request):
        try:
            # username is given
            user_name = request.POST.get('username')
            booking_records = Booking.objects.all()
            api_response = {}

            if user_name:
                for book_record in booking_records:
                    if book_record.user_id.username == user_name:
                        api_response[book_record.id] = {
                            "room_no": book_record.room_no.room_no,
                            "room_location": book_record.booking_location,
                            "room_type": book_record.booking_room_type,
                            "guests": book_record.number_of_guests,
                            "amenities": book_record.booking_amenities,
                            "start_day": book_record.start_day,
                            "end_day": book_record.end_day,
                            "total_amount": book_record.amount,
                            "booked_date": book_record.booked_on
                        }

                return Response({
                    "status": "success",
                    "data": api_response},
                    status=status.HTTP_200_OK)
            else:
                for book_record in booking_records:
                    api_response[book_record.id] = {
                        "room_no": book_record.room_no.room_no,
                        "room_location": book_record.booking_location,
                        "room_type": book_record.booking_room_type,
                        "guests": book_record.number_of_guests,
                        "amenities": book_record.booking_amenities,
                        "start_day": book_record.start_day,
                        "end_day": book_record.end_day,
                        "total_amount": book_record.amount,
                        "booked_date": book_record.booked_on
                    }

                return Response({
                    "status": "success",
                    "data": api_response},
                    status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "data": str(e)},
                status=status.HTTP_400_BAD_REQUEST)


class SearchRoom(APIView):
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
            pricing_records = {
                "new_price": {},
                "old_price": {}
            }
            all_room_records = copy.deepcopy(Room.objects.all())
            context = DynamicPricing()

            if location:
                all_room_records = all_room_records.filter(room_location=location)

            if start_date:
                # get records from booking table and check room details
                booked_rooms = Booking.objects.all()
                booked_map = {}

                for book_record in booked_rooms:
                    if book_record.room_no.room_no in booked_map:
                        booked_map[book_record.room_no.room_no].append({
                            "start_day": book_record.start_day,
                            "end_day": book_record.end_day
                        })
                    else:
                        booked_map[book_record.room_no.room_no] = [{
                            "start_day": book_record.start_day,
                            "end_day": book_record.end_day
                        }]

                all_room_records = all_room_records.filter(start_date__lte=start_date)

                remove_records = []
                for room_record in all_room_records:
                    if str(room_record.room_no) in booked_map:
                        all_records = booked_map[str(room_record.room_no)]
                        requested_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')

                        for index in all_records:
                            if index["start_day"] <= requested_start_date.date() <= index["end_day"]:
                                remove_records.append(str(room_record.room_no))

                all_room_records = all_room_records.exclude(room_no__in=remove_records)

                date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                us_holidays = holidays.US()
                day = date_time_obj.weekday()

                if start_date in us_holidays:
                    context.setStrategy(holidayPricing())
                    pricing_records["DynamicPricing"] = "Holiday"
                elif 0 <= day < 4:
                    context.setStrategy(weekdayPricing())
                    pricing_records["DynamicPricing"] = "Weekday"
                else:
                    context.setStrategy(weekendPricing())
                    pricing_records["DynamicPricing"] = "Weekend"

                dynamic_pricing_percentage = context.executeStrategy()

                for room in all_room_records:
                    pricing_records["old_price"][room.room_no] = room.price
                    pricing_records["IncreasedBy"] = dynamic_pricing_percentage
                    room.price = room.price + (room.price * dynamic_pricing_percentage * 0.01)
                    pricing_records["new_price"][room.room_no] = room.price

            if price_range_first and price_range_end:
                all_room_records = all_room_records.filter(price__gte=price_range_first, price__lte=price_range_end)
            elif price_range_first:
                all_room_records = all_room_records.filter(price__gte=price_range_first)

            if user_name:
                user_detail = User.objects.filter(username=user_name)[0]
                user_profile = UserProfile.objects.filter(user=user_detail)[0]

                if user_profile.user_level == "Diamond":
                    for room in all_room_records:
                        pricing_records["LoyalityDiscount"] = 50
                        room.price = room.price - 50
                elif user_profile.user_level == "Gold":
                    for room in all_room_records:
                        pricing_records["LoyalityDiscount"] = 30
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
                "pricing_data": pricing_records,
                "data": room_records},
                status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)
