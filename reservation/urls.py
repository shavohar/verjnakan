from django.urls import path
from reservation.views import ReserveTableView, ConfirmReservationView, CancelReservationView

app_name = "reservation"

urlpatterns = [
    path('reserve/', ReserveTableView.as_view(), name='reserve_table'),
    path('confirm/<int:reservation_id>/', ConfirmReservationView.as_view(), name='confirm_reservation'),
    path('cancel/<int:reservation_id>/', CancelReservationView.as_view(), name='cancel_reservation'),
]
