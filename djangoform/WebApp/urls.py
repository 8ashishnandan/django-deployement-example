from django.urls import path
from WebApp import views

app_name='WebApp'
urlpatterns=[
path('other/',views.other,name='other'),
path('',views.page,name='page'),
path('form_page/',views.users,name='form_page'),
]
