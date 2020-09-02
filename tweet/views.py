import re
from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet import forms, models
from notification.models import Notification
from twitteruser.models import TwitterUser

# Create your views here.
def tweet_view(request, tweet_id):
    tweet = models.Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet.html", {"Tweet":tweet})



def create_tweet(request):
    if request.method == "POST":
        form = forms.MakeTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            at_user = re.findall(r'@([\w]+)', data.get("tweet"))
            new_tweet = models.Tweet.objects.create(
                tweet = data.get("tweet"),
                twitter_user= request.user
            )
            if at_user:
                for at in at_user:
                    new_notification = Notification.objects.create(
                        tweet = new_tweet,
                        receiver = TwitterUser.objects.get(username=at)
                    )
            return HttpResponseRedirect(reverse("homepage"))
    form = forms.MakeTweetForm()
    return render(request, "generic_form.html", {"form": form})
