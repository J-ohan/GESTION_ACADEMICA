from rest_framework import serializers

from . import models


def _create_serializer_class(model):
    meta = type("Meta", (), {"model": model, "fields": "__all__"})

    serializer_name = f"{model.__name__}Serializer"
    return type(serializer_name, (serializers.ModelSerializer,), {"Meta": meta})


serializer_map = {}
for attribute_name in dir(models):
    attr = getattr(models, attribute_name)
    if isinstance(attr, type) and hasattr(attr, "_meta") and attr.__module__ == models.__name__:
        serializer_map[attribute_name] = _create_serializer_class(attr)
