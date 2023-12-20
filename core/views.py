from djando shortcuts import render, HttpResponse

def home(request):
  return render(response, "core/home.html")

def about(request):
  return render(response, "core/about.html")
