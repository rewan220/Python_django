from django.shortcuts import render
from snippet_test.models import SnippetTest

# Create your views here.
def snippet_test_view(request):

    snippet_test = SnippetTest.objects.all()
    context = {
   
   'snippet_test' : snippet_test

    }

    return render(request,"snippet_test/snippet_home.html",context)