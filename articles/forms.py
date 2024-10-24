from django import forms

from .models import Article  # On importe le modèle Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # Le modèle auquel le formulaire est lié
        fields = ['titre', 'resume', 'contenu', 'image']  # cham à iclre.forml
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.TextInput(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
        }
