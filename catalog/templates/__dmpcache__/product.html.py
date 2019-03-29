# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553804355.388206
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
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def inside_left():
            return render_inside_left(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        plist = context.get('plist', UNDEFINED)
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
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context)
        plist = context.get('plist', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n    <div class="row">\n        <div class="col-sm">\n            <ul >\n                \n')
        for pr in plist :
            __M_writer('                \n\n                <a href="/catalog/product/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('/">\n                <img data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('" class="ppimagethumb" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(pr))
            __M_writer('"/>\n                </a>\n                \n\n')
        __M_writer('            \n            </ul>\n        </div>\n        <div class="col-md">\n            \n            \xa0 \xa0 <div class="product-tile">\n                    </br>\n                    </br>\n                    </br>\n                    </br>\n                    </br>\n                    </br>\n                    </br>\n                    </br>\n                    </br>\n                    \n            \xa0 \xa0 \xa0 \xa0<a href="/catalog/product/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
        __M_writer('/"> <div class="product-image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.image_url()))
        __M_writer('"/></div> </a>\n            \xa0 \xa0 \xa0 \xa0 \n            \xa0 \xa0 </div>\n           \n        </div>\n        <div class="col-sm">\n        \n            <div class="product-name"><h2>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</h2></div>\n            <div class="product-price">$')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
        __M_writer('</div></br>\n          <form method="post">\n            <table>\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\n            </table>\n            <input type="submit" value="Submit">\n        </form>\n        </div>\n    </div>\n</div>\n')
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
{"filename": "/Users/rhettburton/sprint1/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 52, "54": 58, "59": 62, "65": 3, "75": 3, "76": 9, "77": 10, "78": 12, "79": 12, "80": 13, "81": 13, "82": 13, "83": 13, "84": 18, "85": 34, "86": 34, "87": 34, "88": 34, "89": 41, "90": 41, "91": 42, "92": 42, "93": 45, "94": 45, "100": 54, "106": 54, "112": 60, "118": 60, "124": 118}}
__M_END_METADATA
"""
