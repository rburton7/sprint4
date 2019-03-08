# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552006473.7894568
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_left', 'inside_left']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def inside_left():
            return render_inside_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        def site_left():
            return render_site_left(context)
        def inside_left():
            return render_inside_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n\n    <ul class="nav flex-column">\n')
        for category in categories:
            __M_writer('            <li class="nav-item"><a class="nav-link" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category.id))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category.name))
            __M_writer('</a> </li>\n')
        __M_writer('    </ul>\n\n')
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
{"filename": "/Users/rhettburton/sprint1/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 19, "51": 4, "61": 4, "62": 10, "63": 11, "64": 11, "65": 11, "66": 11, "67": 11, "68": 13, "73": 17, "79": 15, "85": 15, "91": 85}}
__M_END_METADATA
"""
