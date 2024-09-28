from rest_framework import serializers
from .custom_user import User
from .models import Ticket
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'email', 'role', 'password']
        extra_kwargs={'password':{'write_only': True}}
        
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class TicketSerializer(serializers.ModelSerializer):
    # user=UserSerializer(read_only=True)
    class Meta:
        model=Ticket
        fields=['train_name', 'seat_number', 'departure_time', 'is_confirmed']
    # def create(self, validated_data):
    #     user_data=validated_data.pop('user')
    #     user=User.objects.create_user(**user_data)
    #     ticket=Ticket.objects.create(user=user,**validated_data)
    #     return ticket