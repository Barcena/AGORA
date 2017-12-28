from django.shortcuts import render
from .models import Partner

# Create your views here.
def viewPartners(request):
	#if request.user.is_authenticated():
	partners = Partner.objects.all()

	return render(request,'partners/partners.html',{'partners':partners})
	#return redirect('/')
