from django import forms
from .models import Search
from .models import USER_CONCERNS

class mainForm(forms.ModelForm):
	userAddress = forms.CharField(widget=forms.TextInput(
		attrs={
			'id': 'autocomplete',
			'class': 'form-control',
			'placeholder': 'Enter your current address',
			'style': 'font-size:24px'
		}
	))

	# componentForm = forms.CharField(widget=forms.TextInput()

	userConcern = forms.ChoiceField(choices=USER_CONCERNS, widget=forms.Select(
		attrs={
			'class': 'form-control',
			'style': 'font-size:24px',
		}
	))

	class Meta:
	    model = Search
	    fields = ('userAddress', 'userConcern')


	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    # self.fields['userConcern'].queryset = Search.userConcernsList
	    self.fields['userAddress'].label = "Address"
	    # self.fields['userAddress'].label.font-size = 30
	    self.fields['userConcern'].label = "Concern"