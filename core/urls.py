from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularRedocView,
        SpectacularSwaggerView,
    )

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include("authentications.urls")),
    path("api/product/", include("product_management.urls")),
    path("api/cart/", include("cart_management.urls")),
    path("api/checkout/", include("checkout_management.urls")),
    path("api/vendor/", include("vendors.urls")),
]

media_url = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
urlpatterns += media_url
swagger_urlpatterns = [
        path(
            "api/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
        ),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
urlpatterns += swagger_urlpatterns