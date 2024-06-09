
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('<str:id>/',downloadFile,name="download")
] +static(settings.MEDIA_ROOT,document_root=settings.MEDIA_URL)
