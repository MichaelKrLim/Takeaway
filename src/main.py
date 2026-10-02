import flet as ft
from dataclasses import dataclass

from lib.State import *
from pages.order_list import order_list
from pages.basket import basket
from pages.confirmation import confirmation

@ft.component
def layout():
    outlet = ft.use_route_outlet()
    header_button_style = ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT, color=ft.Colors.WHITE)

    header = ft.Container(
        content=ft.Row(
            [
                ft.TextButton(
                    content=ft.Text("Takeaway", size=20, weight=ft.FontWeight.BOLD),
                    style=header_button_style,
                    on_click=lambda: ft.context.page.navigate("/")
                ),
                ft.Container(expand=True),
                ft.TextButton("Basket", on_click=lambda: ft.context.page.navigate("/basket"), style=header_button_style)
            ]
        ),
        bgcolor=ft.Colors.SURFACE_BRIGHT,
        padding=10,
    )

    footer = ft.Container(
        content=ft.Text("Takeaway - (c) 2026", color=ft.Colors.GREY),
        padding=10,
        alignment=ft.Alignment.CENTER,
    )

    return ft.Column(
        [
            header,
            ft.Container(content=outlet, expand=True),
            footer
        ],
        expand=True
    )


@ft.component
def app():
    state = State(set(), None)
    return ft.Container(
        expand=True,
        content=ft.SafeArea(
        content=ft.Router(
            [
                ft.Route(
                    component=layout,
                    children = [
                        ft.Route(index=True,          component=lambda: order_list(state)  ),
                        ft.Route(path="basket",       component=lambda: basket(state)      ),
                        ft.Route(path="confirmation", component=lambda: confirmation(state)),
                    ],
                ),
            ],
        )
    ))

def main(page: ft.Page):
    page.padding=0
    page.title="Takeaway"
    page.render(app)

ft.run(main)
