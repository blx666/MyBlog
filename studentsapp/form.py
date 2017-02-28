
from django import forms
from studentsapp.models import *


class FileForm(forms.Form):

    ExcelFile = forms.FileField(allow_empty_file=True)
#
# class FileFormModel(forms.ModelForm):
#     class Meta:
#         model = UploadFile
#         fields = ['message']