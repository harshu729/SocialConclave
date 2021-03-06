from django import forms
from .models import *
from django.core import validators


class DelegateForm(forms.ModelForm):
    class Meta:
        model = Delegate
        fields = ['name', 'age', 'email', 'phoneNumber', 'address',
                  'gender', 'topicPref1', 'topicPref2', 'topicPref3', 'city', 'schoolName', 'courseName', 'yearGrad']
        labels = {
            "name": "",
            "age": "",
            'email': '',
            "phoneNumber": "",
            "address": "",
            'gender': 'Gender',
            "topicPref1": "Enter First Preference",
            "topicPref2": "Enter Second Preference",
            "topicPref3": "Enter Third Preference",
            "city": "",
            "schoolName": "",
            "courseName": "",
            "yearGrad": "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'required': 'required'}),

            'phoneNumber': forms.NumberInput(attrs={'placeholder': 'Contact Number', 'required': 'required'}),

            'schoolName': forms.TextInput(attrs={'placeholder': 'College Name', 'required': 'required'}),

            'address': forms.Textarea(attrs={'placeholder': 'Address', 'required': 'required', 'class': 'form-control'}),

            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': 'required'}),

            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'required': 'required'}),

            'city': forms.TextInput(attrs={'placeholder': 'Country', 'required': 'required'}),

            'courseName': forms.TextInput(attrs={'placeholder': 'Course'}),

            'yearGrad': forms.NumberInput(attrs={'placeholder': 'Year Of Graduation', 'required': 'required'}),

            'gender': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),

            'topicPref1': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref2': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref3': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
        }
