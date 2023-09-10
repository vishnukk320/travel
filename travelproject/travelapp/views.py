
from django.shortcuts import render


# Create your views here.
def demo(request):
    # name = "aby"
    return render(request, "index.html")


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     resultt = x + y
#     return render(request, "result.html", {'resul': resultt})
