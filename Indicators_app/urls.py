from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

app_name = 'indicators'

router = routers.DefaultRouter()
router.register(r'section', api.SectionViewSet)
router.register(r'indicator', api.IndicatorViewSet)
router.register(r'periode', api.PeriodeViewSet)
router.register(r'output', api.OutputViewSet)
router.register(r'indicatorsectionperiode', api.IndicatorSectionPeriodeViewSet)
router.register(r'partner', api.PartnerViewSet)
router.register(r'report', api.ReportViewSet)
router.register(r'involvedpartner', api.InvolvedPartnerViewSet)
router.register(r'concernedreport', api.ConcernedReportViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Section
    path('Indicators_app/section/', views.SectionListView.as_view(), name='Indicators_app_section_list'),
    path('Indicators_app/section/create/', views.SectionCreateView.as_view(), name='Indicators_app_section_create'),
    path('Indicators_app/section/detail/<int:pk>/', views.SectionDetailView.as_view(), name='Indicators_app_section_detail'),
    path('Indicators_app/section/update/<int:pk>/', views.SectionUpdateView.as_view(), name='Indicators_app_section_update'),
)

urlpatterns += (
    # urls for Indicator
    path('Indicators_app/indicator/', views.IndicatorListView.as_view(), name='Indicators_app_indicator_list'),
    path('Indicators_app/indicator/create/', views.IndicatorCreateView.as_view(), name='Indicators_app_indicator_create'),
    path('Indicators_app/indicator/detail/<int:pk>/', views.IndicatorDetailView.as_view(), name='Indicators_app_indicator_detail'),
    path('Indicators_app/indicator/update/<int:pk>/', views.IndicatorUpdateView.as_view(), name='Indicators_app_indicator_update'),
)

urlpatterns += (
    # urls for Periode
    path('Indicators_app/periode/', views.PeriodeListView.as_view(), name='Indicators_app_periode_list'),
    path('Indicators_app/periode/create/', views.PeriodeCreateView.as_view(), name='Indicators_app_periode_create'),
    path('Indicators_app/periode/detail/<int:pk>/', views.PeriodeDetailView.as_view(), name='Indicators_app_periode_detail'),
    path('Indicators_app/periode/update/<int:pk>/', views.PeriodeUpdateView.as_view(), name='Indicators_app_periode_update'),
)

urlpatterns += (
    # urls for Output
    path('Indicators_app/output/', views.OutputListView.as_view(), name='Indicators_app_output_list'),
    path('Indicators_app/output/create/', views.OutputCreateView.as_view(), name='Indicators_app_output_create'),
    path('Indicators_app/output/detail/<int:pk>/', views.OutputDetailView.as_view(), name='Indicators_app_output_detail'),
    path('Indicators_app/output/update/<int:pk>/', views.OutputUpdateView.as_view(), name='Indicators_app_output_update'),
)

urlpatterns += (
    # urls for IndicatorSectionPeriode
    path('Indicators_app/indicatorsectionperiode/', views.IndicatorSectionPeriodeListView.as_view(), name='Indicators_app_indicatorsectionperiode_list'),
    path('Indicators_app/indicatorsectionperiode/create/', views.IndicatorSectionPeriodeCreateView.as_view(), name='Indicators_app_indicatorsectionperiode_create'),
    path('Indicators_app/indicatorsectionperiode/detail/<int:pk>/', views.IndicatorSectionPeriodeDetailView.as_view(), name='Indicators_app_indicatorsectionperiode_detail'),
    path('Indicators_app/indicatorsectionperiode/update/<int:pk>/', views.IndicatorSectionPeriodeUpdateView.as_view(), name='Indicators_app_indicatorsectionperiode_update'),
)

urlpatterns += (
    # urls for Partner
    path('Indicators_app/partner/', views.PartnerListView.as_view(), name='Indicators_app_partner_list'),
    path('Indicators_app/partner/create/', views.PartnerCreateView.as_view(), name='Indicators_app_partner_create'),
    path('Indicators_app/partner/detail/<int:pk>/', views.PartnerDetailView.as_view(), name='Indicators_app_partner_detail'),
    path('Indicators_app/partner/update/<int:pk>/', views.PartnerUpdateView.as_view(), name='Indicators_app_partner_update'),
)

urlpatterns += (
    # urls for Report
    path('Indicators_app/report/', views.ReportListView.as_view(), name='Indicators_app_report_list'),
    path('Indicators_app/report/create/', views.ReportCreateView.as_view(), name='Indicators_app_report_create'),
    path('Indicators_app/report/detail/<int:pk>/', views.ReportDetailView.as_view(), name='Indicators_app_report_detail'),
    path('Indicators_app/report/update/<int:pk>/', views.ReportUpdateView.as_view(), name='Indicators_app_report_update'),
)

urlpatterns += (
    # urls for InvolvedPartner
    path('Indicators_app/involvedpartner/', views.InvolvedPartnerListView.as_view(), name='Indicators_app_involvedpartner_list'),
    path('Indicators_app/involvedpartner/create/', views.InvolvedPartnerCreateView.as_view(), name='Indicators_app_involvedpartner_create'),
    path('Indicators_app/involvedpartner/detail/<int:pk>/', views.InvolvedPartnerDetailView.as_view(), name='Indicators_app_involvedpartner_detail'),
    path('Indicators_app/involvedpartner/update/<int:pk>/', views.InvolvedPartnerUpdateView.as_view(), name='Indicators_app_involvedpartner_update'),
)

urlpatterns += (
    # urls for ConcernedReport
    path('Indicators_app/concernedreport/', views.ConcernedReportListView.as_view(), name='Indicators_app_concernedreport_list'),
    path('Indicators_app/concernedreport/create/', views.ConcernedReportCreateView.as_view(), name='Indicators_app_concernedreport_create'),
    path('Indicators_app/concernedreport/detail/<int:pk>/', views.ConcernedReportDetailView.as_view(), name='Indicators_app_concernedreport_detail'),
    path('Indicators_app/concernedreport/update/<int:pk>/', views.ConcernedReportUpdateView.as_view(), name='Indicators_app_concernedreport_update'),
)

