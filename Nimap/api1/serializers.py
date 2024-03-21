from rest_framework import serializers
from .models import Client, Project,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializer(serializers.ModelSerializer):
    # projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']

class ClientwithallSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name','projects', 'created_at', 'created_by', 'updated_at']





# class ProjectSerializer2(serializers.ModelSerializer):
#     users = UserSerializer(many=True, read_only=True)
#     # client = ClientSerializer(source='project', read_only=True)
#     class Meta:
#         model = Project
#         fields = ['id', 'project_name','client', 'users','created_at', 'created_by']  
        

class ProjectSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def create(self, validated_data):
        """
        Custom create method to handle nested relationships (users)
        """
        users_data = validated_data.pop('users', [])  
        project = Project.objects.create(**validated_data)  

        # Add users to the project
        for user_data in users_data:
            user_id = user_data.get('id')
            if user_id:  
                user = User.objects.get(pk=user_id)
                project.users.add(user)

        return project




















