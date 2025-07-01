import pyvisual as pv
from ui.ui import create_ui
import cv2
import pymysql
from functools import partial

# ===================================================
# ================ 1. LOGIC CODE ====================
# ===================================================

# (Your logic code here)

# Configuración correcta para conectarse a la base de datos ya existente
config = {
    'host': 'localhost',
    'user': 'Usuario_nuevo',
    'password': 'Test987654321',
    'database': 'sistema_monitoreo'  
    }
        

# Función para verificar si un usuario y contraseña existen en la tabla 'usuarios'
def verificar_usuario(usuario, password):
    try:
        # Conectar a la base de datos
        conn = pymysql.connect(host=config['host'],
                               user=config['user'],
                               password=config['password'],
                               database=config['database'])
        cursor = conn.cursor()
        sql = """SELECT usuario, password FROM Operadores WHERE 
        usuario = %s AND password = %s"""
        cursor.execute(sql, (usuario, password))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return True, resultado[0], resultado[1]
        else:
            return False, None, None

    except Exception as e:
        print(f"Error en login: {e}")
        return False, None, None

# Maneja el login al presionar el botón
def hacer_login(instance, ui):
    print("Por favor, ingresa tus credenciales")

    usuario = ui['page_0']['txt_usuario'].text
    password = ui['page_0']['txt_Pass'].text

    exito, usuario, password = verificar_usuario(usuario, password)

    if exito:
        print(f'Bienvenido {usuario}')
        ui['page_2']['lbl_usuario'].text = f"{usuario}"
        ui['pages'].set_current_page(2)
    else:
        print("Usuario o contraseña incorrectos")


# Registra un nuevo usuario
def registrar_usuario(instance, ui):
    try:

        config = {
            'host': 'localhost',
            'user': 'Usuario_nuevo',
            'password': 'Test987654321',
            'database': 'sistema_monitoreo'  
        }
        # Conectar a la base de datos
        conn = pymysql.connect(host=config['host'],
                               user=config['user'],
                               password=config['password'],
                               database=config['database'])
        cursor = conn.cursor()

        nombre = ui['page_1']['txt_registro_nombre'].text.strip()
        usuario = ui['page_1']['txt_registro_usuario'].text.strip()
        password = ui['page_1']['txt_registro_password'].text.strip()

        print(f"Intentando registrar: nombre={nombre}, usuario={usuario}, password={password}")

        if not nombre or not usuario or not password:
            print("Error: Todos los campos son obligatorios")
            return  # No cambia de página si falta info

        sql = """INSERT INTO Operadores (nombre, usuario, password) 
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (nombre, usuario, password))
        conn.commit()
        print("Usuario registrado correctamente")

        conn.close()

        # Limpiar campos para nuevo registro
        ui['page_1']['txt_registro_nombre'].text = ''
        ui['page_1']['txt_registro_usuario'].text = ''
        ui['page_1']['txt_registro_password'].text = ''

        ui['pages'].set_current_page(0)

    except Exception as e:
        print(f"Error insertando usuario: {e}")



# ===================================================
# ============== Botones =====================
# Botón que lleva a la página de registro
def button_Registrar(instance, ui):
    print('Cambio a pagina 1')
    ui['pages'].set_current_page(1)

# Botón que regresa al login
def button_Regresar(instance, ui):
    print('Cambio a pagina 0')
    ui['pages'].set_current_page(0)



# ===================================================
# ============== 2. EVENT BINDINGS ==================
# ===================================================


def attach_events(ui):
    """
    Bind events to UI components.
    :param ui: Dictionary containing UI components.
    """
    # Página 0 - Login
    ui['page_0']['boton_ingresar'].on_click = partial(hacer_login, ui=ui)
    ui['page_0']['boton_registrar'].on_click = partial(button_Registrar, ui=ui)
    ui['page_0']['txt_usuario'].on_change = lambda instance: print(f"Usuario ingresado: {instance.text}")
    ui['page_0']['txt_Pass'].on_change = lambda instance: print(f"Contraseña ingresada: {instance.text}")

    #Página 1 - Registro
    ui['page_1']['boton_regresar'].on_click = partial(button_Regresar, ui=ui)
    ui['page_1']['boton_guardar_datos'].on_click = partial(registrar_usuario, ui=ui)
    ui['page_1']['txt_registro_nombre'].on_change = lambda instance: print(f"Nombre registrado: {instance.text}")
    ui['page_1']['txt_registro_usuario'].on_change = lambda instance: print(f"Usuario registrado: {instance.text}")
    ui['page_1']['txt_registro_password'].on_change = lambda instance: print(f"Contraseña registrada: {instance.text}")

    # Página 2 - Mostrar usuario
    ui['page_2']['lbl_usuario'].on_change = lambda instance: print(f"Usuario mostrado: {instance.text}")

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
