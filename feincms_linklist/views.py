
from django.views.generic import direct_to_template as render
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from feincms.module.page.models import Page

from feincms.views.base import Handler


class PageIdFallbackHandler(Handler):
    """ This handler allows for calling a page by its id instead of URL.
        In case a page got moved and the link was hardcoded.
        The URL must be in the form /en/mypage/?p=10
    """
    def __call__(self, request, path=None):
        try:
            page = Page.objects.best_match_for_path(path, raise404=True)
            return self.build_response(request, page)
        except Http404:
            try:
                page = get_object_or_404(Page, pk=request.GET.get('p', None))
            except ValueError:
                raise Http404
            return redirect(page)

handler = PageIdFallbackHandler()


def linklist(request):
    """ This creates a page tree for the dropdown menu in TinyMCE.
        You need to add TINYMCE_LINK_LIST_URL to FEINCMS_RICHTEXT_INIT_CONTEXT:
        FEINCMS_RICHTEXT_INIT_CONTEXT  = {
            'TINYMCE_JS_URL': TINYMCE_JS_URL,
            'TINYMCE_CONTENT_CSS_URL': None,
            'TINYMCE_LINK_LIST_URL': '/linklist.js'
        }
    """
    pages = Page.objects.all()

    for p in pages:
        p.depth_indicator = '-' * p.level

    return render(request, 'feincms/linklist.js', {
        'pages': pages,
    }, mimetype="text/javascript")

