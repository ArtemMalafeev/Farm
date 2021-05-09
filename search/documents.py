from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from handbook.models import Fertilizer


@registry.register_document
class FertilizersDocument(Document):
    class Index:
        name = 'fertilizers'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Fertilizer

        fields = [
            'name',
            'slug',
            'units',
            'color',
            'description',
            'advantages',
            'created',
            'updated',
            'post',
        ]
