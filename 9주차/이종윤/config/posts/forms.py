from django import forms
from posts.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "댓글 달기...",
                    "rows": 1,  # rows를 1로 설정
                    "style": "resize: none; height: 40px; width: calc(100% - 90px);"
                }
            )
        }
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields =[
            "content",
        ]
