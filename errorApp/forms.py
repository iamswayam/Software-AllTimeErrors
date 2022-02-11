from .models import allErrors
from django import forms


class allErrorsForm(forms.ModelForm):
    class Meta:
        model = allErrors
        fields = '__all__'

    # widgets = {
    #     'section': forms.Select(attrs={'class': 'form-control'}),
    #     'question': forms.TextInput(attrs={'class': 'form-control'}),
    #     'answer': forms.Textarea(attrs={'class': 'form-control'}),
    # }
