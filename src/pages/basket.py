import flet as ft
from datetime import datetime as dt

from lib.State import *
from lib.items import items
from lib.send_sms import *

@ft.component
def basket(state: State) -> ft.Container:
    value, set_value=ft.use_state("")
    error, set_error=ft.use_state(None)

    def submit():
        if (not value.strip().isdigit()) or len(value.strip())>15:
            set_error("Invalid phone number")
            return

        state.number=value.strip()
        try:
            res = send_to(value, f"Your order has been submit! [{dt.now()}]")
        except HttpRequestError as e:
            print(e.value())
            return
        else:
            print(f"[MESSAGE SENT]: {res}")

        ft.context.page.navigate("/confirmation")

    orders = ft.Column(
        tight=True,
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        # I would usually simplify this line
        controls=[ft.Text(item.name) for item in state.basket]+[ft.Text(f"£{sum([item.price for item in state.basket]):.2f}", weight=ft.FontWeight.BOLD)],
    )

    form = ft.Column(
        [
            ft.TextField(
                value         = value,
                label         = "Phone number",
                keyboard_type = ft.KeyboardType.NUMBER,
                error         = error,
                on_change     = lambda e: (set_value(e.control.value), set_error(None)),
                on_submit     = submit
            ),
        ],
        tight=True
    )

    return ft.Container(
    	ft.Row(
            [
                ft.Container(content=orders, expand=1, padding=10, alignment=ft.Alignment.CENTER),
                ft.Container(content=form, expand=1, padding=10, alignment=ft.Alignment.CENTER)
            ],
            expand=True
        ),
        alignment=ft.Alignment.CENTER,
        expand=True
    )
