import unittest
from django.urls import reverse
from django.test import Client
from .models import Section, Indicator, Periode, Output, IndicatorSectionPeriode, Partner, Report, InvolvedPartner, ConcernedReport
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_section(**kwargs):
    defaults = {}
    defaults["section_designation"] = "section_designation"
    defaults.update(**kwargs)
    return Section.objects.create(**defaults)


def create_indicator(**kwargs):
    defaults = {}
    defaults["indicator_designation"] = "indicator_designation"
    defaults.update(**kwargs)
    return Indicator.objects.create(**defaults)


def create_periode(**kwargs):
    defaults = {}
    defaults["periode_designation"] = "periode_designation"
    defaults.update(**kwargs)
    return Periode.objects.create(**defaults)


def create_output(**kwargs):
    defaults = {}
    defaults["output_designation"] = "output_designation"
    defaults["output_description"] = "output_description"
    defaults.update(**kwargs)
    return Output.objects.create(**defaults)


def create_indicatorsectionperiode(**kwargs):
    defaults = {}
    defaults["target_value"] = "target_value"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "section" not in defaults:
        defaults["section"] = create_section()
    if "indicator" not in defaults:
        defaults["indicator"] = create_indicator()
    if "periode" not in defaults:
        defaults["periode"] = create_periode()
    if "output" not in defaults:
        defaults["output"] = create_output()
    return IndicatorSectionPeriode.objects.create(**defaults)


def create_partner(**kwargs):
    defaults = {}
    defaults["partner_designation"] = "partner_designation"
    defaults.update(**kwargs)
    return Partner.objects.create(**defaults)


def create_report(**kwargs):
    defaults = {}
    defaults["report_designation"] = "report_designation"
    defaults.update(**kwargs)
    return Report.objects.create(**defaults)


def create_involvedpartner(**kwargs):
    defaults = {}
    defaults["results"] = "results"
    defaults.update(**kwargs)
    if "indicator" not in defaults:
        defaults["indicator"] = create_indicatorsectionperiode()
    if "partner" not in defaults:
        defaults["partner"] = create_partner()
    return InvolvedPartner.objects.create(**defaults)


