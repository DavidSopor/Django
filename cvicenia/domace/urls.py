from django.urls import path
from . import views

urlpatterns = [
    path('', views.domace, name='domace'),
    path('vizitka', views.vizitka, name='vizitka'),
]