from rest_framework import pagination


class ClientAdminPagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 20


class HundredPagination(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 100
