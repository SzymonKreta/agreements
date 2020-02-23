from rest_framework import routers

from terms_of_service_agreements import views as agreement_views

router = routers.DefaultRouter()
router.register(r'users', agreement_views.UserViewset)
router.register(r'user_agreements', agreement_views.AgreementViewset)
router.register(r'terms', agreement_views.TermsOfServiceViewset)
