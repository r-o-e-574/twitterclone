from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from notification.models import Notification

# Create your views here.
@login_required
def notification_view(request, user_id):
    notifications = Notification.objects.filter(receiver__id=user_id)
    received_notification = []
    for notified in notifications:
        if not notified.viewed_at:
            received_notification.append(notified.tweet)
        notified.viewed_at = timezone.now()
        notified.save()
    
    
    return render(request, "notification_view.html",{"rn": received_notification[::-1]})