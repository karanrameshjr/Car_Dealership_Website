from django.contrib import admin
from django.urls import include, path
from homepage import views as home_views  # Import your home app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),  # Set the root URL to your home view
    path('home/', include('homepage.urls')),  # Include the URLs for your home app
    path('inventory/', include('inventory.urls')),  # Include the URLs for your inventory app
]

