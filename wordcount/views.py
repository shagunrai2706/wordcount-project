from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET["fulltext"]
    worddict={}
    wordlist=fulltext.split()

    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1

    sortedword=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})

def Info(request):
    return render(request,'Info.html')


