import flet as ft

from lib.State import *


@ft.component
def confirmation(state: State) -> ft.Container:
    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Card(
            content=ft.Container(
                padding=40,
                content=ft.Column(
                    tight=True,
                    spacing=12,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, size=96, color=ft.Colors.GREEN),
                        ft.Text("Order confirmed!", size=32, weight=ft.FontWeight.BOLD),
                        ft.Text("We've sent a confirmation text to", color=ft.Colors.ON_SURFACE_VARIANT),
                        ft.Text(state.number, size=22, weight=ft.FontWeight.W_600),
                        ft.Text("Enjoy your meal!", size=16),
                    ],
                ),
            )
        ),
    )
