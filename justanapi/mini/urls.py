
from django.urls import path, include
from .views import QuoteCreateAPIView

app_name = "mini"

urlpatterns = [
	path('my_quotes/', QuoteCreateAPIView.as_view()),
]