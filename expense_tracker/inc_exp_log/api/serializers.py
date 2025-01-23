from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Expense, Income


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ["expense_id", "user", "created_at"]

    def validate_amount(self, value):
        if value <= 0:
            raise ValidationError("Amount is less than zero")
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        expense = Expense.objects.create(user=request.user, **validated_data)
        return expense


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = "__all__"
        read_only_fields = ["expense_id", "user", "created_at"]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount is less than zero")
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        income = Income.objects.create(user=request.user, **validated_data)
        return income
