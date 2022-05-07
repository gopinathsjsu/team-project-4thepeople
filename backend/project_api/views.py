from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Room, Contact
from .decorators import DynamicPricing, holidayPricing, weekendPricing, weekdayPricing
from datetime import date
import datetime
import holidays


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
                        'price': objects['price'],
                        'is_available': objects['is_available'],
                        'no_of_days_advance': objects['no_of_days_advance'],
                        'room_image': objects['room_image'],
                        'start_date': objects['start_date']
                    }
            return Response({"status": "success",
                             "room_detail": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Error",
                             "room_detail": e},
                            status=status.HTTP_400_BAD_REQUEST)

