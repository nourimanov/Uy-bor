from django.conf.urls.static import static
from django.urls import path
from config import settings
from apps.views import (IndexView, AgentSingleView, AgentGridView, PropertySingleView, PropertyGridView,
                        BlogSingleView, BlogGridView, ContactView, AboutView, SignUpView, SignInView, logout_view,
                        AddPropertyView, AddBlogView)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('agent-single/<int:pk>', AgentSingleView.as_view(), name='agent-single'),
    path('agent-grid', AgentGridView.as_view(), name='agent-grid'),
    path('property-single/<int:pk>', PropertySingleView.as_view(), name='property-single'),
    path('property-grid', PropertyGridView.as_view(), name='property-grid'),
    path('blog-single/<int:pk>', BlogSingleView.as_view(), name='blog-single'),
    path('blog-grid', BlogGridView.as_view(), name='blog-grid'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('sign-up', SignUpView.as_view(), name='sign-up'),
    path('sign-in', SignInView.as_view(), name='sign-in'),
    path('log-out', logout_view, name='log-out'),
    path('add-property', AddPropertyView.as_view(), name='add-property'),
    path('add-blog', AddBlogView.as_view(), name='add-blog'),

]

