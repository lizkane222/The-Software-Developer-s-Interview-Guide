from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. code responsible for rendering views/api endpoints

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

def home(request):
    # return HttpResponse("<h1>running 🏃🏻‍♀️</h1>")
    return render(request, 'home.html')

def tree(request):
    return HttpResponse("Tree of Knowledge")


class Card:
    def __init__(self, term, altname, subterms, definitions, category, topic, creator):
        self.term = term
        self.altname = altname
        self.subterms = subterms
        self.definitions = definitions
        self.category = category
        self.topic = topic
        self.creator = creator

        cards = [
            Card('API', 'Application Programming Interface', ['a set of rules that allow programs to tlak to each other', 'the developer creates the API on teh server and allows the client to talk to it'], 'back-end', 'cross language vocabulary', 'Liz Kane'),
            Card('REST', 'Representational State Transfer', ['determines how the API looks', 'set of rules that devs follow when they create their API', 'one of these rules states that <you should be able to get a piece of data (called a resource) when you link to a specific URL>', 'Each URL is called a request while the data sent back to you is called a response'], 'back-end', 'cross language vocabulary', 'Liz Kane'),
        ]


def cards_index(request):
    context = {'cards': cards}
    return render(request, './cards/index.html', context)

