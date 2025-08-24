from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            'tags': TagWidget(),
        }
 # Override save() so author is automatically set

    def save(self, commit=True, user=None):
        post = super().save(commit=False)
        if user:
            post.author = user
        if commit: 
            post.save()
        return post
    
    # def  is_valid(self):
    #     tag = self.is_valid.

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email has already been registered')
        return email
    
#Form setup for comment section:
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        # fields = ['post', 'author', 'content', 'created_at', 'updated_at']

        def clean_content(self):
            content = self.clean_content.get()
            if len(content) < 5:
                raise forms.ValidationError("Length too short")
            return content

        # def clean_content(self):
        #     content = self.clean_content.get()
        #     if len(content) < 5:
        #         raise forms.ValidationError('Text too short')
        #     return content

    