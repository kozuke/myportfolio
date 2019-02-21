from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import ExpnsCatg, AccountBook

#一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義
class AccountBookListView(ListView):
   #利用するモデルを指定
   model = AccountBook
   #データを渡すテンプレートファイルを指定
   template_name = 'accountbook/account_book_list.html'

   #家計簿テーブルの全データを取得するメソッドを定義
   def queryset(self):
       return AccountBook.objects.all()