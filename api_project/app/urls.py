from django.urls import path
from .views import EnterpriseView

urlpatterns = [
    path('enterprises/', EnterpriseView.as_view(), name='enterprises_list'),
    path('enterprises/<int:nit>', EnterpriseView.as_view(),
         name='enterprises_process')
]
