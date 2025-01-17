import typing

from gi.repository import GLib
from gi.repository import GObject
T = typing.TypeVar("T")

ALLOCATOR_SYSMEM: str = "SystemMemory"
BUFFER_COPY_ALL: int = 0
BUFFER_COPY_METADATA: int = 0
BUFFER_OFFSET_NONE: int = 18446744073709551615
CAN_INLINE: int = 1
CAPS_FEATURE_MEMORY_SYSTEM_MEMORY: str = "memory:SystemMemory"
CLOCK_TIME_NONE: int = 18446744073709551615
DEBUG_BG_MASK: int = 240
DEBUG_FG_MASK: int = 15
DEBUG_FORMAT_MASK: int = 65280
ELEMENT_FACTORY_KLASS_DECODER: str = "Decoder"
ELEMENT_FACTORY_KLASS_DECRYPTOR: str = "Decryptor"
ELEMENT_FACTORY_KLASS_DEMUXER: str = "Demuxer"
ELEMENT_FACTORY_KLASS_DEPAYLOADER: str = "Depayloader"
ELEMENT_FACTORY_KLASS_ENCODER: str = "Encoder"
ELEMENT_FACTORY_KLASS_ENCRYPTOR: str = "Encryptor"
ELEMENT_FACTORY_KLASS_FORMATTER: str = "Formatter"
ELEMENT_FACTORY_KLASS_HARDWARE: str = "Hardware"
ELEMENT_FACTORY_KLASS_MEDIA_AUDIO: str = "Audio"
ELEMENT_FACTORY_KLASS_MEDIA_IMAGE: str = "Image"
ELEMENT_FACTORY_KLASS_MEDIA_METADATA: str = "Metadata"
ELEMENT_FACTORY_KLASS_MEDIA_SUBTITLE: str = "Subtitle"
ELEMENT_FACTORY_KLASS_MEDIA_VIDEO: str = "Video"
ELEMENT_FACTORY_KLASS_MUXER: str = "Muxer"
ELEMENT_FACTORY_KLASS_PARSER: str = "Parser"
ELEMENT_FACTORY_KLASS_PAYLOADER: str = "Payloader"
ELEMENT_FACTORY_KLASS_SINK: str = "Sink"
ELEMENT_FACTORY_KLASS_SRC: str = "Source"
ELEMENT_FACTORY_TYPE_ANY: int = 562949953421311
ELEMENT_FACTORY_TYPE_AUDIOVIDEO_SINKS: int = 3940649673949188
ELEMENT_FACTORY_TYPE_AUDIO_ENCODER: int = 1125899906842626
ELEMENT_FACTORY_TYPE_DECODABLE: int = 1377
ELEMENT_FACTORY_TYPE_DECODER: int = 1
ELEMENT_FACTORY_TYPE_DECRYPTOR: int = 1024
ELEMENT_FACTORY_TYPE_DEMUXER: int = 32
ELEMENT_FACTORY_TYPE_DEPAYLOADER: int = 256
ELEMENT_FACTORY_TYPE_ENCODER: int = 2
ELEMENT_FACTORY_TYPE_ENCRYPTOR: int = 2048
ELEMENT_FACTORY_TYPE_FORMATTER: int = 512
ELEMENT_FACTORY_TYPE_HARDWARE: int = 4096
ELEMENT_FACTORY_TYPE_MAX_ELEMENTS: int = 281474976710656
ELEMENT_FACTORY_TYPE_MEDIA_ANY: int = 18446462598732840960
ELEMENT_FACTORY_TYPE_MEDIA_AUDIO: int = 1125899906842624
ELEMENT_FACTORY_TYPE_MEDIA_IMAGE: int = 2251799813685248
ELEMENT_FACTORY_TYPE_MEDIA_METADATA: int = 9007199254740992
ELEMENT_FACTORY_TYPE_MEDIA_SUBTITLE: int = 4503599627370496
ELEMENT_FACTORY_TYPE_MEDIA_VIDEO: int = 562949953421312
ELEMENT_FACTORY_TYPE_MUXER: int = 16
ELEMENT_FACTORY_TYPE_PARSER: int = 64
ELEMENT_FACTORY_TYPE_PAYLOADER: int = 128
ELEMENT_FACTORY_TYPE_SINK: int = 4
ELEMENT_FACTORY_TYPE_SRC: int = 8
ELEMENT_FACTORY_TYPE_TIMESTAMPER: int = 8192
ELEMENT_FACTORY_TYPE_VIDEO_ENCODER: int = 2814749767106562
ELEMENT_METADATA_AUTHOR: str = "author"
ELEMENT_METADATA_DESCRIPTION: str = "description"
ELEMENT_METADATA_DOC_URI: str = "doc-uri"
ELEMENT_METADATA_ICON_NAME: str = "icon-name"
ELEMENT_METADATA_KLASS: str = "klass"
ELEMENT_METADATA_LONGNAME: str = "long-name"
EVENT_NUM_SHIFT: int = 8
EVENT_TYPE_BOTH: int = 0
FLAG_SET_MASK_EXACT: int = 4294967295
FORMAT_PERCENT_MAX: int = 1000000
FORMAT_PERCENT_SCALE: int = 10000
GROUP_ID_INVALID: int = 0
LICENSE_UNKNOWN: str = "unknown"
LOCK_FLAG_READWRITE: int = 0
MAP_READWRITE: int = 0
META_TAG_MEMORY_REFERENCE_STR: str = "memory-reference"
META_TAG_MEMORY_STR: str = "memory"
MSECOND: int = 1000000
NSECOND: int = 1
PARAM_CONDITIONALLY_AVAILABLE: int = 16384
PARAM_CONTROLLABLE: int = 512
PARAM_DOC_SHOW_DEFAULT: int = 8192
PARAM_MUTABLE_PAUSED: int = 2048
PARAM_MUTABLE_PLAYING: int = 4096
PARAM_MUTABLE_READY: int = 1024
PARAM_USER_SHIFT: int = 65536
PROTECTION_SYSTEM_ID_CAPS_FIELD: str = "protection-system"
PROTECTION_UNSPECIFIED_SYSTEM_ID: str = "unspecified-system-id"
QUERY_NUM_SHIFT: int = 8
QUERY_TYPE_BOTH: int = 0
SECOND: int = 1000000000
SEGMENT_INSTANT_FLAGS: int = 912
SEQNUM_INVALID: int = 0
TAG_ALBUM: str = "album"
TAG_ALBUM_ARTIST: str = "album-artist"
TAG_ALBUM_ARTIST_SORTNAME: str = "album-artist-sortname"
TAG_ALBUM_GAIN: str = "replaygain-album-gain"
TAG_ALBUM_PEAK: str = "replaygain-album-peak"
TAG_ALBUM_SORTNAME: str = "album-sortname"
TAG_ALBUM_VOLUME_COUNT: str = "album-disc-count"
TAG_ALBUM_VOLUME_NUMBER: str = "album-disc-number"
TAG_APPLICATION_DATA: str = "application-data"
TAG_APPLICATION_NAME: str = "application-name"
TAG_ARTIST: str = "artist"
TAG_ARTIST_SORTNAME: str = "artist-sortname"
TAG_ATTACHMENT: str = "attachment"
TAG_AUDIO_CODEC: str = "audio-codec"
TAG_BEATS_PER_MINUTE: str = "beats-per-minute"
TAG_BITRATE: str = "bitrate"
TAG_CODEC: str = "codec"
TAG_COMMENT: str = "comment"
TAG_COMPOSER: str = "composer"
TAG_COMPOSER_SORTNAME: str = "composer-sortname"
TAG_CONDUCTOR: str = "conductor"
TAG_CONTACT: str = "contact"
TAG_CONTAINER_FORMAT: str = "container-format"
TAG_CONTAINER_SPECIFIC_TRACK_ID: str = "container-specific-track-id"
TAG_COPYRIGHT: str = "copyright"
TAG_COPYRIGHT_URI: str = "copyright-uri"
TAG_DATE: str = "date"
TAG_DATE_TIME: str = "datetime"
TAG_DESCRIPTION: str = "description"
TAG_DEVICE_MANUFACTURER: str = "device-manufacturer"
TAG_DEVICE_MODEL: str = "device-model"
TAG_DURATION: str = "duration"
TAG_ENCODED_BY: str = "encoded-by"
TAG_ENCODER: str = "encoder"
TAG_ENCODER_VERSION: str = "encoder-version"
TAG_EXTENDED_COMMENT: str = "extended-comment"
TAG_GENRE: str = "genre"
TAG_GEO_LOCATION_CAPTURE_DIRECTION: str = "geo-location-capture-direction"
TAG_GEO_LOCATION_CITY: str = "geo-location-city"
TAG_GEO_LOCATION_COUNTRY: str = "geo-location-country"
TAG_GEO_LOCATION_ELEVATION: str = "geo-location-elevation"
TAG_GEO_LOCATION_HORIZONTAL_ERROR: str = "geo-location-horizontal-error"
TAG_GEO_LOCATION_LATITUDE: str = "geo-location-latitude"
TAG_GEO_LOCATION_LONGITUDE: str = "geo-location-longitude"
TAG_GEO_LOCATION_MOVEMENT_DIRECTION: str = "geo-location-movement-direction"
TAG_GEO_LOCATION_MOVEMENT_SPEED: str = "geo-location-movement-speed"
TAG_GEO_LOCATION_NAME: str = "geo-location-name"
TAG_GEO_LOCATION_SUBLOCATION: str = "geo-location-sublocation"
TAG_GROUPING: str = "grouping"
TAG_HOMEPAGE: str = "homepage"
TAG_IMAGE: str = "image"
TAG_IMAGE_ORIENTATION: str = "image-orientation"
TAG_INTERPRETED_BY: str = "interpreted-by"
TAG_ISRC: str = "isrc"
TAG_KEYWORDS: str = "keywords"
TAG_LANGUAGE_CODE: str = "language-code"
TAG_LANGUAGE_NAME: str = "language-name"
TAG_LICENSE: str = "license"
TAG_LICENSE_URI: str = "license-uri"
TAG_LOCATION: str = "location"
TAG_LYRICS: str = "lyrics"
TAG_MAXIMUM_BITRATE: str = "maximum-bitrate"
TAG_MIDI_BASE_NOTE: str = "midi-base-note"
TAG_MINIMUM_BITRATE: str = "minimum-bitrate"
TAG_NOMINAL_BITRATE: str = "nominal-bitrate"
TAG_ORGANIZATION: str = "organization"
TAG_PERFORMER: str = "performer"
TAG_PREVIEW_IMAGE: str = "preview-image"
TAG_PRIVATE_DATA: str = "private-data"
TAG_PUBLISHER: str = "publisher"
TAG_REFERENCE_LEVEL: str = "replaygain-reference-level"
TAG_SERIAL: str = "serial"
TAG_SHOW_EPISODE_NUMBER: str = "show-episode-number"
TAG_SHOW_NAME: str = "show-name"
TAG_SHOW_SEASON_NUMBER: str = "show-season-number"
TAG_SHOW_SORTNAME: str = "show-sortname"
TAG_SUBTITLE_CODEC: str = "subtitle-codec"
TAG_TITLE: str = "title"
TAG_TITLE_SORTNAME: str = "title-sortname"
TAG_TRACK_COUNT: str = "track-count"
TAG_TRACK_GAIN: str = "replaygain-track-gain"
TAG_TRACK_NUMBER: str = "track-number"
TAG_TRACK_PEAK: str = "replaygain-track-peak"
TAG_USER_RATING: str = "user-rating"
TAG_VERSION: str = "version"
TAG_VIDEO_CODEC: str = "video-codec"
TOC_REPEAT_COUNT_INFINITE: int = -1
URI_NO_PORT: int = 0
USECOND: int = 1000
VALUE_EQUAL: int = 0
VALUE_GREATER_THAN: int = 1
VALUE_LESS_THAN: int = -1
VALUE_UNORDERED: int = 2
VERSION_MAJOR: int = 1
VERSION_MICRO: int = 11
VERSION_MINOR: int = 24
VERSION_NANO: int = 0
_introspection_module = ... # FIXME Constant
_lock = ... # FIXME Constant
_namespace: str = "Gst"
_overrides_module = ... # FIXME Constant
_version: str = "1.0"

