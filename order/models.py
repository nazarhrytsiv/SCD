from django.db import models
from TypeTransaction.models import TypeTransaction
# Create your models here.

class Order(models.Model):
    type_transaction = models.ForeignKey(TypeTransaction, on_delete=models.SET_NULL, related_name='orders')
    pass