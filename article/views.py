from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse #comment ekleme redirect için
from django.contrib import messages
from .forms import ArticleForm
from .models import Article, Comment
#login olmadan işlem yapmayı engellemek için yaptık
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse("Anasayfa")
    context = {
        "number1":7,
        "number2":10
    }
    #return render(request, "index.html",{"number":7})#content sözlük olarak verilmesi lazım
    return render(request, "index.html",context)#content sözlük olarak verilmesi lazım

def about(request):
    return render(request, "about.html")
"""
def detail(request,id):
    #return render(request, "about.html")
    return HttpResponse("Detail:"+str(id))
"""

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url = "user:login")
def addArticle(request):
    #Resim alanı ekledik, bunun için aşağıdaki gibi ekleme yaptık
    #form = ArticleForm(request.POST or None)
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla kayıt edildi...")
        return redirect("index")

    context = {
        "form" : form
    }
    return render(request, "addarticle.html",context)

def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)

    comments = article.comments.all()

    context = {
        "article":article,
        "comments":comments
    }
    return render(request, "detail.html", context)

@login_required(login_url = "user:login")
def update(request, id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncellendi...")
        return redirect("index")

    context = {
        "form":form
    }
    return render(request, "update.html", context)

@login_required(login_url = "user:login")
def delete(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request,"Makale başarıyla silindi...")
    return redirect("article:dashboard")

def articles(request):
    #arama fonksiyonu için ekledik
    #Arama işlemini klasik form ve get kullanarak değişik bir şekilde yaptık, action ve method = post parametrelerini sildik. 
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
    else:
        articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request, "articles.html", context)

#Yorum Ekleme
def addComment(request, id):
    article = get_object_or_404(Article, id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    #return redirect("/articles/article/" + str(id))
    #dinamik url redirect edilirken reverse kullanmak gerekiyor
    return redirect(reverse("article:detail", kwargs={"id":id}))


