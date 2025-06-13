import pyvisual as pv
from ui.ui import create_ui
from functools import partial
import pymysql
# ===================================================
# ================ 1. LOGIC CODE ====================
# ===================================================

# (Your logic code here)

# Funcion para entrar a la pantalla de registro
def button_registrar(instance, ui):
    print("Pagina para registrar")
    ui['pages'].set_current_page(1)
    

# Funcion de la pagina de ingreso
def page_ingresar(instance, ui):
    pass


# Función para la pagina de registro
def page_registrar(instances, ui):
    pass

def button_back(instances, ui):
    ui['pages'].set_current_page(0)


# ===================================================
# ============== 2. EVENT BINDINGS ==================
# ===================================================

def attach_events(ui):
    """
    Bind events to UI components.
    :param ui: Dictionary containing UI components.
    """

    ui['page_0']['boton_registrar'].on_click = partial(button_registrar, ui = ui)           # Boton para ir de pagina 0 hacía 1
    ui['page_1']['btn_back'].on_click = partial(button_back, ui = ui)                     # Boton para regresar de pagina 1 a 0




# ===================================================
# ============== 3. MAIN FUNCTION ==================
# ===================================================


def main():
    app = pv.PvApp()
    ui = create_ui()
    attach_events(ui)
    ui["window"].show()
    app.run()


if __name__ == '__main__':
    main()
