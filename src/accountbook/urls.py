from django.urls import path

from . import views

app_name = 'accountbook'

urlpatterns = [
    path('accountbook_list/', views.AccountBookListView.as_view(), name='accountbook_list'),
    ]