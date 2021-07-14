from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]

# # Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
#
# ]
