from django.urls import path
from profesionales import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('prof/', views.prof_list),
]