from django.urls import include, path
from .views import ViewCore


urlpatterns = [
    path('', ViewCore.as_view()),
]