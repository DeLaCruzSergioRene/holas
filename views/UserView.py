import flet as ft


def UserView(page: ft.Page):
    user = page.current_user

    return ft.View(
        route="/usuario",
        appbar=ft.AppBar(title=ft.Text("Perfil")),
        controls=[
            ft.Column([
                ft.Text(f"Nombre: {user['nombre']}", size=20),
                ft.Text(f"Email: {user['email']}", size=16),
                ft.ElevatedButton("Volver", on_click=lambda _: page.go("/tarea"))
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
        ]
    )
