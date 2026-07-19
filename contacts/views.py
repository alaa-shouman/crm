from django.shortcuts import render

# Create your views here.
from .models import Contact
from core.responses import api_response

def contact_list(request):
    contacts = Contact.objects.all().values("uuid", "name", "email", "phone", "notes", "created_at", "updated_at")
    return api_response(data=list(contacts), safe=False)

def contact_detail(request, pk):
    try:
        contact = Contact.objects.values("uuid", "name", "email", "phone", "notes", "created_at", "updated_at").get(pk=pk)
    except Contact.DoesNotExist:
        return api_response(message="Contact not found", status=404)

    return api_response(data=contact, message="Contact retrieved successfully")