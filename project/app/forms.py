from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField , PasswordChangeForm , PasswordResetForm ,SetPasswordForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import widgets
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation
from django.core.validators import MaxValueValidator, MinValueValidator 
from .models import Student
YES_OR_NO = (
    ('yes','yes'),
    ('no','no'),
)
certifications = (
    ('shell programming','shell programming'),
    ('machine learning','machine learning'),
    ('app development','app development'),
    ('python','python'),
    ('r programming','r programming'),
    ('information security','information security'),
    ('hadoop','hadoop'),
    ('distro making','distro making'),
    ('full stack','full stack'),
)
skills = (
    ('poor','poor'),
    ('medium','medium'),
    ('excellent','excellent'),
)
subject = (
    ('cloud computing','cloud computing'),
    ('networks','networks'),
    ('hacking','hacking'),
    ('Computer Architecture','Computer Architecture'),
    ('parallel computing','parallel computing'),
    ('IOT','IOT'),
    ('data engineering','data engineering'),
    ('Software Engineering','Software Engineering'),
    ('Management','Management'),
)
career = (
    ('system developer','system developer'),
    ('Business process analyst','Business process analyst'),
    ('developer','developer'),
    ('testing','testing'),
    ('security','security'),
    ('cloud computing','cloud computing'),
)
studies = (
    ('higherstudies','higherstudies'),
    ('job','job')
)
companies =(
    ('Web Services','Web Services'),
    ('SAaS services','SAaS services'),
    ('Sales and Marketing','Sales and Marketing'),
    ('Testing and Maintainance Services','Testing and Maintainance Services'),
    ('product development','product development'),
    ('BPA','BPA'),
    ('Service Based','Service Based'),
    ('Product based','Product based'),
    ('Cloud Services','Cloud Services'),
    ('Finance','Finance'),
)
books = (
    ('Prayer books','Prayer books'),
    ('Childrens','Childrens'),
    ('Travel','Travel'),
    ('Romance','Romance'),
    ('Cookbooks','Cookbooks'),
    ('Self help','Self help'),
    ('Drama','Drama'),
    ('Math','Math'),
    ('Religion-Spiritality','Religion-Spiritality'),
    ('Anthology','Anthology'),
    ('Trilogy','Trilogy'),
    ('Autobiographies','Autobiographies'),
    ('Mystery','Mystery'),
    ('Diaries','Diaries'),
    ('Journals','Journals'),
    ('History','History'),
    ('Art','Art'),
    ('Dictionaries','Dictionaries'),
    ('Horror','Horror'),
    ('Encyclopedias','Encyclopedias'),
    ('Action and Adventure','Action and Adventure'),
    ('Fantasy','Fantasy'),
    ('Comics','Comics'),
    ('Science fiction','Science fiction'),
    ('Series','Series'),
    ('Guide','Guide'),
    ('Biographies','Biographies'),
    ('Health','Health'),
    ('Satire','Satire'),
    ('Science','Science'),
    ('Poetry','Poetry'),
    
)
behaviour = (
    ('stubborn','stubborn'),
    ('gentle','gentle'),
)
management_technical = (
    ('Technical','Technical'),
    ('Management','Management'),
)
worker = (
    ('smart worker','smart worker'),
    ('hard worker','hard worker'),
)


class StudentRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(label = _("Email"),max_length=250,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))


class Test(forms.Form):
    academic_percentage_in_operating_system = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_algorithm = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_programming_concepts = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_software_engineering = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_computer_networks = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_electronics_subjects = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_computer_architecture = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_mathematics = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_communication_skills = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    how_many_hours_in_a_day_you_can_work = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)])
    Rate_your_logical_quotient=forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    How_may_hackathon_have_you_participated=forms.IntegerField()
    Rate_your_coding_skills=forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    Rate_your_public_speaking=forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    can_work_long_time_before_system = forms.ChoiceField(choices = YES_OR_NO)
    self_learning_capability = forms.ChoiceField(choices=YES_OR_NO)
    which_certifications_do_you_prefer = forms.ChoiceField(choices=certifications)
    any_talenttests_taken= forms.ChoiceField(choices=YES_OR_NO)
    scale_your_reading_and_writing_skills = forms.ChoiceField(choices=skills)
    scale_your_memory_capability_score = forms.ChoiceField(choices=skills)
    Interested_subjects = forms.ChoiceField(choices=subject)
    interested_career_area = forms.ChoiceField(choices=career)
    what_do_you_prefer_job_or_higher_studies = forms.ChoiceField(choices=studies)
    type_of_company_you_prefer = forms.ChoiceField(choices=companies)
    intereaction_with_seniors = forms.ChoiceField(choices=YES_OR_NO)
    do_you_love_games = forms.ChoiceField(choices=YES_OR_NO)
    type_of_books_you_prefer = forms.ChoiceField(choices=books)
    most_likely_behaviour = forms.ChoiceField(choices=behaviour)
    what_you_prefer_managemet_or_technical = forms.ChoiceField(choices= management_technical)
  
    have_you_ever_worked_with_teams = forms.ChoiceField(choices=YES_OR_NO)
    Are_you_an_Introvert= forms.ChoiceField(choices=YES_OR_NO) 







