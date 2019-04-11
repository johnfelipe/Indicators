from . import models
from . import serializers
from rest_framework import viewsets, permissions


class SectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Section class"""

    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndicatorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Indicator class"""

    queryset = models.Indicator.objects.all()
    serializer_class = serializers.IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]


class PeriodeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Periode class"""

    queryset = models.Periode.objects.all()
    serializer_class = serializers.PeriodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class OutputViewSet(viewsets.ModelViewSet):
    """ViewSet for the Output class"""

    queryset = models.Output.objects.all()
    serializer_class = serializers.OutputSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndicatorSectionPeriodeViewSet(viewsets.ModelViewSet):
    """ViewSet for the IndicatorSectionPeriode class"""

    queryset = models.IndicatorSectionPeriode.objects.all()
    serializer_class = serializers.IndicatorSectionPeriodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PartnerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Partner class"""

    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportViewSet(viewsets.ModelViewSet):
    """ViewSet for the Report class"""

    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvolvedPartnerViewSet(viewsets.ModelViewSet):
    """ViewSet for the InvolvedPartner class"""

    queryset = models.InvolvedPartner.objects.all()
    serializer_class = serializers.InvolvedPartnerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConcernedReportViewSet(viewsets.ModelViewSet):
    """ViewSet for the ConcernedReport class"""

    queryset = models.ConcernedReport.objects.all()
    serializer_class = serializers.ConcernedReportSerializer
    permission_classes = [permissions.IsAuthenticated]


