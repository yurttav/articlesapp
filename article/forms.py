from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    #form oluşturmada kolay metot, class göre model oluşturma, detaylar için internet modelform django
    class Meta:
        model = Article
        fields = ["title","content","image"]
  