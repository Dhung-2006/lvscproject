from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
from django.http import JsonResponse 
def index(request):
    return render(request, "index.html", locals())
def runConvert(request):
    if request.method == "POST":
        # main.Cov()
        context = {
            'file':'result.pdf'
        }
        return JsonResponse(context)
    else:
        return HttpResponse("Invalid request", status=400)
        

# merge test