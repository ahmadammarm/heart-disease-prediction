from django.urls import path
from . import views

app_name = 'classifier'
urlpatterns = [
    path('model/<int:dataset_id>/', views.model, name='model'),
    path('predict/<int:dataset_id>/', views.predict, name='predict'),
    path('result/<int:dataset_id>/', views.result, name='result'),
]