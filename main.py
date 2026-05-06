import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.RegisterView import RegisterView
from views.TareaView import TareaView
from views.UserView import UserView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/registro":
            page.views.append(RegisterView(page, auth_ctrl))
        elif page.route == "/tarea":
            if hasattr(page, 'current_user') and page.current_user:
                page.views.append(TareaView(page, task_ctrl))
            else:
                page.go("/")
        elif page.route == "/usuario":
            if hasattr(page, 'current_user') and page.current_user:
                page.views.append(UserView(page))
            else:
                page.go("/")
        page.update()

    page.on_route_change = route_change
    page.route = "/"
    route_change(page.route)

def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()