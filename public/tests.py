from django.test import TestCase

# Create your tests here.

@api_view(['GET','POST'])
def greetings(request):
    if request.method== 'GET':
        greet = 'Public'
        return Response(greet)