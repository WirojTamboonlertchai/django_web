from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# django เตรียม API มาให้แล้ว เมื่อ migrate แล้ว จะได้ Primary Key มาเลย จึงไม่ต้องกำหนด Primary Key ให้กับแต่ละตาราง

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') # date_published คือ ค่าของคอมเม้นต์ที่อธิบายว่าเป็นวันที่อะไร

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # กำหนดความสัมพันธ์กับ class Question
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text