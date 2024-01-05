from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def foodmenu(request):
    return render(request,'foodmenu.html')
def category(request):
    return render(request,'category.html')
def mandhi(request):
    return render(request,'mandhi.html')
def Desserts(request):
    return render(request,'Desserts.html')
def Juices(request):
    return render(request,'Juices.html')
def testimony(request):
    return render(request,'testimony.html')
def contact(request):
    return render(request,'contact.html')
