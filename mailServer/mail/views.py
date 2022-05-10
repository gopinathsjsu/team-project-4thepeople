from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .decorators import  Observable, Observer


#mail notification after booking
class SendMailView(APIView):
    def post(self, request):

        recipient_mail = request.POST.get("mails")
        room_no = request.POST.get("room_no")
        start_day = request.POST.get("start_day")
        end_day = request.POST.get("end_day")
        total_amount = request.POST.get("total_amount")
        location  = request.POST.get("location")
        guest = request.POST.get("guest")
        username = request.POST.get("username")
        phone_no = request.POST.get("phone_no")

        #confirmation to customer after booking
        subject_mail = "Booking Confirmation from Paradise"
        msg_customer = "Booking confirmed for your stay at Paradise " + location + " Room No:" + room_no + " for " \
              + guest + " guest. We are looking forward for your stay from "+start_day+ " to "+ end_day + ". Your billing amount " + total_amount + ". Please show this mail at reception on arrival."

        #mail to hotel  after booking confirmation
        subject_mail_manager= "New Booking Confirmation from Customer "+username + " .Room Number : "+room_no
        msg_manager = "Booking confirmed by customer at" + location + " Room No:" + room_no + " ,number of guests " \
              + guest + " guest. The days booked by customer "+start_day+ " to "+ end_day + ". Please do the necessary arrangements for customer."

        subject = Observable()
        observer1 = Observer(subject)
        subject.notify_observers(msg_customer, subject_mail, recipient_mail)
        if phone_no:
            subject.notify_SMS(msg_customer, phone_no)
        subject.notify_observers(msg_manager, subject_mail_manager, "harikanalamhk@gmail.com")

        return Response({
                    "status": "success",
                    "message": "mail Successfully Done"},
                    status=status.HTTP_200_OK)

