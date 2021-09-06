
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('', views.job_list,name='liste'),
    path('detail/<int:id>',views.job_detail,name='detail')

]


