# This file contains configuration properties for the Action Editor.

default_transition = "dissolve"
hide_window_in_animation = True
allow_animation_skip = True
default_warper = "linear"
default_rot = True
focusing = False
default_show_camera_icon = True
default_one_line_one_prop = False
default_legacy_gui = False
fps_keymap = True
default_open_only_one_page = False
tab_amount_in_page = 5
_camera_blur_amount = 2.0 
_camera_blur_warper = "linear" 
wide_range = 1500
narrow_range = 7.0
narrow_drag_speed = 1./200
""" wide_drag_speed = int(config.screen_width/200) """
time_range = 7.0
default_channel_list = ["sound"]
default_sideview = True
default_graphic_editor_narrow_range = 2.
default_graphic_editor_wide_range = 2000
preview_size=0.6
preview_background_color="#111"

props_sets = (
        ("Child/Pos    ", ("child", "xpos", "ypos", "zpos", "xalignaround", "yalignaround", "radius", "angle", "rotate","xrotate", "yrotate", "zrotate", "xorientation", "yorientation", "zorientation", "point_to",)), 
        ("3D Matrix    ", ("matrixtransform",)),
        ("Anchor/Offset", ("xanchor", "yanchor", "matrixanchorX", "matrixanchorY", "xoffset", "yoffset")), 
        ("Zoom/Crop    ", ("xzoom", "yzoom", "zoom", "cropX", "cropY", "cropW", "cropH")), 
        ("Effect       ", ("blend", "alpha", "blur", "additive", "matrixcolor", "dof", "focusing")),
        ("Misc         ", ("zzoom", "perspective", "function", "xpan", "ypan", "xtile", "ytile")),
        )

props_groups = {
    "alignaround":["xalignaround", "yalignaround"], 
    "matrixanchor":["matrixanchorX", "matrixanchorY"], 
    "crop":["cropX", "cropY", "cropW", "cropH"], 
    "focusing":["focusing", "dof"], 
    "orientation":["xorientation", "yorientation", "zorientation"], 
}

force_wide_range = {"rotate", "rotateX", "rotateY", "rotateZ", "offsetX", "offsetY", "offsetZ", "zpos", "xoffset", "yoffset", "hue", "dof", "focusing", "angle", "xpan", "ypan", "xrotate", "yrotate", "zrotate", "xorientation", "yorientation", "zorientation"}
force_narrow_range = {"xtile", "ytile"}
force_plus = {"additive", "blur", "alpha", "invert", "contrast", "saturate", "cropW", "cropH", "dof", "focusing", "xtile", "ytile"}
not_used_by_default = {"rotate", "cropX", "cropY", "cropW", "cropH", "xpan", "ypan", "function"}
force_float = ("zoom", "xzoom", "yzoom", "alpha", "additive", "blur", "invert", "contrast", "saturate", "bright", "xalignaround", "yalignaround", "scaleX", "scaleY", "scaleZ", "xrotate", "yrotate", "zrotate", "xorientation", "yorientation", "zorientation")
boolean_props = {"zzoom"}
any_props = {"blend", "point_to"}
def check_perspective(v):
    if isinstance(v, (int, float)):
        return True
    if isinstance(v, tuple) and len(v) == 3:
        for i in v:
            if not isinstance(v, (int, float)):
                return False
        else:
            return True
check_any_props = {"perspective":check_perspective}
def check_poi(v):
    if isinstance(v, tuple) and len(v) == 3:
        x, y, z = v
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
            return True
    elif isinstance(v, renpy.display.transform.Camera):
        return True
    elif v is None:
        return True
    else:
        return False
check_any_props = {"point_to":check_poi}

sort_order_list = (
"blend",
"pos",
"anchor",
"offset",
"xpos", 
"xanchor", 
"xoffset", 
"ypos", 
"yanchor", 
"yoffset", 
"alignaround",
"radius",
"angle",
"zpos", 
"xrotate",
"yrotate",
"zrotate",
"orientation",
"point_to",
"matrixtransform", 
"matrixanchor", 
"rotate", 
"xzoom", 
"yzoom", 
"zoom", 
"crop", 
"alpha", 
"additive", 
"blur", 
"matrixcolor", 
"xpan", 
"ypan", 
"xtile", 
"ytile", 
)


special_props = {"child", "function"}
in_editor = False
""" aspect_16_9 = round(float(config.screen_width)/config.screen_height, 2) == 1.78 """
