from rest_framework import serializers
from django.contrib.auth.models import User

from items.models import Item , FavoriteItem

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):

	num_of_likes = serializers.SerializerMethodField()

	detail = serializers.HyperlinkedIdentityField(
		view_name='item-detail',
		lookup_field='id',
		lookup_url_kwarg='item_id'
		)

	added_by = UserSerializer()

	class Meta:
		model = Item 
		fields = ['name', 'detail', 'added_by', 'num_of_likes']

	def get_num_of_likes(self, obj):
		liked_objects = FavoriteItem.objects.filter(item=obj)
		count = len(liked_objects)
		return count


class ItemDetailsSerializer(serializers.ModelSerializer):

	names_of_lovely_ppl = serializers.SerializerMethodField()

	class Meta:
		model = Item 
		fields = ['image', 'name', 'description', 'names_of_lovely_ppl']


	def get_names_of_lovely_ppl(self, obj):
		favorited  = FavoriteItem.objects.filter(item=obj)
		# .distinct()
		
		name_list =[]

		for name in favorited:
			name1 = name.user
			name_list.append(name1)

		serialized_names = UserSerializer(name_list, many=True)

		return serialized_names.data

