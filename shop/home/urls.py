from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    # path('/', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('api/', views.api, name='api'),
]
