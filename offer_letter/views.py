from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from candidate.forms import *
from django.shortcuts import get_object_or_404, render
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



@login_required
def index(request):
    candidates = Candidate.objects.all().order_by('issued_date')
    context = {
        'candidates':candidates,
    }
    return render(request, 'offer_letter/index.html', context)



@login_required
def create(request):
    candidate_form = CandidateForm(request.POST or None, request.FILES or None)
    address_form = AddressForCandidateForm(request.POST or None)
    contact_form = ContactForCandidateForm(request.POST or None)

    if request.method == "POST":
        if candidate_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            #saving candidate
            candidate = candidate_form.save()
            

            #saving address
            address = address_form.save(commit=False)
            address.candidate = candidate
            address.save()

            #saving contact
            contact = contact_form.save(commit=False)
            contact.candidate= candidate
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Offer letter Created!')

          
            return HttpResponseRedirect(reverse('offer_letter:detail',args=[candidate.pk]))

    context = {
        'candidate_form': candidate_form,
        'address_form': address_form,
        'contact_form': contact_form,
        'form_url': reverse_lazy('offer_letter:create')

    }

    return render(request, 'offer_letter/create.html', context)



@login_required
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



def userlogin(request):
    if request.method == 'GET':
        messages.add_message(request, messages.SUCCESS, 'You need to login to create an offer letter!')
        return render(request, 'assignment/login.html')
    else:
        username = request.POST['login-name']
        password = request.POST['login-pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/offer_letter/")
            else:
                messages.add_message(request, messages.SUCCESS, 'The password is valid, but the account has been disabled!')
                return HttpResponseRedirect("/login/")
        else:
            
            messages.add_message(request, messages.SUCCESS, 'The username and password were incorrect.')
            return HttpResponseRedirect("/login/")


def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/login/")
