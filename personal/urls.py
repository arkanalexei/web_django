from django.urls import path
from personal.views import show_personal, tailwind

app_name = 'personal'

urlpatterns = [
    path('old', show_personal, name='show_personal'),
    path('', tailwind, name='tailwind'),

]