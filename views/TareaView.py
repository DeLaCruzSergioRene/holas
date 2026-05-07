import flet as ft


def TareaView(page: ft.Page, tarea_controller):
    user = page.current_user
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    # Campos para crear una tarea nueva
    txt_titulo = ft.TextField(label="Título", expand=True)
    txt_descripcion = ft.TextField(label="Descripción", expand=True, min_lines=2)
    dropdown_prioridad = ft.Dropdown(
        label="Prioridad",
        value="media",
        options=[
            ft.dropdown.Option("baja"),
            ft.dropdown.Option("media"),
            ft.dropdown.Option("alta")
        ]
    )

    def refresh_tareas():
        # Recargar la lista de tareas desde la base de datos
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.ListTile(
                    title=ft.Text(t['titulo']),
                    subtitle=ft.Text(f"{t['descripcion']} • {t['prioridad']}")
                )
            )
        page.update()

    def add_tarea(e):
        if txt_titulo.value:
            tarea_controller.guardar_nueva(
                user['id_usuario'],
                txt_titulo.value,
                txt_descripcion.value or "",
                dropdown_prioridad.value,
                "personal"
            )
            txt_titulo.value = ""
            txt_descripcion.value = ""
            refresh_tareas()

    refresh_tareas()

    return ft.View(
        route="/tarea",
        bgcolor="#101820",
        appbar=ft.AppBar(
            title=ft.Text(f"Tareas - {user['nombre']}"),
            bgcolor="#1f2937",
            color="white",
            actions=[ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))]
        ),
        controls=[
            ft.Container(
                bgcolor="#111827",
                expand=True,
                padding=20,
                content=ft.Column([
                    ft.Row([txt_titulo, ft.IconButton(ft.Icons.ADD, on_click=add_tarea)]),
                    txt_descripcion,
                    dropdown_prioridad,
                    lista_tareas
                ], expand=True, spacing=15)
            )
        ]
    )
