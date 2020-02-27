from django.urls import path, include
from . import views
from .views import SignUpView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', SignUpView.as_view(), name='registration'),
    # path('login/', LoginView.as_view(), name='login'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)