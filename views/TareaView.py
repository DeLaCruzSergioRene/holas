import flet as ft


def TareaView(page: ft.Page):
    return ft.View(
        route="/tarea",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Vista de Tareas", size=24, weight="bold")
        ]
    )
