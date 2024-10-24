from django.conf import settings
from django.urls import path
from .views import home, useradmin, new_article, modifier_article, supprimer_article
from django.conf.urls.static import static

urlpatterns = [

    path("", home, name="home"),
    path("useradmin/", useradmin, name="useradmin"),
    path("editarticle/<int:id>/", modifier_article, name='update'),
    path('supprimer_article/<int:id>/', supprimer_article, name='supprimer_article'),
    path("useradmin/new_article", new_article, name="new"),
    # path('about/', about, name='about'),
    # path('contact/', contact, name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
