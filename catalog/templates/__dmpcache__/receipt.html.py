# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553876511.9023948
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/catalog/templates/receipt.html'
_template_uri = 'receipt.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
        def site_center():
            return render_site_center(context._locals(__M_locals))
        SI = context.get('SI', UNDEFINED)
        myproducts = context.get('myproducts', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        SI = context.get('SI', UNDEFINED)
        myproducts = context.get('myproducts', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container">\n  <h2>Receipt</h2>\n  <p>Thank you for your purchase!</p>            \n  <table class="table table-bordered">\n    <thead>\n      <tr>\n        <th>Product Image</th>\n        <th>Product Name</th>\n        <th>Quantity</th>\n        <th>Price</th>\n        <th>Extended</th>\n        \n      </tr>\n    </thead>\n    <tbody>\n      \n\n')
        for item in SI :
            __M_writer('            <tr>\n\n                <td> <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
            __M_writer('"/></td>\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name))
            __M_writer('</td>\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.quantity))
            __M_writer('</td>\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.price))
            __M_writer('</td>\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.price * item.quantity))
            __M_writer('</td>\n               \n                \n            </tr>\n')
        __M_writer('\n        \n        \n    \n      <tr>\n        <td></td>\n        <td>Tax</td>\n        <td></td>\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(myproducts.tax))
        __M_writer('</td>\n        <td></td>\n      </tr>\n     <tr>\n        <td></td>\n        <td>Total</td>\n        <td></td>\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(myproducts.total))
        __M_writer('</td>\n        <td></td>\n      </tr>\n    </tbody>\n  </table>\n</div>\n\n<div>\n\n<a class="btn-lg btn-success" href="/catalog/index/">Return to Products</a>\n\n</div>\n</br>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/catalog/templates/receipt.html", "uri": "receipt.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 22, "60": 23, "61": 25, "62": 25, "63": 26, "64": 26, "65": 27, "66": 27, "67": 28, "68": 28, "69": 29, "70": 29, "71": 34, "72": 42, "73": 42, "74": 49, "75": 49, "81": 75}}
__M_END_METADATA
"""
