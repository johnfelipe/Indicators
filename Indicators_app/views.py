from django.shortcuts import render
from Indicators_app.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import F
import json


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

@login_required
def general_info(request):
	d = {}
	d["pagetitle"] = "General informations"

	general_indicators_informations = (IndicatorSectionPeriode.objects.all()
	.annotate(periode_designation = F('periode__periode_designation'))
	.annotate(section_designation = F('section__section_designation'))
	.annotate(indicator_designation = F('indicator__indicator_designation'))
	.annotate(output_designation = F('output__output_designation'))
	.values()
	)

	for indi in general_indicators_informations:
		related_reports = (ConcernedReport.objects.filter(indicator = indi["id"])
		.annotate(report_designation = F('report__report_designation'))
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
					one_report_name = ", "+r["report_designation"]
				reports_list.append(one_report_name)
		indi["related_reports"] = reports_list

		related_partners = (InvolvedPartner.objects.filter(indicator = indi["id"])
		.annotate(partner_name = F('partner__partner_designation'))
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
					one_partner_name = ", "+p["partner_name"]
				partner_list.append(one_partner_name)
		indi["related_partners"] = partner_list

	rows = json.dumps(list(general_indicators_informations), default=date_handler)

	return render(request, 'general_info.html', {'rows':rows})