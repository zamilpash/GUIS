import pyvisual as pv


def create_page_1_ui(window,ui):
    """
    Create and return UI elements for Page 1.
    :param container: The page widget for Page 1.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["txt_new_usuario"] = pv.PvTextInput(container=window, x=240, y=213, width=200,
        height=40, background_color=(228, 228, 228, 1), is_visible=True, placeholder='Usuario',
        text_alignment='left', default_text='', paddings=(12, 0, 20, 0), font='assets/fonts/Ubuntu/Ubuntu.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", corner_radius=16, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_new_usuario')

    ui_page["txt_new_pass"] = pv.PvTextInput(container=window, x=240, y=267, width=200,
        height=40, background_color=(228, 228, 228, 1), is_visible=True, placeholder='Contraseña',
        text_alignment='left', default_text='', paddings=(12, 0, 20, 0), font='assets/fonts/Ubuntu/Ubuntu.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", corner_radius=16, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_new_pass')

    ui_page["txt_nombre"] = pv.PvTextInput(container=window, x=240, y=157, width=200,
        height=40, background_color=(228, 228, 228, 1), is_visible=True, placeholder='Nombre completo',
        text_alignment='left', default_text='Nombre', paddings=(12, 0, 20, 0), font='assets/fonts/Ubuntu/Ubuntu.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", corner_radius=16, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='txt_nombre')

    ui_page["btn_registrar"] = pv.PvButton(container=window, x=265, y=342, width=151,
        height=35, text='Registrar', font='assets/fonts/Outfit/Outfit.ttf', font_size=16,
        font_color=(0, 0, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 255, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=15, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path='assets/icons/76689c2264.svg', icon_position='left', icon_color=(0, 0, 255, 1), icon_color_hover=None,
        icon_spacing=15, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag='btn_registrar')

    ui_page["Icon_4"] = pv.PvIcon(container=window, x=284, y=24, width=112,
        height=112, idle_color=(255, 255, 255, 1), icon_path='assets/icons/489092ab81.svg', corner_radius=0,
        preserve_original_colors=False, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["btn_back"] = pv.PvButton(container=window, x=477, y=387, width=180,
        height=35, text='Regresar', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(56, 136, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=25, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag='btn_back')

    return ui_page
