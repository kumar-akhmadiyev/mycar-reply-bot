from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path("users/", include("users.urls")),
    path("messages/", include("tg_bot.urls")),
    path("admin/", admin.site.urls),
]
