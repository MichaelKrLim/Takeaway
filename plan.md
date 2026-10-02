**Stories**

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

**Analysis**

Store all dishes, `Dish` type perhaps?

'Selecting dishes' -> add to basket??

So essentially I need a list of meals, a basket and checkout page, and send a text on order.

A ui lib would be nice here. Let's use flet.

I need three pages, a list of orders, checkout and a confirmation page. Flet uses routing, with a rounter in main.py

**Function signatures**

```
def item_container(item: Item, state: State) -> ft.Container:
def to_international(number: str, default_country_code: str = "44") -> str:
def send_to(number: str, message: str) -> SendMessageResponse:
def State::toggle_item(self, item: Item) -> None:
def basket(state: State) -> ft.Container:
def basket::submit():
def confirmation(state: State) -> ft.Container:
def order_list(state: State) -> ft.Container:
```

**examples**

to_international("03847273843") -> "+44 3847273843"
send_to(...) -> SendMessageResponse("message_uuid='698dd06b-e404-44e3-aefb-eabd59430968' workflow_id=None")
st.toggle_item("ex item") -> removes / adds "ex item from basket"
