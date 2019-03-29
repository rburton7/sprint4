# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553818590.160116
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


from django.conf import settings 

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
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        stripeTotal = context.get('stripeTotal', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        stripeTotal = context.get('stripeTotal', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<form action="" method="post">\n    \n        <table>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table()))
        __M_writer(' \n        </table>\n        <!-- <input type="submit" class="btn btn-info" value="Buy Now"> -->\n\n    <script\n    src="https://checkout.stripe.com/checkout.js" class="stripe-button"\n    data-key="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STRIPE_PUBLIC_KEY ))
        __M_writer('"\n    data-amount="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( stripeTotal ))
        __M_writer('"\n    data-name="Stripe.com"\n    data-description="Widget"\n    data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\n    data-locale="auto"\n    data-zip-code="true">\n  </script>\n\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "41": 1, "42": 2, "52": 4, "61": 4, "62": 9, "63": 9, "64": 15, "65": 15, "66": 16, "67": 16, "73": 67}}
__M_END_METADATA
"""
