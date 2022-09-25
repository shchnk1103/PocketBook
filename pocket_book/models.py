import uuid
from datetime import datetime

from django.db import models

from my_user.models import MyUser


class PocketBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='pocket_book')
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=200)
    # 金额 max_digits:允许的最大位数  decimal_places:精度
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    created_date = models.DateTimeField(default=datetime.now)
    # 发生时间
    time_of_occurrence = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
