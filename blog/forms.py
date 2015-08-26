__author__ = 'think'
from django import  forms
from .models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)
        widgets = {'text':forms.Textarea(attrs={'rows':15}),}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','email','text')
        widgets = {
            'text':forms.Textarea(attrs={'rows':7}),
        }