def create_concernedreport(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "indicator" not in defaults:
        defaults["indicator"] = create_indicatorsectionperiode()
    if "report" not in defaults:
        defaults["report"] = create_report()
    return ConcernedReport.objects.create(**defaults)


class SectionViewTest(unittest.TestCase):
    '''
    Tests for Section
    '''
    def setUp(self):
        self.client = Client()

    def test_list_section(self):
        url = reverse('Indicators_app_section_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_section(self):
        url = reverse('Indicators_app_section_create')
        data = {
            "section_designation": "section_designation",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_section(self):
        section = create_section()
        url = reverse('Indicators_app_section_detail', args=[section.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_section(self):
        section = create_section()
        data = {
            "section_designation": "section_designation",
        }
        url = reverse('Indicators_app_section_update', args=[section.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class IndicatorViewTest(unittest.TestCase):
    '''
    Tests for Indicator
    '''
    def setUp(self):
        self.client = Client()

    def test_list_indicator(self):
        url = reverse('Indicators_app_indicator_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_indicator(self):
        url = reverse('Indicators_app_indicator_create')
        data = {
            "indicator_designation": "indicator_designation",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_indicator(self):
        indicator = create_indicator()
        url = reverse('Indicators_app_indicator_detail', args=[indicator.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_indicator(self):
        indicator = create_indicator()
        data = {
            "indicator_designation": "indicator_designation",
        }
        url = reverse('Indicators_app_indicator_update', args=[indicator.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PeriodeViewTest(unittest.TestCase):
    '''
    Tests for Periode
    '''
    def setUp(self):
        self.client = Client()

    def test_list_periode(self):
        url = reverse('Indicators_app_periode_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_periode(self):
        url = reverse('Indicators_app_periode_create')
        data = {
            "periode_designation": "periode_designation",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_periode(self):
        periode = create_periode()
        url = reverse('Indicators_app_periode_detail', args=[periode.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_periode(self):
        periode = create_periode()
        data = {
            "periode_designation": "periode_designation",
        }
        url = reverse('Indicators_app_periode_update', args=[periode.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OutputViewTest(unittest.TestCase):
    '''
    Tests for Output
    '''
    def setUp(self):
        self.client = Client()

    def test_list_output(self):
        url = reverse('Indicators_app_output_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_output(self):
        url = reverse('Indicators_app_output_create')
        data = {
            "output_designation": "output_designation",
            "output_description": "output_description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_output(self):
        output = create_output()
        url = reverse('Indicators_app_output_detail', args=[output.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_output(self):
        output = create_output()
        data = {
            "output_designation": "output_designation",
            "output_description": "output_description",
        }
        url = reverse('Indicators_app_output_update', args=[output.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class IndicatorSectionPeriodeViewTest(unittest.TestCase):
    '''
    Tests for IndicatorSectionPeriode
    '''
    def setUp(self):
        self.client = Client()

    def test_list_indicatorsectionperiode(self):
        url = reverse('Indicators_app_indicatorsectionperiode_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_indicatorsectionperiode(self):
        url = reverse('Indicators_app_indicatorsectionperiode_create')
        data = {
            "target_value": "target_value",
            "value": "value",
            "section": create_section().pk,
            "indicator": create_indicator().pk,
            "periode": create_periode().pk,
            "output": create_output().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_indicatorsectionperiode(self):
        indicatorsectionperiode = create_indicatorsectionperiode()
        url = reverse('Indicators_app_indicatorsectionperiode_detail', args=[indicatorsectionperiode.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_indicatorsectionperiode(self):
        indicatorsectionperiode = create_indicatorsectionperiode()
        data = {
            "target_value": "target_value",
            "value": "value",
            "section": create_section().pk,
            "indicator": create_indicator().pk,
            "periode": create_periode().pk,
            "output": create_output().pk,
        }
        url = reverse('Indicators_app_indicatorsectionperiode_update', args=[indicatorsectionperiode.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PartnerViewTest(unittest.TestCase):
    '''
    Tests for Partner
    '''
    def setUp(self):
        self.client = Client()

    def test_list_partner(self):
        url = reverse('Indicators_app_partner_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_partner(self):
        url = reverse('Indicators_app_partner_create')
        data = {
            "partner_designation": "partner_designation",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_partner(self):
        partner = create_partner()
        url = reverse('Indicators_app_partner_detail', args=[partner.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_partner(self):
        partner = create_partner()
        data = {
            "partner_designation": "partner_designation",
        }
        url = reverse('Indicators_app_partner_update', args=[partner.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportViewTest(unittest.TestCase):
    '''
    Tests for Report
    '''
    def setUp(self):
        self.client = Client()

    def test_list_report(self):
        url = reverse('Indicators_app_report_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_report(self):
        url = reverse('Indicators_app_report_create')
        data = {
            "report_designation": "report_designation",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_report(self):
        report = create_report()
        url = reverse('Indicators_app_report_detail', args=[report.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_report(self):
        report = create_report()
        data = {
            "report_designation": "report_designation",
        }
        url = reverse('Indicators_app_report_update', args=[report.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InvolvedPartnerViewTest(unittest.TestCase):
    '''
    Tests for InvolvedPartner
    '''
    def setUp(self):
        self.client = Client()

    def test_list_involvedpartner(self):
        url = reverse('Indicators_app_involvedpartner_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_involvedpartner(self):
        url = reverse('Indicators_app_involvedpartner_create')
        data = {
            "results": "results",
            "indicator": create_indicatorsectionperiode().pk,
            "partner": create_partner().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_involvedpartner(self):
        involvedpartner = create_involvedpartner()
        url = reverse('Indicators_app_involvedpartner_detail', args=[involvedpartner.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_involvedpartner(self):
        involvedpartner = create_involvedpartner()
        data = {
            "results": "results",
            "indicator": create_indicatorsectionperiode().pk,
            "partner": create_partner().pk,
        }
        url = reverse('Indicators_app_involvedpartner_update', args=[involvedpartner.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ConcernedReportViewTest(unittest.TestCase):
    '''
    Tests for ConcernedReport
    '''
    def setUp(self):
        self.client = Client()

    def test_list_concernedreport(self):
        url = reverse('Indicators_app_concernedreport_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_concernedreport(self):
        url = reverse('Indicators_app_concernedreport_create')
        data = {
            "indicator": create_indicatorsectionperiode().pk,
            "report": create_report().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_concernedreport(self):
        concernedreport = create_concernedreport()
        url = reverse('Indicators_app_concernedreport_detail', args=[concernedreport.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_concernedreport(self):
        concernedreport = create_concernedreport()
        data = {
            "indicator": create_indicatorsectionperiode().pk,
            "report": create_report().pk,
        }
        url = reverse('Indicators_app_concernedreport_update', args=[concernedreport.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

