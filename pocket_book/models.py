import uuid
from datetime import datetime

from django.db import models


class PocketBook(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.CharField(max_length=150)
    image = models.ImageField()
    title = models.CharField(max_length=200)
    # 金额
    amount = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now)
    # 发生时间
    time_of_occurrence = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.author
