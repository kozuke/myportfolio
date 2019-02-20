from django.db import models
from datetime import datetime


class ExpnsCatg(models.Model):
    class Meta:
        db_table = "ExpnsCatg"

    expns_catg_nm = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.expns_catg_nm


class AccountBook(models.Model):
    class Meta:
        db_table = "AccountBook"

    sls_dt = models.DateField(verbose_name="日付", default=datetime.now)
    expns_catg_nm = models.ForeignKey(
        ExpnsCatg, on_delete=models.PROTECT, verbose_name="カテゴリ")
    prc_amt = models.IntegerField(verbose_name="金額", help_text="単位は日本円")
    memo = models.CharField(verbose_name="メモ", max_length=500)

    def __str__(self):
        return self.memo
