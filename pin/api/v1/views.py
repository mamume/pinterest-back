from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pin.models import Pin
from .serializers import PinSerializer

@api_view(["GET", "POST"]) # tells django that this is a type of rest view
def hello_world(request):
    if request.method == 'POST':
        return Response(
        {'message': 'Post request-Response'}, status=status.HTTP_201_CREATED)
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

#
#@api_view(["GET"])
#def movie_index(request):
#    movies = Movie.objects.all()
#    serializer = MovieSerializer(instance=movies, many=True)
#    return Response(data=serializer.data, status=status.HTTP_200_OK)

#@api_view(['POST'])
#def create_movie(request):
#    if request.method == 'POST':
#        serializer = MovieSerializer(data=request.data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##CRUD
#Create
@api_view(['POST'])
def pin_create(request):
    if request.method == 'POST':
        serializer = PinSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Read
@api_view(["GET"])
def pin_list(request):
    pins = Pin.objects.all()
    serialized_pins = PinSerializer(instance=pins, many=True)
    return Response(data=serialized_pins.data,status=status.HTTP_200_OK)

@api_view(["GET"])
def single_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)
    except Exception as e:
        return Response(data={"msg": "this pin does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serialized_pin = PinSerializer(instance=pin)
    return Response(data=serialized_pin.data,status=status.HTTP_200_OK)


#Update
@api_view(["PUT", "PATCH"])
def update_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_pin = PinSerializer(instance=pin, data = request.data )
    if serialized_pin.is_valid():
        serialized_pin.save()
        return Response(serialized_pin.data, status=status.HTTP_200_OK)
    return Response(serialized_pin.errors, status=status.HTTP_400_BAD_REQUEST)


#D
@api_view(["DELETE"])
def delete_pin(request, pk):
    res = {}
    try:
        pin  = Pin.objects.get(pk = pk)
        pin.delete()
        res['data']= 'Successfully deleted the pin'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))
