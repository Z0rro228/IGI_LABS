from django.shortcuts import render, redirect

from .forms import FeedbackForm, FAQCreationForm, FAQUpdateForm, FAQDeleteForm
from .models import *
from .services.joke_service import JokeService

from translate import Translator


# Create your views here.


def about_view(request):
    description = About.objects.all()[0].description
    return render(request, "core/about.html", {"description": description})


def news_view(request):
    news = News.objects.all()
    return render(request, "core/news.html", {"news": news})


def faq_view(request):
    faq = FAQ.objects.all()
    return render(request, "core/faq.html", {"faq": faq})


def contacts_view(request):
    contacts = Contacts.objects.all()
    return render(request, "core/contacts.html", {"contacts": contacts})


def policy_view(request):
    policy = ConfidentialityPolicy.objects.all()[0].policy
    return render(request, "core/policy.html", {"policy": policy})


def vacancies_view(request):
    vacancies = Vacancies.objects.all()
    return render(request, "core/vacancies.html", {"vacancies": vacancies})


def feedback_view(request):
    feedback = Feedback.objects.all()
    return render(request, "core/feedback.html", {"feedback": feedback})


def places_view(request):
    places = Places.objects.all()
    return render(request, "core/places.html", {"places": places})


def accept_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
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

    return render(request, 'core/joke.html', {'full_text': full_text, 'joke': joke})


def create_faq_view(request):
    form = FAQCreationForm()
    return render(request, "core/create_faq.html", {"form": form})


def create_new_faq(request):
    if request.method == "POST":
        form = FAQCreationForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()
            return redirect("/")
        else:
            form = FAQCreationForm()
    return render(request, "core/create_faq.html", {"form": form})


def update_faq_view(request):
    form = FAQUpdateForm([(x.question, x.question) for x in FAQ.objects.all()])
    return render(request, "core/update_faq.html", {"form": form})


def update_faq(request):
    if request.method == "POST":
        FAQ.objects.filter(question=request.POST['question']).update(answer=request.POST['new_answer'])
        FAQ.objects.filter(question=request.POST['question']).update(question=request.POST['new_question'])
        return redirect("/")
    form = FAQCreationForm([(x.question, x.question) for x in FAQ.objects.all()])
    return render(request, "core/update_faq.html", {"form": form})


def delete_faq_view(request):
    form = FAQDeleteForm([(x.question, x.question) for x in FAQ.objects.all()])
    return render(request, "core/delete_faq.html", {"form": form})


def delete_faq(request):
    if request.method == "POST":
        FAQ.objects.all().filter(question=request.POST['question'])[0].delete()
        return redirect("/")
    form = FAQCreationForm([(x.question, x.question) for x in FAQ.objects.all()])
    return render(request, "core/delete_faq.html", {"form": form})
