from django.urls import path
from . import views
from .models import Inventorius
from .views import InventoriusCreateView, InventoriusUpdateView, InventoriusDeleteView, statistika

urlpatterns = [
    path('', views.pradinis, name='pradinis'),
    path('naujas/', InventoriusCreateView.as_view(), name='kurti'),
    path('redaguoti/<int:pk>/', InventoriusUpdateView.as_view(), name='redaguoti'),
    path('istrinti/<int:pk>/', InventoriusDeleteView.as_view(), name='istrinti'),
    path('statistika/', statistika, name='statistika'),
    path('veiksmas/', views.pasirinktas_veiksmas, name='pasirinktas_veiksmas'),
]
