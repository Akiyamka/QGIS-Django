from django.conf.urls import url
from django.urls import path

from .views import(StyleListView,
                   StyleCreateView,
                   StyleDetailView,
                   StyleDeleteView,
                   StyleUpdateView,
                   StyleUnapprovedListView,
                   StyleRequireActionListView,
                   style_download,
                   style_review,
                   style_nav_content,
                   style_type_list)

urlpatterns = [
    path('', StyleListView.as_view(), name='style_list'),
    path('add/', StyleCreateView.as_view(), name='style_create'),
    path('<int:pk>/', StyleDetailView.as_view(), name='style_detail'),
    path('<int:pk>/download/', style_download, name='style_download'),
    path('<int:pk>/delete/', StyleDeleteView.as_view(), name='style_delete'),
    path('<int:pk>/update/', StyleUpdateView.as_view(), name='style_update'),

    path('unapproved/', StyleUnapprovedListView.as_view(), name='style_unapproved'),
    path('require_action/', StyleRequireActionListView.as_view(), name='style_require_action'),
    path('<int:pk>/review/', style_review, name='style_review'),

    # JSON
    path('sidebarnav/', style_nav_content, name="style_nav_content"),
    path('sidebarnav_type/', style_type_list, name="style_nav_typelist"),
]
