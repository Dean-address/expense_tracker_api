from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from ..models import Expense
from .serializers import ExpenseSerializer, IncomeSerializer


class ExpenseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ExpenseSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            expense = serializer.save()
            serializer_data = ExpenseSerializer(expense).data
            return Response(
                {
                    "data": serializer_data,
                    "message": "Expense successfully added",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = request.user

        expense = Expense.objects.filter(user=user.email)
        serializer = ExpenseSerializer(expense, many=True)
        return Response(
            {
                "data": serializer.data,
            },
        )


class IncomeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = IncomeSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            income = serializer.save()
            serializer_data = IncomeSerializer(income).data
            return Response(
                {
                    "data": serializer_data,
                    "message": "Income successfully added",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, *args, **kwargs):
    #     pass
