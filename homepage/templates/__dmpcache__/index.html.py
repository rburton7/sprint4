# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549419708.144431
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'inside_left', 'site_center', 'site_right']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def inside_left():
            return render_inside_left(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'inside_left'):
            context['self'].inside_left(**pageargs)
        

        __M_writer('\n\n<div id="site_center">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n</div>\n\n<div id="site_right">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(' Home  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inside_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def inside_left():
            return render_inside_left(context)
        __M_writer = context.writer()
        __M_writer("\n\n<hr>\nWhaaaaaa...?\n<br>\n<br>\nThat's the reaction \nmost normal folks have, <br>\nwhen \nthey see our art.\n<br>\nBut what can we say?\n<br>\nIt comes straight from the <br>heart.\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\n    <img class="image-center" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/homepagepic.jpg" alt="python">\n\n    <div id="titletext"> \n    \n    Welcome to Panic Art\n    <hr>\n    \n    <span style="font-size: 20px">American Fork, UT</span>\n    \n    \n    </div>\n    \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\n    Our Art\n\n<div class="flex-column">\n\n<ul>\n<li><img class="image-center" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/lion.jpg" alt="python" style="width: 100%"></li>\n<li><img class="image-center" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/wolf.jpeg" alt="python" style="width: 100%"></li>\n<li><img class="image-center" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bear.jpeg" alt="python" style="width: 100%"></li>\n<li><img class="image-center" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/swirl.jpeg" alt="python" style="width: 100%"></li>\n<li><img class="image-center" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/wolf2.jpeg" alt="python" style="width: 100%"></li>\n\n\n</ul>\n</div>\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 3, "54": 19, "59": 35, "64": 55, "70": 3, "76": 3, "82": 5, "88": 5, "94": 22, "102": 22, "103": 23, "104": 23, "110": 39, "118": 39, "119": 45, "120": 45, "121": 46, "122": 46, "123": 47, "124": 47, "125": 48, "126": 48, "127": 49, "128": 49, "134": 128}}
__M_END_METADATA
"""
