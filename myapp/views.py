from django.shortcuts import render
from excel_to_word import main
from django.http import HttpResponse
from django.http import JsonResponse 
from django.http import FileResponse
from django.contrib import messages
from django.shortcuts import redirect
import glob
import os 
def index(request):
    return render(request, "index.html", locals())


def templates(request):
    file_path  = './convertTemplate.7z'
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
    if request.method == "POST":
        files_excel = request.FILES.get('ExcelData')
        with open(f'./excel_to_word/processingData/{files_excel.name}', 'wb+') as destination:
            for chunk in files_excel.chunks():
                destination.write(chunk)
        files_img = request.FILES.getlist('folderFiles[]')
        for file in files_img:
            with open(f'./excel_to_word/processingData/{file.name}', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        a = main.Cov()
        print(a)
        if a :
            return_file(request)
        else:
            try:
                os.remove('./excel_to_word/alreadyPDF/result.pdf')
                
                files = glob.glob('./excel_to_word/processingData/*.*')
                for file in files:
                    os.remove(file)
            except:
                print('allen huang is stupid')
                files = glob.glob('./excel_to_word/processingData/*.*')
                for file in files:
                    os.remove(file)
        return HttpResponse('return correct',status = 200)
    else:
        return HttpResponse("Invalid request", status=405)
    


# merge test