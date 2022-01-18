from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gallery/', views.gallery),
    path('submitted',views.submitted),
    path('<int:num>/',views.nxt_pg),
    path('making/', views.making),
    path('making1/',views.making1),
    path('making2/', views.making2),
]

