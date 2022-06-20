from rest_framework import serializers
from .models import CompUsers


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompUsers
        fields = (
            'id',
            'name',
            'surname',
            'employed',
            'salary',
            'position'
        )


class WorkerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompUsers
        fields = (
            'id',
            'name',
            'surname',
            'employed',
            'salary',
            'position'
        )
        read_only_fields = ('id', 'name', 'surname')

