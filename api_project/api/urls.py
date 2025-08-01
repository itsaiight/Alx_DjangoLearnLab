from django.contrib import admin
from django.urls import path
from api.views import BookList
from django.urls import include

urlpatterns = [
    path('api/', include('api.urls')),  # Include API URLs
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
