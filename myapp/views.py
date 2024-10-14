from django.shortcuts import render
from excel_to_word import main
# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def click_button():
    main.Cov()