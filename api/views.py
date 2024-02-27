from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def nameDetail(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateItem(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=items, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


class DeleteAPIView(APIView):
    def put(self, request, pk, format=None):
        try:
            instance = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)