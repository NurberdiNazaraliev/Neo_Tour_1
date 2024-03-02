from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *



# Create your views here.


class adminTourView(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAdminUser]


class adminCategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ToursByCategoryView(ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = get_object_or_404(Category, name=category_name)
        return Tour.objects.filter(category=category)

class CurrentSeasonToursView(ListAPIView):
    ##filter the tours that are currently running
    def get_queryset(self):
        current_time = datetime.now().date()
        return Tour.objects.filter(season_start__lte=current_time, season_end__gte=current_time)

    serializer_class = TourSerializer


class SummerToursView(ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        current_time = datetime.now().date()
        is_mainstream = self.request.query_params.get('mainstream', None)

        # Define date ranges for summer
        season_start = datetime(current_time.year, 6, 1).date()
        season_end = datetime(current_time.year, 8, 31).date()

        # Filter tours by summer and mainstream
        query = Q(season_start__gte=season_start, season_end__lte=season_end, mainstream=True)

        return Tour.objects.filter(query)

class WinterToursView(ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        current_time = datetime.now().date()
        is_mainstream = self.request.query_params.get('mainstream', None)

        # Define date ranges for summer
        season_start = datetime(current_time.year, 12, 1).date()
        season_end = datetime(current_time.year+1, 2, 28).date()

        # Filter tours by summer and mainstream
        query = Q(season_start__gte=season_start, season_end__lte=season_end, mainstream=True)

        return Tour.objects.filter(query)


class AutumnToursView(ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        current_time = datetime.now().date()
        is_mainstream = self.request.query_params.get('mainstream', None)

        # Define date ranges for summer
        season_start = datetime(current_time.year, 9, 1).date()
        season_end = datetime(current_time.year, 11, 30).date()

        # Filter tours by summer and mainstream
        query = Q(season_start__gte=season_start, season_end__lte=season_end, mainstream=True)

        return Tour.objects.filter(query)

class SpringToursView(ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        current_time = datetime.now().date()
        is_mainstream = self.request.query_params.get('mainstream', None)

        # Define date ranges for summer
        season_start = datetime(current_time.year, 3, 1).date()
        season_end = datetime(current_time.year, 5, 31).date()

        # Filter tours by summer and mainstream
        query = Q(season_start__gte=season_start, season_end__lte=season_end, mainstream=True)

        return Tour.objects.filter(query)



class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserRegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    form_class = UserCreationForm


class TourDetailView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(Tour, name=name)

    # def post(self, request, name):
    #     tour = self.get_object()
    #     serializer = BookingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(tour=tour)
    #         return Response({'success': True, 'message': 'Tour successfully booked.'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    operation_description="List all tours."
)
class adminBookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]




class TourListView(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    @swagger_auto_schema(tags=['my custom tag'])
    def get(self, request, client_id=None):
        pass



