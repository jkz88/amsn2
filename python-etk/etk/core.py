import c_etk

from c_etk import main, main_iterate, main_quit, EtkMeta, \
    theme_widget_set_from_path, theme_edje_object_set_from_parent, \
    theme_edje_object_set


# Another way to registering is defining the '_etk_type' attribute
# in the class definition
register = c_etk._object_mapping_register


class Object(c_etk.Object):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Object"


class Widget(c_etk.Widget):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Widget"


class Window(c_etk.Window, c_etk.WindowEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Window"


class Embed(c_etk.Embed, c_etk.EmbedEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Embed"


class Label(c_etk.Label, c_etk.LabelEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Label"


class Button(c_etk.Button, c_etk.ButtonEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Button"


class Table(c_etk.Table, c_etk.TableEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Table"


class HBox(c_etk.HBox, c_etk.BoxEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_HBox"


class VBox(c_etk.VBox, c_etk.BoxEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_VBox"


class Entry(c_etk.Entry, c_etk.EntryEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Entry"


class Combobox(c_etk.Combobox, c_etk.ComboboxEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Combobox"


class ComboboxItem(c_etk.ComboboxItem):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Combobox_Item"


class ComboboxEntry(c_etk.ComboboxEntry, c_etk.ComboboxEntryEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Combobox_Entry"


class ComboboxEntryItem(c_etk.ComboboxEntryItem):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Combobox_Entry_Item"


class Image(c_etk.Image, c_etk.ImageEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Image"


class ProgressBar(c_etk.ProgressBar, c_etk.ProgressBarEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Progress_Bar"


class HSlider(c_etk.HSlider, c_etk.SliderEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_HSlider"


class VSlider(c_etk.VSlider, c_etk.SliderEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_VSlider"


class Frame(c_etk.Frame, c_etk.FrameEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Frame"


class Canvas(c_etk.Canvas, c_etk.CanvasEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Canvas"


class ToggleButton(c_etk.ToggleButton, c_etk.ToggleButtonEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Toggle_Button"


class Viewport(c_etk.Viewport, c_etk.ViewportEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Viewport"


class ScrolledView(c_etk.ScrolledView, c_etk.ScrolledViewEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Scrolled_View"


class Alignment(c_etk.Alignment, c_etk.AlignmentEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Alignment"


class Scrollbar(c_etk.Scrollbar, c_etk.ScrollbarEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Scrollbar"


class VScrollbar(c_etk.VScrollbar):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_VScrollbar"


class HScrollbar(c_etk.HScrollbar):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_HScrollbar"


class Separator(c_etk.Separator, c_etk.SeparatorEnums):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_Separator"


class VSeparator(c_etk.VSeparator):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_VSeparator"


class HSeparator(c_etk.HSeparator):
    __metaclass__ = EtkMeta
    _etk_type = "Etk_HSeparator"