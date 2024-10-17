from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
def index(request):
    return render(request, "index.html", locals())
def runConvert(request):
    if request.method == "POST":
        # main.Cov()
        context = {
        'State': "1",
        }
        render(request, 'index.html', context)
        return HttpResponse("Done Process", status=200)
    else:
        return HttpResponse("Invalid request", status=400)
