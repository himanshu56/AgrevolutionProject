from django.urls import path
from .views import *

urlpatterns = [
    path('', SingUpCustomer.as_view()),
    path('custDash/', dash1.as_view()),
    path('orderpalced/', OrderDetails.as_view()),
    path('adminlogin/', admin_sales_login.as_view()),
    path('salesdash/', salesdash.as_view()),
    path('logout/', logoute.as_view()),
]
