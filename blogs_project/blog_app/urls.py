from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
   path('', views.all_blogs, name='all_blogs'),
   path('<int:pk>/', views.detail, name='detail'),
]
