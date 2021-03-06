# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553802446.627483
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'menu_items', 'site_left', 'site_center', 'site_right']


 
from datetime import datetime


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>Sprint 1 &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('  </title>\n\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.2.1-dist/js/bootstrap.min.js"></script>\n        <link rel="stylesheet" type="text/css"  href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.2.1-dist/css/bootstrap.min.css">\n\n\n')
        __M_writer('\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico" alt="python" />\n       \n        <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script> -->\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n\n    <body>\n        <div   id="maintenance_message"  class="alert alert-danger" > Hey there. The server is going down tonight. Boo Hoo </div>\n        <header id="header" >\n                \n            \n')
        __M_writer('            <div>\n         \n\n\n\n<nav class="navbar navbar-expand-lg navbar-light bg-light">\n  <a class="navbar-brand" href="#">\n   <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL ))
        __M_writer('homepage/media/bird.png" alt="bird"> \n  </a>\n  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n    <span class="navbar-toggler-icon"></span>\n  </button>\n  <div class="collapse navbar-collapse" id="navbarNav">\n\n <ul class="navbar-nav mr-auto">\n      <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer(' ">\n        <a class="nav-link" href="/index/">Home <span class="sr-only">(current)</span></a>\n      </li>\n      <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else ''))
        __M_writer(' ">\n        <a class="nav-link" href="/contact/">Contact</a>\n      </li>\n      <li class="nav-item">\n        <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else ''))
        __M_writer(' " href="/catalog/index/">Products</a>\n      </li>\n</ul>\n\n<ul class="navbar-nav ml-auto">\n    <li class="nav-item dropdown" >\n                        \n                    \n')
        if request.user.is_authenticated :
            __M_writer('                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                             Welcome, Homer\n                            </a>\n                            <div class="dropdown-menu" aria-labelledby="navbarDropdown">\n                            <a class="dropdown-item" href="/account/logout/">Logout</a>\n                            <a class="dropdown-item" href="/catalog/cart/">Cart</a>\n')
        else: 
            __M_writer('                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                             Welcome!\n                            </a>\n                            <div class="dropdown-menu" aria-labelledby="navbarDropdown">\n                            <a class="dropdown-item" href="/account/login/">Login</a>\n')
        __M_writer('                        <div class="dropdown-divider"></div>\n                        <a class="dropdown-item" href="#">Settings</a>\n                        </div>\n     </li>\n</ul>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n  </div>\n</nav>\n\n\n\n\n\n\n\n\n           \n            \n        </header>\n\n        <main>\n\n\n\n            <div id="site_left">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\n             </div>\n\n\n             <div id="site_center">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n            </div>\n\n             <div id="site_right">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\n             </div>\n          \n        </main>\n\n        <footer>\n         ')
        __M_writer('\n             &copy; ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(datetime.now().strftime('%Y') ))
        __M_writer(' \n          \n            \n        </footer>\n           \n    </body>\n   \n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\n                Left Side\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\n                Center of the Page\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\n               Right Side\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 129, "22": 0, "40": 2, "45": 8, "46": 11, "47": 11, "48": 11, "49": 12, "50": 12, "51": 13, "52": 13, "53": 17, "54": 18, "55": 18, "56": 25, "57": 26, "58": 26, "59": 36, "60": 43, "61": 43, "62": 51, "63": 51, "64": 54, "65": 54, "66": 58, "67": 58, "68": 66, "69": 67, "70": 73, "71": 74, "72": 80, "77": 88, "82": 110, "87": 117, "92": 123, "93": 131, "94": 132, "95": 132, "101": 8, "112": 86, "118": 86, "124": 108, "130": 108, "136": 115, "142": 115, "148": 121, "154": 121, "160": 154}}
__M_END_METADATA
"""
