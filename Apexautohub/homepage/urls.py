from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import index_view, contact_form_view, LogoutView

urlpatterns = [
    # Your other URL patterns here
    path('', views.home, name='home'),
    path('index/', views.index_view, name='index'),  # Ensure the name matches the one used in the redirect
    path('contact/', contact_form_view, name= 'contact_form'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


