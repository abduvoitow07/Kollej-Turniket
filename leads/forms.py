from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Agent

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "ismi",
            "familiyasi",
            "yoshi",
            "agent",
            'izoh',
            'email',  
        )
        labels = {
            "ismi":"Familiya",
            "familiyasi":"Ism",
            "yoshi":"Guruh",
            "agent":"Kuratr",
            "izoh":"Manzil"
        }

class LeadForm(forms.Form):
    ismi = forms.CharField(max_length=20)
    familiyasi = forms.CharField(max_length=20)
    yoshi = forms.IntegerField(min_value=0)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset = Agent.objects.none(), label='Kuratr')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )