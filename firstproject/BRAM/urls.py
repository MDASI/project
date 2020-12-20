from django.conf.urls import url
from BRAM import views

urlpatterns = [
     url('view-books',views.viewBooks),
     url('edit-book',views.editBook),
     url('delete-book',views.deleteBook),
     url('new-book',views.newBook),
     url('add',views.add),
     url('edit',views.edit),
     url('greeting',views.greeting),
]
