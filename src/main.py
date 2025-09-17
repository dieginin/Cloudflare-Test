import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)
    page.padding = 0
    page.title = "Cloudflare Test4"

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.Container(
            counter,
            alignment=ft.alignment.center,
        )
    )


ft.app(main)
