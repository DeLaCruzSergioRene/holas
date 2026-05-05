import flet as ft


def RegisterView(page: ft.Page, auth_controller):
    nombre_input = ft.TextField(
        label="Nombre completo",
        width=350,
        border_radius=10
    )

    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )

    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )

    pass_confirm = ft.TextField(
        label="Confirmar contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )

    def register_click(e):
        if not nombre_input.value or not email_input.value or not pass_input.value or not pass_confirm.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        if pass_input.value != pass_confirm.value:
            page.snack_bar = ft.SnackBar(ft.Text("Las contraseñas no coinciden"))
            page.snack_bar.open = True
            page.update()
            return

        success, msg = auth_controller.registrar_usuario(nombre_input.value, email_input.value, pass_input.value)
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

        if success:
            page.go("/")

    register_button = ft.ElevatedButton(
        "Registrar",
        on_click=register_click,
        width=350,
        bgcolor="green",
        color="white"
    )

    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Registro"),
            bgcolor="bluegrey900",
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Crea tu cuenta", size=24, weight="bold"),
                    nombre_input,
                    email_input,
                    pass_input,
                    pass_confirm,
                    register_button,
                    ft.TextButton(
                        "Volver al login",
                        on_click=lambda _: page.go("/")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=15
            )
        ]
    )
