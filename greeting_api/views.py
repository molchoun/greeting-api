import logging
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from greeting_api.serializers import GreetingSerializer
from django.contrib.auth import get_user_model
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.auth.session.authentication import SessionAuthenticationAllowInactiveUser
from openedx.core.lib.api.authentication import BearerAuthenticationAllowInactiveUser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from greeting_api.models import Greeting


logger = logging.getLogger(__name__)


class GreetingView(APIView):
    authentication_classes = (
        JwtAuthentication,
        BearerAuthenticationAllowInactiveUser,
        SessionAuthenticationAllowInactiveUser,
    )
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)
    def post(self, request):

        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.data["message"]
            logger.info(f"Message from user: {message}")
            Greeting.objects.create(message=message)
            if message.lower() == "hello":
                message = "goodbye"
                request.data._mutable = True
                request.data["message"] = message
                self.post(request)
                return Response({"Message from user": message})

        message = serializer.data["message"]
        return Response({"Message from user": message})

    def get(self, request):
        return Response({"message": "Hello!"})
