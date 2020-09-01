from django import forms
from tweet.models import Tweet
# from countable_field import CountableField

class MakeTweetForm(forms.ModelForm):
    class Meta:
        model =Tweet
        fields = ["tweet"]
        
        
        
        # .widget = \
        #         CountableWidget(attrs={'data-count': 'characters',
        #                                'data-max-count': this.tweet_max_length})