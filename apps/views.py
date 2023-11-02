from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from apps.forms import AgentRegisterForm, AgentLoginForm, PropertyForm, BlogForm, CommentForm, TextCategoryForm, \
    EmailForm
from apps.models import Agent, Property, Blog, Comment, TextToProperty, Email


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        context['agents'] = Agent.objects.all()
        context['blogs'] = Blog.objects.all()
        context['pr_comments'] = TextToProperty.objects.all()
        return context
   

class AgentSingleView(DetailView):
    queryset = Agent.objects.all()
    context_object_name = 'agent'
    template_name = 'agent-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = self.get_object()
        context['properties'] = Property.objects.filter(author_id=agent.pk)
        return context


class AgentGridView(ListView):
    queryset = Agent.objects.all()
    context_object_name = 'agents'
    template_name = 'agents-grid.html'


class PropertySingleView(CreateView, DetailView):
    model = TextToProperty
    form_class = TextCategoryForm
    queryset = Property.objects.all()
    context_object_name = 'property'
    template_name = 'property-single.html'

    def get_success_url(self):
        return reverse('property-single', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prop = self.get_object()
        context['comments'] = TextToProperty.objects.filter(to_category=prop.id)
        return context


class PropertyGridView(ListView):
    queryset = Property.objects.all()
    context_object_name = 'properties'
    template_name = 'property-grid.html'


class BlogSingleView(CreateView, DetailView):
    form_class = CommentForm
    queryset = Blog.objects.all()
    context_object_name = 'blog'
    template_name = 'blog-single.html'

    def get_success_url(self):
        return reverse('blog-single', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        context['comments'] = Comment.objects.filter(to_blog=blog.id)
        return context


class BlogGridView(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog-grid.html'


class ContactView(CreateView):
    form_class = EmailForm
    queryset = Email.objects.all()
    context_object_name = 'email'
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        email_sender = form.save()

        subject = 'Email from {}'.format(email_sender.name)
        sender = email_sender.email
        message = f"from: {sender}\nText: {email_sender.text}"
        recipient_list = ['nourimanov@gmail.com']
        send_mail(subject, message, 'tulqinov571@gmail.com', recipient_list)
        return super().form_valid(form)


class AboutView(ListView):
    queryset = Agent.objects.all()
    context_object_name = 'agents'
    template_name = 'about.html'


class AddPropertyView(CreateView):
    model = Property
    template_name = 'add-property.html'
    form_class = PropertyForm
    context_object_name = 'properties'
    success_url = reverse_lazy('index')


class AddBlogView(CreateView):
    model = Blog
    template_name = 'add-blog.html'
    form_class = BlogForm
    context_object_name = 'blogs'
    success_url = reverse_lazy('index')


class SignUpView(CreateView):
    queryset = Agent.objects.all()
    template_name = 'sign-up.html'
    form_class = AgentRegisterForm
    success_url = reverse_lazy('sign-in')


class SignInView(LoginView):
    form_class = AgentLoginForm
    template_name = 'sign-in.html'
    next_page = reverse_lazy('index')


def logout_view(request):
    logout(request)
    return redirect('index')
