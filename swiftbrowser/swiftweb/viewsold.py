from django.shortcuts import render

from django.shortcuts import render_to_response, redirect,HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("test")
    #render_to_response("template_name, context, content_type, status, using")
