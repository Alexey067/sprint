from django.urls import path
from . import views

urlpatterns = [
    path('submit-data/', views.submitData, name='submit-data'),
    path('submitData/<int:pk>/', views.get_pereval_by_id, name='pereval-detail'),
    path('submitData/<int:pk>/update/', views.edit_pereval, name='pereval-update'),
    path('submitData/email/', views.get_pereval_by_user_email, name='pereval-list'),
]
