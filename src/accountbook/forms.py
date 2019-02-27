from django import forms
from .models import AccountBook

class AccountBookForm(forms.ModelForm):
   """
   新規データ登録画面用のフォーム定義
   """
   class Meta:
       model = AccountBook
       fields =['sls_dt', 'expns_catg_nm', 'prc_amt', 'memo'] 