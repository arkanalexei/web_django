from django.urls import path
from personal.views import show_personal

app_name = 'personal'

urlpatterns = [
    path('', show_personal, name='show_mywatchlist'),

]