from django.urls import path
from .views import TourList, TourCreate, TourDetail, TourUpdate, TourDelete

urlpatterns = [
    path('tours/', TourList.as_view(), name='tour-list'),
    path('tours/create/', TourCreate.as_view(), name='tour-create'),
    path('tours/<int:pk>/', TourDetail.as_view(), name='tour-detail'),
    path('tours/<int:pk>/update/', TourUpdate.as_view(), name='tour-update'),
    path('tours/<int:pk>/delete/', TourDelete.as_view(), name='tour-delete'),
]
