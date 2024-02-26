from __future__ import annotations

from django import template

from tag_menu.models import TagMenu


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def make_menu(context, menu: str | TagMenu):
    if isinstance(menu, str):
        try:
            context['selected_name'] = context.get('selected_name', menu)
            menu = TagMenu.objects.filter(name=menu)[0].root
        except IndexError:
            return {
                'to_draw': False
            }
    return {
        'menu': menu,
        'selected_name': context.get('selected_name', menu.name),
        'before_selected': context.get('before_selected', True),
        'to_draw': True,
        'parent_context': context,
    }


@register.simple_tag(takes_context=True)
def change_context(context, attr: str, new_val):
    context[attr] = new_val
    cur = context.get('parent_context', None)
    while cur is not None:
        context = cur
        context[attr] = new_val
        cur = context.get('parent_context', None)
    return ''
