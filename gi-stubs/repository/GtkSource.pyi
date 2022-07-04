
from typing import Optional

from gi.repository import Gtk
from gi.repository import GObject


_namespace: str = ...
_version: str = ...

def completion_error_quark(*args, **kwargs): ...
def encoding_get_all(*args, **kwargs): ...
def encoding_get_current(*args, **kwargs): ...
def encoding_get_default_candidates(*args, **kwargs): ...
def encoding_get_from_charset(*args, **kwargs): ...
def encoding_get_utf8(*args, **kwargs): ...
def file_loader_error_quark(*args, **kwargs): ...
def file_saver_error_quark(*args, **kwargs): ...
def finalize(*args, **kwargs): ...
def init(*args, **kwargs): ...
def utils_escape_search_text(*args, **kwargs): ...
def utils_unescape_search_text(*args, **kwargs): ...


class Buffer(Gtk.TextBuffer):
    def backward_iter_to_source_mark(*args, **kwargs): ...
    def begin_not_undoable_action(*args, **kwargs): ...
    def can_redo(*args, **kwargs): ...
    def can_undo(*args, **kwargs): ...
    def change_case(*args, **kwargs): ...
    def create_source_mark(*args, **kwargs): ...
    def end_not_undoable_action(*args, **kwargs): ...
    def ensure_highlight(*args, **kwargs): ...
    def forward_iter_to_source_mark(*args, **kwargs): ...
    def get_context_classes_at_iter(*args, **kwargs): ...
    def get_highlight_matching_brackets(*args, **kwargs): ...
    def get_highlight_syntax(*args, **kwargs): ...
    def get_implicit_trailing_newline(*args, **kwargs): ...
    def get_language(self) -> Optional[Language]: ...
    def get_max_undo_levels(*args, **kwargs): ...
    def get_source_marks_at_iter(*args, **kwargs): ...
    def get_source_marks_at_line(*args, **kwargs): ...
    def get_style_scheme(self) -> Optional[StyleScheme]: ...
    def get_undo_manager(*args, **kwargs): ...
    def iter_backward_to_context_class_toggle(*args, **kwargs): ...
    def iter_forward_to_context_class_toggle(*args, **kwargs): ...
    def iter_has_context_class(*args, **kwargs): ...
    def join_lines(*args, **kwargs): ...
    @classmethod
    def new_with_language(cls, language: Language) -> Buffer: ...
    def redo(*args, **kwargs): ...
    def remove_source_marks(*args, **kwargs): ...
    def set_highlight_matching_brackets(self, highlight: bool) -> None: ...
    def set_highlight_syntax(self, highlight: bool) -> None: ...
    def set_implicit_trailing_newline(*args, **kwargs): ...
    def set_language(self, language: Optional[Language]) -> None: ...
    def set_max_undo_levels(*args, **kwargs): ...
    def set_style_scheme(self, scheme: Optional[StyleScheme]) -> None: ...
    def set_undo_manager(*args, **kwargs): ...
    def sort_lines(*args, **kwargs): ...
    def undo(*args, **kwargs): ...
    
    def do_bracket_matched(self, *args, **kwargs): ...
    def do_redo(self, *args, **kwargs): ...
    def do_undo(self, *args, **kwargs): ...
    

class Completion:
    parent_instance = ...
    priv = ...
    
    def add_provider(*args, **kwargs): ...
    def block_interactive(*args, **kwargs): ...
    def create_context(*args, **kwargs): ...
    def get_info_window(*args, **kwargs): ...
    def get_providers(*args, **kwargs): ...
    def get_view(*args, **kwargs): ...
    def hide(*args, **kwargs): ...
    def remove_provider(*args, **kwargs): ...
    def start(*args, **kwargs): ...
    def unblock_interactive(*args, **kwargs): ...
    
    def do_activate_proposal(self, *args, **kwargs): ...
    def do_hide(self, *args, **kwargs): ...
    def do_move_cursor(self, *args, **kwargs): ...
    def do_move_page(self, *args, **kwargs): ...
    def do_populate_context(self, *args, **kwargs): ...
    def do_proposal_activated(self, *args, **kwargs): ...
    def do_show(self, *args, **kwargs): ...
    

