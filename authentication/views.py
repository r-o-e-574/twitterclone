from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from authentication import forms

# Create your views here.
class LoginView(TemplateView):
    
    def get(self,request):
        form = forms.LoginForm()
        return render(request, "generic_form.html", {"form": form})
    
    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "generic_form.html", {"form": form})




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))