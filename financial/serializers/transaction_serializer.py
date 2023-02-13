from rest_framework import serializers

from financial.models import PrimeTransaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimeTransaction
        fields = ['id', 'amount', 'description', 'transaction_time']
