"""Routes for the register app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("send_verification/", views.send_verification, name="send_verification"),
    path(
        "confirm_verification/", views.confirm_verification, name="confirm_verification"
    ),
    path(
        "success/", views.successful_confirmation, name="successful_confirmation"
    ),
]
