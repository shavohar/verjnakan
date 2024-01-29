from django.contrib import messages

from .forms import ReserveTableForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from reservation.models import Reservation


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == "POST":
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
    messages.success(request, "Once your reservation has been accepted, we will reply to you by e-mail")

    return render(request, "reservation/reservation.html", {"form": reserve_form})
# class ReserveTableView(View):
#     template_name = "reservation/reservation.html"
#
#     def get(self, request, *args, **kwargs):
#         available_tables = Reservation.objects.filter(is_table_booked=False)
#         context = {"form": ReserveTableForm(), "available_tables": available_tables}
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         reserve_form = ReserveTableForm(request.POST)
#
#         if reserve_form.is_valid():
#             reservation = reserve_form.save(commit=False)
#
#             if Reservation.objects.filter(date=reservation.date, time=reservation.time, is_table_booked=False).exists():
#                 reservation.is_table_booked = True
#                 reservation.save()
#                 return redirect('home:home')
#             else:
#                 context = {"form": reserve_form, "error_message": "Selected table is not available."}
#                 return render(request, self.template_name, context)
#
#         context = {"form": reserve_form}
#         return render(request, self.template_name, context)


# class ConfirmReservationView(View):
#     def get(self, request, reservation_id):
#         reservation = get_object_or_404(Reservation, id=reservation_id)
#         reservation.confirm_reservation()
#         return redirect('reservation_list')
#
#
# class CancelReservationView(View):
#     def get(self, request, reservation_id):
#         reservation = get_object_or_404(Reservation, id=reservation_id)
#         reservation.cancel_reservation()
#         return redirect('reservation_list')
