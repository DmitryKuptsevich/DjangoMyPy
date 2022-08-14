from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher
from .serializers import TeacherSerializer



class TeacherAPIView(APIView):
      def get (self, request):
          lst = Teacher.objects.all().values( )
          return Response({'posts': list(lst)})

      def post (self, request):
          post_new = Teacher.objects.create(
              title = request.data['title'],
              content = request.data['content'],
              cat_id = request.data['cad_id']
          )
          return Response({'post': model_to_dict(post_new)})


# class TeacherAPIView(generics.ListAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