def TIME_ARGS(time): ... # FIXME Function
def buffer_get_max_memory(*args): ... # FIXME Function
def buffer_list_replace(*args): ... # FIXME Function
def buffer_list_take(*args): ... # FIXME Function
def caps_features_from_string(*args): ... # FIXME Function
def caps_from_string(*args): ... # FIXME Function
def context_replace(*args): ... # FIXME Function
def core_error_quark(*args): ... # FIXME Function
def debug(*args, **kwargs): ... # FIXME Function
def debug_add_log_function(func: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
def debug_add_ring_buffer_logger(max_size_per_thread: int, thread_timeout: int) -> None: ...
def debug_bin_to_dot_data(*args): ... # FIXME Function
def debug_bin_to_dot_file(*args): ... # FIXME Function
def debug_bin_to_dot_file_with_ts(*args): ... # FIXME Function
def debug_construct_term_color(*args): ... # FIXME Function
def debug_construct_win_color(*args): ... # FIXME Function
def debug_get_all_categories(*args): ... # FIXME Function
def debug_get_color_mode(*args): ... # FIXME Function
def debug_get_default_threshold(*args): ... # FIXME Function
def debug_get_stack_trace(*args): ... # FIXME Function
def debug_is_active(*args): ... # FIXME Function
def debug_is_colored(*args): ... # FIXME Function
def debug_level_get_name(*args): ... # FIXME Function
def debug_log_default(*args): ... # FIXME Function
def debug_log_get_line(*args): ... # FIXME Function
def debug_log_id_literal(*args): ... # FIXME Function
def debug_log_literal(*args): ... # FIXME Function
def debug_print_stack_trace(*args): ... # FIXME Function
def debug_remove_log_function(func: typing.Optional[typing.Callable[..., None]] = None) -> int: ...
def debug_remove_log_function_by_data(data: None) -> int: ...
def debug_remove_ring_buffer_logger() -> None: ...
def debug_ring_buffer_logger_get_logs(*args): ... # FIXME Function
def debug_set_active(active: bool) -> None: ...
def debug_set_color_mode(mode: DebugColorMode) -> None: ...
def debug_set_color_mode_from_string(mode: str) -> None: ...
def debug_set_colored(colored: bool) -> None: ...
def debug_set_default_threshold(level: DebugLevel) -> None: ...
def debug_set_threshold_for_name(*args): ... # FIXME Function
def debug_set_threshold_from_string(*args): ... # FIXME Function
def debug_unset_threshold_for_name(*args): ... # FIXME Function
def deinit(): ... # FIXME Function
def dynamic_type_register(*args): ... # FIXME Function
def error(*args, **kwargs): ... # FIXME Function
def error_get_message(*args): ... # FIXME Function
def event_type_get_flags(*args): ... # FIXME Function
def event_type_get_name(*args): ... # FIXME Function
def event_type_to_quark(*args): ... # FIXME Function
def event_type_to_sticky_ordering(*args): ... # FIXME Function
def filename_to_uri(*args): ... # FIXME Function
def fixme(*args, **kwargs): ... # FIXME Function
def flow_get_name(*args): ... # FIXME Function
def flow_to_quark(*args): ... # FIXME Function
def format_get_by_nick(*args): ... # FIXME Function
def format_get_details(*args): ... # FIXME Function
def format_get_name(*args): ... # FIXME Function
def format_iterate_definitions(*args): ... # FIXME Function
def format_register(*args): ... # FIXME Function
def format_to_quark(*args): ... # FIXME Function
def formats_contains(*args): ... # FIXME Function
def get_main_executable_path(*args): ... # FIXME Function
def info(*args, **kwargs): ... # FIXME Function
# override
def init(argv: Optional[list[str]]=None) -> None:
    ...
# override
def init_check(argv: Optional[list[str]]=None) -> Tuple[bool, list[str]]:
    ...
def init_python(): ... # FIXME Function
def is_caps_features(*args): ... # FIXME Function
def is_initialized() -> bool: ...
def library_error_quark(*args): ... # FIXME Function
def log(*args, **kwargs): ... # FIXME Function
def memdump(*args, **kwargs): ... # FIXME Function
def message_take(*args): ... # FIXME Function
def message_type_get_name(*args): ... # FIXME Function
def message_type_to_quark(*args): ... # FIXME Function
def meta_api_type_get_tags(*args): ... # FIXME Function
def meta_api_type_has_tag(*args): ... # FIXME Function
def meta_api_type_register(*args): ... # FIXME Function
def meta_deserialize(*args): ... # FIXME Function
def meta_get_info(*args): ... # FIXME Function
def meta_register_custom(*args): ... # FIXME Function
def meta_register_custom_simple(*args): ... # FIXME Function
def mini_object_replace(*args): ... # FIXME Function
def mini_object_take(*args): ... # FIXME Function
def pad_mode_get_name(*args): ... # FIXME Function
def param_spec_array(*args): ... # FIXME Function
def param_spec_fraction(*args): ... # FIXME Function
def parent_buffer_meta_api_get_type(*args): ... # FIXME Function
def parent_buffer_meta_get_info(*args): ... # FIXME Function
def parse_bin_from_description(*args): ... # FIXME Function
def parse_bin_from_description_full(*args): ... # FIXME Function
def parse_error_quark(*args): ... # FIXME Function
def parse_launch(*args): ... # FIXME Function
def parse_launch_full(*args): ... # FIXME Function
def parse_launchv(*args): ... # FIXME Function
def parse_launchv_full(*args): ... # FIXME Function
def plugin_error_quark(*args): ... # FIXME Function
def preset_get_app_dir(*args): ... # FIXME Function
def preset_set_app_dir(*args): ... # FIXME Function
def protection_filter_systems_by_available_decryptors(*args): ... # FIXME Function
def protection_meta_api_get_type(*args): ... # FIXME Function
def protection_meta_get_info(*args): ... # FIXME Function
def protection_select_system(*args): ... # FIXME Function
def query_take(*args): ... # FIXME Function
def query_type_get_flags(*args): ... # FIXME Function
def query_type_get_name(*args): ... # FIXME Function
def query_type_to_quark(*args): ... # FIXME Function
def reference_timestamp_meta_api_get_type(*args): ... # FIXME Function
def reference_timestamp_meta_get_info(*args): ... # FIXME Function
def resource_error_quark(*args): ... # FIXME Function
def segtrap_is_enabled(*args): ... # FIXME Function
def segtrap_set_enabled(*args): ... # FIXME Function
def state_change_get_name(*args): ... # FIXME Function
def static_caps_get_type(*args): ... # FIXME Function
def static_pad_template_get_type(*args): ... # FIXME Function
def stream_error_quark(*args): ... # FIXME Function
def stream_type_get_name(*args): ... # FIXME Function
def structure_take(*args): ... # FIXME Function
def tag_exists(*args): ... # FIXME Function
def tag_get_description(*args): ... # FIXME Function
def tag_get_flag(*args): ... # FIXME Function
def tag_get_nick(*args): ... # FIXME Function
def tag_get_type(*args): ... # FIXME Function
def tag_is_fixed(*args): ... # FIXME Function
def tag_list_copy_value(*args): ... # FIXME Function
def tag_list_replace(*args): ... # FIXME Function
def tag_list_take(*args): ... # FIXME Function
def tag_merge_strings_with_comma(*args): ... # FIXME Function
def tag_merge_use_first(*args): ... # FIXME Function
def toc_entry_type_get_nick(*args): ... # FIXME Function
def trace(*args, **kwargs): ... # FIXME Function
def tracing_get_active_tracers(*args): ... # FIXME Function
def tracing_register_hook(*args): ... # FIXME Function
def type_find_get_type(*args): ... # FIXME Function
def type_find_register(*args): ... # FIXME Function
def type_is_plugin_api(*args): ... # FIXME Function
def type_mark_as_plugin_api(*args): ... # FIXME Function
def update_registry(*args): ... # FIXME Function
def uri_construct(*args): ... # FIXME Function
def uri_error_quark(*args): ... # FIXME Function
def uri_from_string(*args): ... # FIXME Function
def uri_from_string_escaped(*args): ... # FIXME Function
def uri_get_location(*args): ... # FIXME Function
def uri_get_protocol(*args): ... # FIXME Function
def uri_has_protocol(*args): ... # FIXME Function
def uri_is_valid(*args): ... # FIXME Function
def uri_join_strings(*args): ... # FIXME Function
def uri_protocol_is_supported(*args): ... # FIXME Function
def uri_protocol_is_valid(*args): ... # FIXME Function
def util_array_binary_search(*args): ... # FIXME Function
def util_ceil_log2(*args): ... # FIXME Function
def util_double_to_fraction(*args): ... # FIXME Function
def util_dump_buffer(*args): ... # FIXME Function
def util_dump_mem(*args): ... # FIXME Function
def util_filename_compare(*args): ... # FIXME Function
def util_fraction_add(*args): ... # FIXME Function
def util_fraction_compare(*args): ... # FIXME Function
def util_fraction_multiply(*args): ... # FIXME Function
def util_fraction_to_double(*args): ... # FIXME Function
def util_gdouble_to_guint64(*args): ... # FIXME Function
def util_get_object_array(*args): ... # FIXME Function
def util_get_timestamp(*args): ... # FIXME Function
def util_greatest_common_divisor(*args): ... # FIXME Function
def util_greatest_common_divisor_int64(*args): ... # FIXME Function
def util_group_id_next(*args): ... # FIXME Function
def util_guint64_to_gdouble(*args): ... # FIXME Function
def util_seqnum_compare(*args): ... # FIXME Function
def util_seqnum_next(*args): ... # FIXME Function
def util_set_object_arg(*args): ... # FIXME Function
def util_set_object_array(*args): ... # FIXME Function
def util_set_value_from_string(*args): ... # FIXME Function
def util_simplify_fraction(*args): ... # FIXME Function
def util_uint64_scale(*args): ... # FIXME Function
def util_uint64_scale_ceil(*args): ... # FIXME Function
def util_uint64_scale_int(*args): ... # FIXME Function
def util_uint64_scale_int_ceil(*args): ... # FIXME Function
def util_uint64_scale_int_round(*args): ... # FIXME Function
def util_uint64_scale_round(*args): ... # FIXME Function
def value_can_compare(*args): ... # FIXME Function
def value_can_intersect(*args): ... # FIXME Function
def value_can_subtract(*args): ... # FIXME Function
def value_can_union(*args): ... # FIXME Function
def value_compare(*args): ... # FIXME Function
def value_deserialize(*args): ... # FIXME Function
def value_deserialize_with_pspec(*args): ... # FIXME Function
def value_fixate(*args): ... # FIXME Function
def value_fraction_multiply(*args): ... # FIXME Function
def value_fraction_subtract(*args): ... # FIXME Function
def value_get_bitmask(*args): ... # FIXME Function
def value_get_caps(*args): ... # FIXME Function
def value_get_caps_features(*args): ... # FIXME Function
def value_get_double_range_max(*args): ... # FIXME Function
def value_get_double_range_min(*args): ... # FIXME Function
def value_get_flagset_flags(*args): ... # FIXME Function
def value_get_flagset_mask(*args): ... # FIXME Function
def value_get_fraction_denominator(*args): ... # FIXME Function
def value_get_fraction_numerator(*args): ... # FIXME Function
def value_get_fraction_range_max(*args): ... # FIXME Function
def value_get_fraction_range_min(*args): ... # FIXME Function
def value_get_int64_range_max(*args): ... # FIXME Function
def value_get_int64_range_min(*args): ... # FIXME Function
def value_get_int64_range_step(*args): ... # FIXME Function
def value_get_int_range_max(*args): ... # FIXME Function
def value_get_int_range_min(*args): ... # FIXME Function
def value_get_int_range_step(*args): ... # FIXME Function
def value_get_structure(*args): ... # FIXME Function
def value_init_and_copy(*args): ... # FIXME Function
def value_intersect(*args): ... # FIXME Function
def value_is_fixed(*args): ... # FIXME Function
def value_is_subset(*args): ... # FIXME Function
def value_register(*args): ... # FIXME Function
def value_serialize(*args): ... # FIXME Function
def value_set_bitmask(*args): ... # FIXME Function
def value_set_caps(*args): ... # FIXME Function
def value_set_caps_features(*args): ... # FIXME Function
def value_set_double_range(*args): ... # FIXME Function
def value_set_flagset(*args): ... # FIXME Function
def value_set_fraction(*args): ... # FIXME Function
def value_set_fraction_range(*args): ... # FIXME Function
def value_set_fraction_range_full(*args): ... # FIXME Function
def value_set_int64_range(*args): ... # FIXME Function
def value_set_int64_range_step(*args): ... # FIXME Function
def value_set_int_range(*args): ... # FIXME Function
def value_set_int_range_step(*args): ... # FIXME Function
def value_set_structure(*args): ... # FIXME Function
def value_subtract(*args): ... # FIXME Function
def value_union(*args): ... # FIXME Function
def version(*args): ... # FIXME Function
def version_string(*args): ... # FIXME Function
def warning(*args, **kwargs): ... # FIXME Function

class AddError:
    args = ... # FIXME Constant
    
    def add_note(self, *args, **kwargs): ... # FIXME Function
    def with_traceback(self, *args, **kwargs): ... # FIXME Function
    

class AllocationParams(GObject.GBoxed):
    """
    :Constructors:

    ::

        AllocationParams()
        new() -> Gst.AllocationParams
    """
    flags: MemoryFlags = ...
    align: int = ...
    prefix: int = ...
    padding: int = ...
    _gst_reserved: list[None] = ...
    def copy(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def init(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    

class Allocator(Object):
    """
    :Constructors:

    ::

        Allocator(**properties)

    Object GstAllocator

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    mem_type: str = ...
    mem_map: typing.Callable[[Memory, int, MapFlags], None] = ...
    mem_unmap: typing.Callable[[Memory], None] = ...
    mem_copy: typing.Callable[[Memory, int, int], Memory] = ...
    mem_share: typing.Callable[[Memory, int, int], Memory] = ...
    mem_is_span: typing.Callable[[Memory, Memory, int], bool] = ...
    mem_map_full: typing.Callable[[Memory, MapInfo, int], None] = ...
    mem_unmap_full: typing.Callable[[Memory, MapInfo], None] = ...
    _gst_reserved: list[None] = ...
    priv: AllocatorPrivate = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def alloc(*args): ... # FIXME Function
    def do_alloc(self, size: int, params: typing.Optional[AllocationParams] = None) -> typing.Optional[Memory]: ...
    def do_free(self, memory: Memory) -> None: ...
    def find(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def register(*args): ... # FIXME Function
    def set_default(*args): ... # FIXME Function
    

class AllocatorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AllocatorClass()
    """
    object_class: ObjectClass = ...
    alloc: typing.Callable[[typing.Optional[Allocator], int, typing.Optional[AllocationParams]], typing.Optional[Memory]] = ...
    free: typing.Callable[[Allocator, Memory], None] = ...
    _gst_reserved: list[None] = ...

class AllocatorPrivate(GObject.GPointer): ...

class AtomicQueue(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(initial_size:int) -> Gst.AtomicQueue
    """
    def length(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def peek(*args): ... # FIXME Function
    def pop(*args): ... # FIXME Function
    def push(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def unref(*args): ... # FIXME Function
    

class Bin(Element, ChildProxy):
    """
    :Constructors:

    ::

        Bin(**properties)
        new(name:str=None) -> Gst.Element

    Object GstBin

    Signals from GstBin:
      element-added (GstElement)
      element-removed (GstElement)
      deep-element-added (GstBin, GstElement)
      deep-element-removed (GstBin, GstElement)
      do-latency () -> gboolean

    Properties from GstBin:
      async-handling -> gboolean: Async Handling
        The bin will handle Asynchronous state changes
      message-forward -> gboolean: Message Forward
        Forwards all children messages

    Signals from GstChildProxy:
      child-added (GObject, gchararray)
      child-removed (GObject, gchararray)

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        async_handling: bool
        message_forward: bool
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    element: Element = ...
    numchildren: int = ...
    children: list[Element] = ...
    children_cookie: int = ...
    child_bus: Bus = ...
    messages: list[Message] = ...
    polling: bool = ...
    state_dirty: bool = ...
    clock_dirty: bool = ...
    provided_clock: Clock = ...
    clock_provider: Element = ...
    priv: BinPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, async_handling: bool = ...,
                 message_forward: bool = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add(self, *args): ... # FIXME Function
    def do_add_element(self, element: Element) -> bool: ...
    def do_deep_element_added(self, sub_bin: Bin, child: Element) -> None: ...
    def do_deep_element_removed(self, sub_bin: Bin, child: Element) -> None: ...
    def do_do_latency(self) -> bool: ...
    def do_element_added(self, child: Element) -> None: ...
    def do_element_removed(self, child: Element) -> None: ...
    def do_handle_message(self, message: Message) -> None: ...
    def do_remove_element(self, element: Element) -> bool: ...
    def find_unlinked_pad(*args): ... # FIXME Function
    def get_by_interface(*args): ... # FIXME Function
    def get_by_name(*args): ... # FIXME Function
    def get_by_name_recurse_up(*args): ... # FIXME Function
    def get_suppressed_flags(*args): ... # FIXME Function
    def iterate_all_by_element_factory_name(*args): ... # FIXME Function
    def iterate_all_by_interface(*args): ... # FIXME Function
    def iterate_elements(*args): ... # FIXME Function
    def iterate_recurse(*args): ... # FIXME Function
    def iterate_sinks(*args): ... # FIXME Function
    def iterate_sorted(*args): ... # FIXME Function
    def iterate_sources(*args): ... # FIXME Function
    def make_and_add(self, factoryname, name=None): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def recalculate_latency(*args): ... # FIXME Function
    def remove(*args): ... # FIXME Function
    def set_suppressed_flags(*args): ... # FIXME Function
    def sync_children_states(*args): ... # FIXME Function
    

class BinClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BinClass()
    """
    parent_class: ElementClass = ...
    pool: GLib.ThreadPool = ...
    element_added: typing.Callable[[Bin, Element], None] = ...
    element_removed: typing.Callable[[Bin, Element], None] = ...
    add_element: typing.Callable[[Bin, Element], bool] = ...
    remove_element: typing.Callable[[Bin, Element], bool] = ...
    handle_message: typing.Callable[[Bin, Message], None] = ...
    do_latency: typing.Callable[[Bin], bool] = ...
    deep_element_added: typing.Callable[[Bin, Bin, Element], None] = ...
    deep_element_removed: typing.Callable[[Bin, Bin, Element], None] = ...
    _gst_reserved: list[None] = ...

class BinPrivate(GObject.GPointer): ...

class Bitmask: ...

class Buffer(GObject.GBoxed):
    """
    :Constructors:

    ::

        Buffer()
        new() -> Gst.Buffer
        new_allocate(allocator:Gst.Allocator=None, size:int, params:Gst.AllocationParams=None) -> Gst.Buffer or None
        new_memdup(data:list) -> Gst.Buffer
        new_wrapped(data:list) -> Gst.Buffer
        new_wrapped_bytes(bytes:GLib.Bytes) -> Gst.Buffer
        new_wrapped_full(flags:Gst.MemoryFlags, data:list, maxsize:int, offset:int, user_data=None, notify:GLib.DestroyNotify=None) -> Gst.Buffer
    """
    mini_object: MiniObject = ...
    pool: BufferPool = ...
    pts: int = ...
    dts: int = ...
    duration: int = ...
    offset: int = ...
    offset_end: int = ...
    def add_custom_meta(*args): ... # FIXME Function
    def add_meta(*args): ... # FIXME Function
    def add_parent_buffer_meta(*args): ... # FIXME Function
    def add_protection_meta(*args): ... # FIXME Function
    def add_reference_timestamp_meta(*args): ... # FIXME Function
    def append(*args): ... # FIXME Function
    def append_memory(*args): ... # FIXME Function
    def append_region(*args): ... # FIXME Function
    def copy_deep(*args): ... # FIXME Function
    def copy_into(*args): ... # FIXME Function
    def copy_region(*args): ... # FIXME Function
    def extract(*args): ... # FIXME Function
    def extract_dup(*args): ... # FIXME Function
    def fill(*args): ... # FIXME Function
    def find_memory(*args): ... # FIXME Function
    def foreach_meta(*args): ... # FIXME Function
    def get_all_memory(*args): ... # FIXME Function
    def get_custom_meta(*args): ... # FIXME Function
    def get_flags(*args): ... # FIXME Function
    def get_max_memory(*args): ... # FIXME Function
    def get_memory(*args): ... # FIXME Function
    def get_memory_range(*args): ... # FIXME Function
    def get_meta(*args): ... # FIXME Function
    def get_n_meta(*args): ... # FIXME Function
    def get_reference_timestamp_meta(*args): ... # FIXME Function
    def get_size(*args): ... # FIXME Function
    def get_sizes(*args): ... # FIXME Function
    def get_sizes_range(*args): ... # FIXME Function
    def has_flags(*args): ... # FIXME Function
    def insert_memory(*args): ... # FIXME Function
    def is_all_memory_writable(*args): ... # FIXME Function
    def is_memory_range_writable(*args): ... # FIXME Function
    def map(self, flags): ... # FIXME Function
    def map_range(self, idx, length, flags): ... # FIXME Function
    def memcmp(*args): ... # FIXME Function
    def memset(*args): ... # FIXME Function
    def n_memory(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_allocate(*args): ... # FIXME Function
    def new_memdup(*args): ... # FIXME Function
    def new_wrapped(*args): ... # FIXME Function
    def new_wrapped_bytes(*args): ... # FIXME Function
    # override
    @classmethod
    def new_wrapped_full(cls, flags: MemoryFlags, data: Sequence[int], maxsize: int, offset: int, user_data: None, notify: Optional[Callable[[None], None]]=None, *_user_data: Any) -> Buffer:
        ...
    def peek_memory(*args): ... # FIXME Function
    def prepend_memory(*args): ... # FIXME Function
    def remove_all_memory(*args): ... # FIXME Function
    def remove_memory(*args): ... # FIXME Function
    def remove_memory_range(*args): ... # FIXME Function
    def remove_meta(*args): ... # FIXME Function
    def replace_all_memory(*args): ... # FIXME Function
    def replace_memory(*args): ... # FIXME Function
    def replace_memory_range(*args): ... # FIXME Function
    def resize(*args): ... # FIXME Function
    def resize_range(*args): ... # FIXME Function
    def set_flags(*args): ... # FIXME Function
    def set_size(*args): ... # FIXME Function
    def unmap(self, mapinfo): ... # FIXME Function
    def unset_flags(*args): ... # FIXME Function
    

class BufferList(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gst.BufferList
        new_sized(size:int) -> Gst.BufferList
    """
    def calculate_size(*args): ... # FIXME Function
    def copy_deep(*args): ... # FIXME Function
    def foreach(*args): ... # FIXME Function
    def get(*args): ... # FIXME Function
    def get_writable(*args): ... # FIXME Function
    def insert(*args): ... # FIXME Function
    def length(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_sized(*args): ... # FIXME Function
    def remove(*args): ... # FIXME Function
    def replace(*args): ... # FIXME Function
    def take(*args): ... # FIXME Function
    

class BufferPool(Object):
    """
    :Constructors:

    ::

        BufferPool(**properties)
        new() -> Gst.BufferPool

    Object GstBufferPool

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    flushing: int = ...
    priv: BufferPoolPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def acquire_buffer(*args): ... # FIXME Function
    def config_add_option(*args): ... # FIXME Function
    def config_get_allocator(*args): ... # FIXME Function
    def config_get_option(*args): ... # FIXME Function
    def config_get_params(*args): ... # FIXME Function
    def config_has_option(*args): ... # FIXME Function
    def config_n_options(*args): ... # FIXME Function
    def config_set_allocator(*args): ... # FIXME Function
    def config_set_params(*args): ... # FIXME Function
    def config_validate_params(*args): ... # FIXME Function
    def do_acquire_buffer(self, params: typing.Optional[BufferPoolAcquireParams] = None) -> typing.Tuple[FlowReturn, Buffer]: ...
    def do_alloc_buffer(self, params: typing.Optional[BufferPoolAcquireParams] = None) -> typing.Tuple[FlowReturn, Buffer]: ...
    def do_flush_start(self) -> None: ...
    def do_flush_stop(self) -> None: ...
    def do_free_buffer(self, buffer: Buffer) -> None: ...
    def do_get_options(self) -> list[str]: ...
    def do_release_buffer(self, buffer: Buffer) -> None: ...
    def do_reset_buffer(self, buffer: Buffer) -> None: ...
    def do_set_config(self, config: Structure) -> bool: ...
    def do_start(self) -> bool: ...
    def do_stop(self) -> bool: ...
    def get_config(*args): ... # FIXME Function
    def get_options(*args): ... # FIXME Function
    def has_option(*args): ... # FIXME Function
    def is_active(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def release_buffer(*args): ... # FIXME Function
    def set_active(*args): ... # FIXME Function
    def set_config(*args): ... # FIXME Function
    def set_flushing(*args): ... # FIXME Function
    

class BufferPoolAcquireParams(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferPoolAcquireParams()
    """
    format: Format = ...
    start: int = ...
    stop: int = ...
    flags: BufferPoolAcquireFlags = ...
    _gst_reserved: list[None] = ...

class BufferPoolClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BufferPoolClass()
    """
    object_class: ObjectClass = ...
    get_options: typing.Callable[[BufferPool], list[str]] = ...
    set_config: typing.Callable[[BufferPool, Structure], bool] = ...
    start: typing.Callable[[BufferPool], bool] = ...
    stop: typing.Callable[[BufferPool], bool] = ...
    acquire_buffer: typing.Callable[[BufferPool, typing.Optional[BufferPoolAcquireParams]], typing.Tuple[FlowReturn, Buffer]] = ...
    alloc_buffer: typing.Callable[[BufferPool, typing.Optional[BufferPoolAcquireParams]], typing.Tuple[FlowReturn, Buffer]] = ...
    reset_buffer: typing.Callable[[BufferPool, Buffer], None] = ...
    release_buffer: typing.Callable[[BufferPool, Buffer], None] = ...
    free_buffer: typing.Callable[[BufferPool, Buffer], None] = ...
    flush_start: typing.Callable[[BufferPool], None] = ...
    flush_stop: typing.Callable[[BufferPool], None] = ...
    _gst_reserved: list[None] = ...

class BufferPoolPrivate(GObject.GPointer): ...

class Bus(Object):
    """
    :Constructors:

    ::

        Bus(**properties)
        new() -> Gst.Bus

    Object GstBus

    Properties from GstBus:
      enable-async -> gboolean: Enable Async
        Enable async message delivery for bus watches and gst_bus_pop()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
        enable_async: bool
    props: Props = ...
    object: Object = ...
    priv: BusPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, enable_async: bool = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_signal_watch(*args): ... # FIXME Function
    def add_signal_watch_full(*args): ... # FIXME Function
    def add_watch(*args): ... # FIXME Function
    def async_signal_func(*args): ... # FIXME Function
    def create_watch(*args): ... # FIXME Function
    def disable_sync_message_emission(*args): ... # FIXME Function
    def do_message(self, message: Message) -> None: ...
    def do_sync_message(self, message: Message) -> None: ...
    def enable_sync_message_emission(*args): ... # FIXME Function
    def get_pollfd(*args): ... # FIXME Function
    def have_pending(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def peek(*args): ... # FIXME Function
    def poll(*args): ... # FIXME Function
    def pop(*args): ... # FIXME Function
    def pop_filtered(*args): ... # FIXME Function
    def post(*args): ... # FIXME Function
    def remove_signal_watch(*args): ... # FIXME Function
    def remove_watch(*args): ... # FIXME Function
    def set_flushing(*args): ... # FIXME Function
    def set_sync_handler(*args): ... # FIXME Function
    def sync_signal_handler(*args): ... # FIXME Function
    def timed_pop(*args): ... # FIXME Function
    def timed_pop_filtered(*args): ... # FIXME Function
    

class BusClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BusClass()
    """
    parent_class: ObjectClass = ...
    message: typing.Callable[[Bus, Message], None] = ...
    sync_message: typing.Callable[[Bus, Message], None] = ...
    _gst_reserved: list[None] = ...

class BusPrivate(GObject.GPointer): ...

class ByteArrayInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ByteArrayInterface()
    """
    data: int = ...
    len: int = ...
    resize: typing.Callable[[ByteArrayInterface, int], bool] = ...
    _gst_reserved: list[None] = ...

class Caps(GObject.GBoxed):
    """
    :Constructors:

    ::

        Caps()
        new_any() -> Gst.Caps
        new_empty() -> Gst.Caps
        new_empty_simple(media_type:str) -> Gst.Caps
    """
    mini_object: MiniObject = ...
    def append(*args): ... # FIXME Function
    def append_structure(*args): ... # FIXME Function
    def append_structure_full(*args): ... # FIXME Function
    def can_intersect(*args): ... # FIXME Function
    def copy(*args): ... # FIXME Function
    def copy_nth(*args): ... # FIXME Function
    def filter_and_map_in_place(*args): ... # FIXME Function
    def fixate(*args): ... # FIXME Function
    def foreach(*args): ... # FIXME Function
    def from_string(*args): ... # FIXME Function
    def get_features(*args): ... # FIXME Function
    def get_size(*args): ... # FIXME Function
    def get_structure(*args): ... # FIXME Function
    def intersect(*args): ... # FIXME Function
    def intersect_full(*args): ... # FIXME Function
    def is_always_compatible(*args): ... # FIXME Function
    def is_any(*args): ... # FIXME Function
    def is_empty(*args): ... # FIXME Function
    def is_equal(*args): ... # FIXME Function
    def is_equal_fixed(*args): ... # FIXME Function
    def is_fixed(*args): ... # FIXME Function
    def is_strictly_equal(*args): ... # FIXME Function
    def is_subset(*args): ... # FIXME Function
    def is_subset_structure(*args): ... # FIXME Function
    def is_subset_structure_full(*args): ... # FIXME Function
    def map_in_place(*args): ... # FIXME Function
    def merge(*args): ... # FIXME Function
    def merge_structure(*args): ... # FIXME Function
    def merge_structure_full(*args): ... # FIXME Function
    def new_any(*args): ... # FIXME Function
    def new_empty(*args): ... # FIXME Function
    def new_empty_simple(*args): ... # FIXME Function
    def normalize(*args): ... # FIXME Function
    def remove_structure(*args): ... # FIXME Function
    def serialize(*args): ... # FIXME Function
    def set_features(*args): ... # FIXME Function
    def set_features_simple(*args): ... # FIXME Function
    def set_value(*args): ... # FIXME Function
    def simplify(*args): ... # FIXME Function
    def steal_structure(*args): ... # FIXME Function
    def subtract(*args): ... # FIXME Function
    def to_string(*args): ... # FIXME Function
    def truncate(*args): ... # FIXME Function
    

class CapsFeatures(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_any() -> Gst.CapsFeatures
        new_empty() -> Gst.CapsFeatures
        new_single(feature:str) -> Gst.CapsFeatures
    """
    def add(*args): ... # FIXME Function
    def add_id(*args): ... # FIXME Function
    def contains(*args): ... # FIXME Function
    def contains_id(*args): ... # FIXME Function
    def copy(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def from_string(*args): ... # FIXME Function
    def get_nth(*args): ... # FIXME Function
    def get_nth_id(*args): ... # FIXME Function
    def get_size(*args): ... # FIXME Function
    def is_any(*args): ... # FIXME Function
    def is_equal(*args): ... # FIXME Function
    def new_any(*args): ... # FIXME Function
    def new_empty(*args): ... # FIXME Function
    def new_single(*args): ... # FIXME Function
    def remove(*args): ... # FIXME Function
    def remove_id(*args): ... # FIXME Function
    def set_parent_refcount(*args): ... # FIXME Function
    def to_string(*args): ... # FIXME Function
    

class ChildProxy(GObject.GInterface):
    """
    Interface GstChildProxy

    Signals from GObject:
      notify (GParam)
    """
    def child_added(*args): ... # FIXME Function
    def child_removed(*args): ... # FIXME Function
    def get_child_by_index(*args): ... # FIXME Function
    def get_child_by_name(*args): ... # FIXME Function
    def get_child_by_name_recurse(*args): ... # FIXME Function
    def get_children_count(*args): ... # FIXME Function
    def get_property(*args): ... # FIXME Function
    def lookup(*args): ... # FIXME Function
    def set_property(*args): ... # FIXME Function
    

class ChildProxyInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ChildProxyInterface()
    """
    parent: GObject.TypeInterface = ...
    get_child_by_name: typing.Callable[[ChildProxy, str], typing.Optional[GObject.Object]] = ...
    get_child_by_index: typing.Callable[[ChildProxy, int], typing.Optional[GObject.Object]] = ...
    get_children_count: typing.Callable[[ChildProxy], int] = ...
    child_added: typing.Callable[[ChildProxy, GObject.Object, str], None] = ...
    child_removed: typing.Callable[[ChildProxy, GObject.Object, str], None] = ...
    _gst_reserved: list[None] = ...

class Clock(Object):
    """
    :Constructors:

    ::

        Clock(**properties)

    Object GstClock

    Signals from GstClock:
      synced (gboolean)

    Properties from GstClock:
      window-size -> gint: Window size
        The size of the window used to calculate rate and offset
      window-threshold -> gint: Window threshold
        The threshold to start calculating rate and offset
      timeout -> guint64: Timeout
        The amount of time, in nanoseconds, to sample master and slave clocks

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        timeout: int
        window_size: int
        window_threshold: int
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    priv: ClockPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, timeout: int = ...,
                 window_size: int = ...,
                 window_threshold: int = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_observation(*args): ... # FIXME Function
    def add_observation_unapplied(*args): ... # FIXME Function
    def adjust_unlocked(*args): ... # FIXME Function
    def adjust_with_calibration(*args): ... # FIXME Function
    def do_change_resolution(self, old_resolution: int, new_resolution: int) -> int: ...
    def do_get_internal_time(self) -> int: ...
    def do_get_resolution(self) -> int: ...
    def do_unschedule(self, entry: ClockEntry) -> None: ...
    def do_wait(self, entry: ClockEntry) -> typing.Tuple[ClockReturn, int]: ...
    def do_wait_async(self, entry: ClockEntry) -> ClockReturn: ...
    def get_calibration(*args): ... # FIXME Function
    def get_internal_time(*args): ... # FIXME Function
    def get_master(*args): ... # FIXME Function
    def get_resolution(*args): ... # FIXME Function
    def get_time(*args): ... # FIXME Function
    def get_timeout(*args): ... # FIXME Function
    def id_compare_func(*args): ... # FIXME Function
    def id_get_clock(*args): ... # FIXME Function
    def id_get_time(*args): ... # FIXME Function
    def id_ref(*args): ... # FIXME Function
    def id_unref(*args): ... # FIXME Function
    def id_unschedule(*args): ... # FIXME Function
    def id_uses_clock(*args): ... # FIXME Function
    def id_wait(*args): ... # FIXME Function
    def id_wait_async(*args): ... # FIXME Function
    def is_synced(*args): ... # FIXME Function
    def new_periodic_id(*args): ... # FIXME Function
    def new_single_shot_id(*args): ... # FIXME Function
    def periodic_id_reinit(*args): ... # FIXME Function
    def set_calibration(*args): ... # FIXME Function
    def set_master(*args): ... # FIXME Function
    def set_resolution(*args): ... # FIXME Function
    def set_synced(*args): ... # FIXME Function
    def set_timeout(*args): ... # FIXME Function
    def single_shot_id_reinit(*args): ... # FIXME Function
    def unadjust_unlocked(*args): ... # FIXME Function
    def unadjust_with_calibration(*args): ... # FIXME Function
    def wait_for_sync(*args): ... # FIXME Function
    

class ClockClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClockClass()
    """
    parent_class: ObjectClass = ...
    change_resolution: typing.Callable[[Clock, int, int], int] = ...
    get_resolution: typing.Callable[[Clock], int] = ...
    get_internal_time: typing.Callable[[Clock], int] = ...
    wait: typing.Callable[[Clock, ClockEntry], typing.Tuple[ClockReturn, int]] = ...
    wait_async: typing.Callable[[Clock, ClockEntry], ClockReturn] = ...
    unschedule: typing.Callable[[Clock, ClockEntry], None] = ...
    _gst_reserved: list[None] = ...

class ClockEntry(GObject.GPointer):
    """
    :Constructors:

    ::

        ClockEntry()
    """
    refcount: int = ...
    clock: Clock = ...
    type: ClockEntryType = ...
    time: int = ...
    interval: int = ...
    status: ClockReturn = ...
    func: typing.Callable[..., bool] = ...
    user_data: None = ...
    destroy_data: typing.Callable[[None], None] = ...
    unscheduled: bool = ...
    woken_up: bool = ...
    _gst_reserved: list[None] = ...

class ClockPrivate(GObject.GPointer): ...

class Context(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(context_type:str, persistent:bool) -> Gst.Context
    """
    def copy(*args): ... # FIXME Function
    def get_context_type(*args): ... # FIXME Function
    def get_structure(*args): ... # FIXME Function
    def has_context_type(*args): ... # FIXME Function
    def is_persistent(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def replace(*args): ... # FIXME Function
    def unref(*args): ... # FIXME Function
    def writable_structure(*args): ... # FIXME Function
    

class ControlBinding(Object):
    """
    :Constructors:

    ::

        ControlBinding(**properties)

    Object GstControlBinding

    Properties from GstControlBinding:
      object -> GstObject: Object
        The object of the property
      name -> gchararray: Name
        The name of the property

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: str
        object: Object
        parent: typing.Optional[Object]
    props: Props = ...
    parent: Object = ...
    name: str = ...
    pspec: GObject.ParamSpec = ...
    object: Object = ...
    disabled: bool = ...
    def __init__(self, name: str = ...,
                 object: Object = ...,
                 parent: Object = ...) -> None: ...
    def do_get_g_value_array(self, timestamp: int, interval: int, values: typing.Sequence[typing.Any]) -> bool: ...
    def do_get_value(self, timestamp: int) -> typing.Optional[typing.Any]: ...
    def do_sync_values(self, object: Object, timestamp: int, last_sync: int) -> bool: ...
    def get_g_value_array(*args): ... # FIXME Function
    def get_value(*args): ... # FIXME Function
    def is_disabled(*args): ... # FIXME Function
    def set_disabled(*args): ... # FIXME Function
    def sync_values(*args): ... # FIXME Function
    

class ControlBindingClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ControlBindingClass()
    """
    parent_class: ObjectClass = ...
    sync_values: typing.Callable[[ControlBinding, Object, int, int], bool] = ...
    get_value: typing.Callable[[ControlBinding, int], typing.Optional[typing.Any]] = ...
    get_value_array: None = ...
    get_g_value_array: typing.Callable[[ControlBinding, int, int, typing.Sequence[typing.Any]], bool] = ...
    _gst_reserved: list[None] = ...

class ControlBindingPrivate(GObject.GPointer): ...

class ControlSource(Object):
    """
    :Constructors:

    ::

        ControlSource(**properties)

    Object GstControlSource

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    parent: Object = ...
    get_value: typing.Callable[[ControlSource, int, float], bool] = ...
    get_value_array: typing.Callable[[ControlSource, int, int, int, float], bool] = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def control_source_get_value(*args): ... # FIXME Function
    def control_source_get_value_array(*args): ... # FIXME Function
    

class ControlSourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ControlSourceClass()
    """
    parent_class: ObjectClass = ...
    _gst_reserved: list[None] = ...

class CustomMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        CustomMeta()
    """
    meta: Meta = ...
    structure: Structure = ...
    def get_structure(*args): ... # FIXME Function
    def has_name(*args): ... # FIXME Function
    

class DateTime(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(tzoffset:float, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime or None
        new_from_g_date_time(dt:GLib.DateTime=None) -> Gst.DateTime or None
        new_from_iso8601_string(string:str) -> Gst.DateTime or None
        new_from_unix_epoch_local_time(secs:int) -> Gst.DateTime or None
        new_from_unix_epoch_local_time_usecs(usecs:int) -> Gst.DateTime or None
        new_from_unix_epoch_utc(secs:int) -> Gst.DateTime or None
        new_from_unix_epoch_utc_usecs(usecs:int) -> Gst.DateTime or None
        new_local_time(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime or None
        new_now_local_time() -> Gst.DateTime or None
        new_now_utc() -> Gst.DateTime or None
        new_y(year:int) -> Gst.DateTime or None
        new_ym(year:int, month:int) -> Gst.DateTime or None
        new_ymd(year:int, month:int, day:int) -> Gst.DateTime or None
    """
    def get_day(*args): ... # FIXME Function
    def get_hour(*args): ... # FIXME Function
    def get_microsecond(*args): ... # FIXME Function
    def get_minute(*args): ... # FIXME Function
    def get_month(*args): ... # FIXME Function
    def get_second(*args): ... # FIXME Function
    def get_time_zone_offset(*args): ... # FIXME Function
    def get_year(*args): ... # FIXME Function
    def has_day(*args): ... # FIXME Function
    def has_month(*args): ... # FIXME Function
    def has_second(*args): ... # FIXME Function
    def has_time(*args): ... # FIXME Function
    def has_year(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_from_g_date_time(*args): ... # FIXME Function
    def new_from_iso8601_string(*args): ... # FIXME Function
    def new_from_unix_epoch_local_time(*args): ... # FIXME Function
    def new_from_unix_epoch_local_time_usecs(*args): ... # FIXME Function
    def new_from_unix_epoch_utc(*args): ... # FIXME Function
    def new_from_unix_epoch_utc_usecs(*args): ... # FIXME Function
    def new_local_time(*args): ... # FIXME Function
    def new_now_local_time(*args): ... # FIXME Function
    def new_now_utc(*args): ... # FIXME Function
    def new_y(*args): ... # FIXME Function
    def new_ym(*args): ... # FIXME Function
    def new_ymd(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def to_g_date_time(*args): ... # FIXME Function
    def to_iso8601_string(*args): ... # FIXME Function
    def unref(*args): ... # FIXME Function
    

class DebugCategory(GObject.GPointer):
    """
    :Constructors:

    ::

        DebugCategory()
    """
    threshold: int = ...
    color: int = ...
    name: str = ...
    description: str = ...
    def free(*args): ... # FIXME Function
    def get_color(*args): ... # FIXME Function
    def get_description(*args): ... # FIXME Function
    def get_name(*args): ... # FIXME Function
    def get_threshold(*args): ... # FIXME Function
    def reset_threshold(*args): ... # FIXME Function
    def set_threshold(*args): ... # FIXME Function
    

class DebugMessage(GObject.GPointer):
    def get(*args): ... # FIXME Function
    def get_id(*args): ... # FIXME Function
    

class Device(Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object GstDevice

    Signals from GstDevice:
      removed ()

    Properties from GstDevice:
      display-name -> gchararray: Display Name
        The user-friendly name of the device
      device-class -> gchararray: Device Class
        The Class of the device

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        caps: typing.Optional[Caps]
        device_class: str
        display_name: str
        properties: typing.Optional[Structure]
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    parent: Object = ...
    priv: DevicePrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, caps: Caps = ...,
                 device_class: str = ...,
                 display_name: str = ...,
                 properties: Structure = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def create_element(*args): ... # FIXME Function
    def do_create_element(self, name: typing.Optional[str] = None) -> typing.Optional[Element]: ...
    def do_reconfigure_element(self, element: Element) -> bool: ...
    def get_caps(*args): ... # FIXME Function
    def get_device_class(*args): ... # FIXME Function
    def get_display_name(*args): ... # FIXME Function
    def get_properties(*args): ... # FIXME Function
    def has_classes(*args): ... # FIXME Function
    def has_classesv(*args): ... # FIXME Function
    def reconfigure_element(*args): ... # FIXME Function
    

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """
    parent_class: ObjectClass = ...
    create_element: typing.Callable[[Device, typing.Optional[str]], typing.Optional[Element]] = ...
    reconfigure_element: typing.Callable[[Device, Element], bool] = ...
    _gst_reserved: list[None] = ...

class DeviceMonitor(Object):
    """
    :Constructors:

    ::

        DeviceMonitor(**properties)
        new() -> Gst.DeviceMonitor

    Object GstDeviceMonitor

    Properties from GstDeviceMonitor:
      show-all -> gboolean: Show All
        Show all devices, even those from hidden providers

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        show_all: bool
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    parent: Object = ...
    priv: DeviceMonitorPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, show_all: bool = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_filter(*args): ... # FIXME Function
    def get_bus(*args): ... # FIXME Function
    def get_devices(*args): ... # FIXME Function
    def get_providers(*args): ... # FIXME Function
    def get_show_all_devices(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def remove_filter(*args): ... # FIXME Function
    def set_show_all_devices(*args): ... # FIXME Function
    def start(*args): ... # FIXME Function
    def stop(*args): ... # FIXME Function
    

class DeviceMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceMonitorClass()
    """
    parent_class: ObjectClass = ...
    _gst_reserved: list[None] = ...

class DeviceMonitorPrivate(GObject.GPointer): ...

class DevicePrivate(GObject.GPointer): ...

class DeviceProvider(Object):
    """
    :Constructors:

    ::

        DeviceProvider(**properties)

    Object GstDeviceProvider

    Signals from GstDeviceProvider:
      provider-hidden (gchararray)
      provider-unhidden (gchararray)

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    parent: Object = ...
    devices: list[None] = ...
    priv: DeviceProviderPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_metadata(self, key: str, value: str) -> None: ...
    def add_static_metadata(self, key: str, value: str) -> None: ...
    def can_monitor(*args): ... # FIXME Function
    def device_add(*args): ... # FIXME Function
    def device_changed(*args): ... # FIXME Function
    def device_remove(*args): ... # FIXME Function
    def do_start(self) -> bool: ...
    def do_stop(self) -> None: ...
    def get_bus(*args): ... # FIXME Function
    def get_devices(*args): ... # FIXME Function
    def get_factory(*args): ... # FIXME Function
    def get_hidden_providers(*args): ... # FIXME Function
    def get_metadata(*args): ... # FIXME Function
    def hide_provider(*args): ... # FIXME Function
    def is_started(*args): ... # FIXME Function
    def register(*args): ... # FIXME Function
    def set_metadata(self, longname: str, classification: str, description: str, author: str) -> None: ...
    def set_static_metadata(self, longname: str, classification: str, description: str, author: str) -> None: ...
    def start(*args): ... # FIXME Function
    def stop(*args): ... # FIXME Function
    def unhide_provider(*args): ... # FIXME Function
    

class DeviceProviderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceProviderClass()
    """
    parent_class: ObjectClass = ...
    factory: DeviceProviderFactory = ...
    probe: None = ...
    start: typing.Callable[[DeviceProvider], bool] = ...
    stop: typing.Callable[[DeviceProvider], None] = ...
    metadata: None = ...
    _gst_reserved: list[None] = ...
    def add_metadata(*args): ... # FIXME Function
    def add_static_metadata(*args): ... # FIXME Function
    def get_metadata(*args): ... # FIXME Function
    def set_metadata(*args): ... # FIXME Function
    def set_static_metadata(*args): ... # FIXME Function
    

class DeviceProviderFactory(PluginFeature):
    """
    :Constructors:

    ::

        DeviceProviderFactory(**properties)

    Object GstDeviceProviderFactory

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def find(*args): ... # FIXME Function
    def get(*args): ... # FIXME Function
    def get_by_name(*args): ... # FIXME Function
    def get_device_provider_type(*args): ... # FIXME Function
    def get_metadata(*args): ... # FIXME Function
    def get_metadata_keys(*args): ... # FIXME Function
    def has_classes(*args): ... # FIXME Function
    def has_classesv(*args): ... # FIXME Function
    def list_get_device_providers(*args): ... # FIXME Function
    

class DeviceProviderFactoryClass(GObject.GPointer): ...

class DeviceProviderPrivate(GObject.GPointer): ...

class DoubleRange: ...

class DynamicTypeFactory(PluginFeature):
    """
    :Constructors:

    ::

        DynamicTypeFactory(**properties)

    Object GstDynamicTypeFactory

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def load(*args): ... # FIXME Function
    

class DynamicTypeFactoryClass(GObject.GPointer): ...

class Element(Object):
    """
    :Constructors:

    ::

        Element(**properties)

    Object GstElement

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    state_lock: GLib.RecMutex = ...
    state_cond: GLib.Cond = ...
    state_cookie: int = ...
    target_state: State = ...
    current_state: State = ...
    next_state: State = ...
    pending_state: State = ...
    last_return: StateChangeReturn = ...
    bus: Bus = ...
    clock: Clock = ...
    base_time: int = ...
    start_time: int = ...
    numpads: int = ...
    pads: list[Pad] = ...
    numsrcpads: int = ...
    srcpads: list[Pad] = ...
    numsinkpads: int = ...
    sinkpads: list[Pad] = ...
    pads_cookie: int = ...
    contexts: list[Context] = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def abort_state(*args): ... # FIXME Function
    def add_metadata(self, key: str, value: str) -> None: ...
    def add_pad(*args): ... # FIXME Function
    def add_pad_template(self, templ: PadTemplate) -> None: ...
    def add_property_deep_notify_watch(*args): ... # FIXME Function
    def add_property_notify_watch(*args): ... # FIXME Function
    def add_static_metadata(self, key: str, value: str) -> None: ...
    def add_static_pad_template(self, static_templ: StaticPadTemplate) -> None: ...
    def add_static_pad_template_with_gtype(self, static_templ: StaticPadTemplate, pad_type: typing.Type[typing.Any]) -> None: ...
    def call_async(*args): ... # FIXME Function
    def change_state(*args): ... # FIXME Function
    def continue_state(*args): ... # FIXME Function
    def create_all_pads(*args): ... # FIXME Function
    def decorate_stream_id(*args): ... # FIXME Function
    def do_change_state(self, transition: StateChange) -> StateChangeReturn: ...
    def do_get_state(self, timeout: int) -> typing.Tuple[StateChangeReturn, State, State]: ...
    def do_no_more_pads(self) -> None: ...
    def do_pad_added(self, pad: Pad) -> None: ...
    def do_pad_removed(self, pad: Pad) -> None: ...
    def do_post_message(self, message: Message) -> bool: ...
    def do_provide_clock(self) -> typing.Optional[Clock]: ...
    def do_query(self, query: Query) -> bool: ...
    def do_release_pad(self, pad: Pad) -> None: ...
    def do_request_new_pad(self, templ: PadTemplate, name: typing.Optional[str] = None, caps: typing.Optional[Caps] = None) -> typing.Optional[Pad]: ...
    def do_send_event(self, event: Event) -> bool: ...
    def do_set_bus(self, bus: typing.Optional[Bus] = None) -> None: ...
    def do_set_clock(self, clock: typing.Optional[Clock] = None) -> bool: ...
    def do_set_context(self, context: Context) -> None: ...
    def do_set_state(self, state: State) -> StateChangeReturn: ...
    def do_state_changed(self, oldstate: State, newstate: State, pending: State) -> None: ...
    def foreach_pad(*args): ... # FIXME Function
    def foreach_sink_pad(*args): ... # FIXME Function
    def foreach_src_pad(*args): ... # FIXME Function
    def get_base_time(*args): ... # FIXME Function
    def get_bus(*args): ... # FIXME Function
    def get_clock(*args): ... # FIXME Function
    def get_compatible_pad(*args): ... # FIXME Function
    def get_compatible_pad_template(*args): ... # FIXME Function
    def get_context(*args): ... # FIXME Function
    def get_context_unlocked(*args): ... # FIXME Function
    def get_contexts(*args): ... # FIXME Function
    def get_current_clock_time(*args): ... # FIXME Function
    def get_current_running_time(*args): ... # FIXME Function
    def get_factory(*args): ... # FIXME Function
    def get_metadata(*args): ... # FIXME Function
    def get_pad_template(*args): ... # FIXME Function
    def get_pad_template_list(*args): ... # FIXME Function
    def get_request_pad(*args): ... # FIXME Function
    def get_start_time(*args): ... # FIXME Function
    def get_state(*args): ... # FIXME Function
    def get_static_pad(*args): ... # FIXME Function
    def is_locked_state(*args): ... # FIXME Function
    def iterate_pads(*args): ... # FIXME Function
    def iterate_sink_pads(*args): ... # FIXME Function
    def iterate_src_pads(*args): ... # FIXME Function
    def link(*args): ... # FIXME Function
    def link_filtered(*args): ... # FIXME Function
    def link_many(*args): ... # FIXME Function
    def link_pads(*args): ... # FIXME Function
    def link_pads_filtered(*args): ... # FIXME Function
    def link_pads_full(*args): ... # FIXME Function
    def lost_state(*args): ... # FIXME Function
    def make_from_uri(*args): ... # FIXME Function
    def message_full(*args): ... # FIXME Function
    def message_full_with_details(*args): ... # FIXME Function
    def no_more_pads(*args): ... # FIXME Function
    def post_message(*args): ... # FIXME Function
    def provide_clock(*args): ... # FIXME Function
    def query(*args): ... # FIXME Function
    def query_convert(*args): ... # FIXME Function
    def query_duration(*args): ... # FIXME Function
    def query_position(*args): ... # FIXME Function
    def register(*args): ... # FIXME Function
    def release_request_pad(*args): ... # FIXME Function
    def remove_pad(*args): ... # FIXME Function
    def remove_property_notify_watch(*args): ... # FIXME Function
    def request_pad(*args): ... # FIXME Function
    def request_pad_simple(*args): ... # FIXME Function
    def seek(*args): ... # FIXME Function
    def seek_simple(*args): ... # FIXME Function
    def send_event(*args): ... # FIXME Function
    def set_base_time(*args): ... # FIXME Function
    def set_bus(*args): ... # FIXME Function
    def set_clock(*args): ... # FIXME Function
    def set_context(*args): ... # FIXME Function
    def set_locked_state(*args): ... # FIXME Function
    def set_metadata(self, longname: str, classification: str, description: str, author: str) -> None: ...
    def set_start_time(*args): ... # FIXME Function
    def set_state(*args): ... # FIXME Function
    def set_static_metadata(self, longname: str, classification: str, description: str, author: str) -> None: ...
    def state_change_return_get_name(*args): ... # FIXME Function
    def state_get_name(*args): ... # FIXME Function
    def sync_state_with_parent(*args): ... # FIXME Function
    def type_set_skip_documentation(*args): ... # FIXME Function
    def unlink(*args): ... # FIXME Function
    def unlink_pads(*args): ... # FIXME Function
    

class ElementClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ElementClass()
    """
    parent_class: ObjectClass = ...
    metadata: None = ...
    elementfactory: ElementFactory = ...
    padtemplates: list[None] = ...
    numpadtemplates: int = ...
    pad_templ_cookie: int = ...
    pad_added: typing.Callable[[Element, Pad], None] = ...
    pad_removed: typing.Callable[[Element, Pad], None] = ...
    no_more_pads: typing.Callable[[Element], None] = ...
    request_new_pad: typing.Callable[[Element, PadTemplate, typing.Optional[str], typing.Optional[Caps]], typing.Optional[Pad]] = ...
    release_pad: typing.Callable[[Element, Pad], None] = ...
    get_state: typing.Callable[[Element, int], typing.Tuple[StateChangeReturn, State, State]] = ...
    set_state: typing.Callable[[Element, State], StateChangeReturn] = ...
    change_state: typing.Callable[[Element, StateChange], StateChangeReturn] = ...
    state_changed: typing.Callable[[Element, State, State, State], None] = ...
    set_bus: typing.Callable[[Element, typing.Optional[Bus]], None] = ...
    provide_clock: typing.Callable[[Element], typing.Optional[Clock]] = ...
    set_clock: typing.Callable[[Element, typing.Optional[Clock]], bool] = ...
    send_event: typing.Callable[[Element, Event], bool] = ...
    query: typing.Callable[[Element, Query], bool] = ...
    post_message: typing.Callable[[Element, Message], bool] = ...
    set_context: typing.Callable[[Element, Context], None] = ...
    _gst_reserved: list[None] = ...
    def add_metadata(*args): ... # FIXME Function
    def add_pad_template(*args): ... # FIXME Function
    def add_static_metadata(*args): ... # FIXME Function
    def add_static_pad_template(*args): ... # FIXME Function
    def add_static_pad_template_with_gtype(*args): ... # FIXME Function
    def get_metadata(*args): ... # FIXME Function
    def get_pad_template(*args): ... # FIXME Function
    def get_pad_template_list(*args): ... # FIXME Function
    def set_metadata(*args): ... # FIXME Function
    def set_static_metadata(*args): ... # FIXME Function
    

class ElementFactory(PluginFeature):
    """
    :Constructors:

    ::

        ElementFactory(**properties)

    Object GstElementFactory

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def can_sink_all_caps(*args): ... # FIXME Function
    def can_sink_any_caps(*args): ... # FIXME Function
    def can_src_all_caps(*args): ... # FIXME Function
    def can_src_any_caps(*args): ... # FIXME Function
    def create(*args): ... # FIXME Function
    def create_with_properties(*args): ... # FIXME Function
    def find(*args): ... # FIXME Function
    def get_description(self): ... # FIXME Function
    def get_element_type(*args): ... # FIXME Function
    def get_klass(self): ... # FIXME Function
    def get_longname(self): ... # FIXME Function
    def get_metadata(*args): ... # FIXME Function
    def get_metadata_keys(*args): ... # FIXME Function
    def get_num_pad_templates(*args): ... # FIXME Function
    def get_skip_documentation(*args): ... # FIXME Function
    def get_static_pad_templates(*args): ... # FIXME Function
    def get_uri_protocols(*args): ... # FIXME Function
    def get_uri_type(*args): ... # FIXME Function
    def has_interface(*args): ... # FIXME Function
    def list_filter(*args): ... # FIXME Function
    def list_get_elements(*args): ... # FIXME Function
    def list_is_type(*args): ... # FIXME Function
    def make(factoryname, name=None): ... # FIXME Function
    def make_with_properties(*args): ... # FIXME Function
    

class ElementFactoryClass(GObject.GPointer): ...

class Event(GObject.GBoxed):
    """
    :Constructors:

    ::

        Event()
        new_buffer_size(format:Gst.Format, minsize:int, maxsize:int, async:bool) -> Gst.Event
        new_caps(caps:Gst.Caps) -> Gst.Event
        new_custom(type:Gst.EventType, structure:Gst.Structure) -> Gst.Event
        new_eos() -> Gst.Event
        new_flush_start() -> Gst.Event
        new_flush_stop(reset_time:bool) -> Gst.Event
        new_gap(timestamp:int, duration:int) -> Gst.Event
        new_instant_rate_change(rate_multiplier:float, new_flags:Gst.SegmentFlags) -> Gst.Event
        new_instant_rate_sync_time(rate_multiplier:float, running_time:int, upstream_running_time:int) -> Gst.Event
        new_latency(latency:int) -> Gst.Event
        new_navigation(structure:Gst.Structure) -> Gst.Event
        new_protection(system_id:str, data:Gst.Buffer, origin:str) -> Gst.Event
        new_qos(type:Gst.QOSType, proportion:float, diff:int, timestamp:int) -> Gst.Event
        new_reconfigure() -> Gst.Event
        new_seek(rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> Gst.Event
        new_segment(segment:Gst.Segment) -> Gst.Event
        new_segment_done(format:Gst.Format, position:int) -> Gst.Event
        new_select_streams(streams:list) -> Gst.Event
        new_sink_message(name:str, msg:Gst.Message) -> Gst.Event
        new_step(format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool) -> Gst.Event
        new_stream_collection(collection:Gst.StreamCollection) -> Gst.Event
        new_stream_group_done(group_id:int) -> Gst.Event
        new_stream_start(stream_id:str) -> Gst.Event
        new_tag(taglist:Gst.TagList) -> Gst.Event
        new_toc(toc:Gst.Toc, updated:bool) -> Gst.Event
        new_toc_select(uid:str) -> Gst.Event
    """
    mini_object: MiniObject = ...
    type: EventType = ...
    timestamp: int = ...
    seqnum: int = ...
    def copy_segment(*args): ... # FIXME Function
    def get_running_time_offset(*args): ... # FIXME Function
    def get_seqnum(*args): ... # FIXME Function
    def get_structure(*args): ... # FIXME Function
    def has_name(*args): ... # FIXME Function
    def has_name_id(*args): ... # FIXME Function
    # override
    @classmethod
    def new_buffer_size(cls, format: Format, minsize: int, maxsize: int, _async: bool) -> Event:
        ...
    def new_caps(*args): ... # FIXME Function
    def new_custom(*args): ... # FIXME Function
    def new_eos(*args): ... # FIXME Function
    def new_flush_start(*args): ... # FIXME Function
    def new_flush_stop(*args): ... # FIXME Function
    def new_gap(*args): ... # FIXME Function
    def new_instant_rate_change(*args): ... # FIXME Function
    def new_instant_rate_sync_time(*args): ... # FIXME Function
    def new_latency(*args): ... # FIXME Function
    def new_navigation(*args): ... # FIXME Function
    def new_protection(*args): ... # FIXME Function
    def new_qos(*args): ... # FIXME Function
    def new_reconfigure(*args): ... # FIXME Function
    def new_seek(*args): ... # FIXME Function
    def new_segment(*args): ... # FIXME Function
    def new_segment_done(*args): ... # FIXME Function
    def new_select_streams(*args): ... # FIXME Function
    def new_sink_message(*args): ... # FIXME Function
    def new_step(*args): ... # FIXME Function
    def new_stream_collection(*args): ... # FIXME Function
    def new_stream_group_done(*args): ... # FIXME Function
    def new_stream_start(*args): ... # FIXME Function
    def new_tag(*args): ... # FIXME Function
    def new_toc(*args): ... # FIXME Function
    def new_toc_select(*args): ... # FIXME Function
    def parse_buffer_size(*args): ... # FIXME Function
    def parse_caps(*args): ... # FIXME Function
    def parse_flush_stop(*args): ... # FIXME Function
    def parse_gap(*args): ... # FIXME Function
    def parse_gap_flags(*args): ... # FIXME Function
    def parse_group_id(*args): ... # FIXME Function
    def parse_instant_rate_change(*args): ... # FIXME Function
    def parse_instant_rate_sync_time(*args): ... # FIXME Function
    def parse_latency(*args): ... # FIXME Function
    def parse_protection(*args): ... # FIXME Function
    def parse_qos(*args): ... # FIXME Function
    def parse_seek(*args): ... # FIXME Function
    def parse_seek_trickmode_interval(*args): ... # FIXME Function
    def parse_segment(*args): ... # FIXME Function
    def parse_segment_done(*args): ... # FIXME Function
    def parse_select_streams(*args): ... # FIXME Function
    def parse_sink_message(*args): ... # FIXME Function
    def parse_step(*args): ... # FIXME Function
    def parse_stream(*args): ... # FIXME Function
    def parse_stream_collection(*args): ... # FIXME Function
    def parse_stream_flags(*args): ... # FIXME Function
    def parse_stream_group_done(*args): ... # FIXME Function
    def parse_stream_start(*args): ... # FIXME Function
    def parse_tag(*args): ... # FIXME Function
    def parse_toc(*args): ... # FIXME Function
    def parse_toc_select(*args): ... # FIXME Function
    def set_gap_flags(*args): ... # FIXME Function
    def set_group_id(*args): ... # FIXME Function
    def set_running_time_offset(*args): ... # FIXME Function
    def set_seek_trickmode_interval(*args): ... # FIXME Function
    def set_seqnum(*args): ... # FIXME Function
    def set_stream(*args): ... # FIXME Function
    def set_stream_flags(*args): ... # FIXME Function
    def writable_structure(*args): ... # FIXME Function
    

class FlagSet:
    """
    :Constructors:

    ::

        FlagSet(**properties)
    """
    def register(*args): ... # FIXME Function
    

class FormatDefinition(GObject.GPointer):
    """
    :Constructors:

    ::

        FormatDefinition()
    """
    value: Format = ...
    nick: str = ...
    description: str = ...
    quark: int = ...

class Fraction: ...

class FractionRange: ...

class GhostPad(ProxyPad):
    """
    :Constructors:

    ::

        GhostPad(**properties)
        new(name:str=None, target:Gst.Pad) -> Gst.Pad or None
        new_from_template(name:str=None, target:Gst.Pad, templ:Gst.PadTemplate) -> Gst.Pad or None
        new_no_target(name:str=None, dir:Gst.PadDirection) -> Gst.Pad or None
        new_no_target_from_template(name:str=None, templ:Gst.PadTemplate) -> Gst.Pad or None

    Object GstGhostPad

    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)

    Properties from GstPad:
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
      offset -> gint64: Offset
        The running time offset of the pad

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        caps: Caps
        direction: PadDirection
        offset: int
        template: PadTemplate
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    pad: ProxyPad = ...
    priv: GhostPadPrivate = ...
    def __init__(self, direction: PadDirection = ...,
                 offset: int = ...,
                 template: PadTemplate = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def activate_mode_default(*args): ... # FIXME Function
    def construct(*args): ... # FIXME Function
    def get_target(*args): ... # FIXME Function
    def internal_activate_mode_default(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_from_template(*args): ... # FIXME Function
    def new_no_target(*args): ... # FIXME Function
    def new_no_target_from_template(*args): ... # FIXME Function
    def set_target(*args): ... # FIXME Function
    

class GhostPadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GhostPadClass()
    """
    parent_class: ProxyPadClass = ...
    _gst_reserved: list[None] = ...

class GhostPadPrivate(GObject.GPointer): ...

class Int64Range: ...

class IntRange: ...

# override
class Iterator(GObject.GBoxed):
    item: Callable[[Iterator, Any], IteratorItem] = ...
    pushed: Iterator = ...
    type: Type = ...
    lock: GLib.Mutex = ...
    cookie: int = ...
    master_cookie: int = ...
    size: int = ...
    _gst_reserved: list[None] = ...

    def copy(self) -> Iterator:
        ...

    def filter(self, func: Callable[[None, None], int], user_data: Any) -> Iterator:
        ...

    def find_custom(self, func: Callable[[None, None], int], *user_data: Any) -> Tuple[bool, Any]:
        ...

    def fold(self, func: Callable[..., bool], ret: Any, *user_data: Any) -> IteratorResult:
        ...

    def foreach(self, func: Callable[..., None], *user_data: Any) -> IteratorResult:
        ...

    def free(self) -> None:
        ...

    @classmethod
    def new_single(cls, type: Type, object: Any) -> Iterator:
        ...

    def next(self) -> Tuple[IteratorResult, Any]:
        ...

    def push(self, other: Iterator) -> None:
        ...

    def resync(self) -> None:
        ...

class IteratorError:
    args = ... # FIXME Constant
    
    def add_note(self, *args, **kwargs): ... # FIXME Function
    def with_traceback(self, *args, **kwargs): ... # FIXME Function
    

class LinkError:
    args = ... # FIXME Constant
    
    def add_note(self, *args, **kwargs): ... # FIXME Function
    def with_traceback(self, *args, **kwargs): ... # FIXME Function
    

class MapError:
    args = ... # FIXME Constant
    
    def add_note(self, *args, **kwargs): ... # FIXME Function
    def with_traceback(self, *args, **kwargs): ... # FIXME Function
    

class MapInfo: ...

class Memory(GObject.GBoxed):
    """
    :Constructors:

    ::

        Memory()
        new_wrapped(flags:Gst.MemoryFlags, data:list, maxsize:int, offset:int, user_data=None, notify:GLib.DestroyNotify=None) -> Gst.Memory or None
    """
    mini_object: MiniObject = ...
    allocator: Allocator = ...
    parent: Memory = ...
    maxsize: int = ...
    align: int = ...
    offset: int = ...
    size: int = ...
    def copy(*args): ... # FIXME Function
    def get_sizes(*args): ... # FIXME Function
    def is_span(*args): ... # FIXME Function
    def is_type(*args): ... # FIXME Function
    def make_mapped(*args): ... # FIXME Function
    def map(self, flags): ... # FIXME Function
    # override
    @classmethod
    def new_wrapped(cls, flags: MemoryFlags, data: Sequence[int], maxsize: int, offset: int, user_data: None, notify: Optional[Callable[[None], None]]=None, *_user_data: Any) -> Optional[Memory]:
        ...
    def resize(*args): ... # FIXME Function
    def share(*args): ... # FIXME Function
    def unmap(self, mapinfo): ... # FIXME Function
    

class Message(GObject.GBoxed):
    """
    :Constructors:

    ::

        Message()
        new_application(src:Gst.Object=None, structure:Gst.Structure) -> Gst.Message
        new_async_done(src:Gst.Object=None, running_time:int) -> Gst.Message
        new_async_start(src:Gst.Object=None) -> Gst.Message
        new_buffering(src:Gst.Object=None, percent:int) -> Gst.Message
        new_clock_lost(src:Gst.Object=None, clock:Gst.Clock) -> Gst.Message
        new_clock_provide(src:Gst.Object=None, clock:Gst.Clock, ready:bool) -> Gst.Message
        new_custom(type:Gst.MessageType, src:Gst.Object=None, structure:Gst.Structure=None) -> Gst.Message
        new_device_added(src:Gst.Object=None, device:Gst.Device) -> Gst.Message
        new_device_changed(src:Gst.Object=None, device:Gst.Device, changed_device:Gst.Device) -> Gst.Message
        new_device_removed(src:Gst.Object=None, device:Gst.Device) -> Gst.Message
        new_duration_changed(src:Gst.Object=None) -> Gst.Message
        new_element(src:Gst.Object=None, structure:Gst.Structure) -> Gst.Message
        new_eos(src:Gst.Object=None) -> Gst.Message
        new_error(src:Gst.Object=None, error:error, debug:str) -> Gst.Message
        new_error_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message
        new_have_context(src:Gst.Object=None, context:Gst.Context) -> Gst.Message
        new_info(src:Gst.Object=None, error:error, debug:str) -> Gst.Message
        new_info_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message
        new_instant_rate_request(src:Gst.Object=None, rate_multiplier:float) -> Gst.Message
        new_latency(src:Gst.Object=None) -> Gst.Message
        new_need_context(src:Gst.Object=None, context_type:str) -> Gst.Message
        new_new_clock(src:Gst.Object=None, clock:Gst.Clock) -> Gst.Message
        new_progress(src:Gst.Object=None, type:Gst.ProgressType, code:str, text:str) -> Gst.Message
        new_property_notify(src:Gst.Object, property_name:str, val:GObject.Value=None) -> Gst.Message
        new_qos(src:Gst.Object=None, live:bool, running_time:int, stream_time:int, timestamp:int, duration:int) -> Gst.Message
        new_redirect(src:Gst.Object=None, location:str, tag_list:Gst.TagList=None, entry_struct:Gst.Structure=None) -> Gst.Message
        new_request_state(src:Gst.Object=None, state:Gst.State) -> Gst.Message
        new_reset_time(src:Gst.Object=None, running_time:int) -> Gst.Message
        new_segment_done(src:Gst.Object=None, format:Gst.Format, position:int) -> Gst.Message
        new_segment_start(src:Gst.Object=None, format:Gst.Format, position:int) -> Gst.Message
        new_state_changed(src:Gst.Object=None, oldstate:Gst.State, newstate:Gst.State, pending:Gst.State) -> Gst.Message
        new_state_dirty(src:Gst.Object=None) -> Gst.Message
        new_step_done(src:Gst.Object=None, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool, duration:int, eos:bool) -> Gst.Message
        new_step_start(src:Gst.Object=None, active:bool, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool) -> Gst.Message
        new_stream_collection(src:Gst.Object=None, collection:Gst.StreamCollection) -> Gst.Message
        new_stream_start(src:Gst.Object=None) -> Gst.Message
        new_stream_status(src:Gst.Object=None, type:Gst.StreamStatusType, owner:Gst.Element) -> Gst.Message
        new_streams_selected(src:Gst.Object=None, collection:Gst.StreamCollection) -> Gst.Message
        new_structure_change(src:Gst.Object=None, type:Gst.StructureChangeType, owner:Gst.Element, busy:bool) -> Gst.Message
        new_tag(src:Gst.Object=None, tag_list:Gst.TagList) -> Gst.Message
        new_toc(src:Gst.Object=None, toc:Gst.Toc, updated:bool) -> Gst.Message
        new_warning(src:Gst.Object=None, error:error, debug:str) -> Gst.Message
        new_warning_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message
    """
    mini_object: MiniObject = ...
    type: MessageType = ...
    timestamp: int = ...
    src: Object = ...
    seqnum: int = ...
    lock: GLib.Mutex = ...
    cond: GLib.Cond = ...
    def add_redirect_entry(*args): ... # FIXME Function
    def get_num_redirect_entries(*args): ... # FIXME Function
    def get_seqnum(*args): ... # FIXME Function
    def get_stream_status_object(*args): ... # FIXME Function
    def get_structure(*args): ... # FIXME Function
    def has_name(*args): ... # FIXME Function
    def new_application(*args): ... # FIXME Function
    def new_async_done(*args): ... # FIXME Function
    def new_async_start(*args): ... # FIXME Function
    def new_buffering(*args): ... # FIXME Function
    def new_clock_lost(*args): ... # FIXME Function
    def new_clock_provide(*args): ... # FIXME Function
    def new_custom(*args): ... # FIXME Function
    def new_device_added(*args): ... # FIXME Function
    def new_device_changed(*args): ... # FIXME Function
    def new_device_removed(*args): ... # FIXME Function
    def new_duration_changed(*args): ... # FIXME Function
    def new_element(*args): ... # FIXME Function
    def new_eos(*args): ... # FIXME Function
    def new_error(*args): ... # FIXME Function
    def new_error_with_details(*args): ... # FIXME Function
    def new_have_context(*args): ... # FIXME Function
    def new_info(*args): ... # FIXME Function
    def new_info_with_details(*args): ... # FIXME Function
    def new_instant_rate_request(*args): ... # FIXME Function
    def new_latency(*args): ... # FIXME Function
    def new_need_context(*args): ... # FIXME Function
    def new_new_clock(*args): ... # FIXME Function
    def new_progress(*args): ... # FIXME Function
    def new_property_notify(*args): ... # FIXME Function
    def new_qos(*args): ... # FIXME Function
    def new_redirect(*args): ... # FIXME Function
    def new_request_state(*args): ... # FIXME Function
    def new_reset_time(*args): ... # FIXME Function
    def new_segment_done(*args): ... # FIXME Function
    def new_segment_start(*args): ... # FIXME Function
    def new_state_changed(*args): ... # FIXME Function
    def new_state_dirty(*args): ... # FIXME Function
    def new_step_done(*args): ... # FIXME Function
    def new_step_start(*args): ... # FIXME Function
    def new_stream_collection(*args): ... # FIXME Function
    def new_stream_start(*args): ... # FIXME Function
    def new_stream_status(*args): ... # FIXME Function
    def new_streams_selected(*args): ... # FIXME Function
    def new_structure_change(*args): ... # FIXME Function
    def new_tag(*args): ... # FIXME Function
    def new_toc(*args): ... # FIXME Function
    def new_warning(*args): ... # FIXME Function
    def new_warning_with_details(*args): ... # FIXME Function
    def parse_async_done(*args): ... # FIXME Function
    def parse_buffering(*args): ... # FIXME Function
    def parse_buffering_stats(*args): ... # FIXME Function
    def parse_clock_lost(*args): ... # FIXME Function
    def parse_clock_provide(*args): ... # FIXME Function
    def parse_context_type(*args): ... # FIXME Function
    def parse_device_added(*args): ... # FIXME Function
    def parse_device_changed(*args): ... # FIXME Function
    def parse_device_removed(*args): ... # FIXME Function
    def parse_error(*args): ... # FIXME Function
    def parse_error_details(*args): ... # FIXME Function
    def parse_group_id(*args): ... # FIXME Function
    def parse_have_context(*args): ... # FIXME Function
    def parse_info(*args): ... # FIXME Function
    def parse_info_details(*args): ... # FIXME Function
    def parse_instant_rate_request(*args): ... # FIXME Function
    def parse_new_clock(*args): ... # FIXME Function
    def parse_progress(*args): ... # FIXME Function
    def parse_property_notify(*args): ... # FIXME Function
    def parse_qos(*args): ... # FIXME Function
    def parse_qos_stats(*args): ... # FIXME Function
    def parse_qos_values(*args): ... # FIXME Function
    def parse_redirect_entry(*args): ... # FIXME Function
    def parse_request_state(*args): ... # FIXME Function
    def parse_reset_time(*args): ... # FIXME Function
    def parse_segment_done(*args): ... # FIXME Function
    def parse_segment_start(*args): ... # FIXME Function
    def parse_state_changed(*args): ... # FIXME Function
    def parse_step_done(*args): ... # FIXME Function
    def parse_step_start(*args): ... # FIXME Function
    def parse_stream_collection(*args): ... # FIXME Function
    def parse_stream_status(*args): ... # FIXME Function
    def parse_streams_selected(*args): ... # FIXME Function
    def parse_structure_change(*args): ... # FIXME Function
    def parse_tag(*args): ... # FIXME Function
    def parse_toc(*args): ... # FIXME Function
    def parse_warning(*args): ... # FIXME Function
    def parse_warning_details(*args): ... # FIXME Function
    def set_buffering_stats(*args): ... # FIXME Function
    def set_group_id(*args): ... # FIXME Function
    def set_qos_stats(*args): ... # FIXME Function
    def set_qos_values(*args): ... # FIXME Function
    def set_seqnum(*args): ... # FIXME Function
    def set_stream_status_object(*args): ... # FIXME Function
    def streams_selected_add(*args): ... # FIXME Function
    def streams_selected_get_size(*args): ... # FIXME Function
    def streams_selected_get_stream(*args): ... # FIXME Function
    def take(*args): ... # FIXME Function
    def writable_structure(*args): ... # FIXME Function
    

class Meta(GObject.GPointer):
    """
    :Constructors:

    ::

        Meta()
    """
    flags: MetaFlags = ...
    info: MetaInfo = ...
    def api_type_get_tags(*args): ... # FIXME Function
    def api_type_has_tag(*args): ... # FIXME Function
    def api_type_register(*args): ... # FIXME Function
    def compare_seqnum(*args): ... # FIXME Function
    def deserialize(*args): ... # FIXME Function
    def get_info(*args): ... # FIXME Function
    def get_seqnum(*args): ... # FIXME Function
    def register_custom(*args): ... # FIXME Function
    def register_custom_simple(*args): ... # FIXME Function
    def serialize(*args): ... # FIXME Function
    def serialize_simple(*args): ... # FIXME Function
    

class MetaInfo(GObject.GPointer):
    """
    :Constructors:

    ::

        MetaInfo()
    """
    api: typing.Type[typing.Any] = ...
    type: typing.Type[typing.Any] = ...
    size: int = ...
    init_func: typing.Callable[[Meta, None, Buffer], bool] = ...
    free_func: typing.Callable[[Meta, Buffer], None] = ...
    transform_func: typing.Callable[[Buffer, Meta, Buffer, int, None], bool] = ...
    serialize_func: typing.Callable[[Meta, ByteArrayInterface], typing.Tuple[bool, int]] = ...
    deserialize_func: typing.Callable[[MetaInfo, Buffer, int, int, int], typing.Optional[Meta]] = ...
    clear_func: typing.Callable[[Buffer, Meta], None] = ...
    def is_custom(*args): ... # FIXME Function
    def register(*args): ... # FIXME Function
    

class MetaTransformCopy(GObject.GPointer):
    """
    :Constructors:

    ::

        MetaTransformCopy()
    """
    region: bool = ...
    offset: int = ...
    size: int = ...

class MiniObject(GObject.GBoxed):
    """
    :Constructors:

    ::

        MiniObject()
    """
    type: typing.Type[typing.Any] = ...
    refcount: int = ...
    lockstate: int = ...
    flags: int = ...
    copy: typing.Callable[[MiniObject], MiniObject] = ...
    dispose: typing.Callable[[MiniObject], bool] = ...
    free: typing.Callable[[MiniObject], None] = ...
    priv_uint: int = ...
    priv_pointer: None = ...
    def add_parent(*args): ... # FIXME Function
    def get_qdata(*args): ... # FIXME Function
    def is_writable(*args): ... # FIXME Function
    def lock(*args): ... # FIXME Function
    def remove_parent(*args): ... # FIXME Function
    def replace(*args): ... # FIXME Function
    def set_qdata(*args): ... # FIXME Function
    def steal_qdata(*args): ... # FIXME Function
    def take(*args): ... # FIXME Function
    def unlock(*args): ... # FIXME Function
    

class NotInitialized:
    args = ... # FIXME Constant
    
    def add_note(self, *args, **kwargs): ... # FIXME Function
    def with_traceback(self, *args, **kwargs): ... # FIXME Function
    

class Object(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        Object(**properties)

    Object GstObject

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: GObject.InitiallyUnowned = ...
    lock: GLib.Mutex = ...
    name: str = ...
    parent: Object = ...
    flags: int = ...
    control_bindings: list[None] = ...
    control_rate: int = ...
    last_sync: int = ...
    _gst_reserved: None = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_control_binding(*args): ... # FIXME Function
    def check_uniqueness(*args): ... # FIXME Function
    def default_deep_notify(*args): ... # FIXME Function
    def default_error(*args): ... # FIXME Function
    def do_deep_notify(self, orig: Object, pspec: GObject.ParamSpec) -> None: ...
    def get_control_binding(*args): ... # FIXME Function
    def get_control_rate(*args): ... # FIXME Function
    def get_g_value_array(*args): ... # FIXME Function
    def get_name(*args): ... # FIXME Function
    def get_parent(*args): ... # FIXME Function
    def get_path_string(*args): ... # FIXME Function
    def get_value(*args): ... # FIXME Function
    def has_active_control_bindings(*args): ... # FIXME Function
    def has_ancestor(*args): ... # FIXME Function
    def has_as_ancestor(*args): ... # FIXME Function
    def has_as_parent(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def remove_control_binding(*args): ... # FIXME Function
    def replace(*args): ... # FIXME Function
    def set_control_binding_disabled(*args): ... # FIXME Function
    def set_control_bindings_disabled(*args): ... # FIXME Function
    def set_control_rate(*args): ... # FIXME Function
    def set_name(*args): ... # FIXME Function
    def set_parent(*args): ... # FIXME Function
    def suggest_next_sync(*args): ... # FIXME Function
    def sync_values(*args): ... # FIXME Function
    def unparent(*args): ... # FIXME Function
    def unref(*args): ... # FIXME Function
    

class ObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """
    parent_class: GObject.InitiallyUnownedClass = ...
    path_string_separator: str = ...
    deep_notify: typing.Callable[[Object, Object, GObject.ParamSpec], None] = ...
    _gst_reserved: list[None] = ...

class Pad(Object):
    """
    :Constructors:

    ::

        Pad(**properties)
        new(name:str=None, direction:Gst.PadDirection) -> Gst.Pad
        new_from_static_template(templ:Gst.StaticPadTemplate, name:str) -> Gst.Pad
        new_from_template(templ:Gst.PadTemplate, name:str=None) -> Gst.Pad

    Object GstPad

    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)

    Properties from GstPad:
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
      offset -> gint64: Offset
        The running time offset of the pad

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        caps: Caps
        direction: PadDirection
        offset: int
        template: PadTemplate
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    element_private: None = ...
    padtemplate: PadTemplate = ...
    direction: PadDirection = ...
    stream_rec_lock: GLib.RecMutex = ...
    task: Task = ...
    block_cond: GLib.Cond = ...
    probes: GLib.HookList = ...
    mode: PadMode = ...
    activatefunc: typing.Callable[[Pad, Object], bool] = ...
    activatedata: None = ...
    activatenotify: typing.Callable[[None], None] = ...
    activatemodefunc: typing.Callable[[Pad, Object, PadMode, bool], bool] = ...
    activatemodedata: None = ...
    activatemodenotify: typing.Callable[[None], None] = ...
    peer: Pad = ...
    linkfunc: typing.Callable[[Pad, typing.Optional[Object], Pad], PadLinkReturn] = ...
    linkdata: None = ...
    linknotify: typing.Callable[[None], None] = ...
    unlinkfunc: typing.Callable[[Pad, typing.Optional[Object]], None] = ...
    unlinkdata: None = ...
    unlinknotify: typing.Callable[[None], None] = ...
    chainfunc: typing.Callable[[Pad, typing.Optional[Object], Buffer], FlowReturn] = ...
    chaindata: None = ...
    chainnotify: typing.Callable[[None], None] = ...
    chainlistfunc: typing.Callable[[Pad, typing.Optional[Object], BufferList], FlowReturn] = ...
    chainlistdata: None = ...
    chainlistnotify: typing.Callable[[None], None] = ...
    getrangefunc: typing.Callable[[Pad, typing.Optional[Object], int, int, Buffer], FlowReturn] = ...
    getrangedata: None = ...
    getrangenotify: typing.Callable[[None], None] = ...
    eventfunc: typing.Callable[[Pad, typing.Optional[Object], Event], bool] = ...
    eventdata: None = ...
    eventnotify: typing.Callable[[None], None] = ...
    offset: int = ...
    queryfunc: typing.Callable[[Pad, typing.Optional[Object], Query], bool] = ...
    querydata: None = ...
    querynotify: typing.Callable[[None], None] = ...
    iterintlinkfunc: typing.Callable[[Pad, typing.Optional[Object]], Iterator] = ...
    iterintlinkdata: None = ...
    iterintlinknotify: typing.Callable[[None], None] = ...
    num_probes: int = ...
    num_blocked: int = ...
    priv: PadPrivate = ...
    def __init__(self, direction: PadDirection = ...,
                 offset: int = ...,
                 template: PadTemplate = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def activate_mode(*args): ... # FIXME Function
    def add_probe(*args): ... # FIXME Function
    def can_link(*args): ... # FIXME Function
    def chain(*args): ... # FIXME Function
    def chain_list(*args): ... # FIXME Function
    def check_reconfigure(*args): ... # FIXME Function
    def create_stream_id(*args): ... # FIXME Function
    def do_linked(self, peer: Pad) -> None: ...
    def do_unlinked(self, peer: Pad) -> None: ...
    def event_default(*args): ... # FIXME Function
    def forward(*args): ... # FIXME Function
    def get_allowed_caps(*args): ... # FIXME Function
    def get_current_caps(*args): ... # FIXME Function
    def get_direction(*args): ... # FIXME Function
    def get_element_private(*args): ... # FIXME Function
    def get_last_flow_return(*args): ... # FIXME Function
    def get_offset(*args): ... # FIXME Function
    def get_pad_template(*args): ... # FIXME Function
    def get_pad_template_caps(*args): ... # FIXME Function
    def get_parent_element(*args): ... # FIXME Function
    def get_peer(*args): ... # FIXME Function
    def get_range(*args): ... # FIXME Function
    def get_single_internal_link(*args): ... # FIXME Function
    def get_sticky_event(*args): ... # FIXME Function
    def get_stream(*args): ... # FIXME Function
    def get_stream_id(*args): ... # FIXME Function
    def get_task_state(*args): ... # FIXME Function
    def has_current_caps(*args): ... # FIXME Function
    def is_active(*args): ... # FIXME Function
    def is_blocked(*args): ... # FIXME Function
    def is_blocking(*args): ... # FIXME Function
    def is_linked(*args): ... # FIXME Function
    def iterate_internal_links(*args): ... # FIXME Function
    def iterate_internal_links_default(*args): ... # FIXME Function
    def link(self, pad): ... # FIXME Function
    def link_full(*args): ... # FIXME Function
    def link_get_name(*args): ... # FIXME Function
    def link_maybe_ghosting(*args): ... # FIXME Function
    def link_maybe_ghosting_full(*args): ... # FIXME Function
    def mark_reconfigure(*args): ... # FIXME Function
    def needs_reconfigure(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_from_static_template(*args): ... # FIXME Function
    def new_from_template(*args): ... # FIXME Function
    def pause_task(*args): ... # FIXME Function
    def peer_query(*args): ... # FIXME Function
    def peer_query_accept_caps(*args): ... # FIXME Function
    def peer_query_caps(*args): ... # FIXME Function
    def peer_query_convert(*args): ... # FIXME Function
    def peer_query_duration(*args): ... # FIXME Function
    def peer_query_position(*args): ... # FIXME Function
    def proxy_query_accept_caps(*args): ... # FIXME Function
    def proxy_query_caps(*args): ... # FIXME Function
    def pull_range(*args): ... # FIXME Function
    def push(*args): ... # FIXME Function
    def push_event(*args): ... # FIXME Function
    def push_list(*args): ... # FIXME Function
    def query(*args): ... # FIXME Function
    def query_accept_caps(*args): ... # FIXME Function
    def query_caps(self, filter=None): ... # FIXME Function
    def query_convert(*args): ... # FIXME Function
    def query_default(*args): ... # FIXME Function
    def query_duration(*args): ... # FIXME Function
    def query_position(*args): ... # FIXME Function
    def remove_probe(*args): ... # FIXME Function
    def send_event(*args): ... # FIXME Function
    def set_activate_function_full(*args): ... # FIXME Function
    def set_activatemode_function_full(*args): ... # FIXME Function
    def set_active(*args): ... # FIXME Function
    def set_caps(self, caps): ... # FIXME Function
    def set_chain_function(self, func): ... # FIXME Function
    def set_chain_function_full(*args): ... # FIXME Function
    def set_chain_list_function_full(*args): ... # FIXME Function
    def set_element_private(*args): ... # FIXME Function
    def set_event_full_function_full(*args): ... # FIXME Function
    def set_event_function(self, func): ... # FIXME Function
    def set_event_function_full(*args): ... # FIXME Function
    def set_getrange_function_full(*args): ... # FIXME Function
    def set_iterate_internal_links_function_full(*args): ... # FIXME Function
    def set_link_function_full(*args): ... # FIXME Function
    def set_offset(*args): ... # FIXME Function
    def set_query_function(self, func): ... # FIXME Function
    def set_query_function_full(*args): ... # FIXME Function
    def set_unlink_function_full(*args): ... # FIXME Function
    def start_task(*args): ... # FIXME Function
    def sticky_events_foreach(*args): ... # FIXME Function
    def stop_task(*args): ... # FIXME Function
    def store_sticky_event(*args): ... # FIXME Function
    def unlink(*args): ... # FIXME Function
    def use_fixed_caps(*args): ... # FIXME Function
    

class PadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PadClass()
    """
    parent_class: ObjectClass = ...
    linked: typing.Callable[[Pad, Pad], None] = ...
    unlinked: typing.Callable[[Pad, Pad], None] = ...
    _gst_reserved: list[None] = ...

class PadPrivate(GObject.GPointer): ...

class PadProbeInfo(GObject.GPointer):
    """
    :Constructors:

    ::

        PadProbeInfo()
    """
    type: PadProbeType = ...
    id: int = ...
    data: None = ...
    offset: int = ...
    size: int = ...
    def get_buffer(*args): ... # FIXME Function
    def get_buffer_list(*args): ... # FIXME Function
    def get_event(*args): ... # FIXME Function
    def get_query(*args): ... # FIXME Function
    

class PadTemplate(Object):
    """
    :Constructors:

    ::

        PadTemplate(**properties)
        new(name_template:str, direction:Gst.PadDirection, presence:Gst.PadPresence, caps:Gst.Caps) -> Gst.PadTemplate or None
        new_from_static_pad_template_with_gtype(pad_template:Gst.StaticPadTemplate, pad_type:GType) -> Gst.PadTemplate or None
        new_with_gtype(name_template:str, direction:Gst.PadDirection, presence:Gst.PadPresence, caps:Gst.Caps, pad_type:GType) -> Gst.PadTemplate or None

    Object GstPadTemplate

    Signals from GstPadTemplate:
      pad-created (GstPad)

    Properties from GstPadTemplate:
      name-template -> gchararray: Name template
        The name template of the pad template
      direction -> GstPadDirection: Direction
        The direction of the pad described by the pad template
      presence -> GstPadPresence: Presence
        When the pad described by the pad template will become available
      gtype -> GType: GType
        The GType of the pad described by the pad template

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        caps: Caps
        direction: PadDirection
        gtype: typing.Type[typing.Any]
        name_template: str
        presence: PadPresence
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    name_template: str = ...
    direction: PadDirection = ...
    presence: PadPresence = ...
    caps: Caps = ...
    def __init__(self, caps: Caps = ...,
                 direction: PadDirection = ...,
                 gtype: typing.Type[typing.Any] = ...,
                 name_template: str = ...,
                 presence: PadPresence = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def do_pad_created(self, pad: Pad) -> None: ...
    def get_caps(*args): ... # FIXME Function
    def get_documentation_caps(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_from_static_pad_template_with_gtype(*args): ... # FIXME Function
    def new_with_gtype(*args): ... # FIXME Function
    def pad_created(*args): ... # FIXME Function
    def set_documentation_caps(*args): ... # FIXME Function
    

class PadTemplateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PadTemplateClass()
    """
    parent_class: ObjectClass = ...
    pad_created: typing.Callable[[PadTemplate, Pad], None] = ...
    _gst_reserved: list[None] = ...

class ParamArray(GObject.ParamSpec): ...

class ParamFraction(GObject.ParamSpec): ...

class ParamSpecArray(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecArray()
    """
    parent_instance: GObject.ParamSpec = ...
    element_spec: GObject.ParamSpec = ...

class ParamSpecFraction(GObject.GPointer):
    """
    :Constructors:

    ::

        ParamSpecFraction()
    """
    parent_instance: GObject.ParamSpec = ...
    min_num: int = ...
    min_den: int = ...
    max_num: int = ...
    max_den: int = ...
    def_num: int = ...
    def_den: int = ...

class ParentBufferMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        ParentBufferMeta()
    """
    parent: Meta = ...
    buffer: Buffer = ...
    def get_info(*args): ... # FIXME Function
    

class ParseContext(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gst.ParseContext or None
    """
    def copy(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def get_missing_elements(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    

class Pipeline(Bin, ChildProxy):
    """
    :Constructors:

    ::

        Pipeline(**properties)
        new(name:str=None) -> Gst.Element

    Object GstPipeline

    Properties from GstPipeline:
      delay -> guint64: Delay
        Expected delay needed for elements to spin up to PLAYING in nanoseconds
      auto-flush-bus -> gboolean: Auto Flush Bus
        Whether to automatically flush the pipeline's bus when going from READY into NULL state
      latency -> guint64: Latency
        Latency to configure on the pipeline

    Signals from GstChildProxy:
      child-added (GObject, gchararray)
      child-removed (GObject, gchararray)

    Signals from GstBin:
      element-added (GstElement)
      element-removed (GstElement)
      deep-element-added (GstBin, GstElement)
      deep-element-removed (GstBin, GstElement)
      do-latency () -> gboolean

    Properties from GstBin:
      async-handling -> gboolean: Async Handling
        The bin will handle Asynchronous state changes
      message-forward -> gboolean: Message Forward
        Forwards all children messages

    Signals from GstChildProxy:
      child-added (GObject, gchararray)
      child-removed (GObject, gchararray)

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        auto_flush_bus: bool
        delay: int
        latency: int
        async_handling: bool
        message_forward: bool
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    bin: Bin = ...
    fixed_clock: Clock = ...
    stream_time: int = ...
    delay: int = ...
    priv: PipelinePrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, auto_flush_bus: bool = ...,
                 delay: int = ...,
                 latency: int = ...,
                 async_handling: bool = ...,
                 message_forward: bool = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def auto_clock(*args): ... # FIXME Function
    def get_auto_flush_bus(*args): ... # FIXME Function
    def get_bus(*args): ... # FIXME Function
    def get_configured_latency(*args): ... # FIXME Function
    def get_delay(*args): ... # FIXME Function
    def get_latency(*args): ... # FIXME Function
    def get_pipeline_clock(*args): ... # FIXME Function
    def is_live(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def set_auto_flush_bus(*args): ... # FIXME Function
    def set_delay(*args): ... # FIXME Function
    def set_latency(*args): ... # FIXME Function
    def use_clock(*args): ... # FIXME Function
    

class PipelineClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PipelineClass()
    """
    parent_class: BinClass = ...
    _gst_reserved: list[None] = ...

class PipelinePrivate(GObject.GPointer): ...

class Plugin(Object):
    """
    :Constructors:

    ::

        Plugin(**properties)

    Object GstPlugin

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_dependency(*args): ... # FIXME Function
    def add_dependency_simple(*args): ... # FIXME Function
    def add_status_error(*args): ... # FIXME Function
    def add_status_info(*args): ... # FIXME Function
    def add_status_warning(*args): ... # FIXME Function
    def get_cache_data(*args): ... # FIXME Function
    def get_description(*args): ... # FIXME Function
    def get_filename(*args): ... # FIXME Function
    def get_license(*args): ... # FIXME Function
    def get_name(*args): ... # FIXME Function
    def get_origin(*args): ... # FIXME Function
    def get_package(*args): ... # FIXME Function
    def get_release_date_string(*args): ... # FIXME Function
    def get_source(*args): ... # FIXME Function
    def get_status_errors(*args): ... # FIXME Function
    def get_status_infos(*args): ... # FIXME Function
    def get_status_warnings(*args): ... # FIXME Function
    def get_version(*args): ... # FIXME Function
    def is_loaded(*args): ... # FIXME Function
    def list_free(*args): ... # FIXME Function
    def load(*args): ... # FIXME Function
    def load_by_name(*args): ... # FIXME Function
    def load_file(*args): ... # FIXME Function
    def register_static(*args): ... # FIXME Function
    def register_static_full(*args): ... # FIXME Function
    def set_cache_data(*args): ... # FIXME Function
    

class PluginClass(GObject.GPointer): ...

class PluginDesc(GObject.GPointer):
    """
    :Constructors:

    ::

        PluginDesc()
    """
    major_version: int = ...
    minor_version: int = ...
    name: str = ...
    description: str = ...
    plugin_init: typing.Callable[[Plugin], bool] = ...
    version: str = ...
    license: str = ...
    source: str = ...
    package: str = ...
    origin: str = ...
    release_datetime: str = ...
    _gst_reserved: list[None] = ...

class PluginFeature(Object):
    """
    :Constructors:

    ::

        PluginFeature(**properties)

    Object GstPluginFeature

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def check_version(*args): ... # FIXME Function
    def get_plugin(*args): ... # FIXME Function
    def get_plugin_name(*args): ... # FIXME Function
    def get_rank(*args): ... # FIXME Function
    def list_copy(*args): ... # FIXME Function
    def list_debug(*args): ... # FIXME Function
    def list_free(*args): ... # FIXME Function
    def load(*args): ... # FIXME Function
    def rank_compare_func(*args): ... # FIXME Function
    def set_rank(*args): ... # FIXME Function
    

class PluginFeatureClass(GObject.GPointer): ...

class Poll(GObject.GPointer):
    def add_fd(*args): ... # FIXME Function
    def fd_can_read(*args): ... # FIXME Function
    def fd_can_write(*args): ... # FIXME Function
    def fd_ctl_pri(*args): ... # FIXME Function
    def fd_ctl_read(*args): ... # FIXME Function
    def fd_ctl_write(*args): ... # FIXME Function
    def fd_has_closed(*args): ... # FIXME Function
    def fd_has_error(*args): ... # FIXME Function
    def fd_has_pri(*args): ... # FIXME Function
    def fd_ignored(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def get_read_gpollfd(*args): ... # FIXME Function
    def read_control(*args): ... # FIXME Function
    def remove_fd(*args): ... # FIXME Function
    def restart(*args): ... # FIXME Function
    def set_controllable(*args): ... # FIXME Function
    def set_flushing(*args): ... # FIXME Function
    def wait(*args): ... # FIXME Function
    def write_control(*args): ... # FIXME Function
    

class PollFD(GObject.GPointer):
    """
    :Constructors:

    ::

        PollFD()
    """
    fd: int = ...
    idx: int = ...
    def init(*args): ... # FIXME Function
    

class Preset(GObject.GInterface):
    """
    Interface GstPreset
    """
    def delete_preset(*args): ... # FIXME Function
    def get_app_dir(*args): ... # FIXME Function
    def get_meta(*args): ... # FIXME Function
    def get_preset_names(*args): ... # FIXME Function
    def get_property_names(*args): ... # FIXME Function
    def is_editable(*args): ... # FIXME Function
    def load_preset(*args): ... # FIXME Function
    def rename_preset(*args): ... # FIXME Function
    def save_preset(*args): ... # FIXME Function
    def set_app_dir(*args): ... # FIXME Function
    def set_meta(*args): ... # FIXME Function
    

class PresetInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PresetInterface()
    """
    parent: GObject.TypeInterface = ...
    get_preset_names: typing.Callable[[Preset], list[str]] = ...
    get_property_names: typing.Callable[[Preset], list[str]] = ...
    load_preset: typing.Callable[[Preset, str], bool] = ...
    save_preset: typing.Callable[[Preset, str], bool] = ...
    rename_preset: typing.Callable[[Preset, str, str], bool] = ...
    delete_preset: typing.Callable[[Preset, str], bool] = ...
    set_meta: typing.Callable[[Preset, str, str, typing.Optional[str]], bool] = ...
    get_meta: typing.Callable[[Preset, str, str], typing.Tuple[bool, str]] = ...
    _gst_reserved: list[None] = ...

class Promise(GObject.GBoxed):
    """
    :Constructors:

    ::

        Promise()
        new() -> Gst.Promise
        new_with_change_func(func:Gst.PromiseChangeFunc, user_data=None) -> Gst.Promise
    """
    parent: MiniObject = ...
    def expire(*args): ... # FIXME Function
    def get_reply(*args): ... # FIXME Function
    def interrupt(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_with_change_func(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def reply(*args): ... # FIXME Function
    def unref(*args): ... # FIXME Function
    def wait(*args): ... # FIXME Function
    

class ProtectionMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        ProtectionMeta()
    """
    meta: Meta = ...
    info: Structure = ...
    def get_info(*args): ... # FIXME Function
    

class ProxyPad(Pad):
    """
    :Constructors:

    ::

        ProxyPad(**properties)

    Object GstProxyPad

    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)

    Properties from GstPad:
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
      offset -> gint64: Offset
        The running time offset of the pad

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        caps: Caps
        direction: PadDirection
        offset: int
        template: PadTemplate
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    pad: Pad = ...
    priv: ProxyPadPrivate = ...
    def __init__(self, direction: PadDirection = ...,
                 offset: int = ...,
                 template: PadTemplate = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def chain_default(*args): ... # FIXME Function
    def chain_list_default(*args): ... # FIXME Function
    def get_internal(*args): ... # FIXME Function
    def getrange_default(*args): ... # FIXME Function
    def iterate_internal_links_default(*args): ... # FIXME Function
    

class ProxyPadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyPadClass()
    """
    parent_class: PadClass = ...
    _gst_reserved: list[None] = ...

class ProxyPadPrivate(GObject.GPointer): ...

class Query(GObject.GBoxed):
    """
    :Constructors:

    ::

        Query()
        new_accept_caps(caps:Gst.Caps) -> Gst.Query
        new_allocation(caps:Gst.Caps=None, need_pool:bool) -> Gst.Query
        new_bitrate() -> Gst.Query
        new_buffering(format:Gst.Format) -> Gst.Query
        new_caps(filter:Gst.Caps) -> Gst.Query
        new_context(context_type:str) -> Gst.Query
        new_convert(src_format:Gst.Format, value:int, dest_format:Gst.Format) -> Gst.Query
        new_custom(type:Gst.QueryType, structure:Gst.Structure=None) -> Gst.Query
        new_drain() -> Gst.Query
        new_duration(format:Gst.Format) -> Gst.Query
        new_formats() -> Gst.Query
        new_latency() -> Gst.Query
        new_position(format:Gst.Format) -> Gst.Query
        new_scheduling() -> Gst.Query
        new_seeking(format:Gst.Format) -> Gst.Query
        new_segment(format:Gst.Format) -> Gst.Query
        new_selectable() -> Gst.Query
        new_uri() -> Gst.Query
    """
    mini_object: MiniObject = ...
    type: QueryType = ...
    def add_allocation_meta(*args): ... # FIXME Function
    def add_allocation_param(*args): ... # FIXME Function
    def add_allocation_pool(*args): ... # FIXME Function
    def add_buffering_range(*args): ... # FIXME Function
    def add_scheduling_mode(*args): ... # FIXME Function
    def find_allocation_meta(*args): ... # FIXME Function
    def get_n_allocation_metas(*args): ... # FIXME Function
    def get_n_allocation_params(*args): ... # FIXME Function
    def get_n_allocation_pools(*args): ... # FIXME Function
    def get_n_buffering_ranges(*args): ... # FIXME Function
    def get_n_scheduling_modes(*args): ... # FIXME Function
    def get_structure(*args): ... # FIXME Function
    def has_scheduling_mode(*args): ... # FIXME Function
    def has_scheduling_mode_with_flags(*args): ... # FIXME Function
    def new_accept_caps(*args): ... # FIXME Function
    def new_allocation(*args): ... # FIXME Function
    def new_bitrate(*args): ... # FIXME Function
    def new_buffering(*args): ... # FIXME Function
    def new_caps(*args): ... # FIXME Function
    def new_context(*args): ... # FIXME Function
    def new_convert(*args): ... # FIXME Function
    def new_custom(*args): ... # FIXME Function
    def new_drain(*args): ... # FIXME Function
    def new_duration(*args): ... # FIXME Function
    def new_formats(*args): ... # FIXME Function
    def new_latency(*args): ... # FIXME Function
    def new_position(*args): ... # FIXME Function
    def new_scheduling(*args): ... # FIXME Function
    def new_seeking(*args): ... # FIXME Function
    def new_segment(*args): ... # FIXME Function
    def new_selectable(*args): ... # FIXME Function
    def new_uri(*args): ... # FIXME Function
    def parse_accept_caps(*args): ... # FIXME Function
    def parse_accept_caps_result(*args): ... # FIXME Function
    def parse_allocation(*args): ... # FIXME Function
    def parse_bitrate(*args): ... # FIXME Function
    def parse_buffering_percent(*args): ... # FIXME Function
    def parse_buffering_range(*args): ... # FIXME Function
    def parse_buffering_stats(*args): ... # FIXME Function
    def parse_caps(*args): ... # FIXME Function
    def parse_caps_result(*args): ... # FIXME Function
    def parse_context(*args): ... # FIXME Function
    def parse_context_type(*args): ... # FIXME Function
    def parse_convert(*args): ... # FIXME Function
    def parse_duration(*args): ... # FIXME Function
    def parse_latency(*args): ... # FIXME Function
    def parse_n_formats(*args): ... # FIXME Function
    def parse_nth_allocation_meta(*args): ... # FIXME Function
    def parse_nth_allocation_param(*args): ... # FIXME Function
    def parse_nth_allocation_pool(*args): ... # FIXME Function
    def parse_nth_buffering_range(*args): ... # FIXME Function
    def parse_nth_format(*args): ... # FIXME Function
    def parse_nth_scheduling_mode(*args): ... # FIXME Function
    def parse_position(*args): ... # FIXME Function
    def parse_scheduling(*args): ... # FIXME Function
    def parse_seeking(*args): ... # FIXME Function
    def parse_segment(*args): ... # FIXME Function
    def parse_selectable(*args): ... # FIXME Function
    def parse_uri(*args): ... # FIXME Function
    def parse_uri_redirection(*args): ... # FIXME Function
    def parse_uri_redirection_permanent(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def remove_nth_allocation_meta(*args): ... # FIXME Function
    def remove_nth_allocation_param(*args): ... # FIXME Function
    def remove_nth_allocation_pool(*args): ... # FIXME Function
    def set_accept_caps_result(*args): ... # FIXME Function
    def set_bitrate(*args): ... # FIXME Function
    def set_buffering_percent(*args): ... # FIXME Function
    def set_buffering_range(*args): ... # FIXME Function
    def set_buffering_stats(*args): ... # FIXME Function
    def set_caps_result(*args): ... # FIXME Function
    def set_context(*args): ... # FIXME Function
    def set_convert(*args): ... # FIXME Function
    def set_duration(*args): ... # FIXME Function
    def set_formatsv(*args): ... # FIXME Function
    def set_latency(*args): ... # FIXME Function
    def set_nth_allocation_param(*args): ... # FIXME Function
    def set_nth_allocation_pool(*args): ... # FIXME Function
    def set_position(*args): ... # FIXME Function
    def set_scheduling(*args): ... # FIXME Function
    def set_seeking(*args): ... # FIXME Function
    def set_segment(*args): ... # FIXME Function
    def set_selectable(*args): ... # FIXME Function
    def set_uri(*args): ... # FIXME Function
    def set_uri_redirection(*args): ... # FIXME Function
    def set_uri_redirection_permanent(*args): ... # FIXME Function
    def take(*args): ... # FIXME Function
    def writable_structure(*args): ... # FIXME Function
    

class ReferenceTimestampMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        ReferenceTimestampMeta()
    """
    parent: Meta = ...
    reference: Caps = ...
    timestamp: int = ...
    duration: int = ...
    def get_info(*args): ... # FIXME Function
    

class Registry(Object):
    """
    :Constructors:

    ::

        Registry(**properties)

    Object GstRegistry

    Signals from GstRegistry:
      plugin-added (GstPlugin)
      feature-added (GstPluginFeature)

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    priv: RegistryPrivate = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_feature(*args): ... # FIXME Function
    def add_plugin(*args): ... # FIXME Function
    def check_feature_version(*args): ... # FIXME Function
    def feature_filter(*args): ... # FIXME Function
    def find_feature(*args): ... # FIXME Function
    def find_plugin(*args): ... # FIXME Function
    def fork_is_enabled(*args): ... # FIXME Function
    def fork_set_enabled(*args): ... # FIXME Function
    def get(*args): ... # FIXME Function
    def get_feature_list(*args): ... # FIXME Function
    def get_feature_list_by_plugin(*args): ... # FIXME Function
    def get_feature_list_cookie(*args): ... # FIXME Function
    def get_plugin_list(*args): ... # FIXME Function
    def lookup(*args): ... # FIXME Function
    def lookup_feature(*args): ... # FIXME Function
    def plugin_filter(*args): ... # FIXME Function
    def remove_feature(*args): ... # FIXME Function
    def remove_plugin(*args): ... # FIXME Function
    def scan_path(*args): ... # FIXME Function
    

class RegistryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RegistryClass()
    """
    parent_class: ObjectClass = ...

class RegistryPrivate(GObject.GPointer): ...

class Sample(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(buffer:Gst.Buffer=None, caps:Gst.Caps=None, segment:Gst.Segment=None, info:Gst.Structure=None) -> Gst.Sample
    """
    def get_buffer(*args): ... # FIXME Function
    def get_buffer_list(*args): ... # FIXME Function
    def get_caps(*args): ... # FIXME Function
    def get_info(*args): ... # FIXME Function
    def get_segment(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def set_buffer(*args): ... # FIXME Function
    def set_buffer_list(*args): ... # FIXME Function
    def set_caps(*args): ... # FIXME Function
    def set_info(*args): ... # FIXME Function
    def set_segment(*args): ... # FIXME Function
    

class Segment(GObject.GBoxed):
    """
    :Constructors:

    ::

        Segment()
        new() -> Gst.Segment
    """
    flags: SegmentFlags = ...
    rate: float = ...
    applied_rate: float = ...
    format: Format = ...
    base: int = ...
    offset: int = ...
    start: int = ...
    stop: int = ...
    time: int = ...
    position: int = ...
    duration: int = ...
    _gst_reserved: list[None] = ...
    def clip(*args): ... # FIXME Function
    def copy(*args): ... # FIXME Function
    def copy_into(*args): ... # FIXME Function
    def do_seek(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def init(*args): ... # FIXME Function
    def is_equal(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def offset_running_time(*args): ... # FIXME Function
    def position_from_running_time(*args): ... # FIXME Function
    def position_from_running_time_full(*args): ... # FIXME Function
    def position_from_stream_time(*args): ... # FIXME Function
    def position_from_stream_time_full(*args): ... # FIXME Function
    def set_running_time(*args): ... # FIXME Function
    def to_position(*args): ... # FIXME Function
    def to_running_time(*args): ... # FIXME Function
    def to_running_time_full(*args): ... # FIXME Function
    def to_stream_time(*args): ... # FIXME Function
    def to_stream_time_full(*args): ... # FIXME Function
    

class SharedTaskPool(TaskPool):
    """
    :Constructors:

    ::

        SharedTaskPool(**properties)
        new() -> Gst.TaskPool

    Object GstSharedTaskPool

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    parent: TaskPool = ...
    priv: SharedTaskPoolPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def get_max_threads(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def set_max_threads(*args): ... # FIXME Function
    

class SharedTaskPoolClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SharedTaskPoolClass()
    """
    parent_class: TaskPoolClass = ...
    _gst_reserved: list[None] = ...

class SharedTaskPoolPrivate(GObject.GPointer): ...

class StaticCaps(GObject.GPointer):
    """
    :Constructors:

    ::

        StaticCaps()
    """
    caps: Caps = ...
    string: str = ...
    _gst_reserved: list[None] = ...
    def cleanup(*args): ... # FIXME Function
    def get(*args): ... # FIXME Function
    

class StaticPadTemplate(GObject.GPointer):
    """
    :Constructors:

    ::

        StaticPadTemplate()
    """
    name_template: str = ...
    direction: PadDirection = ...
    presence: PadPresence = ...
    static_caps: StaticCaps = ...
    def get(*args): ... # FIXME Function
    def get_caps(*args): ... # FIXME Function
    

class Stream(Object):
    """
    :Constructors:

    ::

        Stream(**properties)
        new(stream_id:str=None, caps:Gst.Caps=None, type:Gst.StreamType, flags:Gst.StreamFlags) -> Gst.Stream

    Object GstStream

    Properties from GstStream:
      stream-id -> gchararray: Stream ID
        The stream ID of the stream
      stream-flags -> GstStreamFlags: Stream Flags
        The stream flags
      stream-type -> GstStreamType: Stream Type
        The type of stream

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        caps: typing.Optional[Caps]
        stream_flags: StreamFlags
        stream_id: typing.Optional[str]
        stream_type: StreamType
        tags: typing.Optional[TagList]
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    stream_id: str = ...
    priv: StreamPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, caps: typing.Optional[Caps] = ...,
                 stream_flags: StreamFlags = ...,
                 stream_id: str = ...,
                 stream_type: StreamType = ...,
                 tags: typing.Optional[TagList] = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def get_caps(*args): ... # FIXME Function
    def get_stream_flags(*args): ... # FIXME Function
    def get_stream_id(*args): ... # FIXME Function
    def get_stream_type(*args): ... # FIXME Function
    def get_tags(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def set_caps(*args): ... # FIXME Function
    def set_stream_flags(*args): ... # FIXME Function
    def set_stream_type(*args): ... # FIXME Function
    def set_tags(*args): ... # FIXME Function
    

class StreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamClass()
    """
    parent_class: ObjectClass = ...
    _gst_reserved: list[None] = ...

class StreamCollection(Object):
    """
    :Constructors:

    ::

        StreamCollection(**properties)
        new(upstream_id:str=None) -> Gst.StreamCollection

    Object GstStreamCollection

    Signals from GstStreamCollection:
      stream-notify (GstStream, GParam)

    Properties from GstStreamCollection:
      upstream-id -> gchararray: Upstream ID
        The stream ID of the parent stream

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        upstream_id: typing.Optional[str]
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    upstream_id: str = ...
    priv: StreamCollectionPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, upstream_id: str = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def add_stream(*args): ... # FIXME Function
    def do_stream_notify(self, stream: Stream, pspec: GObject.ParamSpec) -> None: ...
    def get_size(*args): ... # FIXME Function
    def get_stream(*args): ... # FIXME Function
    def get_upstream_id(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    

class StreamCollectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamCollectionClass()
    """
    parent_class: ObjectClass = ...
    stream_notify: typing.Callable[[StreamCollection, Stream, GObject.ParamSpec], None] = ...
    _gst_reserved: list[None] = ...

class StreamCollectionPrivate(GObject.GPointer): ...

class StreamPrivate(GObject.GPointer): ...

class Structure(GObject.GBoxed):
    """
    :Constructors:

    ::

        Structure()
        from_string(string:str) -> Gst.Structure or None, end:str
        new_empty(name:str) -> Gst.Structure
        new_from_string(string:str) -> Gst.Structure or None
        new_id_empty(quark:int) -> Gst.Structure
    """
    type: typing.Type[typing.Any] = ...
    name: int = ...
    def can_intersect(*args): ... # FIXME Function
    def copy(*args): ... # FIXME Function
    def filter_and_map_in_place(*args): ... # FIXME Function
    def fixate(*args): ... # FIXME Function
    def fixate_field(*args): ... # FIXME Function
    def fixate_field_boolean(*args): ... # FIXME Function
    def fixate_field_nearest_double(*args): ... # FIXME Function
    def fixate_field_nearest_fraction(*args): ... # FIXME Function
    def fixate_field_nearest_int(*args): ... # FIXME Function
    def fixate_field_string(*args): ... # FIXME Function
    def foreach(*args): ... # FIXME Function
    def free(*args): ... # FIXME Function
    def from_string(*args): ... # FIXME Function
    def get_array(*args): ... # FIXME Function
    def get_boolean(*args): ... # FIXME Function
    def get_clock_time(*args): ... # FIXME Function
    def get_date(*args): ... # FIXME Function
    def get_date_time(*args): ... # FIXME Function
    def get_double(*args): ... # FIXME Function
    def get_enum(*args): ... # FIXME Function
    def get_field_type(*args): ... # FIXME Function
    def get_flags(*args): ... # FIXME Function
    def get_flagset(*args): ... # FIXME Function
    def get_fraction(*args): ... # FIXME Function
    def get_int(*args): ... # FIXME Function
    def get_int64(*args): ... # FIXME Function
    def get_list(*args): ... # FIXME Function
    def get_name(*args): ... # FIXME Function
    def get_name_id(*args): ... # FIXME Function
    def get_string(*args): ... # FIXME Function
    def get_uint(*args): ... # FIXME Function
    def get_uint64(*args): ... # FIXME Function
    def get_value(*args): ... # FIXME Function
    def has_field(*args): ... # FIXME Function
    def has_field_typed(*args): ... # FIXME Function
    def has_name(*args): ... # FIXME Function
    def id_get_value(*args): ... # FIXME Function
    def id_has_field(*args): ... # FIXME Function
    def id_has_field_typed(*args): ... # FIXME Function
    def id_set_value(*args): ... # FIXME Function
    def id_take_value(*args): ... # FIXME Function
    def intersect(*args): ... # FIXME Function
    def is_equal(*args): ... # FIXME Function
    def is_subset(*args): ... # FIXME Function
    def keys(self): ... # FIXME Function
    def map_in_place(*args): ... # FIXME Function
    def n_fields(*args): ... # FIXME Function
    def new_empty(*args): ... # FIXME Function
    def new_from_string(*args): ... # FIXME Function
    def new_id_empty(*args): ... # FIXME Function
    def nth_field_name(*args): ... # FIXME Function
    def remove_all_fields(*args): ... # FIXME Function
    def remove_field(*args): ... # FIXME Function
    def serialize(*args): ... # FIXME Function
    def serialize_full(*args): ... # FIXME Function
    def set_array(*args): ... # FIXME Function
    def set_list(*args): ... # FIXME Function
    def set_name(*args): ... # FIXME Function
    def set_parent_refcount(*args): ... # FIXME Function
    def set_value(*args): ... # FIXME Function
    def take(*args): ... # FIXME Function
    def take_value(*args): ... # FIXME Function
    def to_string(*args): ... # FIXME Function
    

class SystemClock(Clock):
    """
    :Constructors:

    ::

        SystemClock(**properties)

    Object GstSystemClock

    Properties from GstSystemClock:
      clock-type -> GstClockType: Clock type
        The type of underlying clock implementation used

    Signals from GstClock:
      synced (gboolean)

    Properties from GstClock:
      window-size -> gint: Window size
        The size of the window used to calculate rate and offset
      window-threshold -> gint: Window threshold
        The threshold to start calculating rate and offset
      timeout -> guint64: Timeout
        The amount of time, in nanoseconds, to sample master and slave clocks

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        clock_type: ClockType
        timeout: int
        window_size: int
        window_threshold: int
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    clock: Clock = ...
    priv: SystemClockPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, clock_type: ClockType = ...,
                 timeout: int = ...,
                 window_size: int = ...,
                 window_threshold: int = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def obtain(*args): ... # FIXME Function
    def set_default(*args): ... # FIXME Function
    

class SystemClockClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SystemClockClass()
    """
    parent_class: ClockClass = ...
    _gst_reserved: list[None] = ...

class SystemClockPrivate(GObject.GPointer): ...

class TagList(GObject.GBoxed):
    """
    :Constructors:

    ::

        TagList()
        new_empty() -> Gst.TagList
        new_from_string(str:str) -> Gst.TagList or None
    """
    mini_object: MiniObject = ...
    def add_value(*args): ... # FIXME Function
    def copy(*args): ... # FIXME Function
    def copy_value(*args): ... # FIXME Function
    def enumerate(self): ... # FIXME Function
    def foreach(*args): ... # FIXME Function
    def get_boolean(*args): ... # FIXME Function
    def get_boolean_index(*args): ... # FIXME Function
    def get_date(*args): ... # FIXME Function
    def get_date_index(*args): ... # FIXME Function
    def get_date_time(*args): ... # FIXME Function
    def get_date_time_index(*args): ... # FIXME Function
    def get_double(*args): ... # FIXME Function
    def get_double_index(*args): ... # FIXME Function
    def get_float(*args): ... # FIXME Function
    def get_float_index(*args): ... # FIXME Function
    def get_int(*args): ... # FIXME Function
    def get_int64(*args): ... # FIXME Function
    def get_int64_index(*args): ... # FIXME Function
    def get_int_index(*args): ... # FIXME Function
    def get_pointer(*args): ... # FIXME Function
    def get_pointer_index(*args): ... # FIXME Function
    def get_sample(*args): ... # FIXME Function
    def get_sample_index(*args): ... # FIXME Function
    def get_scope(*args): ... # FIXME Function
    def get_string(*args): ... # FIXME Function
    def get_string_index(*args): ... # FIXME Function
    def get_tag_size(*args): ... # FIXME Function
    def get_uint(*args): ... # FIXME Function
    def get_uint64(*args): ... # FIXME Function
    def get_uint64_index(*args): ... # FIXME Function
    def get_uint_index(*args): ... # FIXME Function
    def get_value_index(*args): ... # FIXME Function
    def insert(*args): ... # FIXME Function
    def is_empty(*args): ... # FIXME Function
    def is_equal(*args): ... # FIXME Function
    def keys(self): ... # FIXME Function
    def merge(*args): ... # FIXME Function
    def n_tags(*args): ... # FIXME Function
    def new_empty(*args): ... # FIXME Function
    def new_from_string(*args): ... # FIXME Function
    def nth_tag_name(*args): ... # FIXME Function
    def peek_string_index(*args): ... # FIXME Function
    def remove_tag(*args): ... # FIXME Function
    def replace(*args): ... # FIXME Function
    def set_scope(*args): ... # FIXME Function
    def take(*args): ... # FIXME Function
    def to_string(*args): ... # FIXME Function
    

class TagSetter(GObject.GInterface):
    """
    Interface GstTagSetter

    Signals from GObject:
      notify (GParam)
    """
    def add_tag_value(*args): ... # FIXME Function
    def get_tag_list(*args): ... # FIXME Function
    def get_tag_merge_mode(*args): ... # FIXME Function
    def merge_tags(*args): ... # FIXME Function
    def reset_tags(*args): ... # FIXME Function
    def set_tag_merge_mode(*args): ... # FIXME Function
    

class TagSetterInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        TagSetterInterface()
    """
    g_iface: GObject.TypeInterface = ...

class Task(Object):
    """
    :Constructors:

    ::

        Task(**properties)
        new(func:Gst.TaskFunction, user_data=None) -> Gst.Task

    Object GstTask

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    state: TaskState = ...
    cond: GLib.Cond = ...
    lock: GLib.RecMutex = ...
    func: typing.Callable[..., None] = ...
    user_data: None = ...
    notify: typing.Callable[[None], None] = ...
    running: bool = ...
    thread: GLib.Thread = ...
    priv: TaskPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def cleanup_all(*args): ... # FIXME Function
    def get_pool(*args): ... # FIXME Function
    def get_state(*args): ... # FIXME Function
    def join(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def pause(*args): ... # FIXME Function
    def resume(*args): ... # FIXME Function
    def set_enter_callback(*args): ... # FIXME Function
    def set_leave_callback(*args): ... # FIXME Function
    def set_lock(*args): ... # FIXME Function
    def set_pool(*args): ... # FIXME Function
    def set_state(*args): ... # FIXME Function
    def start(*args): ... # FIXME Function
    def stop(*args): ... # FIXME Function
    

class TaskClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TaskClass()
    """
    parent_class: ObjectClass = ...
    pool: TaskPool = ...
    _gst_reserved: list[None] = ...

class TaskPool(Object):
    """
    :Constructors:

    ::

        TaskPool(**properties)
        new() -> Gst.TaskPool

    Object GstTaskPool

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    object: Object = ...
    pool: GLib.ThreadPool = ...
    _gst_reserved: list[None] = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def cleanup(*args): ... # FIXME Function
    def dispose_handle(*args): ... # FIXME Function
    def do_cleanup(self) -> None: ...
    def do_dispose_handle(self, id: None) -> None: ...
    def do_join(self, id: None) -> None: ...
    def do_prepare(self) -> None: ...
    def do_push(self, func: typing.Callable[..., None], *user_data: typing.Any) -> None: ...
    def join(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def prepare(*args): ... # FIXME Function
    def push(*args): ... # FIXME Function
    

class TaskPoolClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TaskPoolClass()
    """
    parent_class: ObjectClass = ...
    prepare: typing.Callable[[TaskPool], None] = ...
    cleanup: typing.Callable[[TaskPool], None] = ...
    push: typing.Callable[..., None] = ...
    join: typing.Callable[[TaskPool, None], None] = ...
    dispose_handle: typing.Callable[[TaskPool, None], None] = ...
    _gst_reserved: list[None] = ...

class TaskPrivate(GObject.GPointer): ...

class TimedValue(GObject.GPointer):
    """
    :Constructors:

    ::

        TimedValue()
    """
    timestamp: int = ...
    value: float = ...

class Toc(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(scope:Gst.TocScope) -> Gst.Toc
    """
    def append_entry(*args): ... # FIXME Function
    def dump(*args): ... # FIXME Function
    def find_entry(*args): ... # FIXME Function
    def get_entries(*args): ... # FIXME Function
    def get_scope(*args): ... # FIXME Function
    def get_tags(*args): ... # FIXME Function
    def merge_tags(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def set_tags(*args): ... # FIXME Function
    

class TocEntry(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(type:Gst.TocEntryType, uid:str) -> Gst.TocEntry
    """
    def append_sub_entry(*args): ... # FIXME Function
    def get_entry_type(*args): ... # FIXME Function
    def get_loop(*args): ... # FIXME Function
    def get_parent(*args): ... # FIXME Function
    def get_start_stop_times(*args): ... # FIXME Function
    def get_sub_entries(*args): ... # FIXME Function
    def get_tags(*args): ... # FIXME Function
    def get_toc(*args): ... # FIXME Function
    def get_uid(*args): ... # FIXME Function
    def is_alternative(*args): ... # FIXME Function
    def is_sequence(*args): ... # FIXME Function
    def merge_tags(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def set_loop(*args): ... # FIXME Function
    def set_start_stop_times(*args): ... # FIXME Function
    def set_tags(*args): ... # FIXME Function
    

class TocSetter(GObject.GInterface):
    """
    Interface GstTocSetter

    Signals from GObject:
      notify (GParam)
    """
    def get_toc(*args): ... # FIXME Function
    def reset(*args): ... # FIXME Function
    def set_toc(*args): ... # FIXME Function
    

class TocSetterInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        TocSetterInterface()
    """
    g_iface: GObject.TypeInterface = ...

class Tracer(Object):
    """
    :Constructors:

    ::

        Tracer(**properties)

    Object GstTracer

    Properties from GstTracer:
      params -> gchararray: Params
        Extra configuration parameters

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        params: str
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    parent: Object = ...
    priv: TracerPrivate = ...
    _gst_reserved: list[None] = ...
    def __init__(self, params: str = ...,
                 name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def register(*args): ... # FIXME Function
    

class TracerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TracerClass()
    """
    parent_class: ObjectClass = ...
    _gst_reserved: list[None] = ...

class TracerFactory(PluginFeature):
    """
    :Constructors:

    ::

        TracerFactory(**properties)

    Object GstTracerFactory

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def get_list(*args): ... # FIXME Function
    def get_tracer_type(*args): ... # FIXME Function
    

class TracerFactoryClass(GObject.GPointer): ...

class TracerPrivate(GObject.GPointer): ...

class TracerRecord(Object):
    """
    :Constructors:

    ::

        TracerRecord(**properties)

    Object GstTracerRecord

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...

class TracerRecordClass(GObject.GPointer): ...

class TypeFind(GObject.GPointer):
    """
    :Constructors:

    ::

        TypeFind()
    """
    peek: typing.Callable[[None, int, int], int] = ...
    suggest: typing.Callable[[None, int, Caps], None] = ...
    data: None = ...
    get_length: typing.Callable[[None], int] = ...
    _gst_reserved: list[None] = ...
    def get_length(*args): ... # FIXME Function
    def peek(*args): ... # FIXME Function
    def register(*args): ... # FIXME Function
    def suggest(*args): ... # FIXME Function
    def suggest_empty_simple(*args): ... # FIXME Function
    

class TypeFindFactory(PluginFeature):
    """
    :Constructors:

    ::

        TypeFindFactory(**properties)

    Object GstTypeFindFactory

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        name: typing.Optional[str]
        parent: typing.Optional[Object]
    props: Props = ...
    def __init__(self, name: typing.Optional[str] = ...,
                 parent: Object = ...) -> None: ...
    def call_function(*args): ... # FIXME Function
    def get_caps(*args): ... # FIXME Function
    def get_extensions(*args): ... # FIXME Function
    def get_list(*args): ... # FIXME Function
    def has_function(*args): ... # FIXME Function
    

class TypeFindFactoryClass(GObject.GPointer): ...

class URIHandler(GObject.GInterface):
    """
    Interface GstURIHandler
    """
    def get_protocols(*args): ... # FIXME Function
    def get_uri(*args): ... # FIXME Function
    def get_uri_type(*args): ... # FIXME Function
    def set_uri(*args): ... # FIXME Function
    

class URIHandlerInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        URIHandlerInterface()
    """
    parent: GObject.TypeInterface = ...
    get_type: typing.Callable[[typing.Type[typing.Any]], URIType] = ...
    get_protocols: typing.Callable[[typing.Type[typing.Any]], list[str]] = ...
    get_uri: typing.Callable[[URIHandler], typing.Optional[str]] = ...
    set_uri: typing.Callable[[URIHandler, str], bool] = ...

class Uri(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str=None, query:str=None, fragment:str=None) -> Gst.Uri
    """
    def append_path(*args): ... # FIXME Function
    def append_path_segment(*args): ... # FIXME Function
    def construct(*args): ... # FIXME Function
    def copy(*args): ... # FIXME Function
    def equal(*args): ... # FIXME Function
    def from_string(*args): ... # FIXME Function
    def from_string_escaped(*args): ... # FIXME Function
    def from_string_with_base(*args): ... # FIXME Function
    def get_fragment(*args): ... # FIXME Function
    def get_host(*args): ... # FIXME Function
    def get_location(*args): ... # FIXME Function
    def get_media_fragment_table(*args): ... # FIXME Function
    def get_path(*args): ... # FIXME Function
    def get_path_segments(*args): ... # FIXME Function
    def get_path_string(*args): ... # FIXME Function
    def get_port(*args): ... # FIXME Function
    def get_protocol(*args): ... # FIXME Function
    def get_query_keys(*args): ... # FIXME Function
    def get_query_string(*args): ... # FIXME Function
    def get_query_string_ordered(*args): ... # FIXME Function
    def get_query_table(*args): ... # FIXME Function
    def get_query_value(*args): ... # FIXME Function
    def get_scheme(*args): ... # FIXME Function
    def get_userinfo(*args): ... # FIXME Function
    def has_protocol(*args): ... # FIXME Function
    def is_normalized(*args): ... # FIXME Function
    def is_valid(*args): ... # FIXME Function
    def is_writable(*args): ... # FIXME Function
    def join(*args): ... # FIXME Function
    def join_strings(*args): ... # FIXME Function
    def make_writable(*args): ... # FIXME Function
    def new(*args): ... # FIXME Function
    def new_with_base(*args): ... # FIXME Function
    def normalize(*args): ... # FIXME Function
    def protocol_is_supported(*args): ... # FIXME Function
    def protocol_is_valid(*args): ... # FIXME Function
    def query_has_key(*args): ... # FIXME Function
    def ref(*args): ... # FIXME Function
    def remove_query_key(*args): ... # FIXME Function
    def set_fragment(*args): ... # FIXME Function
    def set_host(*args): ... # FIXME Function
    def set_path(*args): ... # FIXME Function
    def set_path_segments(*args): ... # FIXME Function
    def set_path_string(*args): ... # FIXME Function
    def set_port(*args): ... # FIXME Function
    def set_query_string(*args): ... # FIXME Function
    def set_query_table(*args): ... # FIXME Function
    def set_query_value(*args): ... # FIXME Function
    def set_scheme(*args): ... # FIXME Function
    def set_userinfo(*args): ... # FIXME Function
    def to_string(*args): ... # FIXME Function
    def to_string_with_keys(*args): ... # FIXME Function
    def unref(*args): ... # FIXME Function
    

class ValueArray:
    """
    :Constructors:

    ::

        ValueArray(**properties)
    """
    def append_and_take_value(*args): ... # FIXME Function
    def append_value(*args): ... # FIXME Function
    def get_size(*args): ... # FIXME Function
    def get_value(*args): ... # FIXME Function
    def init(*args): ... # FIXME Function
    def prepend_value(*args): ... # FIXME Function
    

class ValueList:
    """
    :Constructors:

    ::

        ValueList(**properties)
    """
    def append_and_take_value(*args): ... # FIXME Function
    def append_value(*args): ... # FIXME Function
    def concat(*args): ... # FIXME Function
    def get_size(*args): ... # FIXME Function
    def get_value(*args): ... # FIXME Function
    def init(*args): ... # FIXME Function
    def merge(*args): ... # FIXME Function
    def prepend_value(*args): ... # FIXME Function
    

class ValueTable(GObject.GPointer):
    """
    :Constructors:

    ::

        ValueTable()
    """
    type: typing.Type[typing.Any] = ...
    compare: typing.Callable[[typing.Any, typing.Any], int] = ...
    serialize: typing.Callable[[typing.Any], str] = ...
    deserialize: typing.Callable[[typing.Any, str], bool] = ...
    deserialize_with_pspec: typing.Callable[[typing.Any, str, GObject.ParamSpec], bool] = ...
    _gst_reserved: list[None] = ...

class AllocatorFlags(GObject.GFlags):
    CUSTOM_ALLOC = 16
    LAST = 1048576
    NO_COPY = 32

class BinFlags(GObject.GFlags):
    LAST = 524288
    NO_RESYNC = 16384
    STREAMS_AWARE = 32768

class BufferCopyFlags(GObject.GFlags):
    DEEP = 32
    FLAGS = 1
    MEMORY = 8
    MERGE = 16
    META = 4
    NONE = 0
    TIMESTAMPS = 2

class BufferFlags(GObject.GFlags):
    CORRUPTED = 256
    DECODE_ONLY = 32
    DELTA_UNIT = 8192
    DISCONT = 64
    DROPPABLE = 4096
    GAP = 2048
    HEADER = 1024
    LAST = 1048576
    LIVE = 16
    MARKER = 512
    NON_DROPPABLE = 65536
    RESYNC = 128
    SYNC_AFTER = 32768
    TAG_MEMORY = 16384

class BufferPoolAcquireFlags(GObject.GFlags):
    DISCONT = 4
    DONTWAIT = 2
    KEY_UNIT = 1
    LAST = 65536
    NONE = 0

class BusFlags(GObject.GFlags):
    FLAG_LAST = 32
    FLUSHING = 16

class CapsFlags(GObject.GFlags):
    ANY = 16

class ClockFlags(GObject.GFlags):
    CAN_DO_PERIODIC_ASYNC = 128
    CAN_DO_PERIODIC_SYNC = 64
    CAN_DO_SINGLE_ASYNC = 32
    CAN_DO_SINGLE_SYNC = 16
    CAN_SET_MASTER = 512
    CAN_SET_RESOLUTION = 256
    LAST = 4096
    NEEDS_STARTUP_SYNC = 1024

class DebugColorFlags(GObject.GFlags):
    BG_BLACK = 0
    BG_BLUE = 64
    BG_CYAN = 96
    BG_GREEN = 32
    BG_MAGENTA = 80
    BG_RED = 16
    BG_WHITE = 112
    BG_YELLOW = 48
    BOLD = 256
    FG_BLACK = 0
    FG_BLUE = 4
    FG_CYAN = 6
    FG_GREEN = 2
    FG_MAGENTA = 5
    FG_RED = 1
    FG_WHITE = 7
    FG_YELLOW = 3
    UNDERLINE = 512

class DebugGraphDetails(GObject.GFlags):
    ALL = 15
    CAPS_DETAILS = 2
    FULL_PARAMS = 16
    MEDIA_TYPE = 1
    NON_DEFAULT_PARAMS = 4
    STATES = 8
    VERBOSE = 4294967295

class ElementFlags(GObject.GFlags):
    INDEXABLE = 512
    LAST = 16384
    LOCKED_STATE = 16
    PROVIDE_CLOCK = 128
    REQUIRE_CLOCK = 256
    SINK = 32
    SOURCE = 64

class EventTypeFlags(GObject.GFlags):
    DOWNSTREAM = 2
    SERIALIZED = 4
    STICKY = 8
    STICKY_MULTI = 16
    UPSTREAM = 1

class GapFlags(GObject.GFlags):
    DATA = 1

class LockFlags(GObject.GFlags):
    EXCLUSIVE = 4
    LAST = 256
    READ = 1
    WRITE = 2

class MapFlags(GObject.GFlags):
    FLAG_LAST = 65536
    READ = 1
    WRITE = 2

class MemoryFlags(GObject.GFlags):
    LAST = 1048576
    NOT_MAPPABLE = 256
    NO_SHARE = 16
    PHYSICALLY_CONTIGUOUS = 128
    READONLY = 2
    ZERO_PADDED = 64
    ZERO_PREFIXED = 32

class MessageType(GObject.GFlags):
    ANY = 4294967295
    APPLICATION = 16384
    ASYNC_DONE = 2097152
    ASYNC_START = 1048576
    BUFFERING = 32
    CLOCK_LOST = 1024
    CLOCK_PROVIDE = 512
    DEVICE_ADDED = 2147483649
    DEVICE_CHANGED = 2147483655
    DEVICE_REMOVED = 2147483650
    DURATION_CHANGED = 262144
    ELEMENT = 32768
    EOS = 1
    ERROR = 2
    EXTENDED = 2147483648
    HAVE_CONTEXT = 1073741824
    INFO = 8
    INSTANT_RATE_REQUEST = 2147483656
    LATENCY = 524288
    NEED_CONTEXT = 536870912
    NEW_CLOCK = 2048
    PROGRESS = 33554432
    PROPERTY_NOTIFY = 2147483651
    QOS = 16777216
    REDIRECT = 2147483654
    REQUEST_STATE = 4194304
    RESET_TIME = 134217728
    SEGMENT_DONE = 131072
    SEGMENT_START = 65536
    STATE_CHANGED = 64
    STATE_DIRTY = 128
    STEP_DONE = 256
    STEP_START = 8388608
    STREAMS_SELECTED = 2147483653
    STREAM_COLLECTION = 2147483652
    STREAM_START = 268435456
    STREAM_STATUS = 8192
    STRUCTURE_CHANGE = 4096
    TAG = 16
    TOC = 67108864
    UNKNOWN = 0
    WARNING = 4
    @staticmethod
    def get_name(type: MessageType) -> str: ...
    @staticmethod
    def to_quark(type: MessageType) -> int: ...

class MetaFlags(GObject.GFlags):
    LAST = 65536
    LOCKED = 4
    NONE = 0
    POOLED = 2
    READONLY = 1

class MiniObjectFlags(GObject.GFlags):
    LAST = 16
    LOCKABLE = 1
    LOCK_READONLY = 2
    MAY_BE_LEAKED = 4

class ObjectFlags(GObject.GFlags):
    CONSTRUCTED = 2
    LAST = 16
    MAY_BE_LEAKED = 1

class PadFlags(GObject.GFlags):
    ACCEPT_INTERSECT = 32768
    ACCEPT_TEMPLATE = 65536
    BLOCKED = 16
    BLOCKING = 128
    EOS = 64
    FIXED_CAPS = 2048
    FLUSHING = 32
    LAST = 1048576
    NEED_PARENT = 256
    NEED_RECONFIGURE = 512
    PENDING_EVENTS = 1024
    PROXY_ALLOCATION = 8192
    PROXY_CAPS = 4096
    PROXY_SCHEDULING = 16384

class PadLinkCheck(GObject.GFlags):
    CAPS = 4
    DEFAULT = 5
    HIERARCHY = 1
    NOTHING = 0
    NO_RECONFIGURE = 8
    TEMPLATE_CAPS = 2

class PadProbeType(GObject.GFlags):
    ALL_BOTH = 1776
    BLOCK = 2
    BLOCKING = 3
    BLOCK_DOWNSTREAM = 114
    BLOCK_UPSTREAM = 130
    BUFFER = 16
    BUFFER_LIST = 32
    DATA_BOTH = 240
    DATA_DOWNSTREAM = 112
    DATA_UPSTREAM = 128
    EVENT_BOTH = 192
    EVENT_DOWNSTREAM = 64
    EVENT_FLUSH = 256
    EVENT_UPSTREAM = 128
    IDLE = 1
    INVALID = 0
    PULL = 8192
    PUSH = 4096
    QUERY_BOTH = 1536
    QUERY_DOWNSTREAM = 512
    QUERY_UPSTREAM = 1024
    SCHEDULING = 12288

class PadTemplateFlags(GObject.GFlags):
    LAST = 256

class ParseFlags(GObject.GFlags):
    FATAL_ERRORS = 1
    NONE = 0
    NO_SINGLE_ELEMENT_BINS = 2
    PLACE_IN_BIN = 4

class PipelineFlags(GObject.GFlags):
    FIXED_CLOCK = 524288
    LAST = 8388608

class PluginAPIFlags(GObject.GFlags):
    MEMBERS = 1

class PluginDependencyFlags(GObject.GFlags):
    FILE_NAME_IS_PREFIX = 8
    FILE_NAME_IS_SUFFIX = 4
    NONE = 0
    PATHS_ARE_DEFAULT_ONLY = 2
    PATHS_ARE_RELATIVE_TO_EXE = 16
    RECURSE = 1

class PluginFlags(GObject.GFlags):
    BLACKLISTED = 32
    CACHED = 16

class QueryTypeFlags(GObject.GFlags):
    DOWNSTREAM = 2
    SERIALIZED = 4
    UPSTREAM = 1

class SchedulingFlags(GObject.GFlags):
    BANDWIDTH_LIMITED = 4
    SEEKABLE = 1
    SEQUENTIAL = 2

class SeekFlags(GObject.GFlags):
    ACCURATE = 2
    FLUSH = 1
    INSTANT_RATE_CHANGE = 1024
    KEY_UNIT = 4
    NONE = 0
    SEGMENT = 8
    SKIP = 16
    SNAP_AFTER = 64
    SNAP_BEFORE = 32
    SNAP_NEAREST = 96
    TRICKMODE = 16
    TRICKMODE_FORWARD_PREDICTED = 512
    TRICKMODE_KEY_UNITS = 128
    TRICKMODE_NO_AUDIO = 256

class SegmentFlags(GObject.GFlags):
    NONE = 0
    RESET = 1
    SEGMENT = 8
    SKIP = 16
    TRICKMODE = 16
    TRICKMODE_FORWARD_PREDICTED = 512
    TRICKMODE_KEY_UNITS = 128
    TRICKMODE_NO_AUDIO = 256

class SerializeFlags(GObject.GFlags):
    BACKWARD_COMPAT = 1
    NONE = 0
    STRICT = 2

class StackTraceFlags(GObject.GFlags):
    FULL = 1
    NONE = 0

class StreamFlags(GObject.GFlags):
    NONE = 0
    SELECT = 2
    SPARSE = 1
    UNSELECT = 4

class StreamType(GObject.GFlags):
    AUDIO = 2
    CONTAINER = 8
    TEXT = 16
    UNKNOWN = 1
    VIDEO = 4
    @staticmethod
    def get_name(stype: StreamType) -> str: ...

class TracerValueFlags(GObject.GFlags):
    AGGREGATED = 2
    NONE = 0
    OPTIONAL = 1

class BufferingMode(GObject.GEnum):
    DOWNLOAD = 1
    LIVE = 3
    STREAM = 0
    TIMESHIFT = 2

class BusSyncReply(GObject.GEnum):
    ASYNC = 2
    DROP = 0
    PASS = 1

class CapsIntersectMode(GObject.GEnum):
    FIRST = 1
    ZIG_ZAG = 0

class ClockEntryType(GObject.GEnum):
    PERIODIC = 1
    SINGLE = 0

class ClockReturn(GObject.GEnum):
    BADTIME = 4
    BUSY = 3
    DONE = 7
    EARLY = 1
    ERROR = 5
    OK = 0
    UNSCHEDULED = 2
    UNSUPPORTED = 6

class ClockType(GObject.GEnum):
    MONOTONIC = 1
    OTHER = 2
    REALTIME = 0
    TAI = 3

class CoreError(GObject.GEnum):
    CAPS = 10
    CLOCK = 13
    DISABLED = 14
    EVENT = 8
    FAILED = 1
    MISSING_PLUGIN = 12
    NEGOTIATION = 7
    NOT_IMPLEMENTED = 3
    NUM_ERRORS = 15
    PAD = 5
    SEEK = 9
    STATE_CHANGE = 4
    TAG = 11
    THREAD = 6
    TOO_LAZY = 2
    @staticmethod
    def quark() -> int: ...

class DebugColorMode(GObject.GEnum):
    OFF = 0
    ON = 1
    UNIX = 2

class DebugLevel(GObject.GEnum):
    COUNT = 10
    DEBUG = 5
    ERROR = 1
    FIXME = 3
    INFO = 4
    LOG = 6
    MEMDUMP = 9
    NONE = 0
    TRACE = 7
    WARNING = 2
    @staticmethod
    def get_name(level: DebugLevel) -> str: ...

class EventType(GObject.GEnum):
    BUFFERSIZE = 23054
    CAPS = 12814
    CUSTOM_BOTH = 79367
    CUSTOM_BOTH_OOB = 81923
    CUSTOM_DOWNSTREAM = 71686
    CUSTOM_DOWNSTREAM_OOB = 74242
    CUSTOM_DOWNSTREAM_STICKY = 76830
    CUSTOM_UPSTREAM = 69121
    EOS = 28174
    FLUSH_START = 2563
    FLUSH_STOP = 5127
    GAP = 40966
    INSTANT_RATE_CHANGE = 46090
    INSTANT_RATE_SYNC_TIME = 66817
    LATENCY = 56321
    NAVIGATION = 53761
    PROTECTION = 33310
    QOS = 48641
    RECONFIGURE = 61441
    SEEK = 51201
    SEGMENT = 17934
    SEGMENT_DONE = 38406
    SELECT_STREAMS = 66561
    SINK_MESSAGE = 25630
    STEP = 58881
    STREAM_COLLECTION = 19230
    STREAM_GROUP_DONE = 26894
    STREAM_START = 10254
    TAG = 20510
    TOC = 30750
    TOC_SELECT = 64001
    UNKNOWN = 0
    @staticmethod
    def get_flags(type: EventType) -> EventTypeFlags: ...
    @staticmethod
    def get_name(type: EventType) -> str: ...
    @staticmethod
    def to_quark(type: EventType) -> int: ...
    @staticmethod
    def to_sticky_ordering(type: EventType) -> int: ...

class FlowReturn(GObject.GEnum):
    CUSTOM_ERROR = -100
    CUSTOM_ERROR_1 = -101
    CUSTOM_ERROR_2 = -102
    CUSTOM_SUCCESS = 100
    CUSTOM_SUCCESS_1 = 101
    CUSTOM_SUCCESS_2 = 102
    EOS = -3
    ERROR = -5
    FLUSHING = -2
    NOT_LINKED = -1
    NOT_NEGOTIATED = -4
    NOT_SUPPORTED = -6
    OK = 0

class Format(GObject.GEnum):
    BUFFERS = 4
    BYTES = 2
    DEFAULT = 1
    PERCENT = 5
    TIME = 3
    UNDEFINED = 0
    @staticmethod
    def get_by_nick(nick: str) -> Format: ...
    @staticmethod
    def get_details(format: Format) -> typing.Optional[FormatDefinition]: ...
    @staticmethod
    def get_name(format: Format) -> typing.Optional[str]: ...
    @staticmethod
    def iterate_definitions() -> Iterator: ...
    @staticmethod
    def register(nick: str, description: str) -> Format: ...
    @staticmethod
    def to_quark(format: Format) -> int: ...

class IteratorItem(GObject.GEnum):
    END = 2
    PASS = 1
    SKIP = 0

class IteratorResult(GObject.GEnum):
    DONE = 0
    ERROR = 3
    OK = 1
    RESYNC = 2

class LibraryError(GObject.GEnum):
    ENCODE = 6
    FAILED = 1
    INIT = 3
    NUM_ERRORS = 7
    SETTINGS = 5
    SHUTDOWN = 4
    TOO_LAZY = 2
    @staticmethod
    def quark() -> int: ...

class PadDirection(GObject.GEnum):
    SINK = 2
    SRC = 1
    UNKNOWN = 0

class PadLinkReturn(GObject.GEnum):
    NOFORMAT = -4
    NOSCHED = -5
    OK = 0
    REFUSED = -6
    WAS_LINKED = -2
    WRONG_DIRECTION = -3
    WRONG_HIERARCHY = -1

class PadMode(GObject.GEnum):
    NONE = 0
    PULL = 2
    PUSH = 1
    @staticmethod
    def get_name(mode: PadMode) -> str: ...

class PadPresence(GObject.GEnum):
    ALWAYS = 0
    REQUEST = 2
    SOMETIMES = 1

class PadProbeReturn(GObject.GEnum):
    DROP = 0
    HANDLED = 4
    OK = 1
    PASS = 3
    REMOVE = 2

class ParseError(GObject.GEnum):
    COULD_NOT_SET_PROPERTY = 4
    DELAYED_LINK = 7
    EMPTY = 6
    EMPTY_BIN = 5
    LINK = 3
    NO_SUCH_ELEMENT = 1
    NO_SUCH_PROPERTY = 2
    SYNTAX = 0
    @staticmethod
    def quark() -> int: ...

class PluginError(GObject.GEnum):
    DEPENDENCIES = 1
    MODULE = 0
    NAME_MISMATCH = 2
    @staticmethod
    def quark() -> int: ...

class ProgressType(GObject.GEnum):
    CANCELED = 3
    COMPLETE = 2
    CONTINUE = 1
    ERROR = 4
    START = 0

class PromiseResult(GObject.GEnum):
    EXPIRED = 3
    INTERRUPTED = 1
    PENDING = 0
    REPLIED = 2

class QOSType(GObject.GEnum):
    OVERFLOW = 0
    THROTTLE = 2
    UNDERFLOW = 1

class QueryType(GObject.GEnum):
    ACCEPT_CAPS = 40963
    ALLOCATION = 35846
    BITRATE = 51202
    BUFFERING = 28163
    CAPS = 43523
    CONTEXT = 48643
    CONVERT = 20483
    CUSTOM = 30723
    DRAIN = 46086
    DURATION = 5123
    FORMATS = 23043
    JITTER = 10243
    LATENCY = 7683
    POSITION = 2563
    RATE = 12803
    SCHEDULING = 38401
    SEEKING = 15363
    SEGMENT = 17923
    SELECTABLE = 53763
    UNKNOWN = 0
    URI = 33283
    @staticmethod
    def get_flags(type: QueryType) -> QueryTypeFlags: ...
    @staticmethod
    def get_name(type: QueryType) -> str: ...
    @staticmethod
    def to_quark(type: QueryType) -> int: ...

class Rank(GObject.GEnum):
    MARGINAL = 64
    NONE = 0
    PRIMARY = 256
    SECONDARY = 128

class ResourceError(GObject.GEnum):
    BUSY = 4
    CLOSE = 8
    FAILED = 1
    NOT_AUTHORIZED = 15
    NOT_FOUND = 3
    NO_SPACE_LEFT = 14
    NUM_ERRORS = 16
    OPEN_READ = 5
    OPEN_READ_WRITE = 7
    OPEN_WRITE = 6
    READ = 9
    SEEK = 11
    SETTINGS = 13
    SYNC = 12
    TOO_LAZY = 2
    WRITE = 10
    @staticmethod
    def quark() -> int: ...

class SearchMode(GObject.GEnum):
    AFTER = 2
    BEFORE = 1
    EXACT = 0

class SeekType(GObject.GEnum):
    END = 2
    NONE = 0
    SET = 1

class State(GObject.GEnum):
    NULL = 1
    PAUSED = 3
    PLAYING = 4
    READY = 2
    VOID_PENDING = 0

class StateChange(GObject.GEnum):
    NULL_TO_NULL = 9
    NULL_TO_READY = 10
    PAUSED_TO_PAUSED = 27
    PAUSED_TO_PLAYING = 28
    PAUSED_TO_READY = 26
    PLAYING_TO_PAUSED = 35
    PLAYING_TO_PLAYING = 36
    READY_TO_NULL = 17
    READY_TO_PAUSED = 19
    READY_TO_READY = 18
    @staticmethod
    def get_name(transition: StateChange) -> str: ...

class StateChangeReturn(GObject.GEnum):
    ASYNC = 2
    FAILURE = 0
    NO_PREROLL = 3
    SUCCESS = 1

class StreamError(GObject.GEnum):
    CODEC_NOT_FOUND = 6
    DECODE = 7
    DECRYPT = 12
    DECRYPT_NOKEY = 13
    DEMUX = 9
    ENCODE = 8
    FAILED = 1
    FORMAT = 11
    MUX = 10
    NOT_IMPLEMENTED = 3
    NUM_ERRORS = 14
    TOO_LAZY = 2
    TYPE_NOT_FOUND = 4
    WRONG_TYPE = 5
    @staticmethod
    def quark() -> int: ...

class StreamStatusType(GObject.GEnum):
    CREATE = 0
    DESTROY = 3
    ENTER = 1
    LEAVE = 2
    PAUSE = 9
    START = 8
    STOP = 10

class StructureChangeType(GObject.GEnum):
    LINK = 0
    UNLINK = 1

class TagFlag(GObject.GEnum):
    COUNT = 4
    DECODED = 3
    ENCODED = 2
    META = 1
    UNDEFINED = 0

class TagMergeMode(GObject.GEnum):
    APPEND = 3
    COUNT = 7
    KEEP = 5
    KEEP_ALL = 6
    PREPEND = 4
    REPLACE = 2
    REPLACE_ALL = 1
    UNDEFINED = 0

class TagScope(GObject.GEnum):
    GLOBAL = 1
    STREAM = 0

class TaskState(GObject.GEnum):
    PAUSED = 2
    STARTED = 0
    STOPPED = 1

class TocEntryType(GObject.GEnum):
    ANGLE = -3
    CHAPTER = 3
    EDITION = -1
    INVALID = 0
    TITLE = 1
    TRACK = 2
    VERSION = -2
    @staticmethod
    def get_nick(type: TocEntryType) -> str: ...

class TocLoopType(GObject.GEnum):
    FORWARD = 1
    NONE = 0
    PING_PONG = 3
    REVERSE = 2

class TocScope(GObject.GEnum):
    CURRENT = 2
    GLOBAL = 1

class TracerValueScope(GObject.GEnum):
    ELEMENT = 2
    PAD = 3
    PROCESS = 0
    THREAD = 1

class TypeFindProbability(GObject.GEnum):
    LIKELY = 80
    MAXIMUM = 100
    MINIMUM = 1
    NEARLY_CERTAIN = 99
    NONE = 0
    POSSIBLE = 50

class URIError(GObject.GEnum):
    BAD_REFERENCE = 3
    BAD_STATE = 2
    BAD_URI = 1
    UNSUPPORTED_PROTOCOL = 0
    @staticmethod
    def quark() -> int: ...

class URIType(GObject.GEnum):
    SINK = 1
    SRC = 2
    UNKNOWN = 0

