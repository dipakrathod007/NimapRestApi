from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Client,Project, User
from .serializers import ClientSerializer,ClientwithallSerializer,ProjectSerializer,ProjectSerializer2
# ---------------------------------------------
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class ClientwithprojectDetail(generics.RetrieveAPIView):    
    queryset = Client.objects.all()
    serializer_class = ClientwithallSerializer
    lookup_field = 'id'


class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdate(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class ClientDelete(generics.DestroyAPIView):
    queryset = Client.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class ProjectCreate(generics.CreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer2


class ProjectDetail(generics.RetrieveAPIView):
    queryset1 = Project.objects.all()
    queryset1 = User.objects.all()

    serializer_class = ProjectSerializer2
    lookup_field = 'id'
    

class ProjectCreate(APIView):
    def post(self, request, *args, **kwargs):
        # Extract data from request
        project_name = request.data.get('project_name')
        client_id = request.data.get('id')
        user_ids = request.data.get('users', [])

        # Check if the client exists
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            return Response({"error": "Client does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Create project instance
        project_data = {'project_name': project_name, 'client': client}
        serializer = ProjectSerializer2(data=project_data)
        if serializer.is_valid():
            project = serializer.save()

            # Add users to the project
            for user_id in user_ids:
                try:
                    user = User.objects.get(pk=user_id)
                    project.users.add(user)
                except User.DoesNotExist:
                    pass  

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










