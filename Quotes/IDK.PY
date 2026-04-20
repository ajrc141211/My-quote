import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    quotes = {
        "English": "May the force be with you",
        "Spanish": "¡Que la Fuerza te acompañe",
        "French": "Que la Force soit avec vous"
    }

    quote_text = ft.Text(
        quotes["English"],
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def change_language(e):
        selected = radio_group.value
        quote_text.value = quotes[selected]
        page.update()

    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="English", label="English"),
            ft.Radio(value="Spanish", label="Spanish"),
            ft.Radio(value="French", label="French"),
        ]),
        value="English",
        on_change=change_language
    )

    page.add(
        ft.Column(
            [
                ft.Text("Quote Translator", size=30, weight="bold"),
                quote_text,
                radio_group
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)