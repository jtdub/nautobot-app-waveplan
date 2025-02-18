"""Waveplan views."""

from nautobot.apps import ui, views

from nautobot_waveplan.models import WavePlan, OpticalPath


class WavePlanUIViewSet(views.NautobotUIViewSet):
    """WavePlan UIViewSet."""
    bulk_update_form_class = None
    filterset_class = None
    filterset_form_class = None
    form_class = None
    serializer_class = None
    queryset = WavePlan.objects.all()
    table_class = None


class OpticalPathUIViewSet(views.NautobotUIViewSet):
    """OpticalPath UIViewSet."""
    bulk_update_form_class = None
    filterset_class = None
    filterset_form_class = None
    form_class = None
    serializer_class = None
    queryset = OpticalPath.objects.all()
    table_class = None
