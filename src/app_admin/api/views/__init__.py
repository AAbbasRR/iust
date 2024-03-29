from .login import AdminLoginView
from .oauth import AdminOauthLoginAPIView
from .reports import (
    AdminCountryRequestsCountAPIView,
    AdminReportApplicationsAPIView,
    AdminReportDiffrentBarAPIView,
    AdminReportHitMapAPIView,
    AdminReportCountryAPIView,
    AdminReportBarChartAPIView,
    AdminReportAverageReviewTimeAPIView,
)
from .staffs_admin import (
    AdminStaffsListAPIView,
    AdminStaffsCreateAPIView,
    AdminStaffsUpdateDeleteAPIView,
)
