from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Section(models.Model):
	""" In this model we store sections """
	section_designation = models.CharField(max_length=200)

	def __unicode__(self):
		return self.section_designation

class Indicator(models.Model):
	""" In this model we store indicators """
	indicator_designation = models.CharField(max_length=500)

	def __unicode__(self):
		return self.indicator_designation

class Periode(models.Model):
	""" In this model we store periodes """
	periode_designation = models.CharField(max_length=100)

	def __unicode__(self):
		return self.periode_designation

class Output(models.Model):
	""" In this model we store outputs """
	output_designation = models.CharField(max_length=500)
	output_description = models.CharField(max_length=500, null=True)

	def __unicode__(self):
		return "{0} - {1}".format(
		self.output_designation, self.output_description
		)

class IndicatorSectionPeriode(models.Model):
	""" In this model we link sections, indicators and periodes """
	section = models.ForeignKey(Section)
	indicator = models.ForeignKey(Indicator)
	periode = models.ForeignKey(Periode)
	output = models.ForeignKey(Output)
	target_value = models.CharField(max_length=100, null=True)
	value = models.CharField(max_length=100, null=True)

	def __unicode__(self):
		return "{0} - {1} - {2} - {3}".format(
		self.section, self.indicator, self.periode, self.value
		)

class Partner(models.Model):
	""" In this model we store partners """
	partner_designation = models.CharField(max_length=100)

	def __unicode__(self):
		return self.partner_designation

class Report(models.Model):
	""" In this model we store reports """
	report_designation = models.CharField(max_length=100)

	def __unicode__(self):
		return self.report_designation


class InvolvedPartner(models.Model):
	""" In this model we will link indicators (for a given section and period) with partners """
	indicator = models.ForeignKey(IndicatorSectionPeriode)
	partner = models.ForeignKey(Partner)
	results = models.CharField(max_length=100, null=True)

	def __unicode__(self):
		return "{0} - {1}".format(
		self.indicator, self.partner
		)


class ConcernedReport(models.Model):
	""" In this model we will link indicators (for a given section and period) with concerned reports """
	indicator = models.ForeignKey(IndicatorSectionPeriode)
	report = models.ForeignKey(Report)

	def __unicode__(self):
		return "{0} - {1}".format(
		self.indicator, self.report
		)