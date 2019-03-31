from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import MyQuotes
from .serializers import QuotesSerializer

# Create your views here.

class QuoteCreateAPIView(ListCreateAPIView):
	serializer_class = QuotesSerializer
	queryset = MyQuotes.objects.all()

