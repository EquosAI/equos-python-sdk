from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.equos_conversation_utterance_author import EquosConversationUtteranceAuthor

T = TypeVar("T", bound="EquosConversationUtterance")


@_attrs_define
class EquosConversationUtterance:
    """
    Attributes:
        id (str):
        author (EquosConversationUtteranceAuthor):
        content (str):
        recorded_at (datetime.datetime):
    """

    id: str
    author: EquosConversationUtteranceAuthor
    content: str
    recorded_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author = self.author.value

        content = self.content

        recorded_at = self.recorded_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author": author,
                "content": content,
                "recordedAt": recorded_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        author = EquosConversationUtteranceAuthor(d.pop("author"))

        content = d.pop("content")

        recorded_at = isoparse(d.pop("recordedAt"))

        equos_conversation_utterance = cls(
            id=id,
            author=author,
            content=content,
            recorded_at=recorded_at,
        )

        equos_conversation_utterance.additional_properties = d
        return equos_conversation_utterance

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
