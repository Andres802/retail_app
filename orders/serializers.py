from rest_framework import serializers

from .models import Orders


class OrdersSerializer(serializers.ModelSerializer):
  text = serializers.CharField(max_length=1000, required=True)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a order item instance in the database
    return Todo.objects.create(
      text=validated_data.get('text')
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the order item instance in the database
    instance.text = validated_data.get('text', instance.text)
    instance.save()
    return instance

  class Meta:
    model = Orders
    fields = (
      'id',
      'text'
    )