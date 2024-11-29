from django import forms
from .page_models import PageComment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = PageComment
        fields = ('author', 'comment_body')
