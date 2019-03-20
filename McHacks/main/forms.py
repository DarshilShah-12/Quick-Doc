from django import forms
from .models import Search

class mainForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['userAddress', 'userConcern']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['userConcern'].queryset = Search.userConcernsList