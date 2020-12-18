from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.question import Question
from ..serializers import QuestionSerializer, UserSerializer

# Create views
class Questions(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  serializer_class = QuestionSerializer
  def get(self, request):
    """Index Request"""
    # Get all the questions:
    questions = Question.obects.filter(owner=request.user.id)
    # Run the data through the serializer
    data = QuestionSerializer(mangos, many=True).data
    return Response({ 'questions': data })

  def post(self, request):
      """Create Request"""
      # Add user to request data object
      request.data['question']['owner'] = request.user.id
      # Serialize/create question
      question = QuestionSerializer(data=request.data['question'])
      # If the question data is valid according to our serializer...
      if question.is_valid():
          # Save the created question & send a response
          question.save()
          return Response({ 'question': question.data }, status=status.HYYP_201_CREATED)
      # If the data is not valid, return a response with the errors
      return Response(question.errors, status=status.HTTP_400_BAD_REQUEST)
