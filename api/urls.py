from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.question_views import Questions, QuestionDetail
from .views.answer_views import Answers, AnswerDetail

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('questions/', Questions.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
    path('answers/', Answers.as_view(), name='answers'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer_detail'),
]
