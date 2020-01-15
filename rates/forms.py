from django import forms
from .models import Project, Profile, Rating
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm
# from pyuploadcare.dj.models import ImageField

class editForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class createForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'photo', 'link']

class ratingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['usability', 'design', 'content']
        exclude = ['avg']

class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['login'].widget.attrs.update({
            'class': 'form-control'
        })  
        

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

class MyCustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

class MyCustomSetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': '',
            })
         

    def save(self):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save()

        # Add your own processing here.

        # Ensure you return the original result
        return email_address


