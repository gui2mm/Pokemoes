from django.urls import include, path
from .views import ViewHome, ViewLogin


urlpatterns = [
    path('', ViewHome.as_view()),

]