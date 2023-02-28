from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
# Register class
class RegisterView(View):
    template_name = "registery/register.html"

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        form =RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(password=password)
            user.save()
            login(request, user)
            return redirect()