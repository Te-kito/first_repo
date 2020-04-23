from django.db import models
from django.conf import settings
from mamazon.models import Product
# Userの設定をしたいからそのままimportすることを推奨していない
User = settings.AUTH_USER_MODEL

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # null =databaseが空でもいいか？ blank = form登録の表記しないといけないか Trueが必須ではない
    # ForeignKeyの時はon_deleteは必須
    products = models.ManyToManyField()
    # 2つともフィールド、クラスの関係性を表す。↑
    # カートと商品は複数だよね。カートto商品の関係の設定
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    # 1,000,000.00
    created = models.DateTimeField(auto_now_add=True)  # 作られたときの時間
    updated = models.DateTimeField(auto_now=True)  # 更新されたときの時間
