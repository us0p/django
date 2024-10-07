from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime

# Each model has a number of class variables, each of which represents a 
# database field in the model.

# To allow django to create the tables and to provide database-access api
# for those models, you need to install your app by adding it to your
# project settings.py.

# After you've installed your app you must create the migrations for the
# models you defined:
# python3 manage.py makemigrations <app_name>

# Note that:
# - table names are automatically generated by combining the name
#   of the app and the lowercase name of the model.
# - django appends "_id" to foreign key field names.

# The dafault behavious can be overrided.

# To apply the generated migrations:
# python3 manage.py migrate


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # Object representation are used throughout Django automatically
    # generated admin.
    def __str__(self):
        return self.question_text
    
    # optional decorator, used to alter how this field is displayed in the
    # change list page in the admin.
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?"
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choide_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choide_text
