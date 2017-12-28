from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from modules.accounts.forms import (
    RegistrationForm, 
    EditProfileForm
) #Django user creation form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import B2cRegisterForm, BusinessCreateForm
from .models import B2cProfile
from django.views.generic import DetailView, CreateView, UpdateView
from modules.items.models import Item
from .models import B2cProfile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# here comes all de logic 
'''def home (request):
    #return render(request, 'accounts/login.html')
    #querys
    numbers =[1,2,3,4,5]
    name='Carlos Bárcena
    args={'myName':name, 'numbers':numbers} # dictionary object
    return render(request,'accounts/home.html', args)'''

def register(request):
    form = B2cRegisterForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj =B2cProfile.objects.create(
            business_name = my_b2c.cleaned_data['business_name'],
            description = my_b2c.cleaned_data['description'],
            city = my_b2c.cleaned_data['website'],
            website = my_b2c.cleaned_data['phone'],
            phone = my_b2c.cleaned_data['phone'],
            cierre = my_b2c.cleaned_data['cierre'],
            apertura = my_b2c.cleaned_data['apertura'],
            )
        return redirect("/")
    if form.errors:
        errors= form.errors

    template_name='business/reg_b2c.html'
    context = {"form":form, "errors":errors}
    return render(request, template_name, context)
    # my_b2c = B2cRegisterForm()
    # if request.method == 'POST':
    #     my_b2c = B2cRegisterForm(request.POST,request.FILES)
    #     if my_b2c.is_valid():

    #         business = B2cProfile.objects.create(

    #                 business_name = my_b2c.cleaned_data['business_name'],
    #                 description = my_b2c.cleaned_data['description'],
    #                 city = my_b2c.cleaned_data['website'],
    #                 website = my_b2c.cleaned_data['phone'],
    #                 phone = my_b2c.cleaned_data['phone'],
    #                 cierre = my_b2c.cleaned_data['cierre'],
    #                 apertura = my_b2c.cleaned_data['apertura'],
    #                 )

    #         user = User.objects.get(pk=request.user.id)

         
    #         user.business = business
    #         user.save()
    #         return redirect('/')
    # return render(request, 'business/reg_b2c.html', {'my_b2c':my_b2c})

def view_b2c_profile(request):

    business = B2cProfile.objects.all()
    return render(request,'base.html',{'business':business})


# def business_view_list(request):
#     template_name ='snippets/b2c_list.html'
#     queryset=B2cProfile.objects.all()
#     context = {
#          "object_list":queryset
#     }
#     return render(request, template_name, context)


class B2cDetailsView(DetailView):
     queryset = B2cProfile.objects.all()

    # def get_object(self):
    #     business = self.kwargs.get("business_name")
    #     if username is None:
    #         raise Htt

     # def get_queryset(self):
     #     return Item.objects.filter(user=self.request.business)

    # def get_context_data(self, *args, **kwargs):
    #   print(self.kwargs)
    #   context= super(RestaurantDetailsView, self).get_context_data(*args, **kwargs)
    #   print(context)
    #   return context

    # def get_object(self, *args, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     obj= get_object_or_404(B2cProfile, slug=slug)
    #     return obj

    # def get_queryset(self):
    #     return B2cProfile.objects.filter(user=self.request.user)


class BusinessCreateView(LoginRequiredMixin, CreateView):
    form_class = BusinessCreateForm
    template_name = 'business/reg_b2c.html'
    # success_url = '/business/'
    #success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(BusinessCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

    def get_queryset(self):
        return Item.objects.filter(user=self.request.business)

class BusinessUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BusinessCreateForm
    login_url = '/login/'
    template_name = 'business/b2cprofile_update.html'
    #success_url = "/restaurants/"

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessUpdateView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return B2cProfile.objects.filter(owner=self.request.user)