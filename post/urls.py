from django.urls import path
from .views import *

urlpatterns=[
    path('name/<str:name>/',Name,name='name'),
    path('person/<int:id>/',Id,name='id'),
    path('gender/<str:gender>',Gender,name='gender'),
    path('zip_code/<int:zip_code>',Zip_code,name='zip_code'),
    path('email/<str:email>',Email,name='email'),
]



