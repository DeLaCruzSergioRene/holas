import flet as ft


def UserView(page: ft.Page):
    return ft.View(
        route="/usuario",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Vista de Usuario", size=24, weight="bold")
        ]
    )
