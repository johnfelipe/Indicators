from django.shortcuts import render
from Indicators_app.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import F
import json
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .forms import *


class SectionListView(ListView):
    model = Section


class SectionCreateView(CreateView):
    model = Section
    form_class = SectionForm


class SectionDetailView(DetailView):
    model = Section


class SectionUpdateView(UpdateView):
    model = Section
    form_class = SectionForm


class IndicatorListView(ListView):
    model = Indicator


class IndicatorCreateView(CreateView):
    model = Indicator
    form_class = IndicatorForm


class IndicatorDetailView(DetailView):
    model = Indicator


class IndicatorUpdateView(UpdateView):
    model = Indicator
    form_class = IndicatorForm


class PeriodeListView(ListView):
    model = Periode


class PeriodeCreateView(CreateView):
    model = Periode
    form_class = PeriodeForm


class PeriodeDetailView(DetailView):
    model = Periode


class PeriodeUpdateView(UpdateView):
    model = Periode
    form_class = PeriodeForm


class OutputListView(ListView):
    model = Output


class OutputCreateView(CreateView):
    model = Output
    form_class = OutputForm


class OutputDetailView(DetailView):
    model = Output


class OutputUpdateView(UpdateView):
    model = Output
    form_class = OutputForm


class IndicatorSectionPeriodeListView(ListView):
    model = IndicatorSectionPeriode


class IndicatorSectionPeriodeCreateView(CreateView):
    model = IndicatorSectionPeriode
    form_class = IndicatorSectionPeriodeForm


class IndicatorSectionPeriodeDetailView(DetailView):
    model = IndicatorSectionPeriode


class IndicatorSectionPeriodeUpdateView(UpdateView):
    model = IndicatorSectionPeriode
    form_class = IndicatorSectionPeriodeForm


class PartnerListView(ListView):
    model = Partner


class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerForm


class PartnerDetailView(DetailView):
    model = Partner


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerForm


class ReportListView(ListView):
    model = Report


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm


class ReportDetailView(DetailView):
    model = Report


class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm


class InvolvedPartnerListView(ListView):
    model = InvolvedPartner


class InvolvedPartnerCreateView(CreateView):
    model = InvolvedPartner
    form_class = InvolvedPartnerForm


class InvolvedPartnerDetailView(DetailView):
    model = InvolvedPartner


class InvolvedPartnerUpdateView(UpdateView):
    model = InvolvedPartner
    form_class = InvolvedPartnerForm


class ConcernedReportListView(ListView):
    model = ConcernedReport


class ConcernedReportCreateView(CreateView):
    model = ConcernedReport
    form_class = ConcernedReportForm


class ConcernedReportDetailView(DetailView):
    model = ConcernedReport


class ConcernedReportUpdateView(UpdateView):
    model = ConcernedReport
    form_class = ConcernedReportForm



def date_handler(obj):
    if hasattr(obj, "isoformat"):
        return obj.isoformat()
    else:
        raise TypeError


def landing(request):
    return render(request, "landing_page.html")


def home(request):
    d = dict()
    d["pagetitle"] = "Choose Sections"
    return render(request, "home.html", d)


def wash(request):
    d = dict()
    d["pagetitle"] = "Choose Sections"
    return render(request, "wash.html", d)



@login_required
def general_info(request):
    d = {}
    d["pagetitle"] = "General informations"

    general_indicators_informations = (
        IndicatorSectionPeriode.objects.all()
        .annotate(periode_designation=F("periode__periode_designation"))
        .annotate(section_designation=F("section__section_designation"))
        .annotate(indicator_designation=F("indicator__indicator_designation"))
        .annotate(output_designation=F("output__output_designation"))
        .values()
    )

    for indi in general_indicators_informations:
        related_reports = (
            ConcernedReport.objects.filter(indicator=indi["id"])
            .annotate(report_designation=F("report__report_designation"))
            .values()
        )
        reports_list = []
        if len(related_reports) > 0:
            first_report = True
            for r in related_reports:
                one_report_name = ""
                if first_report:
                    one_report_name = r["report_designation"]
                else:
                    one_report_name = ", " + r["report_designation"]
                reports_list.append(one_report_name)
        indi["related_reports"] = reports_list

        related_partners = (
            InvolvedPartner.objects.filter(indicator=indi["id"])
            .annotate(partner_name=F("partner__partner_designation"))
            .values()
        )
        partner_list = []
        if len(related_partners) > 0:
            first_partner = True
            for p in related_partners:
                one_partner_name = ""
                if first_partner:
                    one_partner_name = p["partner_name"]
                else:
                    one_partner_name = ", " + p["partner_name"]
                partner_list.append(one_partner_name)
        indi["related_partners"] = partner_list

    rows = json.dumps(list(general_indicators_informations), default=date_handler)

    return render(request, "general_info.html", {"rows": rows})
