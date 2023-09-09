from django import forms
from .models import BlogContent

class BlogContentForm(forms.ModelForm):
    
    class Meta:

        model = BlogContent
        fields = '__all__'
        widgets = {
            'author' : forms.Select(attrs={'class':'form-control'}),
            'blog_title' : forms.TextInput(attrs={'class':'form-control'}),
            'blog_content' : forms.Textarea(attrs={'class':'form-control'}),
        }
