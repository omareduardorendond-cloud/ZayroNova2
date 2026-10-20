import flet as ft

def main(page: ft.Page):
    page.title = "Zayro Nova"
    page.bgcolor = "#F8F4EC"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    nombre = ft.Text(
        "ZAYRO NØVA",
        size=30,
        color="#FFFFFF",
        weight=ft.FontWeight.BOLD,
    )
    #paso 1

    contenido = ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Bienvenido a ZAYRO NØVA",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#6B0021",
                    ),
                ],
            ),
        )
    

    #paso 2
    def cambiar_pantalla(titulo):
            contenido.content = ft.Column(
                controls=[
                    ft.Text(
                        titulo,
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="#6B0021",
                    ),
                    ft.Text(f"Sección: {titulo}"),
                ],
            )
            page.update()
    #paso 3

    drawer =ft.NavigationDrawer(
            bgcolor="#F8F4EC",
            controls=[
                ft.NavigationDrawerDestination(
                      icon=ft.Icons.SHOPPING_CART,
                      label="Punto de Venta"
                ),
                ft.NavigationDrawerDestination(
                      icon=ft.Icons.INVENTORY_2,
                      label="Inventario"
                ),
                ft.NavigationDrawerDestination(
                      icon=ft.Icons.HANDSHAKE,
                      label="Proveedores"
                ),
                ft.NavigationDrawerDestination(
                  icon=ft.Icons.BAR_CHART,
                  label="Reportes"    
                ),
                ft.NavigationDrawerDestination(
                  icon=ft.Icons.LOGOUT,
                  label="Cerrar sesión"    
                ),
            ],
        )
    #paso 4

    def abrir_menu(e):
        drawer.open = True
        page.update()
    
    page.drawer = drawer

    async def abrir_menu(e):
            await page.show_drawer()

    #paso 5

    menu = ft.IconButton(
        icon=ft.Icons.MENU,
        icon_color="#F8F4EC",
        on_click=abrir_menu
    )

    #paso 6

    page.appbar = ft.AppBar(
        title=nombre,
        bgcolor="#4A1525",
        center_title=True,
        leading= menu
    )

    page.add(contenido)


ft.run(main)