
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Ticket
from .forms import TicketForm

@login_required(login_url="/")
def flux(request):
    tickets = Ticket.objects.all()
    return render(request, 'flux/flux.html', context={'tickets': tickets})


@login_required(login_url="/")
def make_ticket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.info(request, "Votre ticket vient d'être publié!")
            return redirect("flux")
    return render(request,"flux/create_ticket.html", context={"form": form})