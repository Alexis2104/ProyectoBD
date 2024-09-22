from django.shortcuts import render

from django.views import generic



class Home(generic.TemplateView):
    template_name = 'base/base.html'

    def get(self, request, *args, **kwargs):
        print("La vista Home ha sido llamada.")
        return super().get(request, *args, **kwargs)
