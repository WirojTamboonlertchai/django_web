from django.shortcuts import render
import datetime
from .forms import ContactForm, SharingForm
from django.http import HttpResponseNotFound, Http404
from django.conf import settings
# Create your views here.

def social(request):
	if request.method == 'POST':
		form = SharingForm(request.POST, request.FILES) #ต้องเพิ่ม request.FILES ลงไปด้วย เพราะมีการเพิ่มไฟล์
		if form.is_valid():
			for field in request.FILES.keys(): #มี field อะไรบ้าง หนึ่งในนั้นคือ photo
				for formfile in request.FILES.getlist(field): #มี attr อะไรบ้าง หนึ่งในนั้นก็คือ attr ที่ชื่อว่า name
					save_uploaded_file_to_media_root(formfile) #เรียกใช้ฟังก์ชันเพื่ออัปโหลดและบันทึกไฟล์ไปยัง media root
				return render(request, 'myapp/social.html')
	else:
		form = SharingForm()
	return render(request, 'myapp/social.html', {'form': form})

def save_uploaded_file_to_media_root(f):
	with open('%s%s'% (settings.MEDIA_ROOT,f.name),'wb+') as destination:
		for chunk in f.chunks(): #ในกรณีที่ไฟล์มีขนาดใหญ่
			destination.write(chunk)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
		#return render(request, 'myapp/about/contact.html', {'form': form})
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			comment = form.cleaned_data.get('comment')
			topic = form.cleaned_data.get('topic')
			dep = form.cleaned_data.get('dep')
			pri = form.cleaned_data.get('pri')
			date = form.cleaned_data.get('date')

			context = {
				'name': name,
				'email': email,
				'comment': comment,
				'topic': topic,
				'dep': dep,
				'pri': pri,
				'date': date,
			}
			return render(request, 'myapp/thankyou.html', context)
	else:
		form = ContactForm()
	return render(request, 'myapp/about/contact.html', {'form': form})


def index(request):
	# JSON, Dictionaries, or Object
	context = { 
		'first_name': 'Wiroj',
		'last_name':  'Tamboonlertchai',
		'birth_date': datetime.datetime(2000, 9, 21, 10, 0, 0),
		'addr': {
			'home':'Klong 1 Klongluang Pathumthani',
			'present':'Klong 2 Klongluang Pathumthani',
			'work':'Din Daeng Bangkok',
		},
		'text': "Joel is a slug,",
		'my_num': 21,
		'e_mail': 'wiroj.tam@cpc.ac.th',
		'logged_in': True,
		'subject': ['Database', 'Programming', 'Web'],
		'web': [
			{'label':'Facebook', 'url':'https://www.facebook.com'},
			{'label':'Google', 'url':'https://www.google.com'},
			{'label':'Stack Overflow', 'url':'https://www.stackoverflow.com'},
		],
		'book': [
			{'title':'I Love Liverpool', 'author':{'name':'Amanda', 'age':30}, 'publish_year':2000},
			{'title':'Man U', 'author':{'name':'John', 'age':47}, 'publish_year':2010},
			{'title':'Burirum U', 'author':{'name':'Oman', 'age':39}, 'publish_year':2020},
		],
	}
	return render(request, "myapp/index.html", context)

def add(request, num_a, num_b):
	total = num_a + num_b
	context = {
		'num_a': num_a,
		'num_b': num_b,
		'total': total,
	}
	return render(request, 'myapp/add.html', context)

def overview(request, id = None):
	context = {
		'products': [
			{
				'p_id'			: 1,
				'p_name'		: 'A',
				'p_desc'		: 'abc',
				'p_image'		: ['1.jpg'],
				'p_price'		: 500,
				'p_sale'		: 750,
				'store_name'	: 'Toei\'s store',
				'vendor'		: 'Wiroj Tamboonlertchai',
				'insert_date'	: datetime.datetime(2000, 9, 21, 10, 0, 0),
				'update_date'	: '',
			},
			{
				'p_id'			: 2,
				'p_name'		: 'B',
				'p_desc'		: 'abc',
				'p_image'		: ['1.jpg'],
				'p_price'		: 500,
				'p_sale'		: 750,
				'store_name'	: 'Toei\'s store',
				'vendor'		: 'Wiroj Tamboonlertchai',
				'insert_date'	: datetime.datetime(2000, 9, 21, 10, 0, 0),
				'update_date'	: '',
			},			
		],
	}

	if id == "":
		return render(request, 'myapp/overview.html', context)

	return render(request, 'myapp/product.html', { 'p': context['products'][id-1] } )



def news(request, p = None):
	
	context = {
		'news': {
			'p1': {
				'id': 'A001',
				'desc': 'abcdefg',
			},
			'p2': {
				'id': 'A002',
				'desc': 'hijklmn',
			},			
		}
	}

	if p == None:
		return render(request, 'myapp/news.html', context)

	try:
		return render(request, 'myapp/news.html', { 'n': context['news'][p] })
	except KeyError as e:
		raise Http404("Page does not exist")