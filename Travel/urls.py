from django.views.generic import TemplateView

from .views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

Tourrouter = DefaultRouter()
Tourrouter.register(r'adminTourView', adminTourView)


Catergoryrouter = DefaultRouter()
Catergoryrouter.register(r'adminCategoryView', adminCategoryView)

Bookingrouter = DefaultRouter()
Bookingrouter.register(r'adminBookingView',adminBookingView)

urlpatterns = [
    path('', include(Tourrouter.urls)),
    path('', include(Catergoryrouter.urls)),
    path('', include(Bookingrouter.urls)),
    path('category-list', CategoryApiView.as_view(), name="category-list"),
    path('tours-by-category/<str:category_name>/', ToursByCategoryView.as_view(), name="tours-by-category"),
    path('current-tours', CurrentSeasonToursView.as_view(), name="current-tours"),
    path('summer-recommended-tours/', SummerToursView.as_view(), name='recommended-tours'),
    path('winter-recommended-tours/', WinterToursView.as_view(), name='recommended-tours'),
    path('autumn-recommended-tours/', AutumnToursView.as_view(), name='recommended-tours'),
    path('spring-recommended-tours/', SpringToursView.as_view(), name='recommended-tours'),
    path('review-add/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('tour-details/<str:name>/', TourDetailView.as_view(), name='tour-detail'),
    path('tour-list/', TourListView.as_view(), name='tour-list')


]