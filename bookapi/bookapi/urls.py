
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.routers import router
from api.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    # path("login/", UserCreate.as_view(), name="user_create"),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


