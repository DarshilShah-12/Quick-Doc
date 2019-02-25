from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from django.views.generic import TemplateView
from main.forms import mainForm

# Create your views here.

# def userForm(request):
#     return render(request=request,
#                   template_name="main/userForm.html",
#                   context={"searches": Search.objects.all})

class mainView(TemplateView):
    template_name = 'main/userForm.html'

    def get(self, request):
        form = mainForm()
        return render(request, self.template_name, {'form': mainForm})

class dashboardView(TemplateView):
	template_name = 'main/dashboard.html'

	def get(self, request):
		return render(request, self.template_name, {})

	def post(self, request):
		form = mainForm(request.POST)
		if form.is_valid():
			userAddress = form.cleaned_data['userAddress']
			userConcern = form.cleaned_data['userConcern']

		args = {'form': form, 'userAddress':userAddress, 'userConcern':userConcern}
		return render(request, self.template_name, args)