from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


class GreetingView(APIView):
    def get(self, request):
        return Response({"message": "Hey!"})
