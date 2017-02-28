from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile, Category


class RegistrationForm(forms.ModelForm):
    username = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):

    accepted_eula = forms.BooleanField(required=True)
    favorite_animal = forms.EmailField(required=False)

    comment = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = UserProfile
        fields = ['accepted_eula', 'favorite_animal']


class UploadFileForm(forms.Form):
    profile = forms.CharField(min_length=5, required=True)
    userpic = forms.FileField()

    ## validation name is number
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 5:
    #         raise ValueError('name is more than five')
    #     return name
    #
    # def clean_text(self):
    #     text = self.cleaned_data['text']
    #     return text


class CategoryForm(forms.ModelForm):
    name = forms.ModelMultipleChoiceField(Category.objects.all(), required=True, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Category
        fields = ['name']


class DreamrealForm(forms.Form):
   website = forms.CharField(max_length = 100)
   name = forms.CharField(max_length = 100)
   phonenumber = forms.CharField(max_length = 50)
   email = forms.CharField(max_length = 100)


