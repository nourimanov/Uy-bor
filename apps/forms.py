from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from apps.models import Agent, Blog, Property, TextToProperty, Email, Comment


class AgentRegisterForm(ModelForm):
    confirm_password = CharField(max_length=255)

    class Meta:
        model = Agent
        fields = ['username', 'image', 'fullname', 'phone', 'email', 'about', 'instagram', 'linkedin', 'password', 'confirm_password']

    def clean_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "The two password fields didn’t match.",
                code="password_mismatch",
            )
        return make_password(password1)


class AgentLoginForm(AuthenticationForm):
    pass


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['image', 'plan_image', 'name', 'about', 'location', 'area', 'room', 'floor', 'price', 'author']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'category', 'about', 'author']


class TextCategoryForm(ModelForm):
    class Meta:
        model = TextToProperty
        fields = ['image', 'fullname', 'text', 'to_category']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['fullname', 'email', 'text', 'to_blog']


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'email', 'text']


