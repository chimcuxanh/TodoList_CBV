from .views import TaskList, TaskDetail,\
    TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', TaskList.as_view(), name='home'),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail'),
    path('edit/', TaskCreate.as_view(), name='edit'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
]