from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
def index(request):
    return render(request, "index.html", locals())

def runConvert(request):
    print("Request received")  # 确保请求被接收
    if request.method == "POST":
        print("POST method confirmed")  # 确保请求方法正确
        return HttpResponse("123556")  # 简单返回
    return HttpResponse("Invalid request", status=400)