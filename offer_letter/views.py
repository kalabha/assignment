# from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse, reverse_lazy
# from django.db.models import F, Q, functions, Value as V
from django.http import HttpResponseRedirect
from candidate.forms import *
from django.shortcuts import get_object_or_404, render
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf
# # from invoice.models import Invoice, Achievements
# from django.db.models import Sum
# from django.contrib import messages
# from erp_core.pagination import paginate
# # from timesheet.models import TimeSheet
# import datetime
# from rest_framework.views import APIView
# from .models import *
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.renderers import JSONRenderer
# from django.forms import inlineformset_factory
# from enquiry.models import Enquiry


# @login_required
# @permission_required('employee.view_employee_list', raise_exception=True)
def create(request):
    user_form = UserForm(request.POST or None)
    candidate_form = CandidateForm(request.POST or None, request.FILES or None)
    address_form = AddressForCandidateForm(request.POST or None)
    contact_form = ContactForCandidateForm(request.POST or None)

   


    if request.method == "POST":
        print(user_form.errors)
        print(candidate_form.errors)
        print(address_form.errors)
        print(contact_form.errors)

        if user_form.is_valid() and candidate_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            #saving user
            user = user_form.save(commit=False)
            user.username = user.email

            # dummy password
            user.password = "password"
            userpassword = "password"
            user.save()

            #saving candidate
            candidate = candidate_form.save(commit=False)
            candidate.user = user
            candidate.save()

            #saving address
            address = address_form.save(commit=False)
            address.candidate = candidate
            address.save()

            #saving contact
            contact = contact_form.save(commit=False)
            contact.candidate= candidate
            contact.save()

          
            return HttpResponseRedirect(reverse('offer_letter:detail',args=[candidate.pk]))

    context = {
        'candidate_form': candidate_form,
        'user_form': user_form,
        'address_form': address_form,
        'contact_form': contact_form,
        'form_url': reverse_lazy('offer_letter:create')

    }

    return render(request, 'offer_letter/create.html', context)




def detail(request,pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    context = {
        'candidate': candidate,
    }
    return render(request, 'offer_letter/single.html', context)



class OfferLetterPDFView(PDFTemplateView):
    template_name = 'offer_letter/letter_pdf.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk', False)
        return super(OfferLetterPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            candidate= Candidate.objects.get(pk=pk),
        )