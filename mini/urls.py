
from django.urls import path, include
from .views import(
	QuoteCreateAPIView, QuoteChangeAPIView,
	DayQuoteAPIView)

app_name = "mini"

urlpatterns = [
	path('my_quotes/', QuoteCreateAPIView.as_view()),
	path('my_quotes/<id>/', QuoteChangeAPIView.as_view()),
	path('quote_of_the_day/', DayQuoteAPIView.as_view())
	# path('my_quotes/today/', DayQuoteAPIView.as_view())
]