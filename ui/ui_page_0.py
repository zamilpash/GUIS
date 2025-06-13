import pyvisual as pv


def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["txt_usuario"] = pv.PvTextInput(container=window, x=242, y=205, width=200,
        height=40, background_color=(211, 226, 243, 1), is_visible=True, placeholder='Username',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Inter/Inter.ttf',
        font_size=13, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=2,
        border_style="solid", corner_radius=20, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/8a75e91c0e.svg',
        icon_scale=0.8, icon_position='left', icon_spacing=7, icon_color=(49, 48, 48, 1),
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='usuario')

    ui_page["txt_pass"] = pv.PvTextInput(container=window, x=242, y=263, width=200,
        height=40, background_color=(211, 226, 243, 1), is_visible=True, placeholder='Password',
        text_alignment='center', default_text='Password', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=13, font_color=(51, 49, 51, 1), border_color=(0, 0, 0, 1), border_thickness=2,
        border_style="solid", corner_radius=34, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/bfe21c2a3a.svg',
        icon_scale=0.8, icon_position='left', icon_spacing=5, icon_color=(62, 61, 61, 1),
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='password')

    ui_page["boton_entrar"] = pv.PvButton(container=window, x=242, y=321, width=200,
        height=35, text='Login', font='assets/fonts/Lexend/Lexend.ttf', font_size=20,
        font_color=(86, 86, 86, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 255, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=17, border_style="ridge", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='right', icon_color=(0, 0, 0, 1), icon_color_hover=None,
        icon_spacing=9, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(none),
        on_release=None, tag='boton_entrar')

    ui_page["Icon_3"] = pv.PvIcon(container=window, x=271, y=38, width=142,
        height=142, idle_color=(255, 255, 255, 1), icon_path='assets/icons/3f39a77104.svg', corner_radius=0,
        preserve_original_colors=False, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["boton_registrar"] = pv.PvButton(container=window, x=470, y=378, width=200,
        height=35, text='Sign in', font='assets/fonts/Lexend/Lexend.ttf', font_size=20,
        font_color=(68, 68, 68, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 255, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=17, border_style="ridge", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='right', icon_color=(0, 0, 0, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(1),
        on_release=None, tag='boton_registrar')

    return ui_page
