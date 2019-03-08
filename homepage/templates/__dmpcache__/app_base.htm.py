# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550617077.6600802
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['menu_items', 'site_left', 'inside_left']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def inside_left():
            return render_inside_left(context._locals(__M_locals))
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def inside_left():
            return render_inside_left(context)
        request = context.get('request', UNDEFINED)
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n<ul class="nav flex-column">\n      <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\n        <a class="nav-link" href="/index/">Home <span class="sr-only">(current)</span></a>\n      </li>\n      <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else ''))
        __M_writer('">\n        <a class="nav-link" href="/contact/">Contact</a>\n      </li>\n      <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else ''))
        __M_writer('">\n        <a class="nav-link" href="#">About</a>\n      </li>\n</ul>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'inside_left'):
            context['self'].inside_left(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inside_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def inside_left():
            return render_inside_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 7, "57": 3, "63": 3, "69": 9, "79": 9, "80": 14, "81": 14, "82": 17, "83": 17, "84": 20, "85": 20, "90": 27, "96": 25, "102": 25, "108": 102}}
__M_END_METADATA
"""
