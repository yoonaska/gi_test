from django.shortcuts import render
from django.views import View

class HomeView(View):
    def __init__(self):
        self.context = {}
        self.context['title'] = 'Dashboard'
        
    def get(self, request, *args, **kwargs):
        return render(request, "dashbord.html", self.context)
