from django.views.generic.edit import FormView

from .forms import UserQuestionForm, UserTestForm


class UserTestView(FormView):
    template_name = 'user_test.html'
    form_class = UserTestForm
    success_url = '/tests/questions/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        result = super().form_valid(form)
        return result


class UserQuestionView(FormView):
    template_name = 'user_question.html'
    form_class = UserQuestionForm
    success_url = '/tests/questions/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        result = super().form_valid(form)
        return result


