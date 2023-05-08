from django.urls import path
from . import views

urlpatterns = [
    path('submit-data/', views.submitData, name='submit-data'),
]