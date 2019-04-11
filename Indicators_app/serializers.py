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

    section = serializers.SerializerMethodField()
    indicator = serializers.SerializerMethodField()
    periode = serializers.SerializerMethodField()
    output =  serializers.SerializerMethodField()

    def get_section(self, indicsecper):
        return indicsecper.section.section_designation

    def get_indicator(self, indicsecper):
        return indicsecper.indicator.indicator_designation

    def get_periode(self, indicsecper):
        return indicsecper.periode.periode_designation

    def get_output(self, indicsecper):
        return "{0} - {1}".format(indicsecper.output.output_designation, indicsecper.output.output_description)


    class Meta:
        model = models.IndicatorSectionPeriode
        fields = (
            'pk', 
            'target_value', 
            'value',
            'section',
            'indicator',
            'periode',
            'output', 
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



class IndicatorMatrix(serializers.ModelSerializer):


    class Meta:
        model = models.ConcernedReport
        fields = (
            'indicator', 
            'report', 
        )