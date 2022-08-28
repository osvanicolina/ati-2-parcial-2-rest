from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class ObjectItem(APIView):
    def get(self, request, format=None):
        return Response({
                "id": 1,
                "name": "Objeto"
            })

class ListItems(APIView):
    def get(self, request, format = None):
        return Response([
            {
                "id": 1,
                "name": "Primer item de lista"
            },
            {
                "id": 2,
                "name": "Segundo item de lista"
            }
        ])

class NestedItem(APIView):
    def get(self, request, format = None):
        return Response({
            "items_list": [
                {
                    "id": 1,
                    "name": "Primer item de lista"
                },
                {
                    "id": 2,
                    "name": "Segundo item de lista"
                }
            ],
            "item_object": {
                "id": 1,
                "name": "Objeto"
            }
        })
