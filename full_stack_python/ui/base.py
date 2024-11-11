import reflex as rx

from .nav import navbar

def base_page(child: rx.Component, hide_navbar=False) -> rx.Component:
    return rx.fragment(
        navbar() if not hide_navbar else None,
        rx.box(
            child,
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            id="my-content-area-el",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        id="my-base-container"
    )