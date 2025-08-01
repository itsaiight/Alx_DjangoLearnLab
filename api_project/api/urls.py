from django.urls import path
from api.views import BookList
from django.urls import include
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),  # This includes all routes registered with the router
]
