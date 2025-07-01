import pyvisual as pv


def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["Icon_0"] = pv.PvIcon(container=window, x=278, y=10, width=144,
        height=144, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/3f39a77104.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["txt_Pass"] = pv.PvTextInput(container=window, x=250, y=242, width=200,
        height=40, background_color=(62, 192, 162, 0), is_visible=True, placeholder='Password',
        text_alignment='left', default_text='', paddings=(10, 0, 10, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=39, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/bfe21c2a3a.svg',
        icon_scale=0.8, icon_position='right', icon_spacing=10, icon_color=(0, 0, 0, 1),
        text_type='Password', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_Pass')

    ui_page["txt_usuario"] = pv.PvTextInput(container=window, x=250, y=179, width=200,
        height=40, background_color=(64, 195, 163, 0), is_visible=True, placeholder='Username',
        text_alignment='left', default_text='', paddings=(10, 0, 10, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=30, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/3b68898455.svg',
        icon_scale=1, icon_position='right', icon_spacing=10, icon_color=(0, 0, 0, 1),
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_usuario')

    ui_page["boton_ingresar"] = pv.PvButton(container=window, x=296, y=324, width=108,
        height=36, text='Entrar', font='assets/fonts/Outfit/Outfit.ttf', font_size=16,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(148, 61, 159, 0), hover_color=None,
        clicked_color=None, border_color=(0, 0, 0, 1), border_hover_color=None, border_thickness=3,
        corner_radius=15, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path='assets/icons/76689c2264.svg', icon_position='right', icon_color=(0, 0, 0, 1), icon_color_hover=None,
        icon_spacing=15, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag='boton_ingresar')

    ui_page["boton_registrar"] = pv.PvButton(container=window, x=558, y=342, width=113,
        height=37, text='Registrar', font='assets/fonts/Poppins/Poppins.ttf', font_size=12,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=True, italic=False,
        underline=False, strikethrough=False, idle_color=(29, 102, 158, 0.01), hover_color=None,
        clicked_color=None, border_color=(255, 255, 255, 1), border_hover_color='null', border_thickness=3,
        corner_radius=22, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path='assets/icons/1466c3e956.svg', icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=8, icon_scale=0.7, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(1),
        on_release=None, tag='boton_registrar')

    return ui_page
