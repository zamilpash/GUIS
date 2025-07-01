import pyvisual as pv


def create_page_1_ui(window,ui):
    """
    Create and return UI elements for Page 1.
    :param container: The page widget for Page 1.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["Text_0"] = pv.PvText(container=window, x=200, y=-2, width=302,
        height=62, idle_color=(213, 184, 228, 0), text='PROCESAMIENTO', is_visible=True,
        text_alignment='center', paddings=(0, 0, 0, 0), font='assets/fonts/BebasNeue/BebasNeue.ttf', font_size=35,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["OpencvVideo_1"] = pv.PvOpencvVideo(container=window, x=325, y=54, width=360,
        height=202, video_path=None, scale=1, corner_radius=10,
        auto_start=True, flip_v=False, flip_h=False, rotate=0,
        border_color=(0, 0, 0, 1), border_hover_color=None, border_thickness=0, border_style="solid",
        is_visible=True, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["OpencvImage_2"] = pv.PvOpencvImage(container=window, x=27, y=54, width=200,
        height=172, idle_color=(217, 217, 217, 1), scale=1, corner_radius=10,
        flip_v=False, flip_h=False, rotate=0, border_color=(0, 0, 0, 1),
        border_hover_color=None, border_thickness=0, border_style="solid", is_visible=True,
        fill=True, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    return ui_page
