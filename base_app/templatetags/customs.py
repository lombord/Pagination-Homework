from django import template
from django.core.paginator import Page
from django.http import HttpRequest, QueryDict

register = template.Library()


def get_left(current, count) -> int:
    """
    Get left range of pages for current page
    with given count
    """
    if count >= current:
        return range(1, current)
    return range(current - count, current)


def get_right(current, count, len_) -> int:
    """
    Get right range of pages for current page
    with given count
    """
    if len_ - current < count:
        return range(current + 1, len_ + 1)
    return range(current + 1, current + count + 1)


def get_params(request):
    """
    Get request's get params
    """
    q_dict = QueryDict(request.GET.urlencode(), mutable=True)
    q_dict.pop('page', None)
    q_dict['page'] = ''
    return q_dict.urlencode()


@register.inclusion_tag("base_app/pagination.html")
def paginate(page_obj: Page, *, count=3, request: HttpRequest = None):
    """Render pagination for a given page
    with custom count of pages"""
    assert request is not None, "Request hasn't been passed!"
    current = page_obj.number
    left = get_left(current, count)
    right = get_right(current, count,
                      page_obj.paginator.num_pages)
    params = get_params(request)

    return {'left_pages': left,
            'page_obj': page_obj,
            'right_pages': right,
            'params': params}
