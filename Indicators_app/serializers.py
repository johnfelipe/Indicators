from . import models

from rest_framework import serializers


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Section
        fields = (
            'pk', 
            'section_designation', 
        )


class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Indicator
        fields = (
            'pk', 
            'indicator_designation', 
        )


class PeriodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Periode
        fields = (
            'pk', 
            'periode_designation', 
        )


class OutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Output
        fields = (
            'pk', 
            'output_designation', 
            'output_description', 
        )


class IndicatorSectionPeriodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.IndicatorSectionPeriode
        fields = (
            'pk', 
            'target_value', 
            'value', 
        )


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Partner
        fields = (
            'pk', 
            'partner_designation', 
        )


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Report
        fields = (
            'pk', 
            'report_designation', 
        )


class InvolvedPartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvolvedPartner
        fields = (
            'pk', 
            'results', 
        )


class ConcernedReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ConcernedReport
        fields = (
            'pk', 
        )


