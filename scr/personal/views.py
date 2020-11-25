from django.shortcuts import render
from personal.models import Question

# Create your views here.
def home_screen_view(request):
   # list_of_value=[]
    #list_of_value.append("first")
    #ist_of_value.append("second")
   # list_of_value.append("third")
    #list_of_value.append("fourth")
    questions = Question.objects.all()

    context = {
    #'some_text': "this is how we pass the data",
   # 'some_num':12345,
   # 'list_of_value': list_of_value
   'questions' : questions
    }

    return render(request,"personal/home.html",context)