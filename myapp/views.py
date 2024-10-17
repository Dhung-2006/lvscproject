from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
from django.http import JsonResponse 
from django.http import FileResponse
import os 
def index(request):
    return render(request, "index.html", locals())
def templates(request):
    file_path  = './convertTemplate.zip'
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=False)
        response['Content-Type'] = 'application/zip'
        # response['Content-Disposition'] = f'attachment;filename={file_path}'
        return response
def return_file(request):
    file_path  = './excel_to_word/alreadyPDF/result.pdf'
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=False)
        response['Content-Type'] = 'application/pdf'
        # response['Content-Disposition'] = f'attachment;filename={file_path}'
        return response
    else:
        return HttpResponse("File not found.", status=404)
    # return HttpResponse('return correct',status = 200)
def runConvert(request):
    # print(request)
    if request.method == "POST":
        main.Cov()
        # print("main.cov")
        return_file(request)
        return HttpResponse('return correct',status = 200)
    else:
        print("fk this")
        return HttpResponse("Invalid request", status=405)
    


# merge test