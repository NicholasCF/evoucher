from django.urls import path
from django.conf.urls import url

from voucher.views import VoucherDetail, CreateVoucherList, upload_email_list, upload_code_list, CreateOrganizationInVoucherList, VoucherTypeList

urlpatterns = [
    path('voucher/', CreateVoucherList.as_view()),
    path('voucher/addEmails/', upload_email_list, name='upload-email' ),
    path('voucher/addCodes/', upload_code_list, name='upload-code' ),
    path('voucher/organization', CreateOrganizationInVoucherList.as_view()),
    path('voucher/type', VoucherTypeList.as_view()),
    path('voucher/<str:pk>', VoucherDetail.as_view())
]