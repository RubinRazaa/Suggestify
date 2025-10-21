from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Suggestion,Comment
from django.urls import reverse_lazy, reverse
from . import forms
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    suggestions = Suggestion.objects.all().order_by('created_at')
    return render(request, 'suggestions/home.html', {'suggestions': suggestions})
    

class SuggestionCreateView(LoginRequiredMixin, CreateView):
    model = Suggestion
    fields = ['title', 'description']
    template_name = 'suggestions/create.html'
    success_url = reverse_lazy('suggestion:home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class Signup(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('suggestion:login')
    template_name = 'suggestions/signup.html'
    
    
class SuggestionDetailView(DetailView):
    model = Suggestion
    template_name = 'suggestions/suggestion_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.suggestion = self.object
            comment.save()
            return redirect('suggestion:detail', pk=self.object.pk)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
    
class SuggestionDeleteView(DeleteView):
    model = Suggestion
    template_name = 'suggestions/suggestion_confirm_delete.html'
    success_url = reverse_lazy('suggestion:home')
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'suggestions/suggestion_confirm_delete.html'
    success_url = reverse_lazy('suggestion:home')
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)
    
    
@login_required
def toggle_upvote(request, suggestion_pk ,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user in comment.upvote.all():
        comment.upvote.remove(request.user)
    else:
        comment.upvote.add(request.user)
    return redirect('suggestion:detail',pk= suggestion_pk)