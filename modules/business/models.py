from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from modules.accounts.models import UserProfile
from django.db.models.signals import post_save
from .utils import unique_slug_generator
from django.urls import reverse



B_CATEGORIES = (
    ("Comida y Bebida","Comida y Bebida"),
    ("Salud y Bienestar","Salud y Bienestar"),
    ("Ropa y Accesorios","Ropa y Accesorios"),
    ("Energía","Energía"),
    ("Arte","Arte"),
    ("Artículos para el Hogar","Aartículos para el Hogar"),
    ("Artículos para Oficina","Artículos para Oficina"),
    ("Atículos Electrónicos","Artículos Electrónicos"),
    ("Juguetes","Juguetes"),
    ("Automóviles","Automóviles"),
    ("Ventas al por Menor","Ventas al por Menor"),
    ("Libros","Libros"),
    ("Serivicios Publicitarios","Servicios Publicitarios"),
    ("Cosmética y Cuidado Personal","Cosmética y Cuidado Personal"),
    ("Artículos Deportivos","Artículos Deportivos"),
    ("Servicios de Limpieza","Sercicios de Limpieza"),
    ("Ventas al por Mayor","Ventas al por Mayor"),
    ("Servicios Empresariales","Servicios Empresariales"),
    ("Servicios de Paquetería","Servicios de Paquetería"),
    ("Servicios Financieros","Servicios Financieros"),
    ("Servicios Bancarios","Servicios Bancarios"),
    ("Organización de Eventos","Organizaciónde de Eventos"),
)

'''class UserProfileManager(models.Manager):
	def  get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city='CDMX')'''

class B2cProfile(models.Model):
	
	  
	owner 			= models.OneToOneField(User, on_delete=models.CASCADE)
	created 		= models.BooleanField(default=True)
	business_name 	= models.CharField(max_length=100,default='')
	description 	= models.TextField(max_length=240, default='')
	location 		= models.CharField(max_length=100,default='')
	website			= models.URLField(default='')
	phone 			= models.IntegerField(default=0)
	apertura		= models.CharField(max_length=100, default='')
	cierre 			= models.CharField(max_length=100, default='')
	category		= models	
	slug            = models.SlugField(null=True, blank=True)
	category      = models.CharField(max_length=50,choices= B_CATEGORIES)
	
	def __str__(self):
			return self.business_name 

	# def __unicode__(self):
 #    		return unicode(self.owner)

 

	def get_absolute_url(self): #get_absolute_url
	        #return f"/restaurants/{self.slug}" 
	    return reverse('business:detail', kwargs={'slug': self.slug})

    # @property
    # def title(self):
    #     return self.name


# def create_b2cprofile(sender,**kwargs):
# 	if kwargs['created']:
# 		b2c_profile = B2cProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_b2cprofile, sender=User)


	@property
	def title(self):
		return self.business_name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # instance.category = instance.category.capitalize()
	# print ('savings..')
	# print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created,  *args, **kwargs)
# 	print ('savings..')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()

pre_save.connect(rl_pre_save_receiver, sender= B2cProfile)




def get_absolute_url(self): 
         
    return reverse('business:detail', kwargs={'pk': self.pk})