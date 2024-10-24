
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


from articles.forms import ArticleForm
from articles.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})


def useradmin(request):
    articles = Article.objects.all()  # Recupère les art
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)  # Crée l'instce mais n l'egt ps
            article.auteur = request.user  # Associe l'user connecté à larticle
            article.save()  # Enregistre l'article en base de données
            messages.success(request, 'Article ajouté avec succès !')
            return redirect('useradmin')  # Redirige vers lq pqge admin
    else:
        form = ArticleForm()  # Formulaire vide si la réquête est GET

    return render(request, "useradmin.html", {'form': form, 'articles': articles})


def new_article(request):
    return render(request, "new_article.html")


def modifier_article(request, id):
    # Recupérer l'article à partir de son ID (pk)
    article = get_object_or_404(Article, id=id)  # Recupère les art
    if request.method == 'POST':
        # Pré-remplir le formulaire avec les données existantes et les mdfc
        edit_form = ArticleForm(request.POST, request.FILES, instance=article)

        if edit_form.is_valid():
            edit_form.save()  # Enregistre les modifications
            return redirect('useradmin')  # Redirige vers la page d'admt ou autre page
    else:
        # Pré-remplir le formulaire avec les données existances si GET
        edit_form = ArticleForm(instance=article)

    return render(request, 'edit_article.html', {'edit_form': edit_form, 'article': article})


def supprimer_article(request, id):
    article = get_object_or_404(Article, pk=id)  # Récupérer l'article ou afficher 404
    article.delete()  # Supprimer l'article de la base de donnée
    messages.success(request, 'Article supprimé avec succès !')  # Message de succès
    return redirect('useradmin')  # Rediriger vers la page admin

# form = ArticleForm(request.POST)
# article = form.save(commit=False)  # Crée l'instce mais n l'egt ps
# article.auteur = request.user  # Associe l'user connecté à larticle
# article.save()  # Enregistre l'article en base de données
# messages.success(request, 'Article ajouté avec succès !')
# return redirect('useradmin')  # Redirige vers lq pqge admin
# else:
# form = ArticleForm()
# Formulaire vide si la réquête est GET
# return render(request, "useradmin.html", {'form': form, 'articles': articles})


# def new_article(request):
# auteur=request.user
# titre=request.POST['titre']
# contenue=request.POST['contenue']
# resume=request.POST['resume']
# if titre and contenue and resume:
# article=Article.objects.create(auteur= auteur, titre=titre, resume=resume, contenue=contenue)
# article.save()
# messages.success(request, 'Article ajouté avec succès !')
# return redirect('ajouter_article')
# else:
# messages.error(request, 'Tous les champs doivent être remplis')
# return render(request, "new_article.html")
