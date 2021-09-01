from rest_framework.pagination import CursorPagination
class mypaginationNumber(CursorPagination):
     page_size = 2
     ordering = 'name'