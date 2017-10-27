from django import forms
from .models import UserProfile, Link, Vote

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user", )

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank_score")
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude = ()