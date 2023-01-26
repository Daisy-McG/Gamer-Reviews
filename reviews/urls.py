from django.urls import path
from .views import (
    CreateReview, Reviews, EditReview, DeleteReview
)

urlpatterns = [
    path('', Reviews.as_view(), name="reviews"),
    path('add/', CreateReview.as_view(), name="add_review"),
    path('edit/<slug:pk>/', EditReview.as_view(), name="edit_review"),
    path('delete/<slug:pk>/', DeleteReview.as_view(), name="delete_review"),
]