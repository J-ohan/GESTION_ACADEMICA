from rest_framework import viewsets

from . import models
from .serializers import serializer_map


def _create_viewset_class(model, serializer):
    return type(
        f"{model.__name__}ViewSet",
        (viewsets.ModelViewSet,),
        {
            "queryset": model.objects.all(),
            "serializer_class": serializer,
            "lookup_field": model._meta.pk.name,
        },
    )


viewset_map = {}
for model_name, serializer in serializer_map.items():
    model = getattr(models, model_name)
    viewset_map[model_name] = _create_viewset_class(model, serializer)
