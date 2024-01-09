from django.shortcuts import render
from .models import Owner, Patient
from .forms import OwnerForm
from django.http import JsonResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
class OwnerList(ListView):
  model = Owner
  template_name = "vetoffice/owner_list.html"

class PatientList(ListView):
  model = Patient
  template_name = "vetoffice/patient_list.html"

class OwnerCreate(CreateView):
  model = Owner
  template_name = "vetoffice/owner_create_form.html"
  fields = ["first_name", "last_name", "phone"]

class PatientCreate(CreateView):
  model = Patient
  template_name = "vetoffice/patient_create_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class OwnerUpdate(UpdateView):
  model = Owner
  template_name = "vetoffice/owner_update_form.html"
  fields = ["first_name", "last_name", "phone"]

class PatientUpdate(UpdateView):
  model = Patient
  template_name = "vetoffice/patient_update_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class OwnerDelete(DeleteView):
  model = Owner
  template_name = "vetoffice/owner_delete_form.html"

class PatientDelete(DeleteView):
  model = Patient
  template_name = "vetoffice/patient_delete_form.html"

def form_view(request):
  form = OwnerForm()
  if request.method == 'POST':
    form = OwnerForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      owner = Owner(
        first_name = cd['first_name'],
        last_name=cd['last_name'],
        phone=cd['phone']
      )
      owner.save()
      return JsonResponse({
        'message': 'success'
      })
  return render(request,'vetoffice/owner_form.html', {'form': form})