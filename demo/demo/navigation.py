# config/nav.py
from django.http import HttpRequest

from django_simple_nav.nav import Nav
from django_simple_nav.nav import NavGroup
from django_simple_nav.nav import NavItem


def simple_permissions_check(request: HttpRequest) -> bool:
    return True


class MainNav(Nav):
    template_name = "main_nav.html"
    items = [
        NavItem(title="Relative URL", url="/relative-url"),
        NavItem(title="Absolute URL", url="https://example.com/absolute-url"),
        NavItem(title="Internal Django URL by Name", url="fake-view"),
        NavGroup(
            title="Group",
            url="/group",
            items=[
                NavItem(title="Relative URL", url="/relative-url"),
                NavItem(title="Absolute URL", url="https://example.com/absolute-url"),
                NavItem(title="Internal Django URL by Name", url="fake-view"),
            ],
        ),
        NavGroup(
            title="Container Group",
            items=[
                NavItem(title="Item", url="#"),
            ],
        ),
        NavItem(
            title="is_authenticated Item", url="#", permissions=["is_authenticated"]
        ),
        NavItem(title="is_staff Item", url="#", permissions=["is_staff"]),
        NavItem(title="is_superuser Item", url="#", permissions=["is_superuser"]),
        NavItem(
            title="myapp.django_perm Item", url="#", permissions=["myapp.django_perm"]
        ),
        NavItem(
            title="Item with callable permission",
            url="#",
            permissions=[simple_permissions_check],
        ),
        NavGroup(
            title="Group with Extra Context",
            items=[
                NavItem(
                    title="Item with Extra Context",
                    url="#",
                    extra_context={"foo": "bar"},
                ),
            ],
            extra_context={"baz": "qux"},
        ),
    ]