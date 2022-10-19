from django.shortcuts import render

# Create your views here.
def show_personal(request):
    return render(request, "personal.html")

def tailwind(request):
    return render(request, 'index.html')