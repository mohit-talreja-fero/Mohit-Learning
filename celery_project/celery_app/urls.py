from django.urls import path
from .views import GenerateRandomUserView, show_users



urlpatterns = [
    path('', GenerateRandomUserView.as_view()),
    path('users', show_users, name='users_list'),
]
