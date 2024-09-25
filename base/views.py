from django.views.generic import TemplateView
from .models import Home, About, Profile, Category, Skills, Portfolio


class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        # Get context data from superclass
        context = super().get_context_data(**kwargs)
        
        # Fetch the latest 'Home' entry
        context['home'] = Home.objects.latest('updated')
        
        context['about'] = About.objects.latest('updated')
        profiles = Profile.objects.filter(about=context['about'])
        
        # Fetch all 'Portfolio' entries
        context['portfolio'] = Portfolio.objects.all()

        # Fetch all categories and their related skills
        context['skills'] = Category.objects.prefetch_related('skills_set').all()

        return context