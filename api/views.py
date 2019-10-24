from items.models import Item
from .serializers import ItemListSerializer, ItemDetailsSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from .permissions import OnlyStaffAndYou


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'description']

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	# permission_classes = [OnlyStaffAndYou]
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'