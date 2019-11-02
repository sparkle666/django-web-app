from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
# Create your models here.
class Design(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to="images")
	likes = models.IntegerField(null= True)
	design_category = models.ForeignKey("DesignCategory", on_delete= models.CASCADE)
	date_added = models.DateTimeField()
	def __str__(self):
		return self.name
		
class DesignCategory(models.Model):
	name = models.CharField(max_length=200, )
	description = models.TextField()
	featured_image = models.ImageField(upload_to="images/%Y/%m/%d", null= True)
	class Meta:
				verbose_name_plural = "Design Categories"
	def __str__(self):
		return self.name
		
