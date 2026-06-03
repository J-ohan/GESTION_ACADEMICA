from rest_framework.routers import DefaultRouter

from . import models, views

router = DefaultRouter()
for model_name, viewset in views.viewset_map.items():
    model = getattr(models, model_name)
    router.register(model._meta.db_table, viewset, basename=model._meta.model_name)

urlpatterns = router.urls
