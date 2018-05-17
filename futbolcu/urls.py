from django.conf.urls import url
from django.urls import include, path
from .views import *

app_name = 'futbolcu'
urlpatterns = [

    path('', index_view, name='index'),
    path('/detail/<int:id>', player_detail, name='detail'),

]
