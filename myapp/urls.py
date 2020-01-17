from django.urls import path
from . import views

urlpatterns=[
    path('',views.indexpage),
    path('css/',views.mycss),
    path('check/',views.checkt),
    path('hello/',views.hello),
    path('last/',views.last),
    path('color/',views.color),
    path('btsasgn1/',views.btas1),
    path('btsasgn2/',views.btas2),
    path('btsasgn3/',views.btas3)
    
]