from django.urls import path

from contacts import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
]


urlpatterns = [
    path("", views.contact_list, name="contact-list"),
    path("<int:pk>/", views.contact_detail, name="contact-detail"),
]