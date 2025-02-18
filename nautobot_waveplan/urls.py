"""Django urlpatterns declaration for nautobot_waveplan app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter

# Uncomment the following line if you have views to import
# from nautobot_waveplan import views


router = NautobotUIViewSetRouter()

# Here is an example of how to register a viewset, you will want to replace views.WaveplanUIViewSet with your viewset
# router.register("nautobot_waveplan", views.WaveplanUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("nautobot_waveplan/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
