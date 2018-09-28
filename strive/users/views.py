from django.views.generic.edit import FormView

from .forms import UserForm


class UserView(FormView):
    template_name = 'contact.html'
    form_class = UserForm
    success_url = '/tests/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        result = super().form_valid(form)
        return result
