from django import forms
from tweet.models import Tweet


class MakeTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["tweet"]