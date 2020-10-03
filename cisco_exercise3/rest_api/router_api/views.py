from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import RouterDetails
from .serializers import RouterDetailsSerializer


# Create your views here.
class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')


class ListView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        router_data = RouterDetails.objects.filter(active=1)
        context = {'router_data': router_data}
        return render(request, 'list.html', context)


class RouterView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sapid = request.GET.get('sapid')
        if sapid is not None:
            router_data = RouterDetails.objects.filter(sapid=sapid)
        else:
            return Response({
                'messgae': 'No Data Found'
            }, status=status.HTTP_400_BAD_REQUEST)

        if router_data:
            serializer = RouterDetailsSerializer(router_data, many=True)
            return Response(serializer.data)
        else:
            return Response({
                'messgae': 'No Data Found'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = RouterDetailsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, ip):
        router_data = RouterDetails.objects.filter(loopback=ip).first()

        serializer = RouterDetailsSerializer(
            router_data, data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Record updated.'},
                            status=status.HTTP_200_OK)
        return Response({'message': 'Record can not be updated.'},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ip):
        router_data = RouterDetails.objects.filter(loopback=ip).first()
        update_data = {'active': 0}
        serializer = RouterDetailsSerializer(
            router_data, update_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Record deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Record can not be deleted.'},
                        status=status.HTTP_400_BAD_REQUEST)
