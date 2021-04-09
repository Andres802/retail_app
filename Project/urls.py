# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.tokens import RefreshToken


from accounts.views import LoginAPI
from Users.views import RegisterAPI
from Users.views import ChangePasswordView

from django.urls import path, include
from knox import views as knox_views

# Apps
from Users import views as apis
from orders import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apis.UserLogin.as_view(), name='login'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('orders/', views.OrdersListView.as_view()),
    path('orders/<int:id>/', views.OrdersListView.as_view()),
    
]