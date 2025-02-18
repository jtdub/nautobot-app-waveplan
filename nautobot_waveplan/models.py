"""WavePlan models."""

from django.db import models
from nautobot.apps.constants import CHARFIELD_MAX_LENGTH
from nautobot.apps.models import OrganizationalModel, extras_features

GRID_TYPE_CHOICES = (("ITU-50", "50 GHz"), ("ITU-100", "100 GHz"), ("ITU-200", "200 GHz"), ("Flex-Grid", "Flexible"))
PROTECTION_TYPE_CHOICES = (("1+1", "1+1 Protection"), ("Shared", "Shared Protection"), ("None", "No Protection"))


@extras_features(
    "custom_links",
    "custom_validators",
    "export_templates",
    "graphql",
    "webhooks",
)
class WavePlan(OrganizationalModel):
    """DWDM Wave Plan model."""

    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    description = models.CharField(max_length=CHARFIELD_MAX_LENGTH, blank=True)
    channel_spacing = models.PositiveIntegerField(help="Channel spacing in GHz (e.g., 50, 100, 200)")
    grid_type = models.CharField(
        max_length=10,
        choices=GRID_TYPE_CHOICES,
        default="ITU-50",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """WavePlan string representation."""
        return self.name


@extras_features(
    "custom_links",
    "custom_validators",
    "export_templates",
    "graphql",
    "webhooks",
)
class OpticalPath(OrganizationalModel):
    """DWDM Optical Path model."""

    name = models.CharField(max_length=100, unique=True)
    wave_plan = models.ForeignKey(WavePlan, on_delete=models.CASCADE, related_name="optical_paths")
    source = models.ForeignKey("dcim.Device", on_delete=models.CASCADE, related_name="optical_source")
    destination = models.ForeignKey("dcim.Device", on_delete=models.CASCADE, related_name="optical_destination")
    circuits = models.ManyToManyField("circuits.Circuit", blank=True)
    protection_type = models.CharField(
        max_length=10,
        choices=PROTECTION_TYPE_CHOICES,
        default="None",
    )

    def __str__(self):
        """OpticalPath string representation."""
        return f"{self.name} ({self.source} -> {self.destination})"
