'''Tag Menu urls module.'''
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tag_menu import views

urlpatterns = [
    path('<path:url>?<str:selected>', views.show_selected, name='select'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
