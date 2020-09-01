from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser import forms, models
from tweet import models
from django.contrib.auth import login

# Create your views here.
@login_required
def index_view(request):
    tweets = models.Tweet.objects.all().order_by('-time_date')
    return render(request, 'index.html', {"Welcome": "Welcome to TWEETER", "tweets": tweets})


def user_profile(request, user_id):
    profile = models.TwitterUser.objects.filter(id=user_id).first()
    tweets = models.Tweet.objects.filter(twitter_user=profile)
    return render(request, "user_profile.html",
                  {"profile": profile,
                   "tweets": tweets,
                  }
                  )


def create_user(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = models.TwitterUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password")
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))
    form = forms.SignupForm()
    return render(request, "generic_form.html", {"form": form})


def following_view(request, following_id):
    current_user = request.user
    follow = models.TwitterUser.objects.filter(id=following_id).first()
    current_user.following.add(follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))