from django.conf.urls import url
from exam import views

urlpatterns=[
     url('instructions',views.iwarning),
     url('test',views.showTest),
     url('result',views.showTest),
     url('News',views.index),

]
