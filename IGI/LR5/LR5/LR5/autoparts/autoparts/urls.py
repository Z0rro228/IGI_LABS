from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="index"),
    path("", index, name="home"),
    path('coupons/', include('coupon.urls')),
    path('portal/', include('portal.urls')),
    path('deals/', include('deal.urls')),
    path('users/', include('users.urls')),
    path('suppliers/', include('supplier.urls')),
    path('statistics/', include('app_statistics.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
