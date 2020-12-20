from django.shortcuts import render
from BRAM import models
from django.http import HttpResponse,HttpResponseRedirect
from BRAM.form import NewBookForm
# Create your views here.
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author}
    form=NewBookForm(initial=fields)
    res=render(request,'BRAM/edit_book.html',{'form':form,'book':book})
    return res
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRAM/view-books')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        #book.id=request.Post['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.save()
        return HttpResponseRedirect('BRAM/view-books')
def viewBooks(request):
    books=models.Book.objects.all()
    #username=request.session['username']
    res=render(request,'BRAM/view_book.html',{'books':books})#'username':username})
    return res
def newBook(request):
    form=NewBookForm()
    res=render(request,'BRAM/new_book.html',{'form':form})
    return res
def add(request):
   if request.method=='POST':
       form=NewBookForm(request.POST)
       book=models.Book()
       book.title=form.data['title']
       book.price=form.data['price']
       book.author=form.data['author']
       book.save()
   s="Record Stored<br><a href='/BRAM/view-books'>view all Books</a>"
   return HttpResponse(s)
def greeting(request):
     s=render(request,'exam/copy.html')
     return (s)
