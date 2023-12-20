from djando shortcuts import render, HttpResponse

def home(request):
  return render(response, 'home.html')

def about(request):
  return render(response, 'about.html')
