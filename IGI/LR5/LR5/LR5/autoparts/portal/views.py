from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from .forms import FeedbackForm, FAQCreationForm, FAQUpdateForm, FAQDeleteForm
from .models import *
from .services.joke_service import JokeService

from translate import Translator

from utils.user_tests import customer_check, employee_check


# Create your views here.


def about_view(request):
    description = About.objects.all()[0].description
    return render(request, "portal/about.html", {"description": description})


def news_view(request):
    news = News.objects.all()
    return render(request, "portal/news.html", {"news": news})


def faq_view(request):
    faq = FAQ.objects.all()
    return render(request, "portal/faq.html", {"faq": faq})


def contacts_view(request):
    contacts = Contacts.objects.all()
    return render(request, "portal/contacts.html", {"contacts": contacts})


def policy_view(request):
    policy = ConfidentialityPolicy.objects.all()[0].policy
    return render(request, "portal/policy.html", {"policy": policy})


def vacancies_view(request):
    vacancies = Vacancies.objects.all()
    return render(request, "portal/vacancies.html", {"vacancies": vacancies})


def feedback_view(request):
    feedback = Feedback.objects.all()
    return render(request, "portal/feedback.html", {"feedback": feedback})


def places_view(request):
    places = Places.objects.all()
    return render(request, "portal/places.html", {"places": places})


@user_passes_test(customer_check)
def accept_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user_name = request.user.first_name
            feedback.save()
            return redirect("/")
        else:
            form = FeedbackForm()
    return render(request, "core/index.html", {"form": form})


def joke_view(request):
    joke = JokeService.get_random_joke()
    setup = joke['setup']
    punchline = joke['punchline']

    translator = Translator(from_lang="en", to_lang="ru")
    full_text = setup + " " + punchline

    return render(request, 'portal/joke.html', {'full_text': full_text, 'joke': joke})


@user_passes_test(employee_check)
def create_faq(request):
    if request.method == "POST":
        form = FAQCreationForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()
            return redirect("/")
    form = FAQCreationForm()
    return render(request, "portal/create_faq.html", {"form": form})


@user_passes_test(employee_check)
def update_faq(request):
    if request.method == "POST":
        FAQ.objects.filter(question=request.POST['question']).update(answer=request.POST['new_answer'])
        FAQ.objects.filter(question=request.POST['question']).update(question=request.POST['new_question'])
        return redirect("/")
    form = FAQUpdateForm()
    return render(request, "portal/update_faq.html", {"form": form})


@user_passes_test(employee_check)
def delete_faq(request):
    if request.method == "POST":
        FAQ.objects.all().filter(question=request.POST['question'])[0].delete()
        return redirect("/")
    form = FAQDeleteForm()
    return render(request, "portal/delete_faq.html", {"form": form})
