from django import forms
from .models import Section, Indicator, Periode, Output, IndicatorSectionPeriode, Partner, Report, InvolvedPartner, ConcernedReport


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_designation']


class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ['indicator_designation']


class PeriodeForm(forms.ModelForm):
    class Meta:
        model = Periode
        fields = ['periode_designation']


class OutputForm(forms.ModelForm):
    class Meta:
        model = Output
        fields = ['output_designation', 'output_description']


class IndicatorSectionPeriodeForm(forms.ModelForm):
    class Meta:
        model = IndicatorSectionPeriode
        fields = ['target_value', 'value', 'section', 'indicator', 'periode', 'output']


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['partner_designation']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_designation']


class InvolvedPartnerForm(forms.ModelForm):
    class Meta:
        model = InvolvedPartner
        fields = ['results', 'indicator', 'partner']


class ConcernedReportForm(forms.ModelForm):
    class Meta:
        model = ConcernedReport
        fields = ['indicator', 'report']


