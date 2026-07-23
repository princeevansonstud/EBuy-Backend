from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect root URL to products API
    path('', RedirectView.as_view(url='/api/products/', permanent=False)),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
