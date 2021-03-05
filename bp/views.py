from django.shortcuts import render
from django.views import generic
from . import models

class Index(generic.TemplateView):

    template_name='bp/index.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['students']= models.studentNumber.objects.all()
        context['date']=     models.Date.objects.all()
        context['exercise']= models.exercises.objects.all()
        context['scores']=   models.score.objects.all()
        return context

class studentslistView(generic.ListView):

    model=models.studentNumber
    template_name='bp/students_list.html'

class exerciseUpload(generic.TemplateView):

    template_name='bp/upload.html'

class login(generic.TemplateView):

    template_name='bp/login.html'
#def index(request):
#    students=  models.studentNumber.objects.all()
#    date=      models.Date.objects.all()
#    exercise=  models.exercises.objects.all()
#    scores=    models.score.objects.all()

#    return render(
#        request,
#        'bp/index.html',
#        context={'students':students,'date':date,'exersise':exercise,'scores':scores}
#    )
