from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from rest_framework import views, generics
from .models import Post
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from django.views.generic import View, UpdateView, DeleteView
# from rest_framework import views, generics
from .forms import PostForm, CommentForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, redirect

# from django.shortcuts import get_list_or_404, redirect


#CRUD operations for Post
class PostListView(ListView):
    model = Post
    template_name = "blog/list.html"
    # authenticated_class = [TokenAuthentication]
    # permission_class = IsAuthenticated
    

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    # authenticated_class = [TokenAuthentication]
    # permission_class = IsAuthenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context["comments"] =comments
        context["comment_form"] = CommentForm()
        return context
    
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect("post-detail", pk=post.pk)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create.html"
    form_class = PostForm
    success_url = reverse_lazy("post-list")
    # success_url = '/'  # change to wherever you want

    # authentication_class = [TokenAuthentication]
    # permission_class = [IsAuthenticated]


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/update.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
#CRUD Operation for Comments

# class CommentListView(ListView):
#     queryset = Comment.objects.all()
#     serializer_class =


class CommentListView(ListView):
    """Display all comments (optional, mostly for debugging)"""
    model = Comment
    template_name = "blog/comment_list.html"
    context_object_name = "comments"

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name ='blog/comment_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    # Registration view

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().author 
    
    def get_success_url(self):
        return self.object.post.get_absloute_url()



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after registration
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

class PostSearchListView(ListView):
    model = Post
    template_name = "blog/search.html"
    content_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get('q')
        query_set = Post.objects_all()
        
        if query:
            query_set = query_set.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return query_set
    

# Login view
class CustomLoginView(LoginView):
    template_name = "blog/login.html"

# Logout view
class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"

# Profile view
@login_required
def profile(request):
    return render(request, "blog/profile.html")


# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostCreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = IsAuthenticated

# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

