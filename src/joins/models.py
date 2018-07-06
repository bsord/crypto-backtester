from django.db import models


# Create your models here.

class Join(models.Model):
	email = models.EmailField()
	friend = models.ForeignKey("self", related_name='referral', null=True, blank=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	ref_id = models.CharField(max_length=120, default='ABC',unique=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	filepath = models.CharField(max_length=120, default='default.py')

	def __unicode__(self):
		return self.email

	class Meta:
		unique_together = ("email", "ref_id",)




class Tick_1yr_1hr(models.Model):
	ticktimestamp = models.DateTimeField()
	tickopen = models.CharField(max_length="12")
	tickhigh = models.CharField(max_length="12")
	ticklow = models.CharField(max_length="12")
	tickclose = models.CharField(max_length="12")

	def __unicode__(self):
		#return self.ticktimestamp
		return unicode(self.ticktimestamp)

	def as_dict(self):
		return {
			"ticktimestamp":str(self.ticktimestamp),
			"tickclose":self.tickclose
		}


# class Tick(models.Model):
# 	email = models.EmailField()
# 	friend = models.ForeignKey("self", related_name='referral', null=True, blank=True)
# 	ip_address = models.CharField(max_length=120, default='ABC')
# 	ref_id = models.CharField(max_length=120, default='ABC',unique=True)
# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
# 	filepath = models.CharField(max_length=120, default='default.py')

# 	def __unicode__(self):
# 		return self.email


# class JoinFriends(models.Model):
# 	email = models.OneToOneField(Join, related_name="Sharer")
# 	friends = models.ManyToManyField(Join, related_name ="Friend", null=True, blank=True)
# 	emailall = models.ForeignKey(Join, related_name='emailall', null=True)


# 	def __unicode__(self):
# 		print "friends are ", self.friends.all()
# 		print self.emailall
# 		print self.email
# 		return self.email.email

#1) Install south: pip install south, add south to settings.py in INSTALLED APPS
#2) ENsure model is in the synced database
#3) Convert the model to south with: python manage.py convert_to_south appname
#4) Make changes to model (eg: Add new fields)
#5) run python manage.py schemamigration appname --auto
#6) run python manage.py migrate

# django 1.7 has south included: just need to run migrate after field changes
# Further guides: https://github.com/codingforentrepreneurs/Guides/blob/master/using_south_in_django.md 
