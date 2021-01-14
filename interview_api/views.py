from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Card, Language, Feature, Category, Code_Snippet, Image, Definition, Concept, Profile
from .forms import Card_Form, Language_Form, Feature_Form,  Category_Form, Code_Snippet_Form, Image_Form, Text_Form, Definition_Form, Concept_Form, Profile_Form
from time import gmtime, strftime, localtime
import datetime
from datetime import datetime
from django.utils import timezone
# Create your views here. code responsible for rendering views/api endpoints

#             Card('REST', 'Representational State Transfer', ['determines how the API looks', 'set of rules that devs follow when they create their API', 'one of these rules states that <you should be able to get a piece of data (called a resource) when you link to a specific URL>', 'Each URL is called a request while the data sent back to you is called a response'], 'back-end', 'cross language vocabulary', 'Liz Kane'),

# /vocabulary
# /topics
# /languages
# /analyticalskills
# /codingskills
# /technicalknowledge-csFundamentals
# /experience
# /culturefit/communicationskills

def main(request):
    return HttpResponse("<h1>running 🏃🏻‍♀️</h1>")

# MAIN INDEX
def home(request):
    cards = Card.objects.all()
    languages = Language.objects.all()

    context = {
        'card_form': Card_Form(),
        'language_form' : Language_Form(),
        'cards': cards,
        'languages': languages,
        # 'time': strftime("%m-%d-%Y %H:%M %p" , gmtime()),
        # "local_time": strftime("%H:%M %p", localtime()),
        'now': datetime.now(),
        'timezone': timezone.now(),
    }
    return render(request, 'home.html', context)

# CATEGORIES & TOPICS
def tree(request):
    languages = Language.objects.all()

    context = {
        'language_form' : Language_Form(),
        'languages': languages,
    }
    return render(request, "tree.html", context)
    # return HttpResponse("Tree of Knowledge", context)

# CARDS INDEX
def cards_index(request):
    if request.method =="GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST)
        definition_form = Definition_Form(request.POST)
        card_form = Card_Form(request.POST)
        if definition_form.is_valid():
            if card_form.is_valid():
                new_definition = definition_form.save(commit=True)
                new_card = card_form.save(commit=True)
                # new_card.user = request.user
                new_definition.save()
                new_card.save()
                return redirect('cards_index')

    definitions = Definition.objects.all()
    definition_form = Definition_Form()
    cards = Card.objects.all()
    card_form = Card_Form()

    context = {
        'card_form': card_form,
        'cards': cards,
        'definition_form' : definition_form,
        'definitions' : definitions,
    }
    return render(request, 'cards/index.html', context)

# FEATURES INDEX
def feature_index(request):
    if request.method == "POST":
        # print(request.POST)
        feature_form = Feature_Form(request.POST)
        if feature_form.is_valid():
            new_feature = feature_form.save(commit=True)
            # new_card.user = request.user
            new_feature.save()
            return redirect('features_index')
    features = Feature.objects.all()
    feature_form = Feature_Form()

    context = {
        'feature_form': feature_form,
        'features' : features,
    }
    return render(request, 'features/index.html', context)


def design_board(request):
    cards = Card.objects.all()
    

    context = {
        'cards': cards,
    }
    return render(request, 'design.html', context)