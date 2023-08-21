# Django
from django.urls import path

# Local
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('', views.base, name='base'),
    path('index/',views.index,name='index')
=======
    path('', views.index, name='index'),
    path('<int:album_id>/', views.detail, name='detail')
>>>>>>> f3dc8e05be5e4a1c2beaf3d99f7d653251d522da
]
