# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552535266.2232609
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/catalog/templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center', 'inside_left', 'site_right']


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
        plist = context.get('plist', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def inside_left():
            return render_inside_left(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'inside_left'):
            context['self'].inside_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        plist = context.get('plist', UNDEFINED)
        product = context.get('product', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n<ul >\n\n')
        for pr in plist :
            __M_writer('\n    <a href="/catalog/product/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('/">\n    <img data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('" class="img-thumbnail" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(pr))
            __M_writer('"/>\n    </a>\n\n')
        __M_writer('\n</ul>\n\n<a href="/catalog/product/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
        __M_writer('/">\n\xa0 \xa0 <div class="product-tile">\n\xa0 \xa0 \xa0 \xa0 <div class="product-image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.image_url()))
        __M_writer('"/></div>\n\xa0 \xa0 \xa0 \xa0 <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</div>\n\xa0 \xa0 \xa0 \xa0 <div class="product-price">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
        __M_writer('</div>\n\xa0 \xa0 </div>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inside_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def inside_left():
            return render_inside_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 24, "53": 30, "58": 34, "64": 3, "73": 3, "74": 7, "75": 8, "76": 9, "77": 9, "78": 10, "79": 10, "80": 10, "81": 10, "82": 14, "83": 17, "84": 17, "85": 19, "86": 19, "87": 20, "88": 20, "89": 21, "90": 21, "96": 26, "102": 26, "108": 32, "114": 32, "120": 114}}
__M_END_METADATA
"""
