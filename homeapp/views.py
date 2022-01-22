from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from registrationapp.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    post=Post.objects.all()
    return render(request, 'homeapp/info.html', {'posts':post})

class PostListView(ListView):
    model=Post
    template_name='homeapp/info.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post

    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False
    success_url='/home'

@login_required
def profile(request):
    if request.method=="POST":    #Need to create the POST request, create the form and save the info by .save() for function-based-view
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your account has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form, 'p_form':p_form}
    return render(request, 'homeapp/profile.html', context)
