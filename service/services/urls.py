from rest_framework import routers

from services.views import SubscriptionView


urlpatterns = [

]

router = routers.DefaultRouter()
router.register(r'subscriptions', SubscriptionView)

urlpatterns += router.urls
