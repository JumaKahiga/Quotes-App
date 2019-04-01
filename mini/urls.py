
from django.urls import path, include
from .views import(
	QuoteCreateAPIView, QuoteChangeAPIView)

app_name = "mini"

urlpatterns = [
	path('my_quotes/', QuoteCreateAPIView.as_view()),
	path('my_quotes/<id>/', QuoteChangeAPIView.as_view())
]