from django.shortcuts import HttpResponse

# Create your views here.


def demo(request):
    return HttpResponse("Inside View")
