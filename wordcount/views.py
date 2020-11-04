from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request): #Everytime django accepts a request it sends a request object so you must enter this into your functions
    return render(request, 'home.html') #If you just put print("Text") it won't work as it needs to respond with an http response

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    wlist = re.sub("[^0-9a-zA-Z]+", ' ', fulltext).rstrip() #I found this snippet off StackFlow. I don't quite understand it but it uses regex.
    swlist = wlist.split()
    wordlist = []
    for sitem in swlist: #This whole loop is just to put the entire list to lowercase so it can then be evaluated.
        wordlist.append(sitem.lower())


    wordcountdictionary = {}

    for word in wordlist:
        if word in wordcountdictionary:
            wordcountdictionary[word] += 1
        else:
            wordcountdictionary[word] = 1

    sortedWords = sorted(wordcountdictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedWords':sortedWords})

