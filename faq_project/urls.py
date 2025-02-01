from django.contrib import admin
from django.urls import path, include  # ✅ Import `include`

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # ✅ No more error
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from rest_framework import routers
from faq_app.views import FAQViewSet

router = routers.DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    # ... existing urls ...
    path('api/', include(router.urls)),
]
