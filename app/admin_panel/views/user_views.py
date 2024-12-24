from dataclasses import Field
from django.views import generic
from django.views import View
from app.base.models import *
from app.users.models import *
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from utils.views import CustomListBaseView
from app.admin_panel.forms import *
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

login_required_m =  method_decorator(login_required(login_url='login') , name="dispatch")


class LoginView(View):
    def get(self, request):
        return render(request, 'admin_panel/login.html', context={})

    def post(self, request): 
        phonenumber = request.POST.get('phonenumber', None)
        password = request.POST.get('password', None)
        remember_me = request.POST.get('remember_me', False)
        
        context = {
            'phonenumber': phonenumber,
            'has_error': False,
            'phone_error': False,
            'password_error': False
        }
        
        if not phonenumber or not password:
            context['has_error'] = True
            if not phonenumber:
                context['phone_error'] = True
            if not password:
                context['password_error'] = True
            return render(request, 'admin_panel/login.html', context=context)
            
        user = authenticate(request, phonenumber=phonenumber, password=password)
        if user:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(60*60*4)  # 30 days
            else:
                request.session.set_expiry(0)  # Expire when browser closes
            request.session.modified = True
            return redirect('dashboard')
        else:
            context['has_error'] = True
            context['phone_error'] = True
            context['password_error'] = True
            return render(request, 'admin_panel/login.html', context=context)


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')

@login_required_m
class DashboardView(View):
    def get(self, request):
        return render(request, 'admin_panel/dashboard.html',context={})


class ListClientsView(CustomListBaseView,generic.ListView):
    model = CustomUser
    context_object_name = 'clients'
    context_fields = ['id','fullName','phonenumber','is_active']
    template_name = 'admin_panel/users/clients/clients_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user_type='CLIENT')


class CreateClientView(generic.CreateView):
    model = OrganizationType
    template_name = 'organization_type_form.html'
    fields = ['name']
    success_url = '/dashboard/clients'

class UpdateClientView(generic.UpdateView):
    model = OrganizationType
    template_name = 'organization_type_form.html'
    fields = ['name']
    success_url = '/dashboard/clients'
    pk_url_kwarg = 'id'


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteClientView(View):
    def post(self, request):
        selected_ids = json.loads(request.POST.get('selected_ids', '[]'))
        if selected_ids:
            OrganizationType.objects.filter(id__in=selected_ids).delete()
            messages.success(request, 'تم حذف العناصر المحددة بنجاح')
        return HttpResponseRedirect(reverse('organization-types'))


class GetClientView(generic.DetailView):
    model = OrganizationType
    template_name = 'organization_type_confirm_delete.html'
    pk_url_kwarg = 'id'




class ListShareeksView(CustomListBaseView,generic.ListView):
    model = CustomUser
    context_object_name = 'shareeks'
    context_fields = ['id','fullName','phonenumber','is_active']
    template_name = 'admin_panel/users/shareeks/shareeks_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user_type='SHAREEK')


class CreateShareekView(View):
    def get(self,request):
        form = ShareekForm()
        return render(request, 'admin_panel/users/shareeks/add_shareek.html', {'form': form})
    # def post(self, request):
    #     form = ShareekForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         shareek = form.save()
    #         return redirect('users/shareek/')
    #     else:
    #         return render(request, 'admin_panel/users/shareeks/add_shareek.html', {'form': form})
    # model = Shareek
    # form_class = ShareekForm
    # template_name = 'admin_panel/users/shareeks/add_shareek.html'
    # success_url = 'users/shareek/'

class UpdateShareekView(generic.UpdateView):
    model = Shareek
    template_name = 'shareek_form.html'
    fields = ['shareek', 'commercial_register_id', 'logo', 'name', 'description', 'organization_type', 'website', 'website_short_link']
    success_url = 'users/shareek/'
    pk_url_kwarg = 'id'


class DeleteShareekView(View):
    def post(self, request):
        selected_ids = json.loads(request.POST.get('selected_ids', '[]'))
        if selected_ids:
            Shareek.objects.filter(id__in=selected_ids).delete()
            messages.success(request, 'تم حذف العناصر المحددة بنجاح')
        return HttpResponseRedirect(reverse('shareeks'))


class GetShareekView(generic.DetailView):
    model = Shareek
    template_name = 'shareek_detail.html'
    pk_url_kwarg = 'id'




class ListSubscriptions(generic.ListView):
    model = Subscription
    template_name = 'subscription_list.html'


class CreateSubscription(generic.CreateView):
    model = Subscription
    template_name = 'subscription_form.html'
    fields = ['shareek', 'commercial_register_id', 'logo', 'name', 'description', 'organization_type', 'website', 'website_short_link']
    success_url = '/admin/organizations/'


class UpdateSubscription(generic.UpdateView):
    model = Subscription
    template_name = 'subscription_form.html'
    fields = ['shareek', 'commercial_register_id', 'logo', 'name', 'description', 'organization_type', 'website', 'website_short_link']
    success_url = '/admin/organizations/'
    pk_url_kwarg = 'id'


class DeleteSubscription(generic.DeleteView):
    model = Subscription
    template_name = 'subscription_confirm_delete.html'
    success_url = '/admin/organizations/'
    pk_url_kwarg = 'id'


class GetSubscription(generic.DetailView):
    model = Subscription
    template_name = 'subscription_detail.html'
    pk_url_kwarg = 'id'




class ListAdminsView(CustomListBaseView,generic.ListView):
    model = CustomUser
    context_object_name = 'admins'
    context_fields = ['id','fullName','phonenumber','is_active']
    template_name = 'admin_panel/users/admins/admins_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user_type='ADMIN')

class CreateAdminView(generic.CreateView):
    model = Shareek
    template_name = 'admin_form.html'
    fields = ['shareek', 'commercial_register_id', 'logo', 'name', 'description', 'organization_type', 'website', 'website_short_link']
    success_url = 'users/shareek/'

class UpdateAdminView(generic.UpdateView):
    model = CustomUser
    template_name = 'admin_form.html'
    fields = ['shareek', 'commercial_register_id', 'logo', 'name', 'description', 'organization_type', 'website', 'website_short_link']
    success_url = 'users/shareek/'
    pk_url_kwarg = 'id'

class DeleteAdminView(View):
    def post(self, request):
        selected_ids = json.loads(request.POST.get('selected_ids', '[]'))
        if selected_ids:
            CustomUser.objects.filter(id__in=selected_ids).delete()
            messages.success(request, 'تم حذف العناصر المحددة بنجاح')
        return HttpResponseRedirect(reverse('admins'))

class GetAdminView(generic.DetailView):
    model = Shareek
    template_name = 'shareek_detail.html'
    pk_url_kwarg = 'id'
