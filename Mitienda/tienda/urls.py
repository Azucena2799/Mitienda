from django.urls import path
from . import views
app_name = 'tienda'





urlpatterns = [
    path('Plantas/',views.Plantas, name ='Plantas'),
    path('Pagar/',views.Pagar, name ='Pagar'),
    path('AgregarPlanta/>',views.AgregarPlanta, name ='AgregarPlanta'),
    path('deletep/<int:idr>',views.deletep,name="deletep"),
    path('AgregarC/>',views.AgregarC, name ='AgregarC'),

]
