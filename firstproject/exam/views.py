from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from newsapi import NewsApiClient
def iwarning(request):
    s="<p>do not move your cursor out side of brower window</p>"
    return HttpResponse(s)
def showTest(request):
    que="who is the inventor of Computer"
    a="arbaz khan"
    b="Charles Babbage"
    c="Virat kohli"
    d="dhoni"
    a='easy'
    que2='who is asif'
    a2='asif is asif'
    dic={'que':que,'a':a,'b':b,'c':c,'d':d,'a':a,'que2':que2,'a1':a2}
    Result=render(request,'exam/test.html',dic)
    return (Result)
# Create your views here.
def index(request):

    newsapi = NewsApiClient(api_key ='3e269940254a4a37aa612b4c22986c0c')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'exam/index.html', context ={"mylist":mylist})
def showResult(request):
  s="<h1>result is</h1>"
  return HttpResponse(s)


# Create your views here.
