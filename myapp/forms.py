# forms.py in app named 'contact'
from django import forms

#tuple datatype
TOPIC_CHOICES = (
	('0', '-Select topic-'),
	('1', 'General'),
	('2', 'Service'),
	('3', 'Review'),
)

DEP_CHOICES = [
	('HR', 'Human Resource'),
	('LG', 'Logistics'),
	('IT', 'Information Technology'),
]

PRI_CHOICES = [
	('0', 'Normal'),
	('1', 'Express'),
	('2', 'Urgent'),
]

class ContactForm(forms.Form):
	name = forms.CharField(required=False) #<input type='text' name='name'>
	email = forms.EmailField(label='Your email') #<input type='email' name='email'>
	comment = forms.CharField(widget=forms.Textarea) #<textarea name='comment'></textarea>
	topic = forms.ChoiceField(
		widget=forms.Select, choices=TOPIC_CHOICES, 
		initial='0', 
		required=True
	)
	dep = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple, 
		choices=DEP_CHOICES, 
		required=False,
		label='Department', #เป็นการตั้งชื่อให้กับ choice ของเรา
	)
	pri = forms.ChoiceField(
		widget=forms.RadioSelect, 
		choices=PRI_CHOICES, 
		required=False,
		label='Priority', #เป็นการตั้งชื่อให้กับ choice ของเรา
	)

	date = forms.DateField(widget=forms.SelectDateWidget)

	field_order = ['name', 'email', 'topic', 'dep', 'pri', 'comment', 'date',] #เรียงลำดับ element ก่อนหลัง
	

	def clean(self):
		super(ContactForm, self).clean()
		name = self.cleaned_data.get('name')
		email = self.cleaned_data.get('email')
		if len(name) < 4:
			raise forms.ValidationError("Name is wrong (Please, specific greater than 4 chars.)!")

class SharingForm(forms.Form):
	photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
