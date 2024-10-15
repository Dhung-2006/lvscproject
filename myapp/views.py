from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
def index(request):
    return render(request, "index.html", locals())

def runConvert(request):
    if request.method == "POST":
        main.Cov()
        return HttpResponse("123556")
    return HttpResponse("Invalid request", status=400)