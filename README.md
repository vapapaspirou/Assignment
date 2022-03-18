# Assignment
API code for assignment


First we install Django with the command 'pip install Django'


We create our project, 'django-admin startproject drf'

We create the app, 'python manage.py startapp accounts'

Two commands to create our database
python manage.py makemigrations
python manage.py migrate 

After that we must write our app in our settings file

We build our models at models file, to create the database.

We create a py file, named serializers and we put in there the information that we need to show.


At accounts/urls.py file the urls urlpatterns = [
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
  
  are the ones what we need write to run the program 
  for example ('http://127.0.0.1:8000/api/register/')
  
  
  

