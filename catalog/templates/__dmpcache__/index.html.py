# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552535179.55535
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center', 'site_right']


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
        page = context.get('page', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

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
        page = context.get('page', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context)
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <div>\n\n')
        if category is not None:
            __M_writer('            <h1>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.name ))
            __M_writer('</h1>\n')
        else: 
            __M_writer('            <h1>  All Products </h1>\n')
        __M_writer('\n\n\n   </div>\n\n\n    <div >\n\n')
        for product in products :
            __M_writer('               <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('"></span>\n')
        __M_writer('    </div>  \n\n<div>\n')
        if page > 1 and page <= numpages:
            __M_writer('           <a class="btn btn-success" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else '' ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 if page != 1 else page))
            __M_writer('/">Previous Page</a>\n')
        __M_writer('\n')
        if page < numpages:
            __M_writer('           <a class="btn btn-success" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else '' ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 if page < numpages else page))
            __M_writer('/">Next Page</a>\n')
        __M_writer('   </div>\n\n \n')
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
{"filename": "/Users/rhettburton/sprint1/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 35, "53": 39, "59": 3, "70": 3, "71": 6, "72": 7, "73": 7, "74": 7, "75": 8, "76": 9, "77": 11, "78": 19, "79": 20, "80": 20, "81": 20, "82": 22, "83": 25, "84": 26, "85": 26, "86": 26, "87": 26, "88": 26, "89": 28, "90": 29, "91": 30, "92": 30, "93": 30, "94": 30, "95": 30, "96": 32, "102": 37, "108": 37, "114": 108}}
__M_END_METADATA
"""
