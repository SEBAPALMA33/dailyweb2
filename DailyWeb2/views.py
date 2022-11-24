from django.http import HttpResponse
from django.template import Template, Context


def index(request):

    plantillaExterna= open("C:/Users/sebas/Desktop/DailyWeb2/DailyWeb2/plantillas/index.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto=Context()
    documento=template.render(contexto)

    return HttpResponse(documento)