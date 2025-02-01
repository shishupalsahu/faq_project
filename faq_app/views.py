from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang', 'en')
        context.update({'lang': lang})
        return context

from django.core.cache import cache

class FAQViewSet(viewsets.ModelViewSet):
    # ... existing code ...

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        data = cache.get(cache_key)

        if not data:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60*60)  # Cache for 1 hour

        return Response(data)
