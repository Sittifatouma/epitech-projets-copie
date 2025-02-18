from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('code/', views.receive_code, name='code'),
    path('token/', views.get_token, name='token'),
    path("user/register", views.register_user, name="register_user"),
    path("user/transaction", views.transaction_user, name="transaction_user"),
    path('predict/', views.predict, name='predict')
]