class CompletionContext:
    parent = ...
    priv = ...
    
    def add_proposals(*args, **kwargs): ...
    def get_activation(*args, **kwargs): ...
    def get_iter(*args, **kwargs): ...
    
    def do_cancelled(self, *args, **kwargs): ...
    

class CompletionInfo:
    parent = ...
    
    def move_to_iter(*args, **kwargs): ...
    

class CompletionItem:
    parent = ...
    priv = ...
    
    def new(*args, **kwargs): ...
    def set_gicon(*args, **kwargs): ...
    def set_icon(*args, **kwargs): ...
    def set_icon_name(*args, **kwargs): ...
    def set_info(*args, **kwargs): ...
    def set_label(*args, **kwargs): ...
    def set_markup(*args, **kwargs): ...
    def set_text(*args, **kwargs): ...
    

class CompletionProposal:
    def changed(*args, **kwargs): ...
    def equal(*args, **kwargs): ...
    def get_gicon(*args, **kwargs): ...
    def get_icon(*args, **kwargs): ...
    def get_icon_name(*args, **kwargs): ...
    def get_info(*args, **kwargs): ...
    def get_label(*args, **kwargs): ...
    def get_markup(*args, **kwargs): ...
    def get_text(*args, **kwargs): ...
    def hash(*args, **kwargs): ...
    

