from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Card, Language, Feature, Category, Code_Snippet, Image, Resource, Text, Definition, Concept, Profile
from .forms import Card_Form, Language_Form, Feature_Form,  Category_Form, Code_Snippet_Form, Image_Form, Text_Form, Definition_Form, Concept_Form, Profile_Form
from time import gmtime, strftime, localtime
import uuid
import boto3

# import datetime
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
    features = Feature.objects.all()
    images = Image.objects.all()
    texts = Text.objects.all()
    concepts = Concept.objects.all()

    context = {
        'features': features,
        'images': images,
        'texts': texts,
        'concepts': concepts,
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
# def cards_index(request):
#     if request.method =="GET":
#         print(request.GET)
#     if request.method == "POST":
#         print(request.POST)
        
#         card_form = Card_Form(request.POST)
#             if card_form.is_valid():
#                 new_card = card_form.save(commit=True)
                # new_card.user = request.user
                # new_card.save()
                # return redirect('cards_index',)
            
                # return redirect('card_detail', card_id=card_id)

    # cards = Card.objects.all()
    # card_form = Card_Form()

    # context = {
    #     'card_form': card_form,
    #     'cards': cards,
    # }
    # return render(request, 'cards/index.html', context)

# CARDS INDEX
def cards_index(request):
    if request.method =="GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST)

        card_form = Card_Form(request.POST)
        if definition_form.is_valid():
            if card_form.is_valid():
                new_definition = definition_form.save(commit=True)
                new_card = card_form.save(commit=True)
                # new_card.user = request.user
                new_definition.save()
                new_card.save()
                return redirect('cards_index',)
                # return redirect('card_detail', card_id=card_id)

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

# CARD DETAIL
def card_detail(request, card_id):
    if request.method =="GET":
        print(request.GET)
    card = Card.objects.get(id=card_id)
    definitions = Definition.objects.all()
    # cards_not_here = Card.objects.exclude(id_in=card.)
    context = {
        'card': card,
        'definitions': definitions
    }
    return render(request, 'cards/detail.html', context)


# CARD EDIT
def card_edit(request, card_id):
    card = Card.objects.get(id=card_id)
    if request.method == 'POST':
        card_form = Card_Form(request.POST, instance=card)
        if card_form.is_valid():
            card_form.save()
            return redirect('detail', card_id=card_id)
    else:
        # in form (instance= The object that we pull back from db)
        card_form = Card_Form(instance=card)
    context = {
        'card':card,
        'card_form': card_form,
    }
    return render(request, 'cards/edit.html', context)

# CARD DELETE
# def card_delete(request, card_id):
#     Card.objects.get(id=cat_id).delete()
#     return redirect("cards_index")



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
    features = Feature.objects.all()
    images = Image.objects.all()
    texts = Text.objects.all()
    languages = Language.objects.all()
    concepts = Concept.objects.all()


    context = {
        'cards': cards,
        'features': features,
        'images': images,
        'texts': texts,
        'languages': languages,
        'concepts': concepts,
    }
    return render(request, 'design.html', context)


def add_photo(request, object_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid3().hex[.6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full URL string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to object_id or object (if you already have an object)
            photo = Image(url=url, object_id=object_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', object_id=object_id)
    