from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from greeting_api.serializers import GreetingSerializer

class GreetingView(APIView):

    def post(self, request):
        serializer = GreetingSerializer(data=request.data)
        username = request.user.username
        if serializer.is_valid():
            message = serializer.data["text"]

            if message == "hello":
                message = "goodbye"
                request.data["text"] = message
                self.post(request)
                return Response({"user": username, "text": message})

        message = request.data["text"]
        return Response({"user": username, "text": message})

    def get(self, request):
        return Response({"message": "Hey!"})
