# Use include() to add paths from the catalog application
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

# urlpatterns = [
#     path('blog/', include('blog.urls')),
#     path('', RedirectView.as_view(url='/blog/', permanent=True)),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]

urlpatterns = [
    path('', views.post_list, name='post_list'),
]