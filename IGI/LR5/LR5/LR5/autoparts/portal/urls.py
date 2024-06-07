from django.urls import re_path

from .services.nationality import nationalize
from .views import *

urlpatterns = [
    re_path(r"^about/$", about_view, name="about"),
    re_path(r"^news/$", news_view, name="news"),
    re_path(r"^faq/$", faq_view, name="faq"),
    re_path(r"^contacts/$", contacts_view, name="contacts"),
    re_path(r"^policy/$", policy_view, name="policy"),
    re_path(r"^vacancies/$", vacancies_view, name="vacancies"),
    re_path(r"^feedback/$", feedback_view, name="feedback"),
    re_path(r"^places/$", places_view, name="places"),
    re_path(r"^joke/$", joke_view, name="joke"),
    re_path(r"^nationalize/$", nationalize, name="nationalize"),
    re_path(r"^create_faq/$", create_faq, name="create_faq"),
    re_path(r"^update_faq/$", update_faq, name="update_faq"),
    re_path(r"^delete_faq/$", delete_faq, name="delete_faq"),
    re_path(r"^accept_feedback/$", accept_feedback, name="accept_feedback"),
]
