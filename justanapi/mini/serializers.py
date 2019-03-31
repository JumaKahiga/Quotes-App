from rest_framework import serializers

from .models import MyQuotes
class QuotesSerializer(serializers.ModelSerializer):
	"""Serializes quotes list."""
	posted = serializers.ReadOnlyField(source="when_created")

	class Meta:
		model = MyQuotes
		fields = ["quote", "posted", "id", "author"]