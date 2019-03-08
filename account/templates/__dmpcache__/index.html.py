# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550524144.215095
_enable_loop = True
_template_filename = '/Users/rhettburton/sprint1/account/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['menu_items', 'site_center']


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
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n\n\n\n<div id="site_center">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n<ul class="navbar-nav ml-auto">\n    <li class="nav-item dropdown" >\n                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                        Welcome, User\n                        </a>\n                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">\n                        <a class="dropdown-item" href="/account/index">Account</a>\n                        <a class="dropdown-item" href="#">Logout</a>\n                        <div class="dropdown-divider"></div>\n                        <a class="dropdown-item" href="#">Settings</a>\n                        </div>\n     </li>\n</ul>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\n    Welcome to Your Account\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rhettburton/sprint1/account/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 22, "48": 29, "54": 4, "60": 4, "66": 27, "72": 27, "78": 72}}
__M_END_METADATA
"""
