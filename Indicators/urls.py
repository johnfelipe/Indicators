from django.conf.urls import url
from django.contrib import admin
import Indicators_app.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^general_info/$", Indicators_app.views.general_info, name="general_info"),
    url(r"^$", Indicators_app.views.landing, name="landing"),
    url(r"^login/$", auth_views.LoginView.as_view(), name="login"),
    url(
        r"^logout/$", auth_views.LogoutView.as_view(), {"next_page": "/"}, name="logout"
    ),
]
