from django import forms

class upload_file_form(forms.Form):
    doc = forms.FileField(required=True)