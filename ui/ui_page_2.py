import pyvisual as pv


def create_page_2_ui(window,ui):
    """
    Create and return UI elements for Page 2.
    :param container: The page widget for Page 2.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["btn_back_1"] = pv.PvButton(container=window, x=472, y=386, width=180,
        height=35, text='Regresar', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(56, 136, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=25, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(0),
        on_release=None, tag='btn_back_1')

    ui_page["lbl_benv"] = pv.PvText(container=window, x=125, y=74, width=450,
        height=80, idle_color=(158, 77, 201, 0), text='BIENVENIDO', is_visible=True,
        text_alignment='center', paddings=(0, 0, 0, 0), font='assets/fonts/Roboto/Roboto.ttf', font_size=60,
        font_color=(255, 255, 255, 1), bold=True, italic=True, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag='lbl_benv')

    ui_page["lbl_usuario"] = pv.PvText(container=window, x=260, y=205, width=180,
        height=80, idle_color=(149, 86, 184, 0), text='', is_visible=True,
        text_alignment='center', paddings=(0, 0, 0, 5), font='assets/fonts/Poppins/Poppins.ttf', font_size=40,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag='lbl_usuario')

    return ui_page
