from django.contrib import admin
from django.urls import path, include
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.first),
    path('second/', myapp.views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')),
]
