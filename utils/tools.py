from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage







def paginator(objects, pre_page_num, page):
    paginator = Paginator(objects, pre_page_num)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects


# def get_login_redirect_url(userprofile):
#     if userprofile.visit_portal_perm in [defs.VISIT_DIAMOND_PORTAL, defs.VISIT_PROTAL_DEFAULT_DIAMOND]:
#         return resolve_url('/')
#     else:
#         return resolve_url('/production/')
#
#
# def format_date(value, default=None):
#     if value:
#         return value.strftime(settings.DATE_FORMAT_PORTAL)
#     else:
#         return default
