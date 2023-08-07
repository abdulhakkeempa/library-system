from django import forms

#form for creating,updating Library Members
class LibraryMemberForm(forms.Form):
  email = forms.EmailField(label="email_address",max_length=255)
  full_name = forms.CharField(label="full_name",max_length=100)
  date_of_birth = forms.DateField(label="dob")
