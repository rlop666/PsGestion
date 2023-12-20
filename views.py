from djando shortcuts import render, HttpResponse

def home(request):
  return HttpResponse("El código HTML que corresponda")

def about(request):
  return HttpResponse("El código HTML que corresponda")
