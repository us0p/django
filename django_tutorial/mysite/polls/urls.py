from django.urls import path

from . import views

# A Django project can have many apps, to be able to differentiate the
# URL names between them we need to specify a namespace in each app's
# URLconf, this whay, Django will know what url to look when we use the
# {% url %} template tag in our templates

app_name = "polls"
urlpatterns = [
    # You can name your routes, this allows you to make global changes
    # to URL patterns of your project while only touching a single file.
    path("list", views.get_questions, name="list_questions"),
    path("create", views.create_question, name="create_questions"),
    # Default way of defining views
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # Defining generic views paths:
    path("", views.IndexView.as_view(), name="index"),
    # Note that, the urls which expeted the pk as parameters were changed
    # from "question_id" to "pk", Generic views expects the primary key
    # to be captured from the URL with "pk".
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
