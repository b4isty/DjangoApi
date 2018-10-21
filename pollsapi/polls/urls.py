from django.urls import path
from .views import polls_list, polls_details
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet,UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

# urlpatterns = [
#     path("polls/",polls_list, name="polls_list"),
#     path("polls/<int:pk>", polls_details, name="polls_details")
# ]

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    # path("polls/",PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>", PollDetail.as_view(), name="polls_details"),
    # path("choices/",ChoiceList.as_view(), name='choice_list'),
    # path("vote/", CreateVote.as_view(), name='create_vote'),

    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name='login')
    # path("login/", views.obtain_auth_token, name='login')

    ]

urlpatterns+=router.urls






