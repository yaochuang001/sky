from django.urls import path
from sky import views
urlpatterns = [
    # index
    path('index/', views.index),

]
