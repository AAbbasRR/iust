from django.db import models
from django.utils.translation import gettext_lazy as _


class FrequentlyQuestion(models.Model):
    class Meta:
        verbose_name = _("Frequently Question")
        verbose_name_plural = _("Frequently Questions")
        ordering = ["-id"]

    question = models.CharField(
        max_length=100, null=False, blank=False, verbose_name=_("Question")
    )
    answer = models.TextField(null=False, blank=False, verbose_name=_("Answer"))

    def __str__(self) -> str:
        return f"{self.question}"
