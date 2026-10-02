import flet as ft

from lib.State import *
from lib.items import *

@ft.component
def item_container(item: Item, state: State) -> ft.Container:
    veg_badge = ft.Container(
        content=ft.Text("V", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        bgcolor=ft.Colors.GREEN,
        border_radius=10,
        padding=ft.Padding.symmetric(horizontal=7, vertical=2),
        visible=item.vegetarian,
    )

    category_chip=ft.Container(
        content=ft.Text(item.category, size=11, color=ft.Colors.ON_SURFACE_VARIANT),
        border_radius=10,
        padding=ft.Padding.symmetric(horizontal=8, vertical=2),
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.ON_SURFACE),
    )

    details=ft.Column(
        [
            ft.Row(
                [
                    ft.Text(item.name, size=18, weight=ft.FontWeight.BOLD),
                    veg_badge,
                ],
                spacing=8,
            ),
            
            ft.Text(item.description, size=14, color=ft.Colors.ON_SURFACE_VARIANT),
            category_chip,
        ],
        spacing=4,
        expand=True,
    )
    
    price_and_add=ft.Column(
        [
            ft.Text(f"£{item.price:.2f}", size=18, weight=ft.FontWeight.BOLD),
            ft.TextButton(
                "Add" if (item not in state.basket) else "Remove",
                on_click=lambda: state.toggle_item(item),
                style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT, color=ft.Colors.WHITE)
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.END,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8,
    )

    return ft.Container(
        content=ft.Row(
            [details, price_and_add],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=15,
        border_radius=12,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
    )
