from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#read
@api_view(['GET'])
def List(request):
    listsobj=ListModel.objects.all()
    serializer=ListSerializer(listsobj,many=True)
    authentication_class=[BasicAuthentication]
    permission_clases =[IsAuthenticated]

    return Response(serializer.data)
class ResgisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':402, 'payload':serializer.errors,'message':'yor data is  not saved'})
        serializer.save()
        user =User.objects.get(username =serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'status':200, 'payload':serializer.data,'token':str(token_obj),'message':'yor data is  saved'})

#create
@api_view(['POST'])
def post_List(request):
    listsobj=ListModel.objects.all()
    serializer=ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
#update
@api_view(['POST'])
def update_List(request,id):
    listsobj=ListModel.objects.get(id= id)
    serializer=ListSerializer(instance=listsobj,data=request.data)
    authentication_class=[BasicAuthentication]
    permission_clases =[IsAuthenticated]

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#delete
@api_view(['DELETE'])
def delete_List(request,id):
    listsobj=ListModel.objects.get(id= id)
    authentication_class=[BasicAuthentication]
    permission_clases =[IsAuthenticated]

    
    listsobj.delete()
    return Response('The field is deleted')




    
