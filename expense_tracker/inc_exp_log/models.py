from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Expense(TimeStampedModel):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expense")
    amount = models.DecimalField(
        max_digits=20, decimal_places=2, null=False, blank=False
    )
    descrption = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username, self.category} expense "


class Income(TimeStampedModel):
    income_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="income")
    amount = models.DecimalField(
        max_digits=20, decimal_places=2, null=False, blank=False
    )
    source = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username} from {self.source}"
