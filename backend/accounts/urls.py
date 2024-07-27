from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    UserRegistrationView,
    SendOTPForEmailVerificationAPIView,
    PasswordResetConfirmationAPIView,
    EmailConfirmationAPIView,
    CustomTokenObtainPairView,
    CustomLogoutView,
    UserProfileGetAPIView,
    UserProfileUpdateAPIView,
    AccountDeletionAPIView,
    SendOTPForPasswordResetAPIView,
    CheckingOTPPasswordResetAPIView,
)

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name='register_customer'),
    path('accounts/email/confirmation/', EmailConfirmationAPIView.as_view(), name='email_confirmation'),
    path('accounts/email/otp/resend/', SendOTPForEmailVerificationAPIView.as_view(), name='resend_otp_for_email_verification'),
    path('accounts/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/check-otp-password-reset/', CheckingOTPPasswordResetAPIView.as_view(), name='check-otp-password-reset'),
    path('accounts/password/reset/confirmation/', PasswordResetConfirmationAPIView.as_view(), name='reset_password_confirmation'),
    path('accounts/profile/me/', UserProfileGetAPIView.as_view(), name='my_profile'),
    path('accounts/profile/update/', UserProfileUpdateAPIView.as_view(), name='my_profile'),
    path('accounts/deletion/me/', AccountDeletionAPIView.as_view(), name='deletion_me'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/password/reset/otp/send/', SendOTPForPasswordResetAPIView.as_view(), name='send_orp_for_password_reset'),
]
