from django_simple_nav.nav import Nav
from django_simple_nav.nav import NavItem


class MainNav(Nav):
    template_name = "partials/sidebar.html"
    items = [
        NavItem(title="Dashboard", url="index"),
        NavItem(title="Authors", url="demo:author_list"),
        NavItem(title="Books", url="demo:book_list"),
    ]
