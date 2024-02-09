from django.urls import path
from BSApp import views
urlpatterns=[
path('',views.home,name="hme"),
path('abt/',views.about,name="ab"),
path('std/',views.student,name="st"),
path('sp/<int:k>/',views.stdup,name="stpd"),
path('sd/<int:m>/',views.stddlt,name="sdel"),
path('empl/',views.emp,name='emp'),
path('eup/<int:z>/',views.eupd,name="eupdt"),
path('emdy/<int:d>/',views.emd,name="edel"),
]