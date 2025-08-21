from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from rest_framework import views, generics
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


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
        context["comments"]
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
        return redirect("post_detail", pk=post.pk)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create.html"
    form_class = PostForm
    success_url = reverse_lazy("post-list")
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

class CommentListView(ListView):
    queryset = Comment.objects.all()
    seriali
    
    # Registration view
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

