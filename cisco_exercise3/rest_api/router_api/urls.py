from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RouterView, LoginView, ListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view'),
    path('list/', ListView.as_view(), name='list_view'),
    path('router/', RouterView.as_view(), name='router_list_add_view'),
    path('update/<str:ip>/', RouterView.as_view(), name='update_view'),
    path('api-token-auth/', obtain_auth_token, name='api_auth_token'),
]
