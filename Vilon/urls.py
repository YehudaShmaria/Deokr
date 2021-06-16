from django.urls import path
from . import views

urlpatterns = [
   path('', views.All, name = 'all'),
   path('tfira', views.VilonTfira, name = 'tfira'),
   path('roma', views.VilonRoma, name = 'roma'),
   path('van/<str:name>', views.VilonVan, name = 'van'),
   path('zebra', views.VilonZebra, name = 'zebra'),
   path('detailes/<int:id>',views.Detailes, name='detailes')
]
