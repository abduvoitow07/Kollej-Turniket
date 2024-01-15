from django.urls import path
from .views import *

app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agent-list"),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('<int:pk>/delete', AgentDeleteView.as_view(), name="agent-delete"),
    path('create/', AgentCreateView.as_view(), name="agent-create"),
]