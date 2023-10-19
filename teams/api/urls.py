from django.urls import path

from teams.api.views import TeamCreateView, TeamRetrieveUpdateDestroyAPIView, TeamListAPIView, UserCreateView, \
    UserListAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('team/create/', TeamCreateView.as_view(), name='team-create'),
    path('team/<int:id>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-retrieve-update-destroy'),
    path('teams/', TeamListAPIView.as_view(), name='team-list'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:id>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
]
