from django import forms
class ColourForm(forms.Form):
    images = forms.ImageField(error_messages={'invalid_image':"It seems there is an error with the file."})
    
