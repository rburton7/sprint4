# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552070596.2402
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_left', 'inside_left']


from catalog import models as cmod

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
        def inside_left():
            return render_inside_left(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n\n')
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
        def inside_left():
            return render_inside_left(context)
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n\n    <ul class="nav flex-column">\n')
        for category in cmod.Category.objects.all() :
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
{"filename": "/Users/rhettburton/sprint1/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "41": 1, "42": 2, "47": 21, "53": 6, "62": 6, "63": 12, "64": 13, "65": 13, "66": 13, "67": 13, "68": 13, "69": 15, "74": 19, "80": 17, "86": 17, "92": 86}}
__M_END_METADATA
"""
