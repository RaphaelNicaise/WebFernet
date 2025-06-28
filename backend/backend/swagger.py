from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Web Fernet API",
        default_version='v1',
        description="Documentación de la API de Web Fernet"
    ),
    public=True,
).with_ui('swagger', cache_timeout=0)