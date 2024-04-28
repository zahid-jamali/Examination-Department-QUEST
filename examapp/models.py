from django.db import models
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField
# Create your models here.

class faq(models.Model):
	id=models.AutoField(primary_key=True)
	question=models.CharField(max_length=1000)
	answer=RichTextField()
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.question



class examination_system(models.Model):
	title=models.CharField(max_length=1000, )
	desc=FroalaField()
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title


class downloads(models.Model):
	id=models.AutoField(primary_key='True')
	title=models.CharField(max_length=500, null=True, blank=True)
	desc=models.TextField()
	files=models.FileField(upload_to="media/media/files/")
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title



class Apply_for(models.Model):
	id=models.AutoField(primary_key='True')
	Category=models.CharField(max_length=1000, default='')

	def __str__(self):
		return self.Category



class Registeration(models.Model):
	id=models.AutoField(primary_key='True')
	name=models.CharField(max_length=500, default='')
	fathername=models.CharField(max_length=500, default='')
	cnic=models.IntegerField(default=0)
	address=models.CharField(max_length=1000, default='')
	hsc_board=models.CharField(max_length=500, default='')
	hsc_percentage=models.IntegerField(default=0)
	phone=models.IntegerField(default=0)
	email=models.EmailField(max_length=100, default='')
	domicile=models.CharField(max_length=300, default='')
	is_questian=models.BooleanField(default=True)
	department=models.CharField(max_length=300, default='')
	Applied_For=models.ForeignKey(Apply_for,null=True, blank=True, on_delete=models.CASCADE)
	cnic_front=models.ImageField(upload_to="media/media/static/", default='')
	cnic_back=models.ImageField(upload_to="media/media/static/", default='')

	def __str__(self):
		return self.name




class msgs(models.Model):
	id=models.AutoField(primary_key='True')
	charge=models.CharField(max_length=255, default="")
	name=models.CharField(max_length=255, default="")
	msg=RichTextField()
	img=models.FileField(upload_to="media/media/static/", default="")

	def __str__(self):
		return self.name

class faculty(models.Model):
	id=models.AutoField(primary_key='true')
	name=models.CharField(max_length=244, default="")
	appointment=models.CharField(max_length=244, default="")
	desc=RichTextField()
	contact=models.CharField(max_length=255, default="")
	img=models.FileField(upload_to="media/media/static/", default="")

	def __str__(self):
		return self.name

class news(models.Model):
	id=models.AutoField(primary_key='true')
	date=models.DateField()
	news=models.CharField(max_length=1000, default='')


	def __str__(self):
		return str(self.date)


class Category(models.Model):
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=123, default="")
	def __str__(self):
		return self.title


class circular(models.Model):
	id=models.AutoField(primary_key='true')
	title=models.CharField(max_length=255, default='')
	desc=RichTextField()
	photo=models.FileField(upload_to='media/media/static', default="")
	category=models.ForeignKey(Category, on_delete=models.CASCADE, default="")
	date=models.CharField(max_length=255, default='')
	def __str__(self):
		return self.title



	
class photos(models.Model):
	id=models.AutoField(primary_key='true')
	photo=models.FileField(upload_to='media/media/static', default="")
	date=models.DateField(default="")
	def __str__(self):
		return str(self.date)

class messages(models.Model):
	id=models.AutoField(primary_key='true')
	name=models.CharField(max_length=255, default='')
	email=models.CharField(max_length=255, default='')
	text=models.TextField()
	
	def __str__(self):
		return self.name
