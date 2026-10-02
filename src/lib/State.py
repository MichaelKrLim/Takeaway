import flet as ft
from dataclasses import dataclass

from lib.items import *

@ft.observable
@dataclass
class State:
    basket: set
    number: str

    def toggle_item(self, item: Item) -> None:
        # if you just use .symmetric_difference_update flet might not notice the update
        if item in self.basket:
            self.basket=self.basket-{item}
        else:
            self.basket = self.basket|{item}


