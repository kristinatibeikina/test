from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *

urlpatterns = [
                  path('', ProductListView.as_view(), name='products'),
                  path('about/', AboutTemplateView.as_view(), name='about'),
                  path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
                  path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('add_product/', CreateProductView.as_view(), name='add_product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
