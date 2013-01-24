from django.db import models
from taggit.managers import TaggableManager
import md5

class Users(models.Model):
	name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)

class Categories(models.Model):
	name =  models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
		
		
class Videos(models.Model):
	video_id = models.CharField(max_length=300)
	link = models.CharField(max_length=300)
	title = models.CharField(max_length=100)
	thumbnail_link = models.CharField(max_length=100)
	category = models.ForeignKey(Categories)
	#~ tags = TaggableManager()
	permalink = models.CharField(max_length=500)
	fb_comments_plugin = models.CharField(max_length  = 1000)
	posted_by = models.ForeignKey(Users)
	timestamp = models.DateTimeField()
	rating = models.FloatField()
	num_views = models.IntegerField()
	meta_file = models.CharField(max_length=1000)
	# badge like lol, omg etc.
	
	def __unicode__(self):
		return self.title
