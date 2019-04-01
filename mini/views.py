from rest_framework.generics import(
	ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from .models import MyQuotes
from .serializers import QuotesSerializer

# Create your views here.

class QuoteCreateAPIView(ListCreateAPIView):
	serializer_class = QuotesSerializer
	queryset = MyQuotes.objects.all()


class QuoteChangeAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = QuotesSerializer
	lookup_field = "id"
	queryset = MyQuotes.objects.all()

