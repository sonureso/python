from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	status = "How are you!"
	msg = "We need to meet as early as possible."
	return render(request,'hello.html',{"status":status,"msg":msg})
	#Passing the argument in dictionary format of variables used in html.
	
def question(request):
	que = "What to do?"
	return render(request,'question.html',{'que':que})
	

