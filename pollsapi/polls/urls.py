from django.urls import path
from .views import polls_list, polls_details
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote
# urlpatterns = [
#     path("polls/",polls_list, name="polls_list"),
#     path("polls/<int:pk>", polls_details, name="polls_details")
# ]

urlpatterns = [
    path("polls/",PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>", PollDetail.as_view(), name="polls_details"),
    path("choices/",ChoiceList.as_view(), name='choice_list'),
    path("vote/", CreateVote.as_view(), name='create_vote')
]