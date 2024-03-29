from django.urls import path 
from . import views 

urlpatterns = [
    # path('register/', views.register, name='register'),
    path('register/', views.registerClass.as_view(), name='register'),
    # path('login/', views.logIn, name='login'),
    path('login/', views.LogInClass.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>/', views.profile, name='profile_with_id'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_profile/', views.edit_profile_class.as_view(), name='edit_profile'),
    path('change_pass/', views.change_password, name="change_pass"),
    path('logout/', views.logOut, name='logout'),
]
