from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Room, Contact
from datetime import date
import datetime
import calendar
from abc import ABC, abstractmethod


# API View here
class CustomersAPI(APIView):
    def get(self, request):
        return Response(
            {"status": "success",
             "data": "Successful Get Request"
            }, status=status.HTTP_200_OK)


#Dynamic pricing - Strategy
class Strategy(ABC):
    @abstractmethod
    def pricingScheme(self):
        pass

class weekdayPricing(Strategy):
    def pricingScheme(self):
        print("weekday no inc in price")
        percentageIncrease = 0
        return percentageIncrease

class weekendPricing(Strategy):
    def pricingScheme(self):
        print("weekend rise in price")
        percentageIncrease = 5
        return percentageIncrease

class Default(Strategy):
    def pricingScheme(self) -> int:
        return 0

class DynamicPricing():

    strategy : Strategy

    def setStrategy(self, strategy: Strategy = None) -> None:
        self.strategy = strategy

    def executeStrategy(self) -> int:
        result = self.strategy.pricingScheme()
        return result;

# Room API
class RoomDetails(APIView):
    def get(self, request):
        room_details = Room.objects.all().values()
        api_response = {}
        today = date.today()
        today_date = today.strftime("%d %m %y")
        day  = datetime.datetime.strptime(today_date, "%d %m %y").weekday()
        context = DynamicPricing()
        if 0 <= day < 4:
            context.setStrategy(weekdayPricing())
        else:
            context.setStrategy(weekendPricing())
        dynamic_pricing_percentage = context.executeStrategy()
        for objects in room_details:
            if objects['is_available']:
                objects['price'] = objects['price'] + (objects['price'] * dynamic_pricing_percentage)
                api_response[objects['room_no']] = {
                    'room_no' : objects['room_no'],
                    'room_type' : objects['room_type'],
                    'price' : objects['price'],
                    'is_available' : objects['is_available'],
                    'no_of_days_advance' : objects['no_of_days_advance'],
                    'room_image' : objects['room_image'],
                    'start_date' : objects['start_date']
                }

        return Response({"status": "success",
                             "room_detail": api_response},
                            status=status.HTTP_200_OK)

class ContactViews(APIView):
    def get(self, request):
        all_contact_objects = Contact.objects.all().values()
        api_responses = {}
        for objects in all_contact_objects:
            api_responses[objects['name']] = {
                'name' : objects['name'],
                'email' : objects['email'],
                'message' : objects['message']
            }
        return Response({"status" : "success", "contact_data":api_responses}, status=status.HTTP_200_OK)
