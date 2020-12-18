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
    questions = Question.objects.filter(owner=request.user.id)
    # Run the data through the serializer
    data = QuestionSerializer(questions, many=True).data
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
          return Response({ 'question': question.data }, status=status.HTTP_201_CREATED)
      # If the data is not valid, return a response with the errors
      return Response(question.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
      """Show Request"""
      # Locate the question to show
      question = get_object_or_404(Question, pk=pk)
      # Only want to show owned questions
      if not request.user.id == question.owner.id:
          raise PermissionDenied('Unauthorized, you do not own this question.')

      # Run the data through the serializer so it's formatted
      data = QuestionSerializer(question).data
      return Response({ 'question': data })

    def delete(self, request, pk):
        """Delete Request"""
        # Locate question to delete
        question = get_object_or_404(Question, pk=pk)
        #  Check the question's owner against the user making this request
        if not request.user.id == question.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this question.')
        # Only delete if the user owns the question
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        question = get_object_or_404(Question, pk=pk)
        if not question.owner.id == request.user.id:
            raise PermissionDenied('Unauthorized, you do not own this question.')
        # Before serializing data and after confirming ownership we attach the currently signed in user as the owner
        request.data['question']['owner'] = request.user.id
        # Validate updates with serializer
        ms = QuestionSerializer(question, data=request.data['question'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
