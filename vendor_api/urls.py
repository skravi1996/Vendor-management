from django.urls import path
from .views import (
    VendorListCreateView,
    VendorDetailView,
    PurchaseOrderListCreateView,
    PurchaseOrderDetailView,
    VendorPerformanceView,
    PurchaseOrderAcknowledgmentView,
    VendorHistoricalPerformanceView,
    
)

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<int:pk>/performance/',VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(),name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(),name='purchase-order-detail'),
    path('purchase_orders/<int:pk>/acknowledge/',PurchaseOrderAcknowledgmentView.as_view(), name='purchase-order-acknowledge'),
    path('historical_performance/', VendorHistoricalPerformanceView.as_view(),name='vendor-historical-performance'),
]
