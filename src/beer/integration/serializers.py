from rest_framework import serializers

class BeerSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.FloatField()


class FriendSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class OrderItemSerializer(serializers.Serializer):

    beer = BeerSerializer(read_only=True)
    beer_id = serializers.CharField(write_only=True)

    friend = FriendSerializer(read_only=True)
    friend_id = serializers.CharField(write_only=True)
    
    quantity = serializers.IntegerField()



class OrderSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)
    items = OrderItemSerializer(many=True)
    is_paid = serializers.BooleanField()
    is_individual_payment = serializers.BooleanField()
