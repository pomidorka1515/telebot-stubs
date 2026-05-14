from abc import ABC
from io import IOBase
from pathlib import Path
from telebot import service_utils as service_utils
from telebot.formatting import apply_html_entities as apply_html_entities
from typing import Any, TypeVar
import logging

DISABLE_KEYLEN_ERROR: bool
DEPRECATION_STACK_SHOW_DEPTH: int
logger: logging.Logger

_T = TypeVar("_T")

def log_deprecation_warning(warning_message: str, logging_level: int = logging.WARNING) -> None: ...

class JsonSerializable:
    def to_json(self) -> Any: ...

class Dictionaryable:
    def to_dict(self) -> dict[Any, Any]: ...

class JsonDeserializable:
    @classmethod
    def de_json(cls, json_string: dict[str, Any]) -> Any: ...
    @staticmethod
    def check_json(json_type: dict[Any, Any], dict_copy: bool = True) -> dict[Any, Any]: ...

class Update(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    update_id: int
    message: Message | None
    edited_message: Message | None
    channel_post: Message | None
    edited_channel_post: Message | None
    inline_query: InlineQuery | None
    chosen_inline_result: ChosenInlineResult | None
    callback_query: CallbackQuery | None
    shipping_query: ShippingQuery | None
    pre_checkout_query: PreCheckoutQuery | None
    poll: Poll | None
    poll_answer: PollAnswer | None
    my_chat_member: ChatMemberUpdated | None
    chat_member: ChatMemberUpdated | None
    chat_join_request: ChatJoinRequest | None
    message_reaction: MessageReactionUpdated | None
    message_reaction_count: MessageReactionCountUpdated | None
    removed_chat_boost: ChatBoostRemoved | None
    chat_boost: ChatBoostUpdated | None
    business_connection: BusinessConnection | None
    business_message: Message | None
    edited_business_message: Message | None
    deleted_business_messages: BusinessMessagesDeleted | None
    purchased_paid_media: PaidMediaPurchased | None
    managed_bot: ManagedBotUpdated | None
    def __init__(self, update_id: int, message: Message | None, edited_message: Message | None, channel_post: Message | None, edited_channel_post: Message | None, inline_query: InlineQuery | None, chosen_inline_result: ChosenInlineResult | None, callback_query: CallbackQuery | None, shipping_query: ShippingQuery | None, pre_checkout_query: PreCheckoutQuery | None, poll: Poll | None, poll_answer: PollAnswer | None, my_chat_member: ChatMemberUpdated | None, chat_member: ChatMemberUpdated | None, chat_join_request: ChatJoinRequest | None, message_reaction: MessageReactionUpdated | None, message_reaction_count: MessageReactionCountUpdated | None, removed_chat_boost: ChatBoostRemoved | None, chat_boost: ChatBoostUpdated | None, business_connection: BusinessConnection | None, business_message: Message | None, edited_business_message: Message | None, deleted_business_messages: BusinessMessagesDeleted | None, purchased_paid_media: PaidMediaPurchased | None, managed_bot: ManagedBotUpdated | None) -> None: ...

class ChatMemberUpdated(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    from_user: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink | None
    via_join_request: bool | None
    via_chat_folder_invite_link: bool | None
    def __init__(self, chat: Chat, from_user: User, date: int, old_chat_member: ChatMember, new_chat_member: ChatMember, invite_link: ChatInviteLink | None = None, via_join_request: bool | None = None, via_chat_folder_invite_link: bool | None = None, **kwargs: Any) -> None: ...
    @property
    def difference(self) -> dict[str, list[Any]]: ...

class ChatJoinRequest(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    from_user: User
    date: str
    bio: str | None
    invite_link: ChatInviteLink | None
    user_chat_id: int
    def __init__(self, chat: Chat, from_user: User, user_chat_id: int, date: str, bio: str | None = None, invite_link: ChatInviteLink | None = None, **kwargs: Any) -> None: ...

class WebhookInfo(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: str | None
    last_error_date: int | None
    last_error_message: str | None
    last_synchronization_error_date: int | None
    max_connections: int | None
    allowed_updates: int | None
    def __init__(self, url: str, has_custom_certificate: bool, pending_update_count: int, ip_address: str | None = None, last_error_date: int | None = None, last_error_message: str | None = None, last_synchronization_error_date: int | None = None, max_connections: int | None = None, allowed_updates: int | None = None, **kwargs: Any) -> None: ...

class User(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: int
    is_bot: bool
    first_name: str
    username: str | None
    last_name: str | None
    language_code: str | None
    can_join_groups: bool | None
    can_read_all_group_messages: bool | None
    supports_inline_queries: bool | None
    is_premium: bool | None
    added_to_attachment_menu: bool | None
    can_connect_to_business: bool | None
    has_main_web_app: bool | None
    has_topics_enabled: bool | None
    allows_users_to_create_topics: bool | None
    can_manage_bots: bool | None
    def __init__(self, id: int, is_bot: bool, first_name: str, last_name: str | None = None, username: str | None = None, language_code: str | None = None, can_join_groups: bool | None = None, can_read_all_group_messages: bool | None = None, supports_inline_queries: bool | None = None, is_premium: bool | None = None, added_to_attachment_menu: bool | None = None, can_connect_to_business: bool | None = None, has_main_web_app: bool | None = None, has_topics_enabled: bool | None = None, allows_users_to_create_topics: bool | None = None, can_manage_bots: bool | None = None, **kwargs: Any) -> None: ...
    @property
    def full_name(self) -> str: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class GroupChat(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: int
    title: str
    def __init__(self, id: int, title: str, **kwargs: Any) -> None: ...

class ChatFullInfo(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: int
    type: str
    title: str | None
    username: str | None
    first_name: str | None
    last_name: str | None
    is_forum: bool | None
    max_reaction_count: int | None
    photo: ChatPhoto | None
    bio: str | None
    join_to_send_messages: bool | None
    join_by_request: bool | None
    has_private_forwards: bool | None
    has_restricted_voice_and_video_messages: bool | None
    description: str | None
    invite_link: str | None
    pinned_message: Message | None
    permissions: ChatPermissions | None
    slow_mode_delay: int | None
    message_auto_delete_time: int | None
    has_protected_content: bool | None
    sticker_set_name: str | None
    can_set_sticker_set: bool | None
    linked_chat_id: int | None
    location: ChatLocation | None
    active_usernames: list[str] | None
    emoji_status_custom_emoji_id: str | None
    has_hidden_members: bool | None
    has_aggressive_anti_spam_enabled: bool | None
    emoji_status_expiration_date: int | None
    available_reactions: list[ReactionType] | None
    accent_color_id: int | None
    background_custom_emoji_id: str | None
    profile_accent_color_id: int | None
    profile_background_custom_emoji_id: str | None
    has_visible_history: bool | None
    unrestrict_boost_count: int | None
    custom_emoji_sticker_set_name: str | None
    business_intro: BusinessIntro | None
    business_location: BusinessLocation | None
    business_opening_hours: BusinessOpeningHours | None
    personal_chat: Chat | None
    birthdate: Birthdate | None
    can_send_paid_media: bool | None
    accepted_gift_types: AcceptedGiftTypes | None
    is_direct_messages: bool | None
    parent_chat: Chat | None
    rating: UserRating | None
    paid_message_star_count: int | None
    unique_gift_colors: UniqueGiftColors | None
    first_profile_audio: Audio | None
    def __init__(self, id: int, type: str, title: str | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, photo: ChatPhoto | None = None, bio: str | None = None, has_private_forwards: bool | None = None, description: str | None = None, invite_link: str | None = None, pinned_message: Message | None = None, permissions: ChatPermissions | None = None, slow_mode_delay: int | None = None, message_auto_delete_time: int | None = None, has_protected_content: bool | None = None, sticker_set_name: str | None = None, can_set_sticker_set: bool | None = None, linked_chat_id: int | None = None, location: ChatLocation | None = None, join_to_send_messages: bool | None = None, join_by_request: bool | None = None, has_restricted_voice_and_video_messages: bool | None = None, is_forum: bool | None = None, max_reaction_count: int | None = None, active_usernames: list[str] | None = None, emoji_status_custom_emoji_id: str | None = None, has_hidden_members: bool | None = None, has_aggressive_anti_spam_enabled: bool | None = None, emoji_status_expiration_date: int | None = None, available_reactions: list[ReactionType] | None = None, accent_color_id: int | None = None, background_custom_emoji_id: str | None = None, profile_accent_color_id: int | None = None, profile_background_custom_emoji_id: str | None = None, has_visible_history: bool | None = None, unrestrict_boost_count: int | None = None, custom_emoji_sticker_set_name: str | None = None, business_intro: BusinessIntro | None = None, business_location: BusinessLocation | None = None, business_opening_hours: BusinessOpeningHours | None = None, personal_chat: Chat | None = None, birthdate: Birthdate | None = None, can_send_paid_media: bool | None = None, accepted_gift_types: AcceptedGiftTypes | None = None, is_direct_messages: bool | None = None, parent_chat: Chat | None = None, rating: UserRating | None = None, paid_message_star_count: int | None = None, unique_gift_colors: UniqueGiftColors | None = None, first_profile_audio: Audio | None = None, **kwargs: Any) -> None: ...
    @property
    def can_send_gift(self) -> bool: ...

class Chat(ChatFullInfo): ...

class MessageID(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    message_id: int
    def __init__(self, message_id: int, **kwargs: Any) -> None: ...

class WebAppData(JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    data: str
    button_text: str
    def __init__(self, data: str, button_text: str, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class Message(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    @classmethod
    def parse_chat(cls, chat: Chat) -> User | GroupChat: ...
    @classmethod
    def parse_photo(cls, photo_size_array: list[dict[str, Any]]) -> list[PhotoSize]: ...
    @classmethod
    def parse_entities(cls, message_entity_array: list[dict[str, Any]]) -> list[MessageEntity]: ...
    content_type: str
    id: int
    message_id: int
    from_user: User | None
    date: int
    chat: Chat
    sender_chat: Chat | None
    is_automatic_forward: bool | None
    reply_to_message: Message | None
    via_bot: User | None
    edit_date: int | None
    has_protected_content: bool | None
    media_group_id: str | None
    author_signature: str | None
    text: str | None
    entities: list[MessageEntity] | None
    caption_entities: list[MessageEntity] | None
    audio: Audio | None
    document: Document | None
    photo: list[PhotoSize] | None
    sticker: Sticker | None
    video: Video | None
    video_note: VideoNote | None
    voice: Voice | None
    caption: str | None
    contact: Contact | None
    location: Location | None
    venue: Venue | None
    animation: Animation | None
    dice: Dice | None
    new_chat_members: list[User] | None
    left_chat_member: User | None
    new_chat_title: str | None
    new_chat_photo: list[PhotoSize] | None
    delete_chat_photo: bool | None
    group_chat_created: bool | None
    supergroup_chat_created: bool | None
    channel_chat_created: bool | None
    migrate_to_chat_id: int | None
    migrate_from_chat_id: int | None
    pinned_message: Message | InaccessibleMessage | None
    invoice: Invoice | None
    successful_payment: SuccessfulPayment | None
    connected_website: str | None
    reply_markup: InlineKeyboardMarkup | None
    message_thread_id: int | None
    is_topic_message: bool | None
    chat_background_set: ChatBackground | None
    forum_topic_created: ForumTopicCreated | None
    forum_topic_closed: ForumTopicClosed | None
    forum_topic_reopened: ForumTopicReopened | None
    has_media_spoiler: bool | None
    forum_topic_edited: ForumTopicEdited | None
    general_forum_topic_hidden: GeneralForumTopicHidden | None
    general_forum_topic_unhidden: GeneralForumTopicUnhidden | None
    write_access_allowed: WriteAccessAllowed | None
    users_shared: UsersShared | None
    chat_shared: ChatShared | None
    story: Story | None
    external_reply: ExternalReplyInfo | None
    quote: TextQuote | None
    link_preview_options: LinkPreviewOptions | None
    giveaway_created: GiveawayCreated | None
    giveaway: Giveaway | None
    giveaway_winners: GiveawayWinners | None
    giveaway_completed: GiveawayCompleted | None
    forward_origin: MessageOrigin | None
    boost_added: ChatBoostAdded | None
    sender_boost_count: int | None
    sender_tag: str | None
    reply_to_story: Story | None
    sender_business_bot: User | None
    business_connection_id: str | None
    is_from_offline: bool | None
    effect_id: str | None
    show_caption_above_media: bool | None
    paid_media: PaidMediaInfo | None
    refunded_payment: RefundedPayment | None
    proximity_alert_triggered: ProximityAlertTriggered | None
    video_chat_scheduled: VideoChatScheduled | None
    video_chat_started: VideoChatStarted | None
    video_chat_ended: VideoChatEnded | None
    video_chat_participants_invited: VideoChatParticipantsInvited | None
    web_app_data: WebAppData | None
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged | None
    gift: GiftInfo | None
    unique_gift: UniqueGiftInfo | None
    paid_message_price_changed: PaidMessagePriceChanged | None
    paid_star_count: int | None
    checklist: Checklist | None
    checklist_tasks_done: ChecklistTasksDone | None
    checklist_tasks_added: list[ChecklistTasksAdded] | None
    direct_message_price_changed: DirectMessagePriceChanged | None
    gift_upgrade_sent: GiftInfo | None
    reply_to_checklist_task_id: int | None
    direct_messages_topic: DirectMessagesTopic | None
    is_paid_post: bool | None
    suggested_post_info: SuggestedPostInfo | None
    suggested_post_approved: SuggestedPostApproved | None
    suggested_post_approval_failed: SuggestedPostApprovalFailed | None
    suggested_post_declined: SuggestedPostDeclined | None
    suggested_post_paid: SuggestedPostPaid | None
    suggested_post_refunded: SuggestedPostRefunded | None
    chat_owner_left: ChatOwnerLeft | None
    chat_owner_changed: ChatOwnerChanged | None
    managed_bot_created: ManagedBotCreated | None
    poll_option_added: PollOptionAdded | None
    poll_option_deleted: PollOptionDeleted | None
    reply_to_poll_option_id: str | None
    json: str
    def __init__(self, message_id: int, from_user: User, date: int, chat: Chat, content_type: str, options: dict[str, Any], json_string: str) -> None: ...
    @property
    def html_text(self) -> str | None: ...
    @property
    def html_caption(self) -> str | None: ...
    @property
    def voice_chat_scheduled(self) -> VideoChatScheduled | None: ...
    @property
    def voice_chat_started(self) -> VideoChatStarted | None: ...
    @property
    def voice_chat_ended(self) -> VideoChatEnded | None: ...
    @property
    def voice_chat_participants_invited(self) -> VideoChatParticipantsInvited | None: ...
    @property
    def new_chat_member(self) -> None: ...
    @property
    def forward_from(self) -> User | None: ...
    @property
    def forward_from_chat(self) -> Chat | None: ...
    @property
    def forward_from_message_id(self) -> int | None: ...
    @property
    def forward_signature(self) -> str | None: ...
    @property
    def forward_sender_name(self) -> str | None: ...
    @property
    def forward_date(self) -> int | None: ...
    @property
    def user_shared(self) -> UsersShared | None: ...
    @property
    def any_text(self) -> str | None: ...
    @property
    def any_entities(self) -> list[MessageEntity] | None: ...

class MessageEntity(Dictionaryable, JsonSerializable, JsonDeserializable):
    @staticmethod
    def to_list_of_dicts(entity_list: list[MessageEntity]) -> list[dict[str, Any]] | None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    offset: int
    length: int
    url: str
    user: User
    language: str
    custom_emoji_id: str | None
    unix_time: int | None
    date_time_format: str | None
    def __init__(self, type: str, offset: int, length: int, url: str | None = None, user: User | None = None, language: str | None = None, custom_emoji_id: str | None = None, unix_time: int | None = None, date_time_format: str | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class Dice(JsonSerializable, Dictionaryable, JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    value: int
    emoji: str
    def __init__(self, value: int, emoji: str, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class PhotoSize(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int | None
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, file_size: int | None = None, **kwargs: Any) -> None: ...

class Audio(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    duration: int
    performer: str | None
    title: str | None
    file_name: str | None
    mime_type: str | None
    file_size: int | None
    thumbnail: PhotoSize | None
    def __init__(self, file_id: str, file_unique_id: str, duration: int, performer: str | None = None, title: str | None = None, file_name: str | None = None, mime_type: str | None = None, file_size: int | None = None, thumbnail: PhotoSize | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...

class Voice(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str | None
    file_size: int | None
    def __init__(self, file_id: str, file_unique_id: str, duration: int, mime_type: str | None = None, file_size: int | None = None, **kwargs: Any) -> None: ...

class Document(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    thumbnail: PhotoSize | None
    file_name: str | None
    mime_type: str | None
    file_size: int | None
    def __init__(self, file_id: str, file_unique_id: str, thumbnail: PhotoSize | None = None, file_name: str | None = None, mime_type: str | None = None, file_size: int | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...

class Video(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: PhotoSize
    file_name: str | None
    mime_type: str | None
    file_size: int | None
    cover: list[PhotoSize] | None
    start_timestamp: int | None
    qualities: list[VideoQuality] | None
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, duration: int, thumbnail: PhotoSize | None = None, file_name: str | None = None, mime_type: str | None = None, file_size: int | None = None, cover: list[PhotoSize] | None = None, start_timestamp: int | None = None, qualities: list[VideoQuality] | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...

class VideoNote(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumbnail: PhotoSize | None
    file_size: int | None
    def __init__(self, file_id: str, file_unique_id: str, length: int, duration: int, thumbnail: PhotoSize | None = None, file_size: int | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...

class Contact(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    phone_number: str
    first_name: str
    last_name: str | None
    user_id: int | None
    vcard: str | None
    def __init__(self, phone_number: str, first_name: str, last_name: str | None = None, user_id: int | None = None, vcard: str | None = None, **kwargs: Any) -> None: ...

class Location(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    longitude: float
    latitude: float
    horizontal_accuracy: float | None
    live_period: int | None
    heading: int | None
    proximity_alert_radius: int | None
    def __init__(self, longitude: float, latitude: float, horizontal_accuracy: float | None = None, live_period: int | None = None, heading: int | None = None, proximity_alert_radius: int | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class Venue(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    location: Location
    title: str
    address: str
    foursquare_id: str | None
    foursquare_type: str | None
    google_place_id: str | None
    google_place_type: str | None
    def __init__(self, location: Location, title: str, address: str, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None, **kwargs: Any) -> None: ...

class UserProfilePhotos(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    total_count: int
    photos: list[PhotoSize]
    def __init__(self, total_count: int, photos: list[PhotoSize] | None = None, **kwargs: Any) -> None: ...

class File(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    file_size: int | None
    file_path: str | None
    def __init__(self, file_id: str, file_unique_id: str, file_size: int | None = None, file_path: str | None = None, **kwargs: Any) -> None: ...

class ForceReply(JsonSerializable):
    selective: bool | None
    input_field_placeholder: str | None
    def __init__(self, selective: bool | None = None, input_field_placeholder: str | None = None) -> None: ...
    def to_json(self) -> str: ...

class ReplyKeyboardRemove(JsonSerializable):
    selective: bool | None
    def __init__(self, selective: bool | None = None) -> None: ...
    def to_json(self) -> str: ...

class WebAppInfo(JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    url: str
    def __init__(self, url: str, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class ReplyKeyboardMarkup(JsonSerializable):
    max_row_keys: int
    resize_keyboard: bool | None
    one_time_keyboard: bool | None
    selective: bool | None
    row_width: int | None
    input_field_placeholder: str | None
    keyboard: list[list[KeyboardButton]]
    is_persistent: bool | None
    def __init__(self, resize_keyboard: bool | None = None, one_time_keyboard: bool | None = None, selective: bool | None = None, row_width: int = 3, input_field_placeholder: str | None = None, is_persistent: bool | None = None) -> None: ...
    def add(self, *args: str | KeyboardButton, row_width: int | None = None) -> ReplyKeyboardMarkup: ...
    def row(self, *args: str) -> ReplyKeyboardMarkup: ...
    def to_json(self) -> str: ...

class KeyboardButtonPollType(Dictionaryable):
    type: str
    def __init__(self, type: str | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class KeyboardButtonRequestUsers(Dictionaryable):
    request_id: int
    user_is_bot: bool | None
    user_is_premium: bool | None
    max_quantity: int | None
    request_name: bool | None
    request_username: bool | None
    request_photo: bool | None
    def __init__(self, request_id: int, user_is_bot: bool | None = None, user_is_premium: bool | None = None, max_quantity: int | None = None, request_name: bool | None = None, request_username: bool | None = None, request_photo: bool | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class KeyboardButtonRequestUser(KeyboardButtonRequestUsers):
    def __init__(self, request_id: int, user_is_bot: bool | None = None, user_is_premium: bool | None = None, max_quantity: int | None = None) -> None: ...

class KeyboardButtonRequestChat(Dictionaryable):
    request_id: int
    chat_is_channel: bool
    chat_is_forum: bool | None
    chat_has_username: bool | None
    chat_is_created: bool | None
    user_administrator_rights: ChatAdministratorRights | None
    bot_administrator_rights: ChatAdministratorRights | None
    bot_is_member: bool | None
    request_title: bool | None
    request_photo: bool | None
    request_username: bool | None
    def __init__(self, request_id: int, chat_is_channel: bool, chat_is_forum: bool | None = None, chat_has_username: bool | None = None, chat_is_created: bool | None = None, user_administrator_rights: ChatAdministratorRights | None = None, bot_administrator_rights: ChatAdministratorRights | None = None, bot_is_member: bool | None = None, request_title: bool | None = None, request_photo: bool | None = None, request_username: bool | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class KeyboardButton(Dictionaryable, JsonSerializable):
    text: str
    request_contact: bool | None
    request_location: bool | None
    request_poll: KeyboardButtonPollType | None
    web_app: WebAppInfo | None
    request_chat: KeyboardButtonRequestChat | None
    request_users: KeyboardButtonRequestUsers | None
    icon_custom_emoji_id: str | None
    style: str | None
    request_managed_bot: KeyboardButtonRequestManagedBot | None
    def __init__(self, text: str, request_contact: bool | None = None, request_location: bool | None = None, request_poll: KeyboardButtonPollType | None = None, web_app: WebAppInfo | None = None, request_user: KeyboardButtonRequestUser | None = None, request_chat: KeyboardButtonRequestChat | None = None, request_users: KeyboardButtonRequestUsers | None = None, icon_custom_emoji_id: str | None = None, style: str | None = None, request_managed_bot: KeyboardButtonRequestManagedBot | None = None) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineKeyboardMarkup(Dictionaryable, JsonSerializable, JsonDeserializable):
    max_row_keys: int
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    row_width: int
    keyboard: list[list[InlineKeyboardButton]]
    def __init__(self, keyboard: list[list[InlineKeyboardButton]] | None = None, row_width: int = 3) -> None: ...
    def add(self, *args: list[InlineKeyboardButton], row_width: int | None = None) -> InlineKeyboardMarkup: ...
    def row(self, *args: list[InlineKeyboardButton]) -> InlineKeyboardMarkup: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineKeyboardButton(Dictionaryable, JsonSerializable, JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    text: str
    url: str | None
    callback_data: str | None
    web_app: WebAppInfo | None
    switch_inline_query: str | None
    switch_inline_query_current_chat: str | None
    switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None
    callback_game: None # NOTE: not implemented
    pay: bool | None
    login_url: LoginUrl | None
    copy_text: CopyTextButton | None
    icon_custom_emoji_id: str | None
    style: str | None
    def __init__(self, text: str, url: str | None = None, callback_data: str | None = None, web_app: WebAppInfo | None = None, switch_inline_query: str | None = None, switch_inline_query_current_chat: str | None = None, switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None = None, callback_game: None = None, pay: bool | None = None, login_url: LoginUrl | None = None, copy_text: CopyTextButton | None = None, icon_custom_emoji_id: str | None = None, style: str | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class LoginUrl(Dictionaryable, JsonSerializable, JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    url: str
    forward_text: str | None
    bot_username: str | None
    request_write_access: bool | None
    def __init__(self, url: str, forward_text: str | None = None, bot_username: str | None = None, request_write_access: bool | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class CallbackQuery(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: int
    from_user: User
    message: Message | InaccessibleMessage | None
    inline_message_id: str | None
    chat_instance: str | None
    data: str | None
    game_short_name: str | None
    json: str
    def __init__(self, id: int, from_user: User, data: str, chat_instance: str, json_string: str, message: Message | InaccessibleMessage | None = None, inline_message_id: str | None = None, game_short_name: str | None = None, **kwargs: Any) -> None: ...

class ChatPhoto(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str
    def __init__(self, small_file_id: str, small_file_unique_id: str, big_file_id: str, big_file_unique_id: str, **kwargs: Any) -> None: ...

class ChatMember(JsonDeserializable, ABC):
    user: User
    status: str
    def __init__(self, user: User, status: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class ChatMemberOwner(ChatMember):
    is_anonymous: bool
    custom_title: str | None
    def __init__(self, user: User, status: str, is_anonymous: bool, custom_title: str | None = None, **kwargs: Any) -> None: ...

class ChatMemberAdministrator(ChatMember):
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_stories: bool
    can_edit_stories: bool
    can_delete_stories: bool
    can_post_messages: bool | None
    can_edit_messages: bool | None
    can_pin_messages: bool | None
    can_manage_topics: bool | None
    custom_title: str | None
    can_manage_direct_messages: bool | None
    can_manage_tags: bool | None
    def __init__(self, user: User, status: str, can_be_edited: bool, is_anonymous: bool, can_manage_chat: bool, can_delete_messages: bool, can_manage_video_chats: bool, can_restrict_members: bool, can_promote_members: bool, can_change_info: bool, can_invite_users: bool, can_post_stories: bool, can_edit_stories: bool, can_delete_stories: bool, can_post_messages: bool | None = None, can_edit_messages: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None, custom_title: str | None = None, can_manage_direct_messages: bool | None = None, can_manage_tags: bool | None = None, **kwargs: Any) -> None: ...
    @property
    def can_manage_voice_chats(self) -> bool: ...

class ChatMemberMember(ChatMember):
    until_date: int | None
    tag: str | None
    def __init__(self, user: User, status: str, until_date: int | None = None, tag: str | None = None, **kwargs: Any) -> None: ...

class ChatMemberRestricted(ChatMember):
    is_member: bool
    can_send_messages: bool
    can_send_audios: bool
    can_send_documents: bool
    can_send_photos: bool
    can_send_videos: bool
    can_send_video_notes: bool
    can_send_voice_notes: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool
    until_date: int | None
    tag: str | None
    can_edit_tag: bool | None
    def __init__(self, user: User, status: str, is_member: bool, can_send_messages: bool, can_send_audios: bool, can_send_documents: bool, can_send_photos: bool, can_send_videos: bool, can_send_video_notes: bool, can_send_voice_notes: bool, can_send_polls: bool, can_send_other_messages: bool, can_add_web_page_previews: bool, can_change_info: bool, can_invite_users: bool, can_pin_messages: bool, can_manage_topics: bool, until_date: int | None = None, tag: str | None = None, can_edit_tag: bool | None = None, **kwargs: Any) -> None: ...

class ChatMemberLeft(ChatMember): ...

class ChatMemberBanned(ChatMember):
    until_date: int | None
    def __init__(self, user: User, status: str, until_date: int | None = None, **kwargs: Any) -> None: ...

class ChatPermissions(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    can_send_messages: bool | None
    can_send_polls: bool | None
    can_send_other_messages: bool | None
    can_add_web_page_previews: bool | None
    can_change_info: bool | None
    can_invite_users: bool | None
    can_pin_messages: bool | None
    can_manage_topics: bool | None
    can_edit_tag: bool | None
    can_send_audios: bool | None
    can_send_documents: bool | None
    can_send_photos: bool | None
    can_send_videos: bool | None
    can_send_video_notes: bool | None
    can_send_voice_notes: bool | None
    def __init__(self, can_send_messages: bool | None = None, can_send_media_messages: bool | None = None, can_send_audios: bool | None = None, can_send_documents: bool | None = None, can_send_photos: bool | None = None, can_send_videos: bool | None = None, can_send_video_notes: bool | None = None, can_send_voice_notes: bool | None = None, can_send_polls: bool | None = None, can_send_other_messages: bool | None = None, can_add_web_page_previews: bool | None = None, can_change_info: bool | None = None, can_invite_users: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None, can_edit_tag: bool | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class BotCommand(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    command: str
    description: str
    def __init__(self, command: str, description: str, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class BotCommandScope(ABC, JsonSerializable):
    type: str
    chat_id: int | str | None
    user_id: int | str | None
    def __init__(self, type: str = 'default', chat_id: int | str | None = None, user_id: int | str | None = None) -> None: ...
    def to_json(self) -> str: ...

class BotCommandScopeDefault(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeAllPrivateChats(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeAllGroupChats(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeAllChatAdministrators(BotCommandScope):
    def __init__(self) -> None: ...

class BotCommandScopeChat(BotCommandScope):
    def __init__(self, chat_id: str | int | None = None) -> None: ...

class BotCommandScopeChatAdministrators(BotCommandScope):
    def __init__(self, chat_id: str | int | None = None) -> None: ...

class BotCommandScopeChatMember(BotCommandScope):
    def __init__(self, chat_id: str | int | None = None, user_id: str | int | None = None) -> None: ...

class InlineQuery(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: str
    from_user: User
    query: str
    offset: str
    chat_type: str | None
    location: Location | None
    def __init__(self, id: str, from_user: User, query: str, offset: str, chat_type: str | None = None, location: Location | None = None, **kwargs: Any) -> None: ...

class InputTextMessageContent(Dictionaryable):
    message_text: str
    parse_mode: str | None
    entities: list[MessageEntity] | None
    link_preview_options: LinkPreviewOptions | None
    def __init__(self, message_text: str, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, disable_web_page_preview: bool | None = None, link_preview_options: LinkPreviewOptions | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputLocationMessageContent(Dictionaryable):
    latitude: float
    longitude: float
    horizontal_accuracy: float | None
    live_period: int | None
    heading: int | None
    proximity_alert_radius: int | None
    def __init__(self, latitude: float, longitude: float, horizontal_accuracy: float | None = None, live_period: int | None = None, heading: int | None = None, proximity_alert_radius: int | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputVenueMessageContent(Dictionaryable):
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str | None
    foursquare_type: str | None
    google_place_id: str | None
    google_place_type: str | None
    def __init__(self, latitude: float, longitude: float, title: str, address: str, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputContactMessageContent(Dictionaryable):
    phone_number: str
    first_name: str
    last_name: str | None
    vcard: str | None
    def __init__(self, phone_number: str, first_name: str, last_name: str | None = None, vcard: str | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputInvoiceMessageContent(Dictionaryable):
    title: str
    description: str
    payload: str
    provider_token: str | None
    currency: str
    prices: list[LabeledPrice]
    max_tip_amount: int | None
    suggested_tip_amounts: list[int] | None
    provider_data: str | None
    photo_url: str | None
    photo_size: int | None
    photo_width: int | None
    photo_height: int | None
    need_name: bool | None
    need_phone_number: bool | None
    need_email: bool | None
    need_shipping_address: bool | None
    send_phone_number_to_provider: bool | None
    send_email_to_provider: bool | None
    is_flexible: bool | None
    def __init__(self, title: str, description: str, payload: str, provider_token: str | None, currency: str, prices: list[LabeledPrice], max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

InputMessageContent = InputTextMessageContent | InputLocationMessageContent | InputVenueMessageContent | InputContactMessageContent | InputInvoiceMessageContent

class ChosenInlineResult(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    result_id: str
    from_user: User
    location: Location | None
    inline_message_id: str | None
    query: str
    def __init__(self, result_id: str, from_user: User, query: str, location: Location | None = None, inline_message_id: str | None = None, **kwargs: Any) -> None: ...

class InlineQueryResultBase(ABC, Dictionaryable, JsonSerializable):
    type: str
    id: str
    title: str | None
    caption: str | None
    input_message_content: InputMessageContent | None
    reply_markup: InlineKeyboardMarkup | None
    caption_entities: list[MessageEntity] | None
    parse_mode: str | None
    def __init__(self, type: str, id: str, title: str | None = None, caption: str | None = None, input_message_content: InputMessageContent | None = None, reply_markup: InlineKeyboardMarkup | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class SentWebAppMessage(JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    inline_message_id: str | None
    def __init__(self, inline_message_id: str | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultArticle(InlineQueryResultBase):
    url: str | None
    hide_url: bool | None
    description: str | None
    thumbnail_url: str | None
    thumbnail_width: int | None
    thumbnail_height: int | None
    def __init__(self, id: str, title: str, input_message_content: InputMessageContent, reply_markup: InlineKeyboardMarkup | None = None, url: str | None = None, hide_url: bool | None = None, description: str | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_width(self) -> int: ...
    @property
    def thumb_height(self) -> int: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultPhoto(InlineQueryResultBase):
    photo_url: str
    thumbnail_url: str
    photo_width: int | None
    photo_height: int | None
    description: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, photo_url: str, thumbnail_url: str, photo_width: int | None = None, photo_height: int | None = None, title: str | None = None, description: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, show_caption_above_media: bool | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultGif(InlineQueryResultBase):
    gif_url: str
    thumbnail_url: str
    gif_width: int | None
    gif_height: int | None
    gif_duration: int | None
    thumbnail_mime_type: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, gif_url: str, thumbnail_url: str, gif_width: int | None = None, gif_height: int | None = None, title: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, gif_duration: int | None = None, parse_mode: str | None = None, thumbnail_mime_type: str | None = None, show_caption_above_media: bool | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_mime_type(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultMpeg4Gif(InlineQueryResultBase):
    mpeg4_url: str
    thumbnail_url: str
    mpeg4_width: int | None
    mpeg4_height: int | None
    mpeg4_duration: int | None
    thumbnail_mime_type: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, mpeg4_url: str, thumbnail_url: str, mpeg4_width: int | None = None, mpeg4_height: int | None = None, title: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, mpeg4_duration: int | None = None, thumbnail_mime_type: str | None = None, show_caption_above_media: bool | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_mime_type(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultVideo(InlineQueryResultBase):
    video_url: str
    mime_type: str
    thumbnail_url: str
    video_width: int | None
    video_height: int | None
    video_duration: int | None
    description: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, video_url: str, mime_type: str, thumbnail_url: str, title: str, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, video_width: int | None = None, video_height: int | None = None, video_duration: int | None = None, description: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, show_caption_above_media: bool | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultAudio(InlineQueryResultBase):
    audio_url: str
    performer: str | None
    audio_duration: int | None
    def __init__(self, id: str, audio_url: str, title: str, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, performer: str | None = None, audio_duration: int | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultVoice(InlineQueryResultBase):
    voice_url: str
    voice_duration: int | None
    def __init__(self, id: str, voice_url: str, title: str, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, voice_duration: int | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultDocument(InlineQueryResultBase):
    document_url: str
    mime_type: str
    description: str | None
    thumbnail_url: str | None
    thumbnail_width: int | None
    thumbnail_height: int | None
    def __init__(self, id: str, title: str, document_url: str, mime_type: str, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, description: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_width(self) -> int: ...
    @property
    def thumb_height(self) -> int: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultLocation(InlineQueryResultBase):
    latitude: float
    longitude: float
    horizontal_accuracy: float
    live_period: int | None
    heading: int | None
    proximity_alert_radius: int | None
    thumbnail_url: str | None
    thumbnail_width: int | None
    thumbnail_height: int | None
    def __init__(self, id: str, title: str, latitude: float, longitude: float, horizontal_accuracy: float, live_period: int | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None, heading: int | None = None, proximity_alert_radius: int | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_width(self) -> int: ...
    @property
    def thumb_height(self) -> int: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultVenue(InlineQueryResultBase):
    latitude: float
    longitude: float
    address: str
    foursquare_id: str | None
    foursquare_type: str | None
    google_place_id: str | None
    google_place_type: str | None
    thumbnail_url: str | None
    thumbnail_width: int | None
    thumbnail_height: int | None
    def __init__(self, id: str, title: str, latitude: float, longitude: float, address: str, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_width(self) -> int: ...
    @property
    def thumb_height(self) -> int: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultContact(InlineQueryResultBase):
    phone_number: str
    first_name: str
    last_name: str | None
    vcard: str | None
    thumbnail_url: str | None
    thumbnail_width: int | None
    thumbnail_height: int | None
    def __init__(self, id: str, phone_number: str, first_name: str, last_name: str | None = None, vcard: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None) -> None: ...
    @property
    def thumb_url(self) -> str: ...
    @property
    def thumb_width(self) -> int: ...
    @property
    def thumb_height(self) -> int: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultGame(InlineQueryResultBase):
    game_short_name: str
    def __init__(self, id: str, game_short_name: str, reply_markup: InlineKeyboardMarkup | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InlineQueryResultCachedBase(ABC, JsonSerializable):
    type: str
    id: str
    title: str | None | Any # Can be freely overriden
    description: str | None
    caption: str | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    caption_entities: list[MessageEntity] | None
    payload_dic: dict[str, Any]
    show_caption_above_media: bool | None
    def __init__(self) -> None: ...
    def to_json(self) -> str: ...

class InlineQueryResultCachedPhoto(InlineQueryResultCachedBase):
    type: str
    id: str
    photo_file_id: str
    title: str | None
    description: str | None
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, photo_file_id: str, title: str | None = None, description: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, show_caption_above_media: bool | None = None) -> None: ...

class InlineQueryResultCachedGif(InlineQueryResultCachedBase):
    type: str
    id: str
    gif_file_id: str
    title: str | None
    description: str | None
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, gif_file_id: str, title: str | None = None, description: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, show_caption_above_media: bool | None = None) -> None: ...

class InlineQueryResultCachedMpeg4Gif(InlineQueryResultCachedBase):
    type: str
    id: str
    mpeg4_file_id: str
    title: str | None
    description: str | None
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, mpeg4_file_id: str, title: str | None = None, description: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, show_caption_above_media: bool | None = None) -> None: ...

class InlineQueryResultCachedSticker(InlineQueryResultCachedBase):
    type: str
    id: str
    sticker_file_id: str
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    def __init__(self, id: str, sticker_file_id: str, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None) -> None: ...

class InlineQueryResultCachedDocument(InlineQueryResultCachedBase):
    type: str
    id: str
    title: str
    document_file_id: str
    description: str | None
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    def __init__(self, id: str, document_file_id: str, title: str, description: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None) -> None: ...

class InlineQueryResultCachedVideo(InlineQueryResultCachedBase):
    type: str
    id: str
    video_file_id: str
    title: str
    description: str | None
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    show_caption_above_media: bool | None
    def __init__(self, id: str, video_file_id: str, title: str, description: str | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, show_caption_above_media: bool | None = None) -> None: ...

class InlineQueryResultCachedVoice(InlineQueryResultCachedBase):
    type: str
    id: str
    voice_file_id: str
    title: str
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    def __init__(self, id: str, voice_file_id: str, title: str, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None) -> None: ...

class InlineQueryResultCachedAudio(InlineQueryResultCachedBase):
    type: str
    id: str
    audio_file_id: str
    caption: str | None
    caption_entities: list[MessageEntity] | None
    reply_markup: InlineKeyboardMarkup | None
    input_message_content: InputMessageContent | None
    parse_mode: str | None
    def __init__(self, id: str, audio_file_id: str, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, parse_mode: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None) -> None: ...

class Game(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    @classmethod
    def parse_photo(cls, photo_size_array: list[dict[str, Any]]) -> list[PhotoSize]: ...
    @classmethod
    def parse_entities(cls, message_entity_array: list[dict[str, Any]]) -> list[MessageEntity]: ...
    title: str
    description: str
    photo: list[PhotoSize]
    text: str
    text_entities: list[MessageEntity]
    animation: Animation
    def __init__(self, title: str, description: str, photo: list[PhotoSize], text: str | None = None, text_entities: list[MessageEntity] | None = None, animation: Animation | None = None, **kwargs: Any) -> None: ...

class Animation(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    width: int | None
    height: int | None
    duration: int | None
    thumbnail: PhotoSize | None
    file_name: str | None
    mime_type: str | None
    file_size: int | None
    def __init__(self, file_id: str, file_unique_id: str, width: int | None = None, height: int | None = None, duration: int | None = None, thumbnail: PhotoSize | None = None, file_name: str | None = None, mime_type: str | None = None, file_size: int | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...

class GameHighScore(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    position: int
    user: User
    score: int
    def __init__(self, position: int, user: User, score: int, **kwargs: Any) -> None: ...

class LabeledPrice(JsonSerializable, Dictionaryable):
    label: str
    amount: int
    def __init__(self, label: str, amount: int) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class Invoice(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int
    def __init__(self, title: str, description: str, start_parameter: str, currency: str, total_amount: int, **kwargs: Any) -> None: ...

class ShippingAddress(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str
    def __init__(self, country_code: str, state: str, city: str, street_line1: str, street_line2: str, post_code: str, **kwargs: Any) -> None: ...

class OrderInfo(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    name: str
    phone_number: str
    email: str | None
    shipping_address: ShippingAddress | None
    def __init__(self, name: str | None = None, phone_number: str | None = None, email: str | None = None, shipping_address: ShippingAddress | None = None, **kwargs: Any) -> None: ...

class ShippingOption(JsonSerializable):
    id: str
    title: str
    prices: list[LabeledPrice]
    def __init__(self, id: str, title: str) -> None: ...
    def add_price(self, *args: LabeledPrice) -> ShippingOption: ...
    def to_json(self) -> str: ...

class SuccessfulPayment(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    subscription_expiration_date: int | None
    is_recurring: bool | None
    is_first_recurring: bool | None
    def __init__(self, currency: str, total_amount: int, invoice_payload: str, shipping_option_id: str | None = None, order_info: OrderInfo | None = None, telegram_payment_charge_id: str | None = None, provider_payment_charge_id: str | None = None, subscription_expiration_date: int | None = None, is_recurring: bool | None = None, is_first_recurring: bool | None = None, **kwargs: Any) -> None: ...

class ShippingQuery(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: str
    from_user: User
    invoice_payload: str
    shipping_address: ShippingAddress
    def __init__(self, id: str, from_user: User, invoice_payload: str, shipping_address: ShippingAddress, **kwargs: Any) -> None: ...

class PreCheckoutQuery(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: str
    from_user: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str | None
    order_info: OrderInfo | None
    def __init__(self, id: str, from_user: User, currency: str, total_amount: int, invoice_payload: str, shipping_option_id: str | None = None, order_info: OrderInfo | None = None, **kwargs: Any) -> None: ...

class StickerSet(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    name: str
    title: str
    sticker_type: str
    stickers: list[Sticker]
    thumbnail: PhotoSize | None
    def __init__(self, name: str, title: str, sticker_type: str, stickers: list[Sticker], thumbnail: PhotoSize | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...
    @property
    def contains_masks(self) -> bool: ...
    @property
    def is_animated(self) -> bool: ...
    @property
    def is_video(self) -> bool: ...

class Sticker(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    file_id: str
    file_unique_id: str
    type: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumbnail: PhotoSize | None
    emoji: str | None
    set_name: str | None
    mask_position: MaskPosition | None
    file_size: int | None
    premium_animation: File | None
    custom_emoji_id: str | None
    needs_repainting: bool | None
    def __init__(self, file_id: str, file_unique_id: str, type: str, width: int, height: int, is_animated: bool, is_video: bool, thumbnail: PhotoSize | None = None, emoji: str | None = None, set_name: str | None = None, mask_position: MaskPosition | None = None, file_size: int | None = None, premium_animation: File | None = None, custom_emoji_id: str | None = None, needs_repainting: bool | None = None, **kwargs: Any) -> None: ...
    @property
    def thumb(self) -> PhotoSize | None: ...

class MaskPosition(Dictionaryable, JsonDeserializable, JsonSerializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    point: str
    x_shift: float
    y_shift: float
    scale: float
    def __init__(self, point: str, x_shift: float, y_shift: float, scale: float, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputMedia(Dictionaryable, JsonSerializable):
    type: str
    media: str
    caption: str | None
    parse_mode: str | None
    caption_entities: list[MessageEntity] | None
    thumbnail: str | InputFile | None
    def __init__(self, type: str, media: str, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, thumbnail: str | InputFile | None = None) -> None: ...
    def to_json(self) -> str: ... 
    def to_dict(self) -> dict[str, Any]: ...
    def convert_input_media(self) -> tuple[str, dict[str, str] | None]: ...

class InputMediaPhoto(InputMedia):
    has_spoiler: bool | None
    show_caption_above_media: bool | None
    def __init__(self, media: str | InputFile, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, has_spoiler: bool | None = None, show_caption_above_media: bool | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputMediaVideo(InputMedia):
    width: int | None
    height: int | None
    duration: int | None
    supports_streaming: bool | None
    has_spoiler: bool | None
    show_caption_above_media: bool | None
    cover: str | None
    start_timestamp: int | None
    def __init__(self, media: str | InputFile, thumbnail: str | InputFile | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, width: int | None = None, height: int | None = None, duration: int | None = None, supports_streaming: bool | None = None, has_spoiler: bool | None = None, show_caption_above_media: bool | None = None, cover: str | InputFile | None = None, start_timestamp: int | None = None) -> None: ...
    @property
    def thumb(self) -> str | Any | None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputMediaAnimation(InputMedia):
    width: int | None
    height: int | None
    duration: int | None
    has_spoiler: bool | None
    show_caption_above_media: bool | None
    def __init__(self, media: str | InputFile, thumbnail: str | InputFile | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, width: int | None = None, height: int | None = None, duration: int | None = None, has_spoiler: bool | None = None, show_caption_above_media: bool | None = None) -> None: ...
    @property
    def thumb(self) -> str | Any | None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputMediaAudio(InputMedia):
    duration: int | None
    performer: str | None
    title: str | None
    def __init__(self, media: str | InputFile, thumbnail: str | InputFile | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, duration: int | None = None, performer: str | None = None, title: str | None = None) -> None: ...
    @property
    def thumb(self) -> str | Any | None: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputMediaDocument(InputMedia):
    disable_content_type_detection: bool | None
    def __init__(self, media: str | InputFile, thumbnail: str | InputFile | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, disable_content_type_detection: bool | None = None) -> None: ...
    @property
    def thumb(self) -> str | Any | None: ...
    def to_dict(self) -> dict[str, Any]: ...

class PollOption(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    text: str
    persistent_id: str
    voter_count: int
    text_entities: list[MessageEntity] | None
    added_by_user: User | None
    added_by_chat: Chat | None
    addition_date: int | None
    def __init__(self, text: str, persistent_id: str, voter_count: int = 0, text_entities: list[MessageEntity] | None = None, added_by_user: User | None = None, added_by_chat: Chat | None = None, addition_date: int | None = None, **kwargs: Any) -> None: ...

class InputPollOption(JsonSerializable):
    text: str
    text_parse_mode: str | None
    text_entities: list[MessageEntity] | None
    def __init__(self, text: str, text_parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class Poll(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: str
    question: str
    options: list[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    explanation: str
    explanation_entities: list[MessageEntity]
    question_entities: list[MessageEntity]
    open_period: int
    close_date: int
    correct_option_ids: list[int]
    allows_revoting: bool
    description: str
    description_entities: list[MessageEntity]
    def __init__(self, question: str, options: list[PollOption], poll_id: str | None = None, total_voter_count: int | None = None, is_closed: bool | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, explanation: str | None = None, explanation_entities: list[MessageEntity] | None = None, open_period: int | None = None, close_date: int | None = None, poll_type: str | None = None, question_entities: list[MessageEntity] | None = None, correct_option_ids: list[int] | None = None, allows_revoting: bool | None = None, description: str | None = None, description_entities: list[MessageEntity] | None = None, **kwargs: Any) -> None: ...
    @property
    def correct_option_id(self) -> int | None: ...
    def add(self, option: list[PollOption], persistent_id: str | None = None) -> None: ...

class PollAnswer(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    poll_id: str
    user: User | None
    option_ids: list[int]
    option_persistent_ids: list[str]
    voter_chat: Chat | None
    def __init__(self, poll_id: str, option_ids: list[int], option_persistent_ids: list[str], user: User | None = None, voter_chat: Chat | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class ChatLocation(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    location: Location
    address: str
    def __init__(self, location: Location, address: str, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class ChatInviteLink(JsonSerializable, JsonDeserializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    invite_link: str
    creator: User
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: str | None
    expire_date: int | None
    member_limit: int | None
    pending_join_request_count: int | None
    def __init__(self, invite_link: str, creator: User, creates_join_request: bool, is_primary: bool, is_revoked: bool, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None, pending_join_request_count: int | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class ProximityAlertTriggered(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    traveler: User
    watcher: User
    distance: int
    def __init__(self, traveler: User, watcher: User, distance: int, **kwargs: Any) -> None: ...

class VideoChatStarted(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    def __init__(self) -> None: ...

class VoiceChatStarted(VideoChatStarted):
    def __init__(self) -> None: ...

class VideoChatScheduled(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    start_date: int
    def __init__(self, start_date: int, **kwargs: Any) -> None: ...

class VoiceChatScheduled(VideoChatScheduled):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class VideoChatEnded(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    duration: int
    def __init__(self, duration: int, **kwargs: Any) -> None: ...

class VoiceChatEnded(VideoChatEnded):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class VideoChatParticipantsInvited(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    users: list[User]
    def __init__(self, users: list[User] | None = None, **kwargs: Any) -> None: ...

class VoiceChatParticipantsInvited(VideoChatParticipantsInvited):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class MessageAutoDeleteTimerChanged(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    message_auto_delete_time: int
    def __init__(self, message_auto_delete_time: int, **kwargs: Any) -> None: ...

class MenuButton(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    def to_json(self) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...

class MenuButtonCommands(MenuButton):
    type: str
    def __init__(self, type: str | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class MenuButtonWebApp(MenuButton):
    type: str
    text: str
    web_app: WebAppInfo
    def __init__(self, type: str, text: str, web_app: WebAppInfo, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class MenuButtonDefault(MenuButton):
    type: str
    def __init__(self, type: str | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class ChatAdministratorRights(JsonDeserializable, JsonSerializable, Dictionaryable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool | None
    can_edit_messages: bool | None
    can_pin_messages: bool | None
    can_manage_topics: bool | None
    can_post_stories: bool | None
    can_edit_stories: bool | None
    can_delete_stories: bool | None
    can_manage_direct_messages: bool | None
    can_manage_tags: bool | None
    def __init__(self, is_anonymous: bool, can_manage_chat: bool, can_delete_messages: bool, can_manage_video_chats: bool, can_restrict_members: bool, can_promote_members: bool, can_change_info: bool, can_invite_users: bool, can_post_messages: bool | None = None, can_edit_messages: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None, can_post_stories: bool | None = None, can_edit_stories: bool | None = None, can_delete_stories: bool | None = None, can_manage_direct_messages: bool | None = None, can_manage_tags: bool | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class InputFile:
    def __init__(self, file: str | IOBase | Path, file_name: str | None = None) -> None: ...
    @property
    def file(self) -> IOBase | str: ...
    @property
    def file_name(self) -> str: ...

class ForumTopicCreated(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    name: str
    icon_color: int
    icon_custom_emoji_id: str | None
    is_name_implicit: bool | None
    def __init__(self, name: str, icon_color: int, icon_custom_emoji_id: str | None = None, is_name_implicit: bool | None = None, **kwargs: Any) -> None: ...

class ForumTopicClosed(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    def __init__(self) -> None: ...

class ForumTopicReopened(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    def __init__(self) -> None: ...

class ForumTopicEdited(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    name: str | None
    icon_custom_emoji_id: str | None
    def __init__(self, name: str | None = None, icon_custom_emoji_id: str | None = None, **kwargs: Any) -> None: ...

class GeneralForumTopicHidden(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    def __init__(self) -> None: ...

class GeneralForumTopicUnhidden(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    def __init__(self) -> None: ...

class ForumTopic(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    message_thread_id: int
    name: str
    icon_color: int
    icon_custom_emoji_id: str | None
    is_name_implicit: bool | None
    def __init__(self, message_thread_id: int, name: str, icon_color: int, icon_custom_emoji_id: str | None = None, is_name_implicit: bool | None = None, **kwargs: Any) -> None: ...

class WriteAccessAllowed(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    web_app_name: str | None
    from_request: bool | None
    from_attachment_menu: bool | None
    def __init__(self, from_request: bool | None = None, web_app_name: str | None = None, from_attachment_menu: bool | None = None, **kwargs: Any) -> None: ...

class ChatShared(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    request_id: int
    chat_id: int
    title: str | None
    photo: list[PhotoSize] | None
    username: str | None
    def __init__(self, request_id: int, chat_id: int, title: str | None = None, photo: list[PhotoSize] | None = None, username: str | None = None, **kwargs: Any) -> None: ...

class BotDescription(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    description: str
    def __init__(self, description: str, **kwargs: Any) -> None: ...

class BotShortDescription(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    short_description: str
    def __init__(self, short_description: str, **kwargs: Any) -> None: ...

class InputSticker(Dictionaryable, JsonSerializable):
    sticker: str | InputFile
    emoji_list: list[str]
    mask_position: MaskPosition | None
    keywords: list[str] | None
    format: str
    def __init__(self, sticker: str | InputFile, emoji_list: list[str], format: str | None = None, mask_position: MaskPosition | None = None, keywords: list[str] | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...
    def convert_input_sticker(self) -> tuple[str, dict[str, Any] | None]: ...

class SwitchInlineQueryChosenChat(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    query: str | None
    allow_user_chats: bool | None
    allow_bot_chats: bool | None
    allow_group_chats: bool | None
    allow_channel_chats: bool | None
    def __init__(self, query: str | None = None, allow_user_chats: bool | None = None, allow_bot_chats: bool | None = None, allow_group_chats: bool | None = None, allow_channel_chats: bool | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class BotName(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    name: str
    def __init__(self, name: str, **kwargs: Any) -> None: ...

class InlineQueryResultsButton(JsonSerializable, Dictionaryable):
    text: str
    web_app: WebAppInfo | None
    start_parameter: str | None
    def __init__(self, text: str, web_app: WebAppInfo | None = None, start_parameter: str | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class Story(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    id: int
    def __init__(self, chat: Chat, id: int, **kwargs: Any) -> None: ...

class ReactionType(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    def __init__(self, type: str) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class ReactionTypeEmoji(ReactionType):
    emoji: str
    def __init__(self, emoji: str, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class ReactionTypeCustomEmoji(ReactionType):
    custom_emoji_id: str
    def __init__(self, custom_emoji_id: str, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class ReactionTypePaid(ReactionType):
    def __init__(self, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class MessageReactionUpdated(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    message_id: int
    user: User | None
    actor_chat: Chat | None
    date: int
    old_reaction: list[ReactionType]
    new_reaction: list[ReactionType]
    def __init__(self, chat: Chat, message_id: int, date: int, old_reaction: list[ReactionType], new_reaction: list[ReactionType], user: User | None = None, actor_chat: Chat | None = None, **kwargs: Any) -> None: ...

class MessageReactionCountUpdated(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    message_id: int
    date: int
    reactions: list[ReactionCount]
    def __init__(self, chat: Chat, message_id: int, date: int, reactions: list[ReactionCount], **kwargs: Any) -> None: ...

class ReactionCount(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: ReactionType
    total_count: int
    def __init__(self, type: ReactionType, total_count: int, **kwargs: Any) -> None: ...

class ExternalReplyInfo(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    origin: MessageOrigin
    chat: Chat | None
    message_id: int | None
    link_preview_options: LinkPreviewOptions | None
    animation: Animation | None
    audio: Audio | None
    document: Document | None
    photo: list[PhotoSize] | None
    sticker: Sticker | None
    story: Story | None
    video: Video | None
    video_note: VideoNote | None
    voice: Voice | None
    has_media_spoiler: bool | None
    contact: Contact | None
    dice: Dice | None
    game: Game | None
    giveaway: Giveaway | None
    giveaway_winners: GiveawayWinners | None
    invoice: Invoice | None
    location: Location | None
    poll: Poll | None
    venue: Venue | None
    paid_media: PaidMediaInfo | None
    checklist: Checklist | None
    def __init__(self, origin: MessageOrigin, chat: Chat | None = None, message_id: int | None = None, link_preview_options: LinkPreviewOptions | None = None, animation: Animation | None = None, audio: Audio | None = None, document: Document | None = None, photo: list[PhotoSize] | None = None, sticker: Sticker | None = None, story: Story | None = None, video: Video | None = None, video_note: VideoNote | None = None, voice: Voice | None = None, has_media_spoiler: bool | None = None, contact: Contact | None = None, dice: Dice | None = None, game: Game | None = None, giveaway: Giveaway | None = None, giveaway_winners: GiveawayWinners | None = None, invoice: Invoice | None = None, location: Location | None = None, poll: Poll | None = None, venue: Venue | None = None, paid_media: PaidMediaInfo | None = None, checklist: Checklist | None = None, **kwargs: Any) -> None: ...

class MessageOrigin(JsonDeserializable, ABC):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    date: int
    def __init__(self, type: str, date: int) -> None: ...

class MessageOriginUser(MessageOrigin):
    sender_user: User
    def __init__(self, date: int, sender_user: User) -> None: ...

class MessageOriginHiddenUser(MessageOrigin):
    sender_user_name: str
    def __init__(self, date: int, sender_user_name: str) -> None: ...

class MessageOriginChat(MessageOrigin):
    sender_chat: Chat
    author_signature: str | None
    def __init__(self, date: int, sender_chat: Chat, author_signature: str | None = None) -> None: ...

class MessageOriginChannel(MessageOrigin):
    chat: Chat
    message_id: int
    author_signature: str | None
    def __init__(self, date: int, chat: Chat, message_id: int, author_signature: str | None = None) -> None: ...

class LinkPreviewOptions(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    is_disabled: bool | None
    url: str | None
    prefer_small_media: bool | None
    prefer_large_media: bool | None
    show_above_text: bool | None
    def __init__(self, is_disabled: bool | None = None, url: str | None = None, prefer_small_media: bool | None = None, prefer_large_media: bool | None = None, show_above_text: bool | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class Giveaway(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chats: list[Chat]
    winners_selection_date: int
    winner_count: int
    only_new_members: bool | None
    has_public_winners: bool | None
    prize_description: str | None
    country_codes: list[str] | None
    premium_subscription_month_count: int | None
    prize_star_count: int | None
    def __init__(self, chats: list[Chat], winners_selection_date: int, winner_count: int, only_new_members: bool | None = None, has_public_winners: bool | None = None, prize_description: str | None = None, country_codes: list[str] | None = None, premium_subscription_month_count: int | None = None, prize_star_count: int | None = None, **kwargs: Any) -> None: ...

class GiveawayWinners(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    giveaway_message_id: int
    winners_selection_date: int
    winner_count: int
    winners: list[User]
    additional_chat_count: int | None
    premium_subscription_month_count: int | None
    unclaimed_prize_count: int | None
    only_new_members: bool | None
    was_refunded: bool | None
    prize_description: str | None
    prize_star_count: int | None
    def __init__(self, chat: Chat, giveaway_message_id: int, winners_selection_date: int, winner_count: int, winners: list[User], additional_chat_count: int | None = None, premium_subscription_month_count: int | None = None, unclaimed_prize_count: int | None = None, only_new_members: bool | None = None, was_refunded: bool | None = None, prize_description: str | None = None, prize_star_count: int | None = None, **kwargs: Any) -> None: ...

class GiveawayCompleted(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    winner_count: int
    unclaimed_prize_count: int | None
    giveaway_message: Message | None
    is_star_giveaway: bool | None
    def __init__(self, winner_count: int, unclaimed_prize_count: int | None = None, giveaway_message: Message | None = None, is_star_giveaway: bool | None = None, **kwargs: Any) -> None: ...

class GiveawayCreated(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    prize_star_count: str | None
    def __init__(self, prize_star_count: str | None = None, **kwargs: Any) -> None: ...

class TextQuote(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    text: str
    entities: list[MessageEntity] | None
    position: int | None
    is_manual: bool | None
    def __init__(self, text: str, position: int, entities: list[MessageEntity] | None = None, is_manual: bool | None = None, **kwargs: Any) -> None: ...
    @property
    def html_text(self) -> str: ...

class ReplyParameters(JsonDeserializable, Dictionaryable, JsonSerializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    message_id: int
    chat_id: int | str | None
    allow_sending_without_reply: bool | None
    quote: str | None
    quote_parse_mode: str | None
    quote_entities: list[MessageEntity] | None
    quote_position: int | None
    checklist_task_id: int | None
    poll_option_id: str | None
    def __init__(self, message_id: int, chat_id: int | str | None = None, allow_sending_without_reply: bool | None = None, quote: str | None = None, quote_parse_mode: str | None = None, quote_entities: list[MessageEntity] | None = None, quote_position: int | None = None, checklist_task_id: int | None = None, poll_option_id: str | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...

class UsersShared(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    request_id: int
    users: list[SharedUser]
    def __init__(self, request_id: int, users: list[SharedUser], **kwargs: Any) -> None: ...
    @property
    def user_id(self) -> None: ...
    @property
    def user_ids(self) -> list[SharedUser]: ...

class ChatBoostUpdated(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    boost: ChatBoost
    def __init__(self, chat: Chat, boost: ChatBoost, **kwargs: Any) -> None: ...

class ChatBoostRemoved(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    boost_id: str
    remove_date: int
    source: ChatBoostSource
    def __init__(self, chat: Chat, boost_id: str, remove_date: int, source: ChatBoostSource, **kwargs: Any) -> None: ...

class ChatBoostSource(ABC, JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class ChatBoostSourcePremium(ChatBoostSource):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    source: str
    user: User
    def __init__(self, source: str, user: User, **kwargs: Any) -> None: ...

class ChatBoostSourceGiftCode(ChatBoostSource):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    source: str
    user: User
    def __init__(self, source: str, user: User, **kwargs: Any) -> None: ...

class ChatBoostSourceGiveaway(ChatBoostSource):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    source: str
    giveaway_message_id: int
    user: User | None
    is_unclaimed: bool | None
    prize_star_count: int | None
    def __init__(self, source: ChatBoostSource, giveaway_message_id: int, user: User | None = None, is_unclaimed: bool | None = None, prize_star_count: int | None = None, **kwargs: Any) -> None: ...

class ChatBoost(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    boost_id: str
    add_date: int
    expiration_date: int
    source: ChatBoostSource
    def __init__(self, boost_id: str, add_date: int, expiration_date: int, source: ChatBoostSource, **kwargs: Any) -> None: ...

class UserChatBoosts(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    boosts: list[ChatBoost]
    def __init__(self, boosts: list[ChatBoost], **kwargs: Any) -> None: ...

class InaccessibleMessage(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    chat: Chat
    message_id: int
    date: int
    def __init__(self, chat: Chat, message_id: int, date: int, **kwargs: Any) -> None: ...
    def __getattr__(self, item: Any) -> None: ...

class ChatBoostAdded(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    boost_count: int
    def __init__(self, boost_count: int, **kwargs: Any) -> None: ...

class BusinessConnection(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: str
    user: User
    user_chat_id: int
    date: int
    rights: BusinessBotRights | None
    is_enabled: bool
    def __init__(self, id: str, user: User, user_chat_id: int, date: int, is_enabled: bool, rights: BusinessBotRights | None = None, **kwargs: Any) -> None: ...
    @property
    def can_reply(self) -> bool: ...

class BusinessMessagesDeleted(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    business_connection_id: str
    chat: Chat
    message_ids: list[int]
    def __init__(self, business_connection_id: str, chat: Chat, message_ids: list[int], **kwargs: Any) -> None: ...

class BusinessIntro(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    title: str | None
    message: str | None
    sticker: Sticker | None
    def __init__(self, title: str | None = None, message: str | None = None, sticker: Sticker | None = None, **kwargs: Any) -> None: ...

class BusinessLocation(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    address: str
    location: Location | None
    def __init__(self, address: str, location: Location | None = None, **kwargs: Any) -> None: ...

class BusinessOpeningHoursInterval(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    opening_minute: int
    closing_minute: int
    def __init__(self, opening_minute: int, closing_minute: int, **kwargs: Any) -> None: ...

class BusinessOpeningHours(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    time_zone_name: str
    opening_hours: list[BusinessOpeningHoursInterval]
    def __init__(self, time_zone_name: str, opening_hours: list[BusinessOpeningHoursInterval], **kwargs: Any) -> None: ...

class SharedUser(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    user_id: int
    first_name: str | None
    last_name: str | None
    username: str | None
    photo: list[PhotoSize] | None
    def __init__(self, user_id: int, first_name: str | None = None, last_name: str | None = None, username: str | None = None, photo: list[PhotoSize] | None = None, **kwargs: Any) -> None: ...

class Birthdate(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    day: int
    month: int
    year: int | None
    def __init__(self, day: int, month: int, year: int | None = None, **kwargs: Any) -> None: ...

class BackgroundFill(ABC, JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class BackgroundFillSolid(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    color: int
    def __init__(self, type: str, color: int, **kwargs: Any) -> None: ...

class BackgroundFillGradient(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    top_color: int
    bottom_color: int
    rotation_angle: int
    def __init__(self, type: str, top_color: int, bottom_color: int, rotation_angle: int, **kwargs: Any) -> None: ...

class BackgroundFillFreeformGradient(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    colors: list[int]
    def __init__(self, type: str, colors: list[str], **kwargs: Any) -> None: ...

class BackgroundType(ABC, JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class BackgroundTypeFill(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    fill: BackgroundFill
    dark_theme_dimming: int
    def __init__(self, type: str, fill: BackgroundFill, dark_theme_dimming: int, **kwargs: Any) -> None: ...

class BackgroundTypeWallpaper(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    document: Document
    dark_theme_dimming: int
    is_blurred: bool | None
    is_moving: bool | None
    def __init__(self, type: str, document: Document, dark_theme_dimming: int, is_blurred: bool | None = None, is_moving: bool | None = None, **kwargs: Any) -> None: ...

class BackgroundTypePattern(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    document: Document
    fill: BackgroundFill
    intensity: int
    is_inverted: bool | None
    is_moving: bool | None
    def __init__(self, type: str, document: Document, fill: BackgroundFill, intensity: int, is_inverted: bool | None = None, is_moving: bool | None = None, **kwargs: Any) -> None: ...

class BackgroundTypeChatTheme(BackgroundFill):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: str
    theme_name: str
    def __init__(self, type: str, theme_name: str, **kwargs: Any) -> None: ...

class ChatBackground(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    type: BackgroundType
    def __init__(self, type: BackgroundType, **kwargs: Any) -> None: ...

class RevenueWithdrawalState(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class RevenueWithdrawalStatePending(RevenueWithdrawalState):
    type: str
    def __init__(self, type: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class RevenueWithdrawalStateSucceeded(RevenueWithdrawalState):
    type: str
    date: int
    url: str
    def __init__(self, type: str, date: int, url: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class RevenueWithdrawalStateFailed(RevenueWithdrawalState):
    type: str
    def __init__(self, type: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartner(JsonDeserializable, ABC):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerFragment(TransactionPartner):
    type: str
    withdrawal_state: RevenueWithdrawalState | None
    def __init__(self, type: str, withdrawal_state: RevenueWithdrawalState | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerTelegramApi(TransactionPartner):
    type: str
    request_count: int
    def __init__(self, type: str, request_count: int, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerUser(TransactionPartner):
    type: str
    user: User
    affiliate: AffiliateInfo | None
    invoice_payload: str | None
    paid_media: list[PaidMedia] | None
    subscription_period: int | None
    gift: Gift | None
    premium_subscription_duration: int | None
    transaction_type: str | None
    def __init__(self, type: str, user: User, affiliate: AffiliateInfo | None = None, invoice_payload: str | None = None, paid_media: list[PaidMedia] | None = None, subscription_period: int | None = None, gift: Gift | None = None, premium_subscription_duration: int | None = None, transaction_type: str | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerTelegramAds(TransactionPartner):
    type: str
    def __init__(self, type: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerOther(TransactionPartner):
    type: str
    def __init__(self, type: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class StarTransaction(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    id: str
    amount: int
    date: int
    source: TransactionPartner | None
    receiver: TransactionPartner | None
    nanostar_amount: int | None 
    def __init__(self, id: str, amount: int, date: int, source: TransactionPartner | None = None, receiver: TransactionPartner | None = None, nanostar_amount: int | None = None, **kwargs: Any) -> None: ...

class StarTransactions(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    transactions: list[StarTransaction]
    def __init__(self, transactions: list[StarTransaction], **kwargs: Any) -> None: ...

class PaidMedia(JsonDeserializable, ABC):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PaidMediaPreview(PaidMedia):
    type: str
    width: int | None
    height: int | None
    duration: int | None
    def __init__(self, type: str, width: int | None = None, height: int | None = None, duration: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PaidMediaPhoto(PaidMedia):
    type: str
    photo: list[PhotoSize]
    def __init__(self, type: str, photo: list[PhotoSize], **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PaidMediaVideo(PaidMedia):
    type: str
    video: Video
    def __init__(self, type: str, video: Video, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PaidMediaInfo(JsonDeserializable):
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...
    star_count: int
    paid_media: list[PaidMedia]
    def __init__(self, star_count: int, paid_media: list[PaidMedia], **kwargs: Any) -> None: ...

class InputPaidMedia(Dictionaryable, JsonSerializable):
    type: str
    media: str | InputFile
    def __init__(self, type: str, media: str | InputFile, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputPaidMediaPhoto(InputPaidMedia):
    def __init__(self, media: str | InputFile, **kwargs: Any) -> None: ...

class InputPaidMediaVideo(InputPaidMedia):
    thumbnail: str | InputFile | None
    width: int | None
    height: int | None
    duration: int | None
    supports_streaming: bool | None
    cover: str | InputFile | None
    start_timestamp: int | None
    def __init__(self, media: str | InputFile, thumbnail: InputFile | None = None, width: int | None = None, height: int | None = None, duration: int | None = None, supports_streaming: bool | None = None, cover: str | InputFile | None = None, start_timestamp: int | None = None, **kwargs: Any) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class RefundedPayment(JsonDeserializable):
    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str | None
    def __init__(self, currency: str, total_amount: int, invoice_payload: str, telegram_payment_charge_id: str, provider_payment_charge_id: str | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PaidMediaPurchased(JsonDeserializable):
    from_user: User
    paid_media_payload: str
    def __init__(self, from_user: User, paid_media_payload: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class CopyTextButton(JsonSerializable, JsonDeserializable):
    text: str
    def __init__(self, text: str, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PreparedInlineMessage(JsonDeserializable):
    id: str
    expiration_date: int
    def __init__(self, id: str, expiration_date: int, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class Gift(JsonDeserializable):
    id: str
    sticker: Sticker
    star_count: int
    total_count: int | None
    remaining_count: int | None
    upgrade_star_count: int | None
    personal_total_count: int | None
    personal_remaining_count: int | None
    is_premium: bool | None
    has_colors: bool | None
    background: GiftBackground | None
    publisher_chat: Chat | None
    unique_gift_variant_count: int | None
    def __init__(self, id: str, sticker: Sticker, star_count: int, total_count: int | None = None, remaining_count: int | None = None, upgrade_star_count: int | None = None, personal_total_count: int | None = None, personal_remaining_count: int | None = None, is_premium: bool | None = None, has_colors: bool | None = None, background: GiftBackground | None = None, publisher_chat: Chat | None = None, unique_gift_variant_count: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class Gifts(JsonDeserializable):
    gifts: list[Gift]
    def __init__(self, gifts: list[Gift], **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerAffiliateProgram(TransactionPartner):
    type: str
    sponsor_user: User | None
    commission_per_mille: int
    def __init__(self, type: str, commission_per_mille: int, sponsor_user: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class AffiliateInfo(JsonDeserializable):
    affiliate_user: User | None
    affiliate_chat: Chat | None
    commission_per_mille: int
    amount: int
    nanostar_amount: int | None
    def __init__(self, commission_per_mille: int, amount: int, affiliate_user: User | None = None, affiliate_chat: Chat | None = None, nanostar_amount: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class TransactionPartnerChat(TransactionPartner):
    type: str
    chat: Chat
    gift: Gift | None
    def __init__(self, type: str, chat: Chat, gift: Gift | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class BusinessBotRights(JsonDeserializable):
    can_reply: bool | None
    can_read_messages: bool | None
    can_delete_outgoing_messages: bool | None
    can_delete_all_messages: bool | None
    can_edit_name: bool | None
    can_edit_bio: bool | None
    can_edit_profile_photo: bool | None
    can_edit_username: bool | None
    can_change_gift_settings: bool | None
    can_view_gifts_and_stars: bool | None
    can_convert_gifts_to_stars: bool | None
    can_transfer_and_upgrade_gifts: bool | None
    can_transfer_stars: bool | None
    can_manage_stories: bool | None
    def __init__(self, can_reply: bool | None = None, can_read_messages: bool | None = None, can_delete_outgoing_messages: bool | None = None, can_delete_all_messages: bool | None = None, can_edit_name: bool | None = None, can_edit_bio: bool | None = None, can_edit_profile_photo: bool | None = None, can_edit_username: bool | None = None, can_change_gift_settings: bool | None = None, can_view_gifts_and_stars: bool | None = None, can_convert_gifts_to_stars: bool | None = None, can_transfer_and_upgrade_gifts: bool | None = None, can_transfer_stars: bool | None = None, can_manage_stories: bool | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class AcceptedGiftTypes(JsonDeserializable, JsonSerializable):
    unlimited_gifts: bool
    limited_gifts: bool
    unique_gifts: bool
    premium_subscription: bool
    gifts_from_channels: bool
    def __init__(self, unlimited_gifts: bool, limited_gifts: bool, unique_gifts: bool, premium_subscription: bool, gifts_from_channels: bool, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class StarAmount(JsonDeserializable):
    amount: int
    nanostar_amount: int | None
    def __init__(self, amount: int, nanostar_amount: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class OwnedGift(JsonDeserializable, ABC):
    type: str
    gift: Gift | UniqueGift | None
    def __init__(self, type: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class OwnedGiftRegular(OwnedGift):
    gift: Gift # type: ignore
    owned_gift_id: str | None
    sender_user: User | None
    send_date: int | None
    text: str | None
    entities: list[MessageEntity] | None
    is_private: bool | None
    is_saved: bool | None
    can_be_upgraded: bool | None
    was_refunded: bool | None
    convert_star_count: int | None
    prepaid_upgrade_star_count: int | None
    is_upgrade_separate: bool | None
    unique_gift_number: int | None
    def __init__(self, type: str, gift: Gift, owned_gift_id: str | None = None, sender_user: User | None = None, send_date: int | None = None, text: str | None = None, entities: list[MessageEntity] | None = None, is_private: bool | None = None, is_saved: bool | None = None, can_be_upgraded: bool | None = None, was_refunded: bool | None = None, convert_star_count: int | None = None, prepaid_upgrade_star_count: int | None = None, is_upgrade_separate: bool | None = None, unique_gift_number: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class OwnedGiftUnique(OwnedGift):
    gift: UniqueGift # type: ignore
    owned_gift_id: str | None
    sender_user: User | None
    send_date: int | None
    is_saved: bool | None
    can_be_transferred: bool | None
    transfer_star_count: int | None
    next_transfer_date: int | None
    def __init__(self, type: str, gift: UniqueGift, owned_gift_id: str | None = None, sender_user: User | None = None, send_date: int | None = None, is_saved: bool | None = None, can_be_transferred: bool | None = None, transfer_star_count: int | None = None, next_transfer_date: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class OwnedGifts(JsonDeserializable):
    total_count: int
    gifts: list[OwnedGift]
    next_offset: str | None
    def __init__(self, total_count: int, gifts: list[OwnedGift], next_offset: str | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGift(JsonDeserializable):
    base_name: str
    name: str
    number: int
    model: UniqueGiftModel
    symbol: UniqueGiftSymbol
    backdrop: UniqueGiftBackdrop
    gift_id: str
    is_from_blockchain: bool | None
    is_premium: bool | None
    colors: UniqueGiftColors | None
    publisher_chat: Chat | None
    is_burned: bool | None
    def __init__(self, base_name: str, name: str, number: int, model: UniqueGiftModel, symbol: UniqueGiftSymbol, backdrop: UniqueGiftBackdrop, gift_id: str, publisher_chat: Chat | None = None, is_from_blockchain: bool | None = None, is_premium: bool | None = None, colors: UniqueGiftColors | None = None, is_burned: bool | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGiftModel(JsonDeserializable):
    name: str
    sticker: Sticker
    rarity_per_mille: int
    rarity: str | None
    def __init__(self, name: str, sticker: Sticker, rarity_per_mille: int, rarity: str | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGiftSymbol(JsonDeserializable):
    name: str
    sticker: Sticker
    rarity_per_mille: int
    def __init__(self, name: str, sticker: Sticker, rarity_per_mille: int, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGiftBackdropColors(JsonDeserializable):
    center_color: int
    edge_color: int
    symbol_color: int
    text_color: int
    def __init__(self, center_color: int, edge_color: int, symbol_color: int, text_color: int, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGiftBackdrop(JsonDeserializable):
    name: str
    colors: UniqueGiftBackdropColors
    rarity_per_mille: int
    def __init__(self, name: str, colors: UniqueGiftBackdropColors, rarity_per_mille: int, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class InputStoryContent(JsonSerializable, ABC):
    type: str
    def __init__(self, type: str, **kwargs: Any) -> None: ...

class InputStoryContentPhoto(InputStoryContent):
    photo: InputFile
    def __init__(self, photo: InputFile, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    def convert_input_story(self) -> tuple[str, dict[str, InputFile]]: ...

class InputStoryContentVideo(InputStoryContent):
    video: InputFile
    duration: float | None
    cover_frame_timestamp: float | None
    is_animation: bool | None
    def __init__(self, video: InputFile, duration: float | None = None, cover_frame_timestamp: float | None = None, is_animation: bool | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    def convert_input_story(self) -> tuple[str, dict[str, InputFile]]: ...

class StoryAreaPosition(JsonSerializable):
    x_percentage: float
    y_percentage: float
    width_percentage: float
    height_percentage: float
    rotation_angle: float
    corner_radius_percentage: float
    def __init__(self, x_percentage: float, y_percentage: float, width_percentage: float, height_percentage: float, rotation_angle: float, corner_radius_percentage: float, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class LocationAddress(JsonSerializable):
    country_code: str
    state: str | None
    city: str | None
    street: str | None
    def __init__(self, country_code: str, state: str | None = None, city: str | None = None, street: str | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class StoryAreaType(JsonSerializable, ABC):
    type: str
    def __init__(self, type: str, **kwargs: Any) -> None: ...

class StoryAreaTypeLocation(StoryAreaType):
    latitude: float
    longitude: float
    address: LocationAddress | None
    def __init__(self, latitude: float, longitude: float, address: LocationAddress | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class StoryAreaTypeSuggestedReaction(StoryAreaType):
    reaction_type: ReactionType
    is_dark: bool | None
    is_flipped: bool | None
    def __init__(self, reaction_type: ReactionType, is_dark: bool | None = None, is_flipped: bool | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class StoryAreaTypeLink(StoryAreaType):
    url: str
    def __init__(self, url: str, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class StoryAreaTypeWeather(StoryAreaType):
    temperature: float
    emoji: str
    background_color: int
    def __init__(self, temperature: float, emoji: str, background_color: int, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class StoryAreaTypeUniqueGift(StoryAreaType):
    name: str
    def __init__(self, name: str, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class StoryArea(JsonSerializable):
    position: StoryAreaPosition
    type: StoryAreaType
    def __init__(self, position: StoryAreaPosition, type: StoryAreaType, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class GiftInfo(JsonDeserializable):
    gift: Gift
    owned_gift_id: str | None
    convert_star_count: int | None
    prepaid_upgrade_star_count: int | None
    can_be_upgraded: bool | None
    text: str | None
    entities: list[MessageEntity] | None
    is_private: bool | None
    is_upgrade_separate: bool | None
    unique_gift_number: int | None
    def __init__(self, gift: Gift, owned_gift_id: str | None = None, convert_star_count: int | None = None, prepaid_upgrade_star_count: int | None = None, can_be_upgraded: bool | None = None, text: str | None = None, entities: list[MessageEntity] | None = None, is_private: bool | None = None, is_upgrade_separate: bool | None = None, unique_gift_number: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGiftInfo(JsonDeserializable):
    gift: UniqueGift
    origin: str
    last_resale_currency: str | None
    last_resale_amount: int | None
    owned_gift_id: str | None
    transfer_star_count: int | None
    next_transfer_date: int | None
    def __init__(self, gift: UniqueGift, origin: str, owned_gift_id: str | None = None, transfer_star_count: int | None = None, next_transfer_date: int | None = None, last_resale_currency: str | None = None, last_resale_amount: int | None = None, **kwargs: Any) -> None: ...
    @property
    def last_resale_star_count(self) -> int | None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PaidMessagePriceChanged(JsonDeserializable):
    paid_message_star_count: int
    def __init__(self, paid_message_star_count: int, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class InputProfilePhoto(JsonSerializable, ABC): ...

class InputProfilePhotoStatic(InputProfilePhoto):
    type: str
    photo: InputFile
    def __init__(self, photo: InputFile, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    def convert_input_profile_photo(self) -> tuple[str, dict[str, InputFile]]: ...

class InputProfilePhotoAnimated(InputProfilePhoto):
    type: str
    animation: InputFile
    main_frame_timestamp: float | None
    def __init__(self, animation: InputFile, main_frame_timestamp: float | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    def convert_input_profile_photo(self) -> tuple[str, dict[str, InputFile]]: ...

class ChecklistTask(JsonDeserializable):
    id: int
    text: str
    text_entities: list[MessageEntity] | None
    completed_by_user: User | None
    completed_by_chat: Chat | None
    completion_date: int | None
    def __init__(self, id: int, text: str, text_entities: list[MessageEntity] | None = None, completed_by_user: User | None = None, completed_by_chat: Chat | None = None, completion_date: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class Checklist(JsonDeserializable):
    title: str
    tasks: list[ChecklistTask]
    title_entities: list[MessageEntity] | None
    others_can_add_tasks: bool | None
    others_can_mark_tasks_as_done: bool | None
    def __init__(self, title: str, tasks: list[ChecklistTask], title_entities: list[MessageEntity] | None = None, others_can_add_tasks: bool | None = None, others_can_mark_tasks_as_done: bool | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class InputChecklistTask(JsonSerializable):
    id: int
    text: str
    parse_mode: str | None
    text_entities: list[MessageEntity] | None
    def __init__(self, id: int, text: str, parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class InputChecklist(JsonSerializable):
    title: str
    tasks: list[InputChecklistTask]
    parse_mode: str | None
    title_entities: list[MessageEntity] | None
    others_can_add_tasks: bool | None
    others_can_mark_tasks_as_done: bool | None
    def __init__(self, title: str, tasks: list[InputChecklistTask], parse_mode: str | None = None, title_entities: list[MessageEntity] | None = None, others_can_add_tasks: bool | None = None, others_can_mark_tasks_as_done: bool | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class ChecklistTasksDone(JsonDeserializable):
    checklist_message: Message | None
    marked_as_done_task_ids: list[int] | None
    marked_as_not_done_task_ids: list[int] | None
    def __init__(self, checklist_message: Message | None = None, marked_as_done_task_ids: list[int] | None = None, marked_as_not_done_task_ids: list[int] | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class ChecklistTasksAdded(JsonDeserializable):
    checklist_message: Message | None
    tasks: list[ChecklistTask]
    def __init__(self, tasks: list[ChecklistTask], checklist_message: Message | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class DirectMessagePriceChanged(JsonDeserializable):
    are_direct_messages_enabled: bool
    direct_message_star_count: int | None
    def __init__(self, are_direct_messages_enabled: bool, direct_message_star_count: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UniqueGiftColors(JsonDeserializable):
    model_custom_emoji_id: str
    symbol_custom_emoji_id: str
    light_theme_main_color: int
    light_theme_other_colors: list[int]
    dark_theme_main_color: int
    dark_theme_other_colors: list[int]
    def __init__(self, model_custom_emoji_id: str, symbol_custom_emoji_id: str, light_theme_main_color: int, light_theme_other_colors: list[int], dark_theme_main_color: int, dark_theme_other_colors: list[int], **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class DirectMessagesTopic(JsonDeserializable):
    topic_id: int
    user: User | None
    def __init__(self, topic_id: int, user: User | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class SuggestedPostPrice(JsonSerializable, JsonDeserializable):
    currency: str
    amount: int
    def __init__(self, currency: str, amount: int, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class SuggestedPostParameters(JsonSerializable):
    price: SuggestedPostPrice | None
    send_date: int | None
    def __init__(self, price: SuggestedPostPrice | None = None, send_date: int | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class SuggestedPostInfo(JsonDeserializable):
    state: str
    price: SuggestedPostPrice | None
    send_date: int | None
    def __init__(self, state: str, price: SuggestedPostPrice | None = None, send_date: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class SuggestedPostApproved(JsonDeserializable):
    suggested_post_message: Message | None
    price: SuggestedPostPrice | None
    send_date: int
    def __init__(self, send_date: int, suggested_post_message: Message | None = None, price: SuggestedPostPrice | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class GiftBackground(JsonDeserializable):
    center_color: int
    edge_color: int
    text_color: int
    def __init__(self, center_color: int, edge_color: int, text_color: int, **kwargs: Any) -> None: ...

class SuggestedPostApprovalFailed(JsonDeserializable):
    suggested_post_message: Message | None
    price: SuggestedPostPrice
    def __init__(self, price: SuggestedPostPrice, suggested_post_message: Message | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class SuggestedPostDeclined(JsonDeserializable):
    suggested_post_message: Message | None
    comment: str | None
    def __init__(self, suggested_post_message: Message | None = None, comment: str | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class SuggestedPostPaid(JsonDeserializable):
    suggested_post_message: Message | None
    currency: str
    amount: int | None
    star_amount: StarAmount | None
    def __init__(self, currency: str, suggested_post_message: Message | None = None, amount: int | None = None, star_amount: StarAmount | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class SuggestedPostRefunded(JsonDeserializable):
    suggested_post_message: Message | None
    reason: str
    def __init__(self, reason: str, suggested_post_message: Message | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UserRating(JsonDeserializable):
    level: int
    rating: int
    current_level_rating: int
    next_level_rating: int | None
    def __init__(self, level: int, rating: int, current_level_rating: int, next_level_rating: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class ChatOwnerLeft(JsonDeserializable):
    new_owner: User | None
    def __init__(self, new_owner: User | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class ChatOwnerChanged(JsonDeserializable):
    new_owner: User
    def __init__(self, new_owner: User, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class VideoQuality(JsonDeserializable):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    codec: str
    file_size: int | None
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, codec: str, file_size: int | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class UserProfileAudios(JsonDeserializable):
    total_count: int
    audios: list[Audio]
    def __init__(self, total_count: int, audios: list[Audio], **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class KeyboardButtonRequestManagedBot(JsonSerializable):
    request_id: int
    suggested_name: str | None
    suggested_username: str | None
    def __init__(self, request_id: int, suggested_name: str | None = None, suggested_username: str | None = None, **kwargs: Any) -> None: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class ManagedBotCreated(JsonDeserializable):
    bot: User
    def __init__(self, bot: User, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class ManagedBotUpdated(JsonDeserializable):
    user: User
    bot: User
    def __init__(self, user: User, bot: User, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PreparedKeyboardButton(JsonDeserializable):
    id: str
    def __init__(self, id: str, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PollOptionAdded(JsonDeserializable):
    poll_message: InaccessibleMessage | Message | None
    option_persistent_id: str
    option_text: str
    option_text_entities: list[MessageEntity] | None
    def __init__(self, option_persistent_id: str, option_text: str, poll_message: InaccessibleMessage | Message | None = None, option_text_entities: list[MessageEntity] | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...

class PollOptionDeleted(JsonDeserializable):
    poll_message: InaccessibleMessage | Message | None
    option_persistent_id: str
    option_text: str
    option_text_entities: list[MessageEntity] | None
    def __init__(self, option_persistent_id: str, option_text: str, poll_message: InaccessibleMessage | Message | None = None, option_text_entities: list[MessageEntity] | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls: type[_T], json_string: dict[str, Any]) -> _T | None: ...