"""
URL mappings for the user API.
"""

from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create-user/', views.CreateUserView.as_view(), name='create-user'),
    path(
        'create-token/',
        views.CreateTokenView.as_view(),
        name='create-token'
    ),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
