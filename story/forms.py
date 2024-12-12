from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    # subject = forms.CharField(max_length=255, required=True, label="Subject", widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'Enter your subject'}))
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-input'}),
            'email': forms.EmailInput(attrs={'class': 'text-input'}),
            'message': forms.Textarea(attrs={'class': 'text-input', 'rows': 5, 'style': 'resize: none;'}),
        }
