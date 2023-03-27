from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def greet(request):
    if request.method== 'GET':
        greet = 'Public Tenant'
        return Response(greet)

@api_view(['GET','POST'])
def greet123(request):
    if request.method== 'GET':
        ss='fdlksfjksdlfjdjkflsdjkfjdkslfdklsfkldsfjkdsjklfdsfdskjnfjsdknjsadngjdsngdsm,g'
        greet = 'gfdklgnfdlkgnfdk Tenant Git checkupgdsjghsjkgnsadghjksdgsahd'
        return Response(greet) gfdglkfkdgg

