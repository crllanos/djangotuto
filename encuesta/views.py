from django.http 		import HttpResponse
from django.shortcuts 	import render
from django.template 	import loader

from .models import Question

"""def index(req):
    return HttpResponse('<title>tutorial Django</title>Hola poh <b>machucao</b> # req: ' + str(req))"""
"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '-'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output + ' //Esas fueron')"""

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('encuesta/index.html')
	return HttpResponse(template.render({'latest_question_list': latest_question_list,}
    								  , request))

def detail(request, question_id):
    return HttpResponse("Buscando pregunta nro %s." % question_id)

def results(request, question_id):
    return HttpResponse("Resultados de pregunta nro %s." % question_id)

def vote(request, question_id):
    return HttpResponse("Votacion sobre encuesta nro %s." % question_id)