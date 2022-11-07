from rest_framework.response import Response
from rest_framework.views import APIView
import requests
# Create your views here.
class MakeRestRequest(APIView):
    def get(self, request, format = None):
        url = "https://realstateapidev.herokuapp.com/properties"
        result = requests.get(url)

        print(result.json())

        return Response(result.json())