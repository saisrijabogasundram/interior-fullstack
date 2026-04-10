from django.urls import path
from .views import (
    DesignerListView,
    DesignerDetailView,
    DesignerCreateView,
    BookingCreateView,
    BookingListView,
    BookingDetailView,
    CustomerBookingView,
    ManageBookingsView,
    LeadCreateView,      
    LeadManageView,      
)

urlpatterns = [
    path('leads/', LeadCreateView.as_view(), name='lead-create'),         
    path('leads/manage/', LeadManageView.as_view(), name='lead-manage'), 
    path('leads/manage/<int:pk>/', LeadManageView.as_view(), name='lead-manage-detail'),

    path('my-bookings/', CustomerBookingView.as_view(), name='my-bookings'),
    path('manage/', ManageBookingsView.as_view(), name='manage-bookings'),
    path('manage/<int:pk>/', ManageBookingsView.as_view(), name='manage-booking-detail'),
    path('designers/', DesignerListView.as_view(), name='designer-list'),
    path('designers/<int:pk>/', DesignerDetailView.as_view(), name='designer-detail'),
    path('designers/create/', DesignerCreateView.as_view(), name='designer-create'),
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('', BookingListView.as_view(), name='booking-list'),
] 