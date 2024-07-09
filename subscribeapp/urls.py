from django.urls import path

from subscribeapp.views import SubscriptionListView, SubscriptionView

# 네임스페이스
app_name = 'subscribeapp'

# subscribeapp용 주소 등록
urlpatterns = [
    # subscribe 주소 등록
    path( 'subscribe/', SubscriptionView.as_view(), name='subscribe' ),
    # list 주소 등록
    path( 'list/', SubscriptionListView.as_view(), name='list' ),
]