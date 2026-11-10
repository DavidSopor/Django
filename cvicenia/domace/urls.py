from django.urls import path
from . import views

urlpatterns = [
    path('', views.domace, name='domace'),
    path('du2_', views.vizitka, name='vizitka'),
]