class CompletionProvider:
    def activate_proposal(*args, **kwargs): ...
    def get_activation(*args, **kwargs): ...
    def get_gicon(*args, **kwargs): ...
    def get_icon(*args, **kwargs): ...
    def get_icon_name(*args, **kwargs): ...
    def get_info_widget(*args, **kwargs): ...
    def get_interactive_delay(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_priority(*args, **kwargs): ...
    def get_start_iter(*args, **kwargs): ...
    def match(*args, **kwargs): ...
    def populate(*args, **kwargs): ...
    def update_info(*args, **kwargs): ...
    

class CompletionWords:
    parent = ...
    priv = ...
    
    def new(*args, **kwargs): ...
    def register(*args, **kwargs): ...
    def unregister(*args, **kwargs): ...
    

class Encoding:
    def free(*args, **kwargs): ...
    def get_all(*args, **kwargs): ...
    def get_charset(*args, **kwargs): ...
    def get_current(*args, **kwargs): ...
    def get_default_candidates(*args, **kwargs): ...
    def get_from_charset(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_utf8(*args, **kwargs): ...
    def to_string(*args, **kwargs): ...
    

class File:
    parent = ...
    priv = ...
    
    def check_file_on_disk(*args, **kwargs): ...
    def get_compression_type(*args, **kwargs): ...
    def get_encoding(*args, **kwargs): ...
    def get_location(*args, **kwargs): ...
    def get_newline_type(*args, **kwargs): ...
    def is_deleted(*args, **kwargs): ...
    def is_externally_modified(*args, **kwargs): ...
    def is_local(*args, **kwargs): ...
    def is_readonly(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_location(*args, **kwargs): ...
    

class FileLoader:
    parent = ...
    priv = ...
    
    def get_buffer(*args, **kwargs): ...
    def get_compression_type(*args, **kwargs): ...
    def get_encoding(*args, **kwargs): ...
    def get_file(*args, **kwargs): ...
    def get_input_stream(*args, **kwargs): ...
    def get_location(*args, **kwargs): ...
    def get_newline_type(*args, **kwargs): ...
    def load_async(*args, **kwargs): ...
    def load_finish(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_from_stream(*args, **kwargs): ...
    def set_candidate_encodings(*args, **kwargs): ...
    

class FileSaver:
    object = ...
    priv = ...
    
    def get_buffer(*args, **kwargs): ...
    def get_compression_type(*args, **kwargs): ...
    def get_encoding(*args, **kwargs): ...
    def get_file(*args, **kwargs): ...
    def get_flags(*args, **kwargs): ...
    def get_location(*args, **kwargs): ...
    def get_newline_type(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_with_target(*args, **kwargs): ...
    def save_async(*args, **kwargs): ...
    def save_finish(*args, **kwargs): ...
    def set_compression_type(*args, **kwargs): ...
    def set_encoding(*args, **kwargs): ...
    def set_flags(*args, **kwargs): ...
    def set_newline_type(*args, **kwargs): ...
    

class Gutter:
    parent = ...
    priv = ...
    
    def get_renderer_at_pos(*args, **kwargs): ...
    def get_view(*args, **kwargs): ...
    def get_window_type(*args, **kwargs): ...
    def insert(*args, **kwargs): ...
    def queue_draw(*args, **kwargs): ...
    def remove(*args, **kwargs): ...
    def reorder(*args, **kwargs): ...
    

class GutterRenderer:
    parent = ...
    priv = ...
    
    def activate(*args, **kwargs): ...
    def begin(*args, **kwargs): ...
    def draw(*args, **kwargs): ...
    def end(*args, **kwargs): ...
    def get_alignment(*args, **kwargs): ...
    def get_alignment_mode(*args, **kwargs): ...
    def get_background(*args, **kwargs): ...
    def get_padding(*args, **kwargs): ...
    def get_size(*args, **kwargs): ...
    def get_view(*args, **kwargs): ...
    def get_visible(*args, **kwargs): ...
    def get_window_type(*args, **kwargs): ...
    def query_activatable(*args, **kwargs): ...
    def query_data(*args, **kwargs): ...
    def query_tooltip(*args, **kwargs): ...
    def queue_draw(*args, **kwargs): ...
    def set_alignment(*args, **kwargs): ...
    def set_alignment_mode(*args, **kwargs): ...
    def set_background(*args, **kwargs): ...
    def set_padding(*args, **kwargs): ...
    def set_size(*args, **kwargs): ...
    def set_visible(*args, **kwargs): ...
    
    def do_activate(self, *args, **kwargs): ...
    def do_begin(self, *args, **kwargs): ...
    def do_change_buffer(self, *args, **kwargs): ...
    def do_change_view(self, *args, **kwargs): ...
    def do_draw(self, *args, **kwargs): ...
    def do_end(self, *args, **kwargs): ...
    def do_query_activatable(self, *args, **kwargs): ...
    def do_query_data(self, *args, **kwargs): ...
    def do_query_tooltip(self, *args, **kwargs): ...
    def do_queue_draw(self, *args, **kwargs): ...
    

class GutterRendererPixbuf:
    def get_gicon(*args, **kwargs): ...
    def get_icon_name(*args, **kwargs): ...
    def get_pixbuf(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_gicon(*args, **kwargs): ...
    def set_icon_name(*args, **kwargs): ...
    def set_pixbuf(*args, **kwargs): ...
    

class GutterRendererText:
    def measure(*args, **kwargs): ...
    def measure_markup(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_markup(*args, **kwargs): ...
    def set_text(*args, **kwargs): ...
    

class Language(GObject.Object):
    parent_instance = ...
    priv = ...
    
    def get_globs(*args, **kwargs): ...
    def get_hidden(*args, **kwargs): ...
    def get_id(*args, **kwargs): ...
    def get_metadata(*args, **kwargs): ...
    def get_mime_types(*args, **kwargs): ...
    def get_name(self) -> str: ...
    def get_section(*args, **kwargs): ...
    def get_style_fallback(*args, **kwargs): ...
    def get_style_ids(*args, **kwargs): ...
    def get_style_name(*args, **kwargs): ...
    

class LanguageManager(GObject.Object):
    parent_instance = ...
    priv = ...
    
    @classmethod
    def get_default(cls) -> LanguageManager: ...
    def get_language(self, id: str) -> Optional[Language]: ...
    def get_language_ids(*args, **kwargs): ...
    def get_search_path(*args, **kwargs): ...
    def guess_language(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_search_path(*args, **kwargs): ...
    

class Map:
    def get_view(*args, **kwargs): ...
    def set_view(*args, **kwargs): ...
    

class Mark:
    priv = ...
    
    def get_category(*args, **kwargs): ...
    def next(*args, **kwargs): ...
    def prev(*args, **kwargs): ...
    

class MarkAttributes:
    parent = ...
    priv = ...
    
    def get_background(*args, **kwargs): ...
    def get_gicon(*args, **kwargs): ...
    def get_icon_name(*args, **kwargs): ...
    def get_pixbuf(*args, **kwargs): ...
    def get_tooltip_markup(*args, **kwargs): ...
    def get_tooltip_text(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def render_icon(*args, **kwargs): ...
    def set_background(*args, **kwargs): ...
    def set_gicon(*args, **kwargs): ...
    def set_icon_name(*args, **kwargs): ...
    def set_pixbuf(*args, **kwargs): ...
    

class PrintCompositor:
    parent_instance = ...
    priv = ...
    
    def draw_page(*args, **kwargs): ...
    def get_body_font_name(*args, **kwargs): ...
    def get_bottom_margin(*args, **kwargs): ...
    def get_buffer(*args, **kwargs): ...
    def get_footer_font_name(*args, **kwargs): ...
    def get_header_font_name(*args, **kwargs): ...
    def get_highlight_syntax(*args, **kwargs): ...
    def get_left_margin(*args, **kwargs): ...
    def get_line_numbers_font_name(*args, **kwargs): ...
    def get_n_pages(*args, **kwargs): ...
    def get_pagination_progress(*args, **kwargs): ...
    def get_print_footer(*args, **kwargs): ...
    def get_print_header(*args, **kwargs): ...
    def get_print_line_numbers(*args, **kwargs): ...
    def get_right_margin(*args, **kwargs): ...
    def get_tab_width(*args, **kwargs): ...
    def get_top_margin(*args, **kwargs): ...
    def get_wrap_mode(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_from_view(*args, **kwargs): ...
    def paginate(*args, **kwargs): ...
    def set_body_font_name(*args, **kwargs): ...
    def set_bottom_margin(*args, **kwargs): ...
    def set_footer_font_name(*args, **kwargs): ...
    def set_footer_format(*args, **kwargs): ...
    def set_header_font_name(*args, **kwargs): ...
    def set_header_format(*args, **kwargs): ...
    def set_highlight_syntax(*args, **kwargs): ...
    def set_left_margin(*args, **kwargs): ...
    def set_line_numbers_font_name(*args, **kwargs): ...
    def set_print_footer(*args, **kwargs): ...
    def set_print_header(*args, **kwargs): ...
    def set_print_line_numbers(*args, **kwargs): ...
    def set_right_margin(*args, **kwargs): ...
    def set_tab_width(*args, **kwargs): ...
    def set_top_margin(*args, **kwargs): ...
    def set_wrap_mode(*args, **kwargs): ...
    

class Region:
    parent_instance = ...
    
    def add_region(*args, **kwargs): ...
    def add_subregion(*args, **kwargs): ...
    def get_bounds(*args, **kwargs): ...
    def get_buffer(*args, **kwargs): ...
    def get_start_region_iter(*args, **kwargs): ...
    def intersect_region(*args, **kwargs): ...
    def intersect_subregion(*args, **kwargs): ...
    def is_empty(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def subtract_region(*args, **kwargs): ...
    def subtract_subregion(*args, **kwargs): ...
    def to_string(*args, **kwargs): ...
    

class RegionIter:
    dummy1 = ...
    dummy2 = ...
    dummy3 = ...
    
    def get_subregion(*args, **kwargs): ...
    def is_end(*args, **kwargs): ...
    def next(*args, **kwargs): ...
    

class SearchContext:
    parent = ...
    priv = ...
    
    def backward(*args, **kwargs): ...
    def backward_async(*args, **kwargs): ...
    def backward_finish(*args, **kwargs): ...
    def forward(*args, **kwargs): ...
    def forward_async(*args, **kwargs): ...
    def forward_finish(*args, **kwargs): ...
    def get_buffer(*args, **kwargs): ...
    def get_highlight(*args, **kwargs): ...
    def get_match_style(*args, **kwargs): ...
    def get_occurrence_position(*args, **kwargs): ...
    def get_occurrences_count(*args, **kwargs): ...
    def get_regex_error(*args, **kwargs): ...
    def get_settings(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def replace(*args, **kwargs): ...
    def replace_all(*args, **kwargs): ...
    def set_highlight(*args, **kwargs): ...
    def set_match_style(*args, **kwargs): ...
    

class SearchSettings:
    parent = ...
    priv = ...
    
    def get_at_word_boundaries(*args, **kwargs): ...
    def get_case_sensitive(*args, **kwargs): ...
    def get_regex_enabled(*args, **kwargs): ...
    def get_search_text(*args, **kwargs): ...
    def get_wrap_around(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_at_word_boundaries(*args, **kwargs): ...
    def set_case_sensitive(*args, **kwargs): ...
    def set_regex_enabled(*args, **kwargs): ...
    def set_search_text(*args, **kwargs): ...
    def set_wrap_around(*args, **kwargs): ...
    

class SpaceDrawer:
    parent = ...
    priv = ...
    
    def bind_matrix_setting(*args, **kwargs): ...
    def get_enable_matrix(*args, **kwargs): ...
    def get_matrix(*args, **kwargs): ...
    def get_types_for_locations(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_enable_matrix(*args, **kwargs): ...
    def set_matrix(*args, **kwargs): ...
    def set_types_for_locations(*args, **kwargs): ...
    

class Style:
    def apply(*args, **kwargs): ...
    def copy(*args, **kwargs): ...


class StyleScheme(GObject.Object):
    base = ...
    priv = ...
    
    def get_authors(*args, **kwargs): ...
    def get_description(*args, **kwargs): ...
    def get_filename(*args, **kwargs): ...
    def get_id(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_style(*args, **kwargs): ...
    

class StyleSchemeChooser:
    def get_style_scheme(*args, **kwargs): ...
    def set_style_scheme(*args, **kwargs): ...
    

class StyleSchemeChooserButton:
    parent = ...
    

class StyleSchemeChooserInterface:
    base_interface = ...
    get_style_scheme = ...
    padding = ...
    set_style_scheme = ...
    

class StyleSchemeChooserWidget:
    parent = ...
    
    def new(*args, **kwargs): ...
    

class StyleSchemeManager(GObject.Object):
    parent = ...
    priv = ...
    
    def append_search_path(*args, **kwargs): ...
    def force_rescan(*args, **kwargs): ...
    @classmethod
    def get_default(cls) -> StyleSchemeManager: ...
    def get_scheme(self, scheme_id: str) -> Optional[StyleScheme]: ...
    def get_scheme_ids(*args, **kwargs): ...
    def get_search_path(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def prepend_search_path(*args, **kwargs): ...
    def set_search_path(*args, **kwargs): ...
    

class Tag: ...

class UndoManager:
    def begin_not_undoable_action(*args, **kwargs): ...
    def can_redo(*args, **kwargs): ...
    def can_redo_changed(*args, **kwargs): ...
    def can_undo(*args, **kwargs): ...
    def can_undo_changed(*args, **kwargs): ...
    def end_not_undoable_action(*args, **kwargs): ...
    def redo(*args, **kwargs): ...
    def undo(*args, **kwargs): ...
    

class View(Gtk.TextView):
    parent = ...
    
    def get_auto_indent(*args, **kwargs): ...
    def get_buffer(self) -> Buffer: ...
    def get_background_pattern(*args, **kwargs): ...
    def get_completion(*args, **kwargs): ...
    def get_gutter(*args, **kwargs): ...
    def get_highlight_current_line(*args, **kwargs): ...
    def get_indent_on_tab(*args, **kwargs): ...
    def get_indent_width(*args, **kwargs): ...
    def get_insert_spaces_instead_of_tabs(*args, **kwargs): ...
    def get_mark_attributes(*args, **kwargs): ...
    def get_right_margin_position(*args, **kwargs): ...
    def get_show_line_marks(*args, **kwargs): ...
    def get_show_right_margin(*args, **kwargs): ...
    def get_smart_backspace(*args, **kwargs): ...
    def get_smart_home_end(*args, **kwargs): ...
    def get_space_drawer(*args, **kwargs): ...
    def get_tab_width(*args, **kwargs): ...
    def get_visual_column(*args, **kwargs): ...
    def indent_lines(*args, **kwargs): ...
    def set_auto_indent(*args, **kwargs): ...
    def set_background_pattern(*args, **kwargs): ...
    def set_highlight_current_line(*args, **kwargs): ...
    def set_indent_on_tab(*args, **kwargs): ...
    def set_indent_width(*args, **kwargs): ...
    def set_insert_spaces_instead_of_tabs(*args, **kwargs): ...
    def set_mark_attributes(*args, **kwargs): ...
    def set_right_margin_position(*args, **kwargs): ...
    def set_show_line_marks(*args, **kwargs): ...
    def set_show_line_numbers(self, show: bool) -> None: ...
    def set_show_right_margin(*args, **kwargs): ...
    def set_smart_backspace(*args, **kwargs): ...
    def set_smart_home_end(*args, **kwargs): ...
    def set_tab_width(*args, **kwargs): ...
    def unindent_lines(*args, **kwargs): ...
    
    def do_line_mark_activated(self, *args, **kwargs): ...
    def do_move_lines(self, *args, **kwargs): ...
    def do_move_words(self, *args, **kwargs): ...
    def do_redo(self, *args, **kwargs): ...
    def do_show_completion(self, *args, **kwargs): ...
    def do_undo(self, *args, **kwargs): ...
    

class CompletionActivation(GObject.GFlags):
    NONE = ...
    INTERACTIVE = ...
    USER_REQUESTED = ...

class FileSaverFlags(GObject.GFlags):
    NONE = ...
    IGNORE_INVALID_CHARS = ...
    IGNORE_MODIFICATION_TIME = ...
    CREATE_BACKUP = ...

class GutterRendererState(GObject.GFlags):
    NORMAL = ...
    CURSOR = ...
    PRELIT = ...
    SELECTED = ...

class SortFlags(GObject.GFlags):
    NONE = ...
    CASE_SENSITIVE = ...
    REVERSE_ORDER = ...
    REMOVE_DUPLICATES = ...

class SpaceLocationFlags(GObject.GFlags):
    NONE = ...
    LEADING = ...
    INSIDE_TEXT = ...
    TRAILING = ...
    ALL = ...

class SpaceTypeFlags(GObject.GFlags):
    NONE = ...
    SPACE = ...
    TAB = ...
    NEWLINE = ...
    NBSP = ...
    ALL = ...

class BackgroundPatternType(GObject.GEnum):
    NONE = ...
    GRID = ...

class BracketMatchType(GObject.GEnum):
    NONE = ...
    OUT_OF_RANGE = ...
    NOT_FOUND = ...
    FOUND = ...

class ChangeCaseType(GObject.GEnum):
    LOWER = ...
    UPPER = ...
    TOGGLE = ...
    TITLE = ...

class CompletionError(GObject.GEnum):
    ALREADY_BOUND = ...
    NOT_BOUND = ...
    quark = ...

class CompressionType(GObject.GEnum):
    NONE = ...
    GZIP = ...

class FileLoaderError(GObject.GEnum):
    TOO_BIG = ...
    ENCODING_AUTO_DETECTION_FAILED = ...
    CONVERSION_FALLBACK = ...
    quark = ...

class FileSaverError(GObject.GEnum):
    INVALID_CHARS = ...
    EXTERNALLY_MODIFIED = ...
    quark = ...

class GutterRendererAlignmentMode(GObject.GEnum):
    CELL = ...
    FIRST = ...
    LAST = ...

class NewlineType(GObject.GEnum):
    LF = ...
    CR = ...
    CR_LF = ...

class SmartHomeEndType(GObject.GEnum):
    DISABLED = ...
    BEFORE = ...
    AFTER = ...
    ALWAYS = ...

class ViewGutterPosition(GObject.GEnum):
    LINES = ...
    MARKS = ...
