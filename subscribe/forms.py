from django import forms
from django.core.mail import send_mail

class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    name = forms.CharField(label = 'First and Last Name', max_length=100)
    human = forms.BooleanField(label='Are you a human?', required=True)

    def register_email(self):
            form_data = self.cleaned_data
            
                
            send_mail(
                    '',
                    'ADD DHGROUP ' + form_data['email'] + ' ' +
                    form_data['name'],
                    'dhi@princeton.edu',
                    ['listserv@princeton.edu'],
                    fail_silently=False,
                    )

