from django.urls import path
from front_end import views
from django.views.generic import TemplateView

app_name = 'front_end'

urlpatterns = [
    path("", views.home, name='home'), # Eli
    # Class-based TemplateViews: https://docs.djangoproject.com/en/4.2/topics/class-based-views/
    path("resources/", TemplateView.as_view(template_name="front_end/resources.html"), name='resources'),
    path("contact/", TemplateView.as_view(template_name="front_end/contact.html"), name='contact'), # Sean
    path("about/", TemplateView.as_view(template_name="front_end/about.html"), name='about'), # Sean
    path("sponsors/", TemplateView.as_view(template_name="front_end/sponsors.html"), name='sponsors'), # Julian


    path("alumni/", TemplateView.as_view(template_name="front_end/alumni.html"), name='alumni'), # Devan
    path("clubs/", TemplateView.as_view(template_name="front_end/clubs.html"), name='clubs'), # Ben
    path("clubs/wicys", TemplateView.as_view(template_name="front_end/wicys.html"), name='wicys'), # Rhea
    path("clubs/ctf", TemplateView.as_view(template_name="front_end/ctf.html"), name='ctf'), # Marina

    path("teams/", TemplateView.as_view(template_name="front_end/teams.html"), name='teams'),
    path("teams/ccdc", TemplateView.as_view(template_name="front_end/ccdc.html"), name='ccdc'), # Ryan
    path("teams/cptc", TemplateView.as_view(template_name="front_end/cptc.html"), name='cptc'), # Areeb
    path("teams/ncae", TemplateView.as_view(template_name="front_end/ncae.html"), name='ncae'), # Alec
    path("teams/cyberforce", TemplateView.as_view(template_name="front_end/cyberforce.html"), name='cyberforce'),
]