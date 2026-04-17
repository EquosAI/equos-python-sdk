from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.equos_conversation_status import EquosConversationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equos_conversation_prompt_template_vars_type_0 import EquosConversationPromptTemplateVarsType0
    from ..models.equos_conversation_utterance import EquosConversationUtterance
    from ..models.equos_timeline_entry import EquosTimelineEntry


T = TypeVar("T", bound="EquosConversation")


@_attrs_define
class EquosConversation:
    """
    Attributes:
        id (str):
        name (str):
        status (EquosConversationStatus):
        charge (bool):
        charge_by_second (float):
        max_seconds (float):
        started_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        character_id (str):
        organization_id (str):
        client (None | str | Unset):
        room (None | str | Unset):
        server_url (None | str | Unset):
        remote_agent_name (None | str | Unset):
        remote_agent_identity (None | str | Unset):
        consumer_name (None | str | Unset):
        consumer_identity (None | str | Unset):
        prompt_ctx (None | str | Unset):
        prompt_template_vars (EquosConversationPromptTemplateVarsType0 | None | Unset):
        transcript (list[EquosConversationUtterance] | None | Unset):
        timeline (list[EquosTimelineEntry] | None | Unset):
        joined_at (datetime.datetime | None | Unset):
        ended_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    status: EquosConversationStatus
    charge: bool
    charge_by_second: float
    max_seconds: float
    started_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    character_id: str
    organization_id: str
    client: None | str | Unset = UNSET
    room: None | str | Unset = UNSET
    server_url: None | str | Unset = UNSET
    remote_agent_name: None | str | Unset = UNSET
    remote_agent_identity: None | str | Unset = UNSET
    consumer_name: None | str | Unset = UNSET
    consumer_identity: None | str | Unset = UNSET
    prompt_ctx: None | str | Unset = UNSET
    prompt_template_vars: EquosConversationPromptTemplateVarsType0 | None | Unset = UNSET
    transcript: list[EquosConversationUtterance] | None | Unset = UNSET
    timeline: list[EquosTimelineEntry] | None | Unset = UNSET
    joined_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.equos_conversation_prompt_template_vars_type_0 import EquosConversationPromptTemplateVarsType0

        id = self.id

        name = self.name

        status = self.status.value

        charge = self.charge

        charge_by_second = self.charge_by_second

        max_seconds = self.max_seconds

        started_at = self.started_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        character_id = self.character_id

        organization_id = self.organization_id

        client: None | str | Unset
        if isinstance(self.client, Unset):
            client = UNSET
        else:
            client = self.client

        room: None | str | Unset
        if isinstance(self.room, Unset):
            room = UNSET
        else:
            room = self.room

        server_url: None | str | Unset
        if isinstance(self.server_url, Unset):
            server_url = UNSET
        else:
            server_url = self.server_url

        remote_agent_name: None | str | Unset
        if isinstance(self.remote_agent_name, Unset):
            remote_agent_name = UNSET
        else:
            remote_agent_name = self.remote_agent_name

        remote_agent_identity: None | str | Unset
        if isinstance(self.remote_agent_identity, Unset):
            remote_agent_identity = UNSET
        else:
            remote_agent_identity = self.remote_agent_identity

        consumer_name: None | str | Unset
        if isinstance(self.consumer_name, Unset):
            consumer_name = UNSET
        else:
            consumer_name = self.consumer_name

        consumer_identity: None | str | Unset
        if isinstance(self.consumer_identity, Unset):
            consumer_identity = UNSET
        else:
            consumer_identity = self.consumer_identity

        prompt_ctx: None | str | Unset
        if isinstance(self.prompt_ctx, Unset):
            prompt_ctx = UNSET
        else:
            prompt_ctx = self.prompt_ctx

        prompt_template_vars: dict[str, Any] | None | Unset
        if isinstance(self.prompt_template_vars, Unset):
            prompt_template_vars = UNSET
        elif isinstance(self.prompt_template_vars, EquosConversationPromptTemplateVarsType0):
            prompt_template_vars = self.prompt_template_vars.to_dict()
        else:
            prompt_template_vars = self.prompt_template_vars

        transcript: list[dict[str, Any]] | None | Unset
        if isinstance(self.transcript, Unset):
            transcript = UNSET
        elif isinstance(self.transcript, list):
            transcript = []
            for transcript_type_0_item_data in self.transcript:
                transcript_type_0_item = transcript_type_0_item_data.to_dict()
                transcript.append(transcript_type_0_item)

        else:
            transcript = self.transcript

        timeline: list[dict[str, Any]] | None | Unset
        if isinstance(self.timeline, Unset):
            timeline = UNSET
        elif isinstance(self.timeline, list):
            timeline = []
            for timeline_type_0_item_data in self.timeline:
                timeline_type_0_item = timeline_type_0_item_data.to_dict()
                timeline.append(timeline_type_0_item)

        else:
            timeline = self.timeline

        joined_at: None | str | Unset
        if isinstance(self.joined_at, Unset):
            joined_at = UNSET
        elif isinstance(self.joined_at, datetime.datetime):
            joined_at = self.joined_at.isoformat()
        else:
            joined_at = self.joined_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "charge": charge,
                "chargeBySecond": charge_by_second,
                "maxSeconds": max_seconds,
                "startedAt": started_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "characterId": character_id,
                "organizationId": organization_id,
            }
        )
        if client is not UNSET:
            field_dict["client"] = client
        if room is not UNSET:
            field_dict["room"] = room
        if server_url is not UNSET:
            field_dict["serverUrl"] = server_url
        if remote_agent_name is not UNSET:
            field_dict["remoteAgentName"] = remote_agent_name
        if remote_agent_identity is not UNSET:
            field_dict["remoteAgentIdentity"] = remote_agent_identity
        if consumer_name is not UNSET:
            field_dict["consumerName"] = consumer_name
        if consumer_identity is not UNSET:
            field_dict["consumerIdentity"] = consumer_identity
        if prompt_ctx is not UNSET:
            field_dict["promptCtx"] = prompt_ctx
        if prompt_template_vars is not UNSET:
            field_dict["promptTemplateVars"] = prompt_template_vars
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if timeline is not UNSET:
            field_dict["timeline"] = timeline
        if joined_at is not UNSET:
            field_dict["joinedAt"] = joined_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equos_conversation_prompt_template_vars_type_0 import EquosConversationPromptTemplateVarsType0
        from ..models.equos_conversation_utterance import EquosConversationUtterance
        from ..models.equos_timeline_entry import EquosTimelineEntry

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = EquosConversationStatus(d.pop("status"))

        charge = d.pop("charge")

        charge_by_second = d.pop("chargeBySecond")

        max_seconds = d.pop("maxSeconds")

        started_at = isoparse(d.pop("startedAt"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        character_id = d.pop("characterId")

        organization_id = d.pop("organizationId")

        def _parse_client(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client = _parse_client(d.pop("client", UNSET))

        def _parse_room(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room = _parse_room(d.pop("room", UNSET))

        def _parse_server_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_url = _parse_server_url(d.pop("serverUrl", UNSET))

        def _parse_remote_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_agent_name = _parse_remote_agent_name(d.pop("remoteAgentName", UNSET))

        def _parse_remote_agent_identity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_agent_identity = _parse_remote_agent_identity(d.pop("remoteAgentIdentity", UNSET))

        def _parse_consumer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumer_name = _parse_consumer_name(d.pop("consumerName", UNSET))

        def _parse_consumer_identity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumer_identity = _parse_consumer_identity(d.pop("consumerIdentity", UNSET))

        def _parse_prompt_ctx(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_ctx = _parse_prompt_ctx(d.pop("promptCtx", UNSET))

        def _parse_prompt_template_vars(data: object) -> EquosConversationPromptTemplateVarsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prompt_template_vars_type_0 = EquosConversationPromptTemplateVarsType0.from_dict(data)

                return prompt_template_vars_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EquosConversationPromptTemplateVarsType0 | None | Unset, data)

        prompt_template_vars = _parse_prompt_template_vars(d.pop("promptTemplateVars", UNSET))

        def _parse_transcript(data: object) -> list[EquosConversationUtterance] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcript_type_0 = []
                _transcript_type_0 = data
                for transcript_type_0_item_data in _transcript_type_0:
                    transcript_type_0_item = EquosConversationUtterance.from_dict(transcript_type_0_item_data)

                    transcript_type_0.append(transcript_type_0_item)

                return transcript_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquosConversationUtterance] | None | Unset, data)

        transcript = _parse_transcript(d.pop("transcript", UNSET))

        def _parse_timeline(data: object) -> list[EquosTimelineEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                timeline_type_0 = []
                _timeline_type_0 = data
                for timeline_type_0_item_data in _timeline_type_0:
                    timeline_type_0_item = EquosTimelineEntry.from_dict(timeline_type_0_item_data)

                    timeline_type_0.append(timeline_type_0_item)

                return timeline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EquosTimelineEntry] | None | Unset, data)

        timeline = _parse_timeline(d.pop("timeline", UNSET))

        def _parse_joined_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                joined_at_type_0 = isoparse(data)

                return joined_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        joined_at = _parse_joined_at(d.pop("joinedAt", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))

        equos_conversation = cls(
            id=id,
            name=name,
            status=status,
            charge=charge,
            charge_by_second=charge_by_second,
            max_seconds=max_seconds,
            started_at=started_at,
            created_at=created_at,
            updated_at=updated_at,
            character_id=character_id,
            organization_id=organization_id,
            client=client,
            room=room,
            server_url=server_url,
            remote_agent_name=remote_agent_name,
            remote_agent_identity=remote_agent_identity,
            consumer_name=consumer_name,
            consumer_identity=consumer_identity,
            prompt_ctx=prompt_ctx,
            prompt_template_vars=prompt_template_vars,
            transcript=transcript,
            timeline=timeline,
            joined_at=joined_at,
            ended_at=ended_at,
        )

        equos_conversation.additional_properties = d
        return equos_conversation

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
