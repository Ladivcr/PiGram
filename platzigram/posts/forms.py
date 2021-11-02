"""Post forms"""

#django
from django import forms
#models
from posts.models import Post

class PostForm(forms.ModelForm):
    """post modelo form"""

    class Meta: 
        """form settings"""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
