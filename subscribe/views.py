from .forms import RegisterForm
from django.views.generic.edit import FormView

# Create your views here.
class RegisterView(FormView):
    template_name='subscribe.html'
    form_class = RegisterForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.register_email()
        return super(RegisterView, self).form_valid(form)

