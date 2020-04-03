from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'surname',
            'email'
        ]

    # def clean_name(self, *args, **kwargs):
    #     name = self.cleaned_data.get("name")
    #     if not "radek" in name:
    #         raise forms.ValidationError("This is not a valid name")
    #     return name
    #
    # def clean_email(self,*args,**kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not 'edu' in email:
    #         raise forms.ValidationError("This is not a valid name")
    #     return email