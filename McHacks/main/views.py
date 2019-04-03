from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from django.views.generic import TemplateView
from django.views.generic import CreateView
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
        return render(request, self.template_name, {'form': form})

    def post(self, request):
    	form = mainForm(request.POST)
    	print(form.errors)
    	if(form.is_valid()):
    		form.save()
    		search = Search()
    		search.userAddress = form.cleaned_data['userAddress']
    		search.userConcern = form.cleaned_data['userConcern']
    		search.longitude = form.cleaned_data['longitude']
    		search.latitude = form.cleaned_data['latitude']
    		args = {'form': form, 'search':search, 'userAddress':search.userAddress, 'userConcern':search.userConcern}
    		return render(request, 'main/dashboard.html', args)
    	print("form not valid :(")
    	return render(request, 'main/dashboard.html')

class dashboardView(TemplateView):
	template_name = 'main/dashboard.html'

	def get(self, request):
		return render(request, self.template_name, {})