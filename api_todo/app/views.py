from black import maybe_install_uvloop

from app.serializers import TodoSerializer
from app.models import Todo
from rest_framework import viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


