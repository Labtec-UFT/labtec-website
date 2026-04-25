from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.interfaces.public.api.v1.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Servir arquivos estáticos da raiz (team.json, favicon.svg, etc)
    urlpatterns += [
        re_path(r'^(?P<path>[\w\-]+\.\w+)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

# SPA Fallback - deve ser o último padrão
# Qualquer URL sem extensão cai no SPA
urlpatterns += [
    re_path(r'^(?!api/|admin/)[^.]*/?$', TemplateView.as_view(template_name='index.html')),
]
