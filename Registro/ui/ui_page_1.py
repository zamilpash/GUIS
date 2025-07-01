import pyvisual as pv


def create_page_1_ui(window,ui):
    """
    Create and return UI elements for Page 1.
    :param container: The page widget for Page 1.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["txt_registro_usuario"] = pv.PvTextInput(container=window, x=250, y=211, width=200,
        height=40, background_color=(64, 195, 163, 0), is_visible=True, placeholder='Username',
        text_alignment='left', default_text='', paddings=(10, 0, 10, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=30, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/3b68898455.svg',
        icon_scale=1, icon_position='right', icon_spacing=10, icon_color=(0, 0, 0, 1),
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_registro_usuario')

    ui_page["txt_registro_password"] = pv.PvTextInput(container=window, x=250, y=264, width=200,
        height=40, background_color=(62, 192, 162, 0), is_visible=True, placeholder='Password',
        text_alignment='left', default_text='', paddings=(10, 0, 10, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=39, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/bfe21c2a3a.svg',
        icon_scale=0.8, icon_position='right', icon_spacing=10, icon_color=(0, 0, 0, 1),
        text_type='Password', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_registro_password')

    ui_page["txt_registro_nombre"] = pv.PvTextInput(container=window, x=250, y=158, width=200,
        height=40, background_color=(211, 226, 243, 0), is_visible=True, placeholder='Nombre completo',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Inter/Inter.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=20, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/8a75e91c0e.svg',
        icon_scale=0.9, icon_position='right', icon_spacing=50, icon_color=(0, 0, 0, 1),
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_registro_nombre')

    ui_page["boton_guardar_datos"] = pv.PvButton(container=window, x=288, y=335, width=123,
        height=33, text='GUARDAR', font='assets/fonts/Inter/Inter.ttf', font_size=12,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=True, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 255, 255, 0), hover_color=None,
        clicked_color=None, border_color=(0, 0, 0, 1), border_hover_color=None, border_thickness=3,
        corner_radius=15, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path='assets/icons/127f1610bb.svg', icon_position='left', icon_color=(0, 0, 0, 1), icon_color_hover=None,
        icon_spacing=9, icon_scale=0.6, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag='boton_guardar_datos')

    ui_page["boton_regresar"] = pv.PvButton(container=window, x=568, y=342, width=105,
        height=34, text='Home', font='assets/fonts/Poppins/Poppins.ttf', font_size=15,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(110, 199, 255, 0), hover_color=None,
        clicked_color=None, border_color=(0, 0, 0, 1), border_hover_color=None, border_thickness=4,
        corner_radius=25, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path='assets/icons/dc8fe43f9a.svg', icon_position='right', icon_color=(0, 0, 0, 1), icon_color_hover=None,
        icon_spacing=14, icon_scale=0.6, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(0),
        on_release=None, tag='boton_regresar')

    ui_page["Icon_5"] = pv.PvIcon(container=window, x=282, y=10, width=135,
        height=135, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/eed2c3deb0.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    return ui_page
