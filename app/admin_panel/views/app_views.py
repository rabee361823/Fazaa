from django.views import View , generic
from app.users.models import *
from app.base.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

login_required_m =  method_decorator(login_required, name="dispatch")




class SocialMediaSlugUrlView(View):
    def get(self,request,slug):
        social = SocialMediaUrl.objects.get(short_url=slug)
        return redirect(social.url)


class WebsiteSligUrl(View):
    def get(self,request,slug):
        organization = Organization.objects.get(website_short_url=slug)
        return redirect(organization.website)



class DeliverySlugUrlView(View):
    def get(self,request,slug):
        delivery = DeliveryCompanyUrl.objects.get(short_url=slug)
        return redirect(delivery.url)


class CatalogSlugUrlView(View):
    def get(self,request,slug):
        catalog = Catalog.objects.get(short_url=slug)
        return redirect(catalog.file.url)


class ListReportsView(generic.ListView):
    model = Report
    context_object_name = 'reports'

class GetReportView(generic.DeleteView):
    model = Report
    context_object_name = 'report'

class DeleteReportView(generic.DeleteView):
    model = Report
    context_object_name = 'report'



class CommonQuestionsView(generic.ListView):
    model = CommonQuestion
    context_object_name = 'questions'

class CreateQuestionView(generic.DeleteView):
    model = CommonQuestion
    context_object_name = 'question'

class UpdateQuestionView(generic.DeleteView):
    model = CommonQuestion
    context_object_name = 'question'

class DeleteQuestionView(generic.DeleteView):
    model = CommonQuestion
    context_object_name = 'question'



class BaseNotificationsView(generic.ListView):
    model = Notification


class SendNotificationView(View):
    def post(self,request):
        pass



class AboutUsView(generic.ListView):
    model = AboutUs
    context_object_name = 'about'


class UpdateAboutUsView(generic.UpdateView):
    model = AboutUs
    context_object_name = 'about'