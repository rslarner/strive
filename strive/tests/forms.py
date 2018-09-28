from django.forms import ModelForm
from .models import UserQuestion, UserTest


class UserTestForm(ModelForm):
    class Meta:
        model = UserTest
        fields = ['test']


class UserQuestionForm(ModelForm):
    class Meta:
        model = UserQuestion
        fields = ['question', 'answer']

