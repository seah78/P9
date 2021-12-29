from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    """Ticket creation form."""

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        
class ReviewForm(forms.ModelForm):
    """Review creation form."""
    
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]