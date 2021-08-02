from rest_framework.serializers import ModelSerializer

from app.model import General_information, Portfolio


class General_infoSerializer(ModelSerializer):
    class Meta:
        model = General_information
        fields = ("__all__")

    def create(self, validated_data):
        portfolio = validated_data.pop("portfolio")
        portfolio_new = Portfolio.objects.create(contract_number=validated_data.get(""))
