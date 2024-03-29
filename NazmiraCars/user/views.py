from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from carbrands.models import Car, Brand
from django.contrib.auth.decorators import login_required
from boughtcar.models import BoughtCar
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = forms.UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration Successful. Please Log in')
#             return redirect('login')

#     form = forms.UserRegisterForm()
#     return render(request, 'user/register.html', {'form': form, 'command': 'Register'})


class registerClass(CreateView):
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')
    form_class = forms.UserRegisterForm

    def get_context_data(self, **kwargs):
        kwargs["command"] = 'Register'
        return super().get_context_data(**kwargs)
    


# def logIn(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "logged in successfully")
#                 return redirect('profile')
#             else:
#                 messages.warning(request, "The username or password is not correct")
#                 return redirect('register')
    
#     form = AuthenticationForm()
#     return render(request, 'user/register.html', {'form': form, "command": "login"})


class LogInClass(LoginView):
    template_name = 'user/register.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['command'] = 'login'
        return context
    

@login_required
def profile(request, id=None):
    data = Brand.objects.all()
    cars = Car.objects.all()
    owned_car = BoughtCar.objects.filter(owner=request.user)
    owner = request.user
    view_car = []
    for car in owned_car:
        view_car.append(car.car)
    brand = None
    if id is not None:
        brand = Brand.objects.filter(id=id)
        print(brand)
        for car in owned_car:
            if car.car.brand == brand:
                # print(car.car, brand)
                view_car.append(car.car)

    print(view_car)
    return render(request, 'user/profile.html', {'data': data, 'cars': view_car, 'owner': owner})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = forms.ChangeUserForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#             return redirect('profile')
#     form = forms.ChangeUserForm(instance=request.user)
#     return render(request, 'user/register.html', {'form': form, 'command': 'Update'})


@method_decorator(login_required, name='dispatch')
class edit_profile_class(View):
    template_name = 'user/register.html'
    
    def get(self, request, *args, **kwargs):
        form = forms.ChangeUserForm(instance=self.request.user)
        return render(self.request, self.template_name, {'form': form, 'command': 'Update'})
    
    def post(self, request, *args, **kwargs):
        form = forms.ChangeUserForm(self.request.POST, instance=self.request.user)

        if form.is_valid():
            form.save()
            messages.success(self.request, "Profile Updated Successfully")
            return redirect('profile')
        return render(self.request, self.template_name, {'form': form, 'command': 'Update'})
    


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "password changed successfully")
            return redirect('profile')
    form = PasswordChangeForm(request.user)
    return render(request, 'user/register.html', {'form': form, 'command': "Change"})


def logOut(request):
    messages.success(request, 'logged out successfully')
    logout(request)
    return redirect('homepage')