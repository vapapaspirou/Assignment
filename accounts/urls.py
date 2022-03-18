from .views import RegisterAPI, AccountsView, SkillsViews, SkillsAllView, SkillsDetailView, UserList, UserDetail,\
    PostList, PostDetail
from knox import views as knox_views
from .views import LoginAPI, ChangePasswordView
from django.urls import path


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/account/', AccountsView.as_view({'get': 'list'}), name='account'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/skills/', SkillsViews.as_view(), name='skills'),
    path('api/allskills/', SkillsAllView.as_view({'get': 'list'}), name='skillsall'),
    path('api/allskills/<pk>/', SkillsDetailView.as_view(), name='skillsalls'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),

]