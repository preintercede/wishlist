from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.AddList.as_view(), name="add_to_list"),
    path('<int:pk>/delete/',   views.ItemDelete.as_view(), name='items_delete'),
]