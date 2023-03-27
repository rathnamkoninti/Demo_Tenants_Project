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


@api_view(['GET','POST'])
def greetings(request):
    if request.method== 'GET':
        greet = 'Private Tenant'
        return Response(greet)


@api_view(['GET','POST'])
def greetings1(request):
    if request.method== 'GET':
        with connection.cursor() as cursor:
            cursor.execute(''' select * from private_publictable1''')
            data=dictfetchall(cursor)
            return Response(data)


@api_view(['GET','POST'])
def greetings2(request):
    if request.method== 'GET':
        with connection.cursor() as cursor:
            cursor.execute(''' select * from private_college''')
            data=dictfetchall(cursor)
            return Response(data)


@api_view(['GET','POST'])
def greetings3(request):
    if request.method== 'GET':
        with connection.cursor() as cursor:
            cursor.execute(''' 
                select clg.name as college_name,clg.address,clg.mobile as college_mobile,
                std.student_name  from private_college clg
                inner join private_student std on std.college_id_id=clg.id  ''')
            data=dictfetchall(cursor)
            return Response(data)