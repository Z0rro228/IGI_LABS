from django.contrib import admin
from django.urls import path
from core.views import index
from django.conf import settings
from django.conf.urls.static import static

from users.views import registration, login, logout_user
from users.models import CustomUser
from supplier.views import get_all_suppliers
from deal.views import buy_item, get_deals
from portal.views import *
from coupon.views import coupons_view, enter_coupon
from portal.services.nationality import nationalize

urlpatterns = [
    path('admin/', admin.site.urls, name="index"),
    path("", index, name="home"),
    path("registration/", registration, name="reg"),
    path("login/", login, name="login"),
    path("logout/", logout_user, name="logout"),
    path("suppliers/", get_all_suppliers, name="suppliers"),
    path("buy<int:pk>/", buy_item, name="buy_item"),
    path("deals/", get_deals, name="deals"),
    path("about/", about_view, name="about"),
    path("news/", news_view, name="news"),
    path("faq/", faq_view, name="faq"),
    path("contacts/", contacts_view, name="contacts"),
    path("policy/", policy_view, name="policy"),
    path("vacancies/", vacancies_view, name="vacancies"),
    path("feedback/", feedback_view, name="feedback"),
    path("places/", places_view, name="places"),
    path("accept_feedback/", accept_feedback, name="accept_feedback"),
    path("coupons/", coupons_view, name="coupons"),
    path("enter_coupon/", enter_coupon, name="enter_coupon"),
    path("joke/", joke_view, name="joke"),
    path("nationalize/", nationalize, name="nationalize"),
    path("create_faq/", create_faq_view, name="create_faq"),
    path("create_new_faq/", create_new_faq, name="create_new_faq"),
    path("update_faq_form/", update_faq_view, name="update_faq_view"),
    path("update_faq/", update_faq, name="update_faq"),
    path("delete_faq_form/", delete_faq_view, name="delete_faq_view"),
    path("delete_faq/", delete_faq, name="delete_faq"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
