from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import datetime
from .models import Question # import model
from .forms import QuestionForm, LoginForm
# Create your views here.

def login(request):
    u_name = "session"
    u_pass = "pass123"
    u_id   = 999
    if request.method == 'POST':
        if u_name == request.POST['username'] and u_pass == request.POST['password']:
            request.session['user_id'] = u_id
            return HttpResponse('You\'re logged in.')
        else:
            return HttpResponse('You user and password didn\'t math.')
    else:
        form = LoginForm()
    return render(request, 'polls/login.html', {'form':form})

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse('you\'re logged out.')

def delete(request, question_id):
	b = Question.objects.get(pk=question_id)
	b.delete()
	return HttpResponseRedirect('/polls/')

def edit(request, question_id):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			dy = request.POST['pub_date_year']
			dm = request.POST['pub_date_month']
			dd = request.POST['pub_date_day']
			dt_str = dy + '-' + dm + '-' + dd			
		Question.objects.filter(pk = question_id).update(
			question_text = request.POST['question_text'], 
			pub_date = datetime.strptime(dt_str, '%Y-%m-%d')
		)
		return HttpResponseRedirect('/polls')
	else:
		data = Question.objects.get(pk = question_id)
		initial_dict = {
			'question_text': data.question_text,
			'pub_date': data.pub_date
		}
	form = QuestionForm(request.POST or None, initial = initial_dict)
	context = {'form': form, "id": data.id}
	return render(request, "polls/edit.html", context)

def create(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			dy = request.POST['pub_date_year']
			dm = request.POST['pub_date_month']
			dd = request.POST['pub_date_day']
			dt_str = dy + '-' + dm + '-' + dd
			p = Question.objects.create(
					question_text = request.POST['question_text'],
					pub_date = datetime.strptime(dt_str, '%Y-%m-%d'),
			)
			return HttpResponseRedirect('/polls')
	else:
		form = QuestionForm()
		context = {
			"form": form
		}
	return render(request, "polls/create.html", context)

def index(request):
	# QuerySet API
	# question_list = Question.objects.order_by('-pub_date') # ทำการ Query ข้อมูลในรูปแบบ Set
	question_list = Question.objects.all()
	context = {
		"question_list": question_list
	}
	return render(request, "polls/index.html", context) # process กับ interface จะอยู่แยกกัน
	# return HttpResponse("Hello World!, You're at the polls index.") #proces กับ interface จะอยู่ด้วยกัน

def detail(request, question_id):
	try:
		question = Question.objects.get(id = question_id)
		print(question)
		context = {
			"question": question
		}
	except Question.DoesNotExist:
		raise HttpResponseNotFound('Question does not exist!!')
	return render(request, 'polls/detail.html', context)
	# return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
	resp = "You are looking at the results of question %s."
	return HttpResponse(resp % question_id)

def vote(request, question_id):
	resp = "You are voting on question %s."
	return HttpResponse(resp % question_id)

def about(request):
	return HttpResponse("Hello, world. You're the polls about.")
