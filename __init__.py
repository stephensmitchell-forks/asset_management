'''
Copyright (C) 2015 Pistiwique, Pitiwazou
 
Created by Pistiwique, Pitiwazou
 
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
 
bl_info = {
    "name": "Asset management",
    "description": "",
    "author": "Pistiwique, Pitiwazou",
    "version": (1, 0, 0),
    "blender": (2, 76, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }
 
 
import bpy 
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import (StringProperty, 
                    BoolProperty, 
                    FloatVectorProperty,
                    FloatProperty,
                    EnumProperty,
                    IntProperty)
 
from . properties import *
from . ui import *
from . preview_utils import (register_AssetM_pcoll_preview,
                            unregister_AssetM_pcoll_preview)
 
 
 
#----VIEW_3D----#
##UI Panel
#def update_ui(self, context):
#    try:
#        bpy.utils.unregister_class(AM_UI)
#    except:
#        pass
# 
#    if context.user_preferences.addons[__name__].preferences.ui_panel:
#        bpy.utils.register_class(AM_UI)
 
##Tool Panel
#def update_tools(self, context):
#    try:
#        bpy.utils.unregister_class(AM_Tools)
#    except:
#        pass
# 
#    if context.user_preferences.addons[__name__].preferences.tools_panel:
#        AM_Tools.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
#        bpy.utils.register_class(AM_Tools)
 
#Panel preferences
class AssetManagementPreferences(AddonPreferences):
    bl_idname = __name__
 
    #Path Library
    asset_M_library_path = bpy.props.StringProperty(
        name="Your library path",
        maxlen=1024,
        subtype='DIR_PATH')
 
    #3DVIEW
    enabled_panel = BoolProperty(
            default=False
            )
 
    info_panel = BoolProperty(
            default=True
            )
 
#    ui_panel = BoolProperty(
#            default=True,
#            update=update_ui
#            )
#    tools_panel = BoolProperty(
#            default=True,
#            update=update_tools
#            ) 
#    tools_category = StringProperty(
#            name="Category",
#            description="Choose a name for the category panel",
#            default="Tools",
#            update=update_tools
#            ) 
 
#    show_labels = BoolProperty(
#            default=True,
#            description="Display name asset in the preview"
#            )  
 
    # Custom object render 
 
    thumbnails_resolution = EnumProperty(
            items=(('256x256', "256x256", '', 'IMAGE_COL', 1),
                ('128x128', "128x128", '', 'IMAGE_COL', 2)),
                default='256x256')
 
    samples_value = IntProperty(
            default=100,
            min=10, max=1000,
            description = "Change Samples of the Thumbnails Render"
            )
 
    render_type = EnumProperty(
            items=(('GPU', "GPU", '', '', 1),
                    ('CPU', "CPU", '', '', 2)),
                    default='CPU')
 
 
    custom_render_enabled = BoolProperty(
            default=False
            )
 
    enabled_obj = BoolProperty(
            default=False
            ) 
 
    obj_fresnel = FloatProperty(
            name="IOR:",
            default=1.45,
            min=0, max=20,
            precision=3
            )
 
    obj_color = FloatVectorProperty(
            name="Color:", 
            default=(0.136, 0.136, 0.136), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR'
            )
 
    obj_color_roughness = FloatProperty(
            name="Roughness:",
            default=0,
            min=0, max=1,
            precision=3
            )
 
    obj_mix = FloatProperty(
            default=0.342,
            min=0, max=1,
            precision=3
            )
 
    aniso_color = FloatVectorProperty(
            name="Color:", 
            default=(0.8, 0.8, 0.8), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR'
            )
 
    aniso_roughness = FloatProperty(
            name="Roughness:",
            default=0.150,
            min=0, max=1,
            precision=3
            )
 
    anisotropy = FloatProperty(
            name="Anisotropy:",
            default=0.5,
            min=0, max=1,
            precision=3
            )
 
    obj_glossy_color = FloatVectorProperty(
            name="Color:", 
            default=(1, 1, 1), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR'
            )
 
    obj_glossy_color_roughness = FloatProperty(
            name="Roughness:", 
            default=0.05, 
            min=0, max=1,
            precision=3, 
            )
 
    ao_color = FloatVectorProperty(
            name="Ambiant Occlusion Color::", 
            default=(0.9, 0.9, 0.9), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR',
            description = "Change the color of the Ambiant Occlusion"
            )
 
    ao_object = FloatProperty(
            name="Ambiant Occlusion:", 
            default=0, 
            min=0, max=1,
            precision=3, 
            description = "Activate the Ambiant Occlusion"
            )
 
    # Custom ground render    
    enabled_ground = BoolProperty(
            default=False
            ) 
 
    ground_fresnel = FloatProperty(
            name="IOR:",
            default=1.45,
            min=0, max=20,
            precision=3
            )
 
    ground_color = FloatVectorProperty(
            name="Color:", 
            default=(0.013, 0.013, 0.013), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR'
            )
 
    ground_color_roughness = FloatProperty(
            name="Roughness:",
            default=0,
            min=0, max=1,
            precision=3
            )
 
    ground_glossy_color = FloatVectorProperty(
            name="Color:", 
            default=(1, 1, 1), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR'
            )
 
    ground_glossy_color_roughness = FloatProperty(
            name="Roughness:", 
            default=0.2, 
            min=0, max=1,
            precision=3, 
            )
 
    opacity = FloatProperty(
            name="Opacity:", 
            default=1, 
            min=0, max=1,
            precision=3, 
            description = "Change the opacity of the Ground"
            )
 
    ao_ground = FloatProperty(
            name="Ambiant Occlusion:", 
            default=0, 
            min=0, max=1,
            precision=3, 
            description = "Activate the Ambiant Occlusion Ground"
            )
 
    ao_ground_color = FloatVectorProperty(
            name="Ambiant Occlusion Color:", 
            default=(0.9, 0.9, 0.9), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR',
            description = "Change the color of the Ambiant Occlusion Ground"
            )
 
    # Custom light render  
    enabled_light = BoolProperty(
            default=False
            )
 
    light_color = FloatVectorProperty(
            name="Color:", 
            default=(1, 1, 1), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR',
            description = "Change the color of the Light"
            )
 
    light_strength = FloatProperty(
            name="Strength:",
            default=2,
            min=0, max=50,
            precision=3,
            description = "Change the strength of the Light"
            )
 
    #Contour
    enabled_contour = BoolProperty(
            default=False
            )
 
    freestyle_on_off = BoolProperty(
            default=False,
            description="Activate the contour on the Thumbnail render"
            )
 
    contour_color = FloatVectorProperty(
            name="Color:", 
            default=(1, 1, 1), 
            min=0, max=1,
            precision=3, 
            subtype='COLOR',
            description = "Change the color of the Contour"
            )
 
    contour_size = FloatProperty(
            name="Size:",
            default=1,
            min=1, max=8,
            precision=3,
            description = "Change the size of the Contour"
            )
 
    contour_opacity = FloatProperty(
            name="Opacity:",
            default=1,
            min=0, max=1,
            precision=3,
            description = "Change the opacity of the Contour"
            )
 
    ao_mix = FloatProperty(
            name="Ambiant Occlusion Strenght:",
            default=0,
            min=0, max=1,
            precision=3,
            description = "Change the streanght of the Ambiant Occlusion"
            )
 
    glow = FloatProperty(
            name="Glow Effect:",
            default=0.2,
            min=0, max=1,
            precision=3,
            description = "Change the streanght of the Glow"
            )
 
    #Documentation
    AM_Tools_Documentation = bpy.props.BoolProperty(
        default=False,
        description="Documentation of the Asset Management Addon"
        )
    #URLs          
    enabled_links = BoolProperty(
            default=False
            ) 
 
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "asset_M_library_path")
 
 
        layout.prop(self, "info_panel", text="Info", icon='UNPINNED')
        if self.info_panel:
            box = layout.box()
            box.label(text="Hello and welcome to the Asset Management !")
            box.separator()
            box.label(text="Use the Addon with Blender 2.76B install and zip versions", icon="ERROR")
            box.separator()
            box.label(text="With Asset Management you can create different types of renders, for the Thumbnails")
            box.label(text="Metalic, Plastic, Ambiant Occlusion , with Background or without etc.")
            box.label(text="You can play with the settings in the Render Customisation.")
            box.separator()
            box.label(text="The Render part of this Addon works correctly with little assets,")
            box.label(text="the object is placed correctly and give you a good result")
            box.separator()
            box.label(text="This feature is experimental !")
            box.separator()
            box.label(text="If you have any issues, use the Opengl Rendering to make your thumbnails.")
            box.label(text="Or Add a custom thumbnail for your Asset.")
 
        # VIEW_3D
#        layout.prop(self, "enabled_panel", text="Panel preferences", icon='PREFERENCES')
#        if self.enabled_panel:
#            box = layout.box()
#            row = box.row()
#            row.label(text="3D View :", icon='MESH_CUBE')
#            row = box.row()
#            row.prop(self, "tools_panel", text="T Panel")
#            if self.tools_panel:
#                row.prop(self, "tools_category")
#            row = box.row()
#            row.prop(self, "ui_panel", text="N Panel")
#            row = box.row()
#            row.prop(self, "show_labels", text="Show labels in the preview")
 
        layout.prop(self, "custom_render_enabled", text="Render customisation", icon='MATERIAL_DATA')
        if self.custom_render_enabled:
            # THUMBNAILS
            row = layout.row(align=True)
            row.label("Thumbnails resolution:")
            row.prop(self, "thumbnails_resolution", text="")
 
            row = layout.row(align=True)
            row.label("Samples:")
            row.prop(self, "samples_value", text="")
 
#            row = layout.row(align=True)
#            row.prop(self, "show_labels", text="Show labels in the preview")
 
#            row = layout.row(align=True)
#            row.label("Compute Device:") 
#            row.prop(self, "render_type", text="")
 
            # OBJECT
            split = layout.split()
            split.prop(self, "enabled_obj", text="Object", icon='MESH_MONKEY')
            if self.enabled_obj:
 
                row = layout.row(align=True)
                row.label("Fresnel:")          
                row.prop(self, "obj_fresnel", text="")
 
                row = layout.row(align=True)
                row.label("Diffuse color:")
                row.prop(self, "obj_color", text="")
 
                row = layout.row(align=True)
                row.label("Diffuse roughness:")
                row.prop(self, "obj_color_roughness", text="")
 
                row = layout.row(align=True)
                row.label("Mix Shader:")
                row.prop(self, "obj_mix", text="")
 
                row = layout.row(align=True)
                row.label("Anisotropic color:")
                row.prop(self, "aniso_color", text="")
 
                row = layout.row(align=True)
                row.label("Anisotropic roughness:")
                row.prop(self, "aniso_roughness", text="")
 
                row = layout.row(align=True)
                row.label("Anisotropic:")
                row.prop(self, "anisotropy", text="")
 
                row = layout.row(align=True)
                row.label("Glossy color:")
                row.prop(self, "obj_glossy_color", text="")
 
                row = layout.row(align=True)
                row.label("Glossy roughness:") 
                row.prop(self, "obj_glossy_color_roughness", text="")
 
                row = layout.row(align=True)
                row.label("Ambiant Occlusion:") 
                row.prop(self, "ao_object", text="")
 
                row = layout.row(align=True)
                row.label("Ambiant Occlusion Color:") 
                row.prop(self, "ao_color", text="")
 
            # GROUND
            split = layout.split()
            split.prop(self, "enabled_ground", text="Ground", icon='MESH_GRID')
            if self.enabled_ground:
 
                row = layout.row(align=True)
                row.label("Fresnel:")     
                row.prop(self, "ground_fresnel", text="")
 
                row = layout.row(align=True)
                row.label("Diffuse color:") 
                row.prop(self, "ground_color", text="")
 
                row = layout.row(align=True)
                row.label("Diffuse roughness:")
                row.prop(self, "ground_color_roughness", text="")
 
                row = layout.row(align=True)
                row.label("Glossy color:")
                row.prop(self, "ground_glossy_color", text="")
 
                row = layout.row(align=True)
                row.label("Glossy roughness:")
                row.prop(self, "ground_glossy_color_roughness", text="")
 
                row = layout.row(align=True)
                row.separator()
 
                row = layout.row(align=True)
                row.label("Opacity:")
                row.prop(self, "opacity", text="")
 
                row = layout.row(align=True)
                row.label("Ambiant Occlusion:") 
                row.prop(self, "ao_ground", text="")
 
                row = layout.row(align=True)
                row.label("Ambiant Occlusion Color:") 
                row.prop(self, "ao_ground_color", text="")
 
            # LIGHT
            split = layout.split()
            split.prop(self, "enabled_light", text="Light", icon='LAMP_SPOT')
            if self.enabled_light:
 
                row = layout.row(align=True)
                row.label("Color:")   
                row.prop(self, "light_color", text="")
 
                row = layout.row(align=True)
                row.label("Strength:")
                row.prop(self, "light_strength", text="")
 
            # Contour
            split = layout.split()
            split.prop(self, "enabled_contour", text="Compositing", icon='ANTIALIASED')
            if self.enabled_contour:
 
                row = layout.row(align=True)
                row.label("Contour On/Off:")
                row.prop(self, "freestyle_on_off", text="")
 
                row = layout.row(align=True)
                row.label("Contour Opacity:")   
                row.prop(self, "contour_opacity", text="")
 
                row = layout.row(align=True)
                row.label("Contour Color:")   
                row.prop(self, "contour_color", text="")
 
                row = layout.row(align=True)
                row.label("Contour Size:")   
                row.prop(self, "contour_size", text="")
 
                layout.separator()
 
                row = layout.row(align=True)
                row.label("Ambiant Occlusion Strenght:")   
                row.prop(self, "ao_mix", text="")
 
                row = layout.row(align=True)
                row.label("Glow Strenght:")   
                row.prop(self, "glow", text="")
 
 
        #Documentation 
        layout.prop(self, "AM_Tools_Documentation", text="Documentation", icon='QUESTION')
        if self.AM_Tools_Documentation:
 
            row = layout.row(align=True)
            row.operator("wm.url_open", text="Doc US").url = "http://www.pitiwazou.com/asset-management-documentation_us/"
            row.operator("wm.url_open", text="Doc FR").url = "http://www.pitiwazou.com/asset-management-documentation-fr/"
 
            layout.separator()
 
            layout.operator("wm.url_open", text="Installation the Screws & Bolts Free Pcack").url = "https://www.youtube.com/watch?v=TLwpyYBy8qI"
 
            layout.separator()
 
            layout.operator("wm.url_open", text="Installation").url = "https://www.youtube.com/watch?v=5nH2kLTEo1E"
            layout.operator("wm.url_open", text="Create Libraries and Categories").url = "https://www.youtube.com/watch?v=_fH-k0wMugE"
 
            layout.separator()
 
            layout.operator("wm.url_open", text="Thumbnails - Addon Render").url = "https://www.youtube.com/watch?v=jMNvEIW7l5A"
            layout.operator("wm.url_open", text="Thumbnails - OpenGL Render").url = "https://www.youtube.com/watch?v=XOQ9q1paorY"
            layout.operator("wm.url_open", text="Thumbnails - Custom Thumbnails ").url = "https://www.youtube.com/watch?v=eOrlgM0vEKQ"
 
            layout.separator()
 
            layout.operator("wm.url_open", text="Prepare your Asset").url = "https://www.youtube.com/watch?v=YhuqpuwqgKE"
            layout.operator("wm.url_open", text="Asset To Selection").url = "https://www.youtube.com/watch?v=Y1mWKCpCDOw"
 
            layout.separator()
 
            layout.operator("wm.url_open", text="Import an existing Library ").url = "https://www.youtube.com/watch?v=_TBpzOoxLxI"
 
        #URls
        layout.prop(self, "enabled_links", text="URL's", icon='URL')
        if self.enabled_links:
            row = layout.row(align=True)
            row.operator("wm.url_open", text="Pistiwique").url = "https://github.com/pistiwique"
            row.operator("wm.url_open", text="Pitiwazou.com").url = "http://www.pitiwazou.com"
            row.operator("wm.url_open", text="Wazou's Ghitub").url = "https://github.com/pitiwazou/Scripts-Blender"
            row.operator("wm.url_open", text="BlenderLounge Forum ").url = "http://blenderlounge.fr/forum/"
 
 
# load and reload submodules
##################################    
 
from . import developer_utils
modules = developer_utils.setup_addon_modules(__path__, __name__)
 
 
 
# register
################################## 
#addon_keymaps = []
 
#def register_keymaps():
#    global addon_keymaps
#    wm = bpy.context.window_manager
#    km = wm.keyconfigs.addon.keymaps.new(name = "3D View", space_type = "VIEW_3D")
#    kmi = km.keymap_items.new(AM_Preview.bl_idname, 'Q', 'PRESS', shift=True, ctrl=True, alt=True)
 
#    addon_keymaps.append(km)
#    
#def unregister_keymaps():
#    global addon_keymaps
#    wm = bpy.context.window_manager
#    for km in addon_keymaps:
#        for kmi in km.keymap_items:
#            km.keymap_items.remove(kmi)
#        wm.keyconfigs.addon.keymaps.remove(km)
#    addon_keymaps.clear()
 
import traceback
 
def register():
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
 
    #Register Panels
#    update_ui(None, bpy.context)
#    update_tools(None, bpy.context)
 
 
    bpy.types.WindowManager.asset_m = bpy.props.PointerProperty(type=AssetManagementCollectionGroup)
    register_AssetM_pcoll_preview()
 
#    register_keymaps()
    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
 
 
def unregister():
 
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
 
    #Unregister Panels
 
#    bpy.types.AM_UI.remove(update_ui)
#    bpy.types.AM_Tools.remove(update_tools)
 
#    bpy.types.update_ui.remove(AM_UI)
#    bpy.types.update_tools.remove(AM_Tools)
 
 
    del bpy.types.WindowManager.asset_m
    unregister_AssetM_pcoll_preview()
#    unregister_keymaps()
    print("Unregistered {}".format(bl_info["name"]))
 
 
 
 
 
