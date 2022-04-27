from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import render


def home_view(req):
    return render(req, 'home.html')

@api_view(['GET'])
def getData(request):
    person = [{
        'name':'Anurag Singh',
        'regno':'20BCE11012',
        'CGPA':8.8
    },
    {
        'name':'Anant Dubey',
        'regno':'20BCE11037',
        'CGPA':8.1
    },
    {
        'name':'Ansh Chauhan',
        'regno':'20BCE11016',
        'CGPA':8.4
    },
    {
        'name':'Subhransu Majhi',
        'regno':'20BCE11014',
        'CGPA':8.7
    },
    {
        'name':'Shristi Bhadwar',
        'regno':'20BCE10329',
        'CGPA':9.2
    },
    {
        'name':'Oishi Basak',
        'regno':'20BAI11012',
        'CGPA':9.6
    }]
    return Response(person)