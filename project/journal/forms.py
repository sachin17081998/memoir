from django import forms
from .models import user_profile,diary
from django.contrib.auth.models import User

class userform(forms.ModelForm):
     password=forms.CharField(widget=forms.PasswordInput())
     class Meta:
         model=User
         fields=('username','email','password')
         widgets = {
            'username': forms.TextInput(attrs={'class': 'signup-fields'}),
            'email': forms.EmailInput(attrs={'class': 'signup-fields'}),
            'password': forms.PasswordInput(attrs={'class': 'signup-fields'}),
        }
    
class profile_form(forms.ModelForm):
   
    class Meta:
        model=user_profile
        fields=('profile_pic',)
        # gender_choices=(('M','Male'),('F','Female'),('O','Other'))
        # gender=forms.ChoiceField(choices=gender_choices)
        # OPTIONS=(('M','Male'),('F','Female'),('O','Other'))
        # gender = forms.MultipleChoiceField(
        #     choices=OPTIONS,
        #     initial='0',
        #     widget=forms.SelectMultiple(),
        #     required=True,
        #     label='gender',
        # )
        # widgets = {
        #     'profile_pic': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        #     }
class diary_form(forms.ModelForm):   
    class Meta:
        model=diary
        fields=('text',)  
         
        # widgets = {
            
        #     'text': forms.TextInput(attrs={'placeholder':'enter here'}),
           
        # }
class update_form(forms.ModelForm):   
    class Meta:
        model=diary
        fields=('text',) 
        widgets = {
            
             'text': forms.TextInput(),
           
        }     
        
    