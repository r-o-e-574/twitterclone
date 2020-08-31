from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet import forms, models

# Create your views here.

def create_tweet(request):
    #regex to add an @to the username
    if request.method == "POST":
        form = forms.MakeTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.Tweet.objects.create(
                tweet = data.get("tweet"),
                twitter_user= request.user
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = forms.MakeTweetForm()
    return render(request, "generic_form.html", {"form": form})
