"""
URL configuration for railway_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from reservation.views import UserLoginView,UserRegistrationView,UserLogoutView
from reservation.ticketview import TicketListCreateView, AdminTicketUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    # Login - JWT Token Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/register/',UserRegistrationView.as_view(),name='user_registration'),
    path('api/login/',UserLoginView.as_view(),name='user_login'),
    path('api/logout/',UserLogoutView.as_view(),name='user_logout'),
    
    path('api/ticket/',TicketListCreateView.as_view(),name='user_action'),
    path('api/getallticket/',AdminTicketUpdateView.as_view(),name='admin_all_tickets'),
    path('api/updateticket/<int:pk>/',AdminTicketUpdateView.as_view(),name='admin_update'),
    path('api/deleteticket/<int:pk>/',AdminTicketUpdateView.as_view(),name='admin_delete')
]
