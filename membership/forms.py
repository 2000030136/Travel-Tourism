from django import forms
from .models import MemberData
class MembershipForm(forms.ModelForm):
    class Meta:
        model = MemberData
        fields = ['firstname','lastname','email','username','password']