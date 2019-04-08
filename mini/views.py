from rest_framework.generics import(
	ListCreateAPIView, ListAPIView, 
	RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from .models import MyQuotes
from .serializers import QuotesSerializer
from .utils import get_random_object

# Create your views here.

class QuoteCreateAPIView(ListCreateAPIView):
	serializer_class = QuotesSerializer
	queryset = MyQuotes.objects.all()


class QuoteChangeAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = QuotesSerializer
	lookup_field = "id"
	queryset = MyQuotes.objects.all()



class DayQuoteAPIView(ListAPIView):
	serializer_class = QuotesSerializer
	
	def get_queryset(self):
		random_id = get_random_object(MyQuotes)
		check_if_exists = MyQuotes.objects.filter(id=random_id).exists()
		if not check_if_exists:
			return MyQuotes.objects.filter(id=get_random_object(MyQuotes))
		return MyQuotes.objects.filter(id=random_id)


