from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.answer import Answer
from ..serializers import AnswerSerializer, UserSerializer

# Create views
class Answers(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  serializer_class = AnswerSerializer
  def get(self, request):
      """Index Request"""
      answers = Answer.objects.filter(owner=request.user.id)
      data = AnswerSerializer(answer, many=True).data
      return Response({ 'answer': data })

  def post(self, request):
      """Create Request"""
      request.data['answer']['owner'] = request.user.id
      answer = AnswerSerializer(data=request.data['answer'])
      if answer.is_valid():
          answer.save()
          return Response({ 'answer': answer.data }, status=status.HTTP_201_CREATED)
      return Response(answer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request, pk):
      """Show Request"""
      answer = get_object_or_404(answer, pk=pk)
      if not request.user.id == answer.owner.id:
          raise PermissionDenied('Unauthorized, you do not own this answer.')
      data = AnswerSerializer(answer).data
      return Response({ 'answer': data })

  def delete(self, request, pk):
      """Delete Request"""
      answer = get_object_or_404(Answer, pk=pk)
      if not request.user.id == answer.owner.id:
          raise PermissionDenied('Unauthorized, you do not own this answer.')
      answer.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
      """Update Request"""
      answer = get_object_or_404(Answer, pk=pk)
      if not answer.owner.id == request.user.id:
          raise PermissionDenied('Unauthorized, you do not own this answer.')
      request.data['answer']['owner'] = request.user.id
      ms = AnswerSerializer(answer, data=request.data['answer'])
      if ms.is_valid():
          ms.save()
          return Response(ms.data)
      return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
