from django.shortcuts import render
from . forms import AccountBookForm
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import ExpnsCatg, AccountBook

# 一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義


class AccountBookListView(ListView):
    # 利用するモデルを指定
    model = AccountBook
    # データを渡すテンプレートファイルを指定
    template_name = 'accountbook/accountbook_list.html'

    # 家計簿テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return AccountBook.objects.all()


class KakeiboCreateView(CreateView):

    # 利用するモデルを指定
    model = AccountBook
    # 利用するフォームクラス名を指定
    form_class = AccountBookForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('accountbook:create_done')
