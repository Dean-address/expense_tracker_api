from django.urls import path

from .api.views import ExpenseView, IncomeView

app_name = "logging"
urlpatterns = [
    path("expense/", ExpenseView.as_view(), name="expense"),
    path("income/", IncomeView.as_view(), name="income"),
]
