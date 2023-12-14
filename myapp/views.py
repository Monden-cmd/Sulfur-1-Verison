from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tour
from .serializers import TourSerializer

class TourList(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

class TourCreate(APIView):
    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TourDetail(APIView):
    def get(self, request, tour_id):
        tour = get_object_or_404(Tour, pk=tour_id)
        serializer = TourSerializer(tour)
        return Response(serializer.data)

class TourUpdate(APIView):
    def put(self, request, tour_id):
        tour = get_object_or_404(Tour, pk=tour_id)
        serializer = TourSerializer(tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TourDelete(APIView):
    def delete(self, request, tour_id):
        tour = get_object_or_404(Tour, pk=tour_id)
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Booking
from .serializers import BookingSerializer

class BookingList(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

class BookingCreate(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(APIView):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, pk=booking_id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

class BookingUpdate(APIView):
    def put(self, request, booking_id):
        booking = get_object_or_404(Booking, pk=booking_id)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDelete(APIView):
    def delete(self, request, booking_id):
        booking = get_object_or_404(Booking, pk=booking_id)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
