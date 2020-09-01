"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as twitteruser_views
from authentication import views as auth_views
from tweet import views as tweet_views

urlpatterns = [
    path('', twitteruser_views.index_view, name="homepage"),
    path('profile/<int:user_id>/', twitteruser_views.user_profile, name="profile"),
    path('tweet/<int:tweet_id>/', tweet_views.tweet_view, name="tweet"),
    path('createtweet/', tweet_views.create_tweet, name="createtweet"),
    path('following/<int:following_id>/', twitteruser_views.following_view, name="following" ),
    path('login/', auth_views.login_view, name="login"),
    path('logout/', auth_views.logout_view, name="logout"),
    path('signup/', twitteruser_views.create_user, name="signup"),
    path('admin/', admin.site.urls),
]
