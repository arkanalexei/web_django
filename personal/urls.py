from django.urls import path
from personal.views import show_personal, tailwind

app_name = 'personal'

urlpatterns = [
    path('', show_personal, name='show_personal'),
    path('tailwind', tailwind, name='tailwind'),

]