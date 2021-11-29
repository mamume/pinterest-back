from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from pin.models import Pin, Note, Category, Section
from .serializers import PinSerializer, NoteSerializer, CategorySerializer, SectionSerializer
from collections import OrderedDict
from rest_framework.decorators import api_view, permission_classes

#############################################################################################################################
##  Start of Pin CRUD
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
@permission_classes([])

def pin_list(request):
    pins = Pin.objects.all()
    serialized_pins = PinSerializer(instance=pins, many=True, context={"request": request })
    return Response(data=serialized_pins.data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([])
def single_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)
    except Exception as e:
        return Response(data={"msg": "this pin does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    print(pin)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    serialized_pin = PinSerializer(instance=pin)
    print(serialized_pin)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    return Response(data=serialized_pin.data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([])
def user_pins(request, user_id):
    try:
        pins  = Pin.objects.select_related("UserProfile").filter(owner__id = user_id)
    except Exception as e:
        return Response(data={"msg": "failed to fetch this users' pins"}, status=status.HTTP_400_BAD_REQUEST)
    print(pins)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    serialized_pins = PinSerializer(instance=pins, many=True)
    print(serialized_pins)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
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

#End of Pin CRUD
#############################################################################################################################


#############################################################################################################################
##  Start of Note CRUD
#Create
#Create
@api_view(['POST'])
def note_create(request, pin_id):
    
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = NoteSerializer(data=data, context={'pin_id': pin_id})
        print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return HttpResponse("hello")

"""@api_view(['GET'])
def note_create(request, pin_id):
    if request.method == 'GET':
        target_pin = Pin.objects.get(pk=pin_id)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(target_pin)
        target_pin = PinSerializer(data=target_pin) 
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(target_pin)
        if target_pin.is_valid():
            target_pin.create(validated_data=target_pin.validated_data)
        return HttpResponse("hello")
        #newdict={}
        #newdict.update(target_pin.data)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(newdict.get('note').append(OrderedDict([('id', 1) , ('title', 'new') ])  ))
        #serialized_pin = PinSerializer(instance=target_pin, data = newdict )
        #if serialized_pin.is_valid():
        #    serialized_pin.save()
        #return Response(serialized_pin.data, status=status.HTTP_200_OK)

        #return Response(target_pin.data, status=status.HTTP_200_OK)
        #serializer = NoteSerializer(data=request.data)
    #if serializer.is_valid():
    #    serializer.save()
    #    return Response(serializer.data, status=status.HTTP_200_OK)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
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
"""


#Update
@api_view(["PUT", "PATCH"])
def update_note(request,pin_id,  pk):
    try:
        note  = Note.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_note = NoteSerializer(instance=note, data = request.data )
    if serialized_note.is_valid():
        serialized_note.save()
        return Response(serialized_note.data, status=status.HTTP_200_OK)
    return Response(serialized_note.errors, status=status.HTTP_400_BAD_REQUEST)


#D
@api_view(["DELETE"])
def delete_note(request,pin_id,  pk):
    res = {}
    try:
        note  = Note.objects.get(pk = pk)
        note.delete()
        res['data']= 'Successfully deleted the note'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))

#End of Note CRUD
#############################################################################################################################


#############################################################################################################################
##  Start of Category CRUD
#Create
#Create
@api_view(['POST'])
def category_create(request, pin_id):
    
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = CategorySerializer(data=data, context={'pin_id': pin_id})
        print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return HttpResponse("hello")

"""@api_view(['GET'])
def note_create(request, pin_id):
    if request.method == 'GET':
        target_pin = Pin.objects.get(pk=pin_id)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(target_pin)
        target_pin = PinSerializer(data=target_pin) 
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(target_pin)
        if target_pin.is_valid():
            target_pin.create(validated_data=target_pin.validated_data)
        return HttpResponse("hello")
        #newdict={}
        #newdict.update(target_pin.data)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(newdict.get('note').append(OrderedDict([('id', 1) , ('title', 'new') ])  ))
        #serialized_pin = PinSerializer(instance=target_pin, data = newdict )
        #if serialized_pin.is_valid():
        #    serialized_pin.save()
        #return Response(serialized_pin.data, status=status.HTTP_200_OK)

        #return Response(target_pin.data, status=status.HTTP_200_OK)
        #serializer = NoteSerializer(data=request.data)
    #if serializer.is_valid():
    #    serializer.save()
    #    return Response(serializer.data, status=status.HTTP_200_OK)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
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
"""


#Update
@api_view(["PUT", "PATCH"])
def update_category(request,pin_id,  pk):
    try:
        category  = Category.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_category = CategorySerializer(instance=category, data = request.data )
    if serialized_category.is_valid():
        serialized_category.save()
        return Response(serialized_category.data, status=status.HTTP_200_OK)
    return Response(serialized_category.errors, status=status.HTTP_400_BAD_REQUEST)


#D
@api_view(["DELETE"])
def delete_category(request,pin_id,  pk):
    res = {}
    try:
        category  = Category.objects.get(pk = pk)
        category.delete()
        res['data']= 'Successfully deleted the category'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))
## End of Category CRUD
#############################################################################################################################

#############################################################################################################################
##  Start of Section CRUD
#Create
#Create
@api_view(['POST'])
def section_create(request, pin_id):
    
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = SectionSerializer(data=data, context={'pin_id': pin_id})
        print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return HttpResponse("hello")

"""@api_view(['GET'])
def note_create(request, pin_id):
    if request.method == 'GET':
        target_pin = Pin.objects.get(pk=pin_id)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(target_pin)
        target_pin = PinSerializer(data=target_pin) 
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(target_pin)
        if target_pin.is_valid():
            target_pin.create(validated_data=target_pin.validated_data)
        return HttpResponse("hello")
        #newdict={}
        #newdict.update(target_pin.data)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(newdict.get('note').append(OrderedDict([('id', 1) , ('title', 'new') ])  ))
        #serialized_pin = PinSerializer(instance=target_pin, data = newdict )
        #if serialized_pin.is_valid():
        #    serialized_pin.save()
        #return Response(serialized_pin.data, status=status.HTTP_200_OK)

        #return Response(target_pin.data, status=status.HTTP_200_OK)
        #serializer = NoteSerializer(data=request.data)
    #if serializer.is_valid():
    #    serializer.save()
    #    return Response(serializer.data, status=status.HTTP_200_OK)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
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
"""


#Update
@api_view(["PUT", "PATCH"])
def update_section(request,pin_id,  pk):
    try:
        section  = Section.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_section = SectionSerializer(instance=section, data = request.data )
    if serialized_section.is_valid():
        serialized_section.save()
        return Response(serialized_section.data, status=status.HTTP_200_OK)
    return Response(serialized_section.errors, status=status.HTTP_400_BAD_REQUEST)


#D
@api_view(["DELETE"])
def delete_section(request,pin_id,  pk):
    res = {}
    try:
        section  = Section.objects.get(pk = pk)
        section.delete()
        res['data']= 'Successfully deleted the section'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))

#End of Section CRUD
#############################################################################################################################




