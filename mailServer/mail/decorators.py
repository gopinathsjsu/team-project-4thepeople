from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client



#notify customer and hotel management after successful booking
class Observer:

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(
        self,
        msg,
        subject,
        recipient_mail
        ):
        print ('Got', msg, subject, 'From', recipient_mail)

class Observable:

    def __init__(self):
        self._observers = []

    #subscribe a mail notification for hotel offers
    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(
        self,
        msg,
        subject,
        recipient_mail
        ):
        print ('in observable Got', msg, subject, 'From', recipient_mail)
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_mail]
        )

    def notify_SMS(
        self,
        msg,
        phone_no
        ):
        # print ('in observable Got', msg, subject, 'From', recipient_mail)
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        hotel_no = settings.PHONE_NO
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                        body=msg,
                                        from_=hotel_no,
                                        to=phone_no
                                    )

    #unsubscribe mail notification
    def unsubscribe(self, observer):
        self._observers.remove(observer)
