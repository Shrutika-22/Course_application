from django.forms import ModelForm
from MyORM.models import *

class TopicForm(ModelForm):
    class Meta:
        model=Topics
        fields="__all__"

class UsersForm(ModelForm):
    class Meta:
        model=Users
        fields="__all__"        

class TopicContentForm(ModelForm):
    class Meta:
        model=TopicContent
        fields="__all__"

class TopicContentCommentsForm(ModelForm):
    class Meta:
        model=TopicContentComments
        fields="__all__"

class LoginForm(ModelForm):
    class Meta:
        model=Users
        fields=["user_name","password"]  

    