from django.contrib import admin
from Indicators_app.models import *
from import_export import resources
from import_export.admin import ExportMixin


class IndicatorSectionPeriodeAdmin(admin.ModelAdmin):
    actions = ["download_csv"]
    list_display = [
        "section",
        "indicator",
        "periode",
    ]

    def get_section_designation(self, obj):
        return obj.section.section_designation

    def get_indicator_designation(self, obj):
        return obj.indicator.indicator_designation

    def get_periode_designation(self, obj):
        return obj.periode.periode_designation

    get_section_designation.short_description = "Section"
    get_indicator_designation.short_description = "Indicator"
    get_periode_designation.short_description = "Periode"


    list_filter = ("section__section_designation", "periode__periode_designation")


class IndicatorSectionPeriodeAdmin(admin.ModelAdmin):
    actions = ["download_csv"]
    list_display = [
        "section",
        "indicator",
        "periode",
        "output",
        "target_value",
        "value",
    ]

    def get_section_designation(self, obj):
        return obj.section.section_designation

    def get_indicator_designation(self, obj):
        return obj.indicator.indicator_designation

    def get_periode_designation(self, obj):
        return obj.periode.periode_designation

    def get_output(self, obj):
        return obj.output

    def get_target_value(self, obj):
        return obj.target_value

    def get_value(self, obj):
        return obj.value

    get_section_designation.short_description = "Section"
    get_indicator_designation.short_description = "Indicator"
    get_periode_designation.short_description = "Periode"
    get_output.short_description = "Output"
    get_target_value.short_description = "Target"
    get_value.short_description = "Value"


    list_filter = ("section__section_designation", "periode__periode_designation")


class InvolvedPartnerAdmin(admin.ModelAdmin):
    actions = ["download_csv"]
    list_display = [
        "indicator",
        "partner",
        "results",
    ]
    def get_indicator_designation(self, obj):
        return obj.indicator.indicator.indicator_designation

    def get_partner_designation(self, obj):
        return obj.partner.partner_designation

    def get_partner_results(self, obj):
        return obj.results

    get_indicator_designation.short_description = "Indicator"
    get_partner_designation.short_description = "Partner"
    get_partner_results.short_description = "Results"

    list_filter = ("partner__partner_designation", "indicator__section__section_designation", "results")


class ConcernedReportAdmin(admin.ModelAdmin):
	actions = ["download_csv"]
	list_display = [
		"indicator",
		"report",
		]

	def get_indicator_designation(self, obj):
		return obj.indicator.indicator.indicator_designation

	def get_report_designation(self, obj):
		return obj.report.report_designation

	get_indicator_designation.short_description = "Indicator"
	get_report_designation.short_description = "Report"

	list_filter = ("report__report_designation", "indicator__section__section_designation")


class ReportAdmin(admin.ModelAdmin):
	actions = ["download_csv"]

	list_display = [
		"report_designation",
		]

	def get_report_designation(self, obj):
		return obj.report_designation

	get_report_designation.short_description = "Report"


class SectionAdmin(admin.ModelAdmin):
	actions = ["download_csv"]

	list_display = [
		"section_designation",
		]

	def get_section_designation(self, obj):
		return obj.section_designation

	get_section_designation.short_description = "Section"


class IndicatorAdmin(admin.ModelAdmin):
	actions = ["download_csv"]

	list_display = [
		"indicator_designation",
		]

	def get_indicator_designation(self, obj):
		return obj.indicator_designation

	get_indicator_designation.short_description = "Indicator"


class PeriodeAdmin(admin.ModelAdmin):
	actions = ["download_csv"]

	list_display = [
		"periode_designation",
		]

	def get_periode_designation(self, obj):
		return obj.periode_designation

	get_periode_designation.short_description = "Periode"


class OutputAdmin(admin.ModelAdmin):
    actions = ["download_csv"]

    list_display = [
        "output_designation",
        "output_description",
        ]

    def get_output_designation(self, obj):
        return obj.output_designation

    def get_output_description(self, obj):
        return obj.output_designation

    get_output_designation.short_description = "Output"
    get_output_description.short_description = "Output"


class PartnerAdmin(admin.ModelAdmin):
	actions = ["download_csv"]

	list_display = [
		"partner_designation",
		]

	def get_partner_designation(self, obj):
		return obj.partner_designation

	get_partner_designation.short_description = "Partner"


admin.site.register(Section, SectionAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Periode, PeriodeAdmin)
admin.site.register(Output, OutputAdmin)
admin.site.register(IndicatorSectionPeriode, IndicatorSectionPeriodeAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(InvolvedPartner, InvolvedPartnerAdmin)
admin.site.register(ConcernedReport, ConcernedReportAdmin)