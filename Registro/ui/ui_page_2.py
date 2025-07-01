import pyvisual as pv


def create_page_2_ui(window,ui):
    """
    Create and return UI elements for Page 2.
    :param container: The page widget for Page 2.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["Text_0"] = pv.PvText(container=window, x=105, y=42, width=472,
        height=123, idle_color=(233, 214, 245, 0), text='BIENVENIDO', is_visible=True,
        text_alignment='center', paddings=(0, 0, 0, 0), font='assets/fonts/FiraSans/FiraSans.ttf', font_size=69,
        font_color=(0, 0, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["lbl_usuario"] = pv.PvText(container=window, x=200, y=179, width=328,
        height=79, idle_color=(194, 155, 215, 0), text='', is_visible=True,
        text_alignment='center', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=37,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag='lbl_usuario')

    ui_page["Button_2"] = pv.PvButton(container=window, x=434, y=303, width=182,
        height=50, text='Regresar', font='assets/fonts/Lexend/Lexend.ttf', font_size=16,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 255, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=25, border_style="solid", box_shadow=None, box_shadow_hover=None,
        icon_path='assets/icons/01c4df648a.svg', icon_position='left', icon_color=(0, 0, 0, 1), icon_color_hover=None,
        icon_spacing=26, icon_scale=1.2, paddings=(2, 0, 3, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(0),
        on_release=None, tag=None)

    return ui_page
