from django.shortcuts import render, HttpResponse
from .models import msgs, news, faq, circular, photos, messages, faculty, Category, Apply_for, Registeration, downloads, examination_system
# Create your views here.


def index(request):
	obj=msgs.objects.all().order_by('-id').values()
	newses=news.objects.all().order_by('-id').values()
	tmp=news.objects.all().count()
	tmplist=[]
	for i in range(tmp):
		tmplist.append(i)
	return render(request, "index.html", {'data':obj, 'news': newses,'tmp':tmplist})


def faqfunc(request):
	data=faq.objects.all()
	return render(request, "faq.html", {'data':data})

def examinationfunc(request):
	data=examination_system.objects.all()
	return render(request, "examination.html",{"data":data})


def download(request):
	obj=downloads.objects.all().order_by("-id")
	return render(request, "download.html", {'data':obj})


def registeration(request):
	obj=Registeration()
	if request.method=='POST':
		name=request.POST.get("name")
		fathername=request.POST.get("fathername")
		address=request.POST.get("address")
		cnic=request.POST.get("cnic")
		hsc_board=request.POST.get("hscboard")
		hsc_percentage=request.POST.get("hscpercentage")
		domicile=request.POST.get("domicile")
		phone=request.POST.get("phone")
		email=request.POST.get("email")
		is_questian=request.POST.get("isquestian")
		department=request.POST.get("department")
		course=request.POST.get("course")

		try:
			front=request.FILES.get("cnicfront")
			back=request.FILES.get("cnicback")
		except:
			pass

		if not is_questian:
			is_questian=False
		
		obj.name=name
		obj.fathername=fathername
		obj.address=address
		obj.cnic=cnic
		obj.hsc_board=hsc_board
		obj.hsc_percentage=hsc_percentage
		obj.domicile=domicile
		obj.phone=phone
		obj.email=email
		obj.is_questian=is_questian
		obj.department=department
		cat=Apply_for.objects.filter(Category=course)
		for i in cat:
			tmp=i
		obj.Applied_For=tmp
		obj.cnic_front=front
		obj.cnic_back=back
		
		obj.save()

	cat=Apply_for.objects.all()
	return render(request, "registeration.html", {'cat':cat})




def facultyinfo(request):
	Id=request.GET.get("id")
	fac=faculty.objects.filter(id=Id)
	return render(request, "facultyinfo.html", {'fac':fac})

def circular_func(request):
	circularvar=circular.objects.all()
	return render(request, 'courses.html', {'courses':circularvar})


def gallery(request):
	pics=photos.objects.all().order_by('-id').values()
	return render(request, 'gallery.html', {'pics':pics})


def facultyfunc(request):
	data=faculty.objects.all()
	return render(request, 'faculty.html', {'data': data} )

def contactus(request):
	if(request.method=='POST'):
		name=request.POST.get('name')
		email=request.POST.get('email')
		text=request.POST.get('text')
		obj=messages()
		obj.name=name
		obj.email=email
		obj.text=text
		obj.save()
	return render(request, 'contactus.html')