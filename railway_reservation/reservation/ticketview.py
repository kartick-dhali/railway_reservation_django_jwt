from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin,IsUser
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.response import Response
class TicketListCreateView(APIView):
    permission_classes=[IsAuthenticated,IsUser]
    def get(self,request):
        tickets=Ticket.objects.filter(user=request.user)
        serializer=TicketSerializer(tickets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AdminTicketUpdateView(APIView):
    permission_classes=[IsAuthenticated,IsAdmin]
    
    def get(self,request):
        tickets=Ticket.objects.all()
        serializer=TicketSerializer(tickets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,pk):
         ticket = Ticket.objects.get(pk=pk)
         serializer = TicketSerializer(ticket, data=request.data, partial=True)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self,request,pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)