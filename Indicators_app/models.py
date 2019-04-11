from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class Section(models.Model):

    # Fields
    section_designation = models.CharField(max_length=200)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_section_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_section_update', args=(self.pk,))


class Indicator(models.Model):

    # Fields
    indicator_designation = models.CharField(max_length=500)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_indicator_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_indicator_update', args=(self.pk,))


class Periode(models.Model):

    # Fields
    periode_designation = models.CharField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_periode_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_periode_update', args=(self.pk,))


class Output(models.Model):

    # Fields
    output_designation = models.CharField(max_length=500)
    output_description = models.CharField(max_length=500, null=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_output_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_output_update', args=(self.pk,))


class IndicatorSectionPeriode(models.Model):

    # Fields
    target_value = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)

    # Relationship Fields
    section = models.ForeignKey(
        'Indicators_app.Section',
        related_name="indicatorsectionperiodes", on_delete=models.CASCADE
    )
    indicator = models.ForeignKey(
        'Indicators_app.Indicator',
        related_name="indicatorsectionperiodes", on_delete=models.CASCADE
    )
    periode = models.ForeignKey(
        'Indicators_app.Periode',
        related_name="indicatorsectionperiodes", on_delete=models.CASCADE
    )
    output = models.ForeignKey(
        'Indicators_app.Output',
        related_name="indicatorsectionperiodes", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_indicatorsectionperiode_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_indicatorsectionperiode_update', args=(self.pk,))


class Partner(models.Model):

    # Fields
    partner_designation = models.CharField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_partner_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_partner_update', args=(self.pk,))


class Report(models.Model):

    # Fields
    report_designation = models.CharField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_report_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_report_update', args=(self.pk,))


class InvolvedPartner(models.Model):

    # Fields
    results = models.CharField(max_length=100, null=True)

    # Relationship Fields
    indicator = models.ForeignKey(
        'Indicators_app.IndicatorSectionPeriode',
        related_name="involvedpartners", on_delete=models.CASCADE
    )
    partner = models.ForeignKey(
        'Indicators_app.Partner',
        related_name="involvedpartners", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_involvedpartner_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_involvedpartner_update', args=(self.pk,))


class ConcernedReport(models.Model):


    # Relationship Fields
    indicator = models.ForeignKey(
        'Indicators_app.IndicatorSectionPeriode',
        related_name="concernedreports", on_delete=models.CASCADE
    )
    report = models.ForeignKey(
        'Indicators_app.Report',
        related_name="concernedreports", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('indicators:Indicators_app_concernedreport_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('indicators:Indicators_app_concernedreport_update', args=(self.pk,))
