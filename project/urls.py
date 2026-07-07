from django.urls import path
from .import views

urlpatterns = [
    path('', views.one),
    path('two', views.two,name="two"),
    path('three', views.three,name="three"),
    path('four', views.four,name="four"),
    path('five', views.five,name="five"),
    path('six', views.six,name="six"),
    path('seven', views.seven,name="seven"),
    path('eight', views.eight,name="eight"),
    path('nine', views.nine,name="nine"),
    path('ten', views.ten,name="ten"),
    path('eleven', views.eleven,name="eleven"),
    path('twovelve', views.twovelve,name="twovelve"),
    path('thirteen', views.thirteen,name="thirteen"),
    path('fourteen', views.fourteen,name="fourteen"),
    path('fifteen', views.fifteen,name="fifteen"),
    path('sixteen', views.sixteen,name="sixteen"),
    path('seventeen', views.seventeen,name="seventeen"),
    path('payment', views.payment, name="payment"),
    path('payment_success', views.payment_success, name='payment_success')
]