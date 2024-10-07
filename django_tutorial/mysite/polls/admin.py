from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question) - default
# admin.site.register(Choice) - default

# Allows a model to be created from within another model page
# This class defines the inner model.
# Inheriting from admin.StackedInline will display the form info as a stack
# Inheriting from admin.TabularInline will display the forms side by side.
class ChoiceInline(admin.StackedInline):
    # Which model to use
    model = Choice
    # The default number of instances to be created.
    # can add or remove more at runtime in the GUI.
    extra = 3

# Change admin form fields for a model
class QuestionAdmin(admin.ModelAdmin):
    # reordering fields
    # fields = ["pub_date", "question_text"]

    # spliting fields into fieldsets
    fieldsets = [
        # tuple with:
        # 1. Fieldset name
        # 2. A dict with a fields key which has a list with the fields of
        #    the given fieldset.
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]
    inlines = [ChoiceInline]

    # By default, Django displays the str() of each object.
    # list of field names to display, as columns, on the change list page 
    # for the object. You can also add methods of your model.
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # add filters over the following fields to the page.
    list_filter = ["pub_date"]
    # add search over the followinf fields to the page.
    search_fields = ["question_text"]

# Them map it to the original model
admin.site.register(Question, QuestionAdmin)

