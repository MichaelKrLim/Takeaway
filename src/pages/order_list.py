import flet as ft

from lib.items import items
from lib.item_container import *
from lib.State import *

@ft.component
def order_list(state: State) -> ft.Container:
    return ft.Container (
        alignment=ft.Alignment.CENTER,
        padding=20,
        content=ft.ListView(
	    controls=[item_container(item,state) for item in items.values()],
	    spacing=10
        ),
        expand=True
    )
