import logging
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from greeting_api.serializers import GreetingSerializer
from django.contrib.auth import get_user_model
from openedx.core.lib.api.authentication import BearerAuthenticationAllowInactiveUser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from greeting_api.models import Greeting


logger = logging.getLogger(__name__)


class GreetingView(APIView):
    def post(self, request):
        logger.info(f"Start post")
        serializer = GreetingSerializer(data=request.data)
        logger.info(f"After serializer")
        if serializer.is_valid():
            message = serializer.data["message"]
            logger.info(f"Message from user: {message}")
            Greeting.objects.create(message=message)
            if message.lower() == "hello":
                message = "goodbye"
                request.data._mutable = True
                request.data["message"] = message
                self.post(request)

        message = serializer.data["message"]
        return Response({"Message from user": message})

    def get(self, request):
        return Response({"message": "Hello!"})
