from django import forms

from modules.business.models import B2cProfile

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [



            'name',
            'business',
            'description',
            'extra_info',
            'politicas',
            'price',
      
           
        ]

    def __init__(self, user=None, *args, **kwargs):
        #print(kwargs.pop('user'))
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args,**kwargs)
        self.fields['business'].queryset = B2cProfile.objects.filter(owner=user)