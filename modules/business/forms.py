from django import forms
from django.contrib.auth.models import User
from .models import B2cProfile

# CATEGORY_CHOICES =(('SEL','Vender'),('LEN','Prestar'),('GAW','Regalar'),('REN','Rentar'),('INT','Intercambiar'))

class B2cRegisterForm(forms.Form):
	
	business_name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea)
	location = forms.CharField(max_length=100)
	website = forms.URLField()
	phone = forms.IntegerField()
	apertura = forms.CharField(max_length=100)
	cierre = forms.CharField(max_length=100)
	
	# categoria = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = CATEGORY_CHOICES)	

class BusinessCreateForm(forms.ModelForm):
    #email           = forms.EmailField()
    # category         = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = B2cProfile
        fields = [
            'business_name',
			'description' ,
			'location',
			'website', 
			'phone' ,
			'apertura', 
			'cierre', 
			'category',

         
        ]