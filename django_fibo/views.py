from django.http import HttpResponse
from django_fibo.fibonacci import fibonacci
 
def hello(request):
  return HttpResponse("Hello world")
  
def fibo(request, n="1"):
  return HttpResponse(fibonacci(long(n)))
  
