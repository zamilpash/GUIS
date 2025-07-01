import pyvisual as pv


def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["Icon_0"] = pv.PvIcon(container=window, x=285, y=16, width=130,
        height=130, idle_color=(75, 75, 75, 1), preserve_original_colors=False, icon_path='assets/icons/3f39a77104.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["txt_usuario"] = pv.PvTextInput(container=window, x=225, y=168, width=250,
        height=35, background_color=(69, 69, 69, 1), is_visible=True, placeholder='Email',
        text_alignment='left', default_text='', paddings=(15, 0, 15, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(204, 204, 204, 1), border_color=(255, 255, 255, 1), border_thickness=1,
        border_style="solid", corner_radius=45, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/3b68898455.svg',
        icon_scale=0.8, icon_position='right', icon_spacing=10, icon_color=(204, 204, 204, 1),
        text_type='Email', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_usuario')

    ui_page["txt_pass"] = pv.PvTextInput(container=window, x=225, y=246, width=250,
        height=35, background_color=(69, 69, 69, 1), is_visible=True, placeholder='Password',
        text_alignment='left', default_text='', paddings=(15, 0, 13, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(204, 204, 204, 1), border_color=(204, 204, 204, 1), border_thickness=1,
        border_style="solid", corner_radius=33, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path='assets/icons/6995168037.svg',
        icon_scale=0.8, icon_position='right', icon_spacing=0, icon_color=(204, 204, 204, 1),
        text_type='Password', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_pass')

    ui_page["boton_entrar"] = pv.PvButton(container=window, x=293, y=334, width=114,
        height=38, text='Next', font='assets/fonts/Outfit/Outfit.ttf', font_size=16,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(69, 69, 69, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=15, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path='assets/icons/76689c2264.svg', icon_position='right', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=15, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=lambda el: ui["pages"].set_current_page(1),
        on_release=None, tag='boton_entrar')

    return ui_page
