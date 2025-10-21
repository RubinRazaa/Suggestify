from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = 'suggestion'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.SuggestionCreateView.as_view(), name='create'),
    path('login/', auth_views.LoginView.as_view(template_name='suggestions/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='suggestion:home'),name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('suggestion/<int:pk>/', views.SuggestionDetailView.as_view(), name='detail'),
    path('suggestion/<int:pk>/delete', views.SuggestionDeleteView.as_view(), name='suggestion_delete'),
    path('suggestion/<int:pk>/Cdelete', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('suggestion/<int:suggestion_pk>/comment/<int:comment_pk>/upvote/', views.toggle_upvote, name='upvote'),
]
