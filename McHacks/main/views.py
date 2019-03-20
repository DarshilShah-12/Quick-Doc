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
        return render(request, self.template_name, {'form': form})

    def post(self, request):
    	form = mainForm(request.POST)
    	if(form.is_valid()):
    		form.save()
    		search = Search()
    		search.save()
    		search.userAddress = form.cleaned_data['userAddress']
    		search.userConcern = form.cleaned_data['userConcern']
    		search.save()



    	args = {'form': form, 'userAddress':search.userAddress, 'userConcern':search.userConcern, 'search':search}
    	return render(request, 'main/dashboard.html', args)

class dashboardView(TemplateView):
	template_name = 'main/dashboard.html'

	def get(self, request):
		return render(request, self.template_name, {})

	# def post(self, request):
	# 	form = mainForm(request.POST)
	# 	if form.is_valid():
	# 		Search.userAddress = form.cleaned_data['userAddress']
	# 		Search.userConcern = form.cleaned_data['userConcern']

	# 	args = {'form': form, 'userAddress':userAddress, 'userConcern':userConcern}
	# 	return render(request, self.template_name, args)

# def search(request):
# 	search = Search(userAddress=request.GET['userAddress'], userConcern=request.GET['userConcern'])
# 	return HttpResponse(search)

def getFormData(request):
	form = mainForm(request.POST)
	return render(request, 'main/dashboard.html', {'form':form})

def post_new(request):
	form = mainForm()
	return render(request, 'main/userForm.html', {'form': form})