from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
def index(request):
    return render(request, "index.html", locals())

def runConvert(request):
    if request.method == "POST":
        main.Cov()
<<<<<<< HEAD
        return HttpResponse("123556")  # 简单返回
    return HttpResponse("Invalid request", status=400)
=======
        return HttpResponse("123556")
    return HttpResponse("Invalid request", status=400)
>>>>>>> f1da90f5d24d6b0f3b763fa9bf05e35fdc61e7ad
