from dataclasses import dataclass

from equos.client.api.brain import create_brain, delete_brain, get_brain, list_brains, update_brain
from equos.client.api.character import (
    create_character,
    delete_character,
    get_character,
    list_characters,
    update_character,
)
from equos.client.api.conversation import (
    get_conversation_by_id,
    list_conversations,
    start_conversation,
    stop_conversation,
)
from equos.client.api.face import create_face, delete_face, get_face, list_faces
from equos.client.api.health import health_check
from equos.client.api.knowledge_base import (
    add_document,
    create_knowledge_base,
    delete_document,
    delete_knowledge_base,
    get_knowledge_base,
    index_document,
    list_knowledge_bases,
)
from equos.client.api.organization import get_freemium_usage
from equos.client.api.tokens import create_token
from equos.client.api.voice import create_voice, delete_voice, get_voice, list_voices, update_voice
from equos.client.client import AuthenticatedClient
from equos.client.models.create_document_request import CreateDocumentRequest
from equos.client.models.create_document_response import CreateDocumentResponse
from equos.client.models.create_equos_brain_request import CreateEquosBrainRequest
from equos.client.models.create_equos_character_request import CreateEquosCharacterRequest
from equos.client.models.create_equos_conversation_request import CreateEquosConversationRequest
from equos.client.models.create_equos_conversation_response import CreateEquosConversationResponse
from equos.client.models.create_equos_face_request import CreateEquosFaceRequest
from equos.client.models.create_equos_token_request import CreateEquosTokenRequest
from equos.client.models.create_equos_token_response import CreateEquosTokenResponse
from equos.client.models.create_equos_voice_request import CreateEquosVoiceRequest
from equos.client.models.create_knowledge_base_request import CreateKnowledgeBaseRequest
from equos.client.models.equos_brain import EquosBrain
from equos.client.models.equos_character import EquosCharacter
from equos.client.models.equos_conversation import EquosConversation
from equos.client.models.equos_document import EquosDocument
from equos.client.models.equos_face import EquosFace
from equos.client.models.equos_knowledge_base import EquosKnowledgeBase
from equos.client.models.equos_voice import EquosVoice
from equos.client.models.health_response import HealthResponse
from equos.client.models.list_equos_brains_response import ListEquosBrainsResponse
from equos.client.models.list_equos_characters_response import ListEquosCharactersResponse
from equos.client.models.list_equos_conversations_response import ListEquosConversationsResponse
from equos.client.models.list_equos_faces_response import ListEquosFacesResponse
from equos.client.models.list_equos_knowledge_bases_response import ListEquosKnowledgeBasesResponse
from equos.client.models.list_equos_voices_response import ListEquosVoicesResponse
from equos.client.models.update_equos_character_request import UpdateEquosCharacterRequest
from equos.client.types import UNSET, Unset

DEFAULT_VERSION = "v3"
DEFAULT_ENDPOINT = "https://api.equos.ai"


@dataclass
class EquosOptions:
    """
    Options for configuring the Equos client.
    """

    endpoint: str | None = None


class _ApiGroup:
    def __init__(self, client: AuthenticatedClient):
        self._client = client


class BrainsApi(_ApiGroup):
    def list(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosBrainsResponse | None:
        return list_brains.sync(client=self._client, take=take, skip=skip, client_query=client_query)

    async def list_async(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosBrainsResponse | None:
        return await list_brains.asyncio(client=self._client, take=take, skip=skip, client_query=client_query)

    def get(self, id: str) -> EquosBrain | None:
        return get_brain.sync(id=id, client=self._client)

    async def get_async(self, id: str) -> EquosBrain | None:
        return await get_brain.asyncio(id=id, client=self._client)

    def create(self, body: CreateEquosBrainRequest) -> EquosBrain | None:
        return create_brain.sync(client=self._client, body=body)

    async def create_async(self, body: CreateEquosBrainRequest) -> EquosBrain | None:
        return await create_brain.asyncio(client=self._client, body=body)

    def update(self, id: str, body: CreateEquosBrainRequest) -> EquosBrain | None:
        return update_brain.sync(id=id, client=self._client, body=body)

    async def update_async(self, id: str, body: CreateEquosBrainRequest) -> EquosBrain | None:
        return await update_brain.asyncio(id=id, client=self._client, body=body)

    def delete(self, id: str) -> EquosBrain | None:
        return delete_brain.sync(id=id, client=self._client)

    async def delete_async(self, id: str) -> EquosBrain | None:
        return await delete_brain.asyncio(id=id, client=self._client)


class CharactersApi(_ApiGroup):
    def list(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosCharactersResponse | None:
        return list_characters.sync(client=self._client, take=take, skip=skip, client_query=client_query)

    async def list_async(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosCharactersResponse | None:
        return await list_characters.asyncio(client=self._client, take=take, skip=skip, client_query=client_query)

    def get(self, id: str) -> EquosCharacter | None:
        return get_character.sync(id=id, client=self._client)

    async def get_async(self, id: str) -> EquosCharacter | None:
        return await get_character.asyncio(id=id, client=self._client)

    def create(self, body: CreateEquosCharacterRequest) -> EquosCharacter | None:
        return create_character.sync(client=self._client, body=body)

    async def create_async(self, body: CreateEquosCharacterRequest) -> EquosCharacter | None:
        return await create_character.asyncio(client=self._client, body=body)

    def update(self, id: str, body: UpdateEquosCharacterRequest) -> EquosCharacter | None:
        return update_character.sync(id=id, client=self._client, body=body)

    async def update_async(self, id: str, body: UpdateEquosCharacterRequest) -> EquosCharacter | None:
        return await update_character.asyncio(id=id, client=self._client, body=body)

    def delete(self, id: str) -> EquosCharacter | None:
        return delete_character.sync(id=id, client=self._client)

    async def delete_async(self, id: str) -> EquosCharacter | None:
        return await delete_character.asyncio(id=id, client=self._client)


class FacesApi(_ApiGroup):
    def list(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosFacesResponse | None:
        return list_faces.sync(client=self._client, take=take, skip=skip, client_query=client_query)

    async def list_async(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosFacesResponse | None:
        return await list_faces.asyncio(client=self._client, take=take, skip=skip, client_query=client_query)

    def get(self, id: str) -> EquosFace | None:
        return get_face.sync(id=id, client=self._client)

    async def get_async(self, id: str) -> EquosFace | None:
        return await get_face.asyncio(id=id, client=self._client)

    def create(self, body: CreateEquosFaceRequest) -> EquosFace | None:
        return create_face.sync(client=self._client, body=body)

    async def create_async(self, body: CreateEquosFaceRequest) -> EquosFace | None:
        return await create_face.asyncio(client=self._client, body=body)

    def delete(self, id: str) -> EquosFace | None:
        return delete_face.sync(id=id, client=self._client)

    async def delete_async(self, id: str) -> EquosFace | None:
        return await delete_face.asyncio(id=id, client=self._client)


class VoicesApi(_ApiGroup):
    def list(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosVoicesResponse | None:
        return list_voices.sync(client=self._client, take=take, skip=skip, client_query=client_query)

    async def list_async(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosVoicesResponse | None:
        return await list_voices.asyncio(client=self._client, take=take, skip=skip, client_query=client_query)

    def get(self, id: str) -> EquosVoice | None:
        return get_voice.sync(id=id, client=self._client)

    async def get_async(self, id: str) -> EquosVoice | None:
        return await get_voice.asyncio(id=id, client=self._client)

    def create(self, body: CreateEquosVoiceRequest) -> EquosVoice | None:
        return create_voice.sync(client=self._client, body=body)

    async def create_async(self, body: CreateEquosVoiceRequest) -> EquosVoice | None:
        return await create_voice.asyncio(client=self._client, body=body)

    def update(self, id: str, body: CreateEquosVoiceRequest) -> EquosVoice | None:
        return update_voice.sync(id=id, client=self._client, body=body)

    async def update_async(self, id: str, body: CreateEquosVoiceRequest) -> EquosVoice | None:
        return await update_voice.asyncio(id=id, client=self._client, body=body)

    def delete(self, id: str) -> EquosVoice | None:
        return delete_voice.sync(id=id, client=self._client)

    async def delete_async(self, id: str) -> EquosVoice | None:
        return await delete_voice.asyncio(id=id, client=self._client)


class ConversationsApi(_ApiGroup):
    def list(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosConversationsResponse | None:
        return list_conversations.sync(client=self._client, take=take, skip=skip, client_query=client_query)

    async def list_async(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosConversationsResponse | None:
        return await list_conversations.asyncio(client=self._client, take=take, skip=skip, client_query=client_query)

    def get(self, id: str) -> EquosConversation | None:
        return get_conversation_by_id.sync(id=id, client=self._client)

    async def get_async(self, id: str) -> EquosConversation | None:
        return await get_conversation_by_id.asyncio(id=id, client=self._client)

    def start(self, body: CreateEquosConversationRequest) -> CreateEquosConversationResponse | None:
        return start_conversation.sync(client=self._client, body=body)

    async def start_async(self, body: CreateEquosConversationRequest) -> CreateEquosConversationResponse | None:
        return await start_conversation.asyncio(client=self._client, body=body)

    def stop(self, id: str) -> EquosConversation | None:
        return stop_conversation.sync(id=id, client=self._client)

    async def stop_async(self, id: str) -> EquosConversation | None:
        return await stop_conversation.asyncio(id=id, client=self._client)


class KnowledgeBasesApi(_ApiGroup):
    def list(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosKnowledgeBasesResponse | None:
        return list_knowledge_bases.sync(
            client=self._client, take=take, skip=skip, client_query=client_query
        )

    async def list_async(
        self,
        *,
        take: float | Unset = 20.0,
        skip: float | Unset = 0.0,
        client_query: str | Unset = UNSET,
    ) -> ListEquosKnowledgeBasesResponse | None:
        return await list_knowledge_bases.asyncio(
            client=self._client, take=take, skip=skip, client_query=client_query
        )

    def get(self, id: str) -> EquosKnowledgeBase | None:
        return get_knowledge_base.sync(id=id, client=self._client)

    async def get_async(self, id: str) -> EquosKnowledgeBase | None:
        return await get_knowledge_base.asyncio(id=id, client=self._client)

    def create(self, body: CreateKnowledgeBaseRequest) -> EquosKnowledgeBase | None:
        return create_knowledge_base.sync(client=self._client, body=body)

    async def create_async(self, body: CreateKnowledgeBaseRequest) -> EquosKnowledgeBase | None:
        return await create_knowledge_base.asyncio(client=self._client, body=body)

    def delete(self, id: str) -> EquosKnowledgeBase | None:
        return delete_knowledge_base.sync(id=id, client=self._client)

    async def delete_async(self, id: str) -> EquosKnowledgeBase | None:
        return await delete_knowledge_base.asyncio(id=id, client=self._client)

    def add_document(self, id: str, body: CreateDocumentRequest) -> CreateDocumentResponse | None:
        return add_document.sync(id=id, client=self._client, body=body)

    async def add_document_async(
        self, id: str, body: CreateDocumentRequest
    ) -> CreateDocumentResponse | None:
        return await add_document.asyncio(id=id, client=self._client, body=body)

    def index_document(self, id: str, doc: str) -> EquosDocument | None:
        return index_document.sync(id=id, doc=doc, client=self._client)

    async def index_document_async(self, id: str, doc: str) -> EquosDocument | None:
        return await index_document.asyncio(id=id, doc=doc, client=self._client)

    def delete_document(self, id: str, doc: str) -> EquosDocument | None:
        return delete_document.sync(id=id, doc=doc, client=self._client)

    async def delete_document_async(self, id: str, doc: str) -> EquosDocument | None:
        return await delete_document.asyncio(id=id, doc=doc, client=self._client)


class OrganizationsApi(_ApiGroup):
    def get_freemium_usage(self) -> float | None:
        return get_freemium_usage.sync(client=self._client)

    async def get_freemium_usage_async(self) -> float | None:
        return await get_freemium_usage.asyncio(client=self._client)


class TokensApi(_ApiGroup):
    def create(self, body: CreateEquosTokenRequest) -> CreateEquosTokenResponse | None:
        return create_token.sync(client=self._client, body=body)

    async def create_async(self, body: CreateEquosTokenRequest) -> CreateEquosTokenResponse | None:
        return await create_token.asyncio(client=self._client, body=body)


class HealthApi(_ApiGroup):
    def check(self) -> HealthResponse | None:
        return health_check.sync(client=self._client)

    async def check_async(self) -> HealthResponse | None:
        return await health_check.asyncio(client=self._client)


class EquosClient:
    """
    Main Equos SDK client (Python).

    Thin wrapper around the generated OpenAPI client, mirroring the TS SDK API.
    """

    def __init__(self, api_key: str, options: EquosOptions | None = None):
        endpoint = options.endpoint if options and options.endpoint else DEFAULT_ENDPOINT

        self._base_url = endpoint

        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token=api_key,
            auth_header_name="x-api-key",
            prefix="",
        )

        self.brains = BrainsApi(self._client)
        self.characters = CharactersApi(self._client)
        self.faces = FacesApi(self._client)
        self.voices = VoicesApi(self._client)
        self.conversations = ConversationsApi(self._client)
        self.knowledge_bases = KnowledgeBasesApi(self._client)
        self.organizations = OrganizationsApi(self._client)
        self.tokens = TokensApi(self._client)
        self.health = HealthApi(self._client)

    @classmethod
    def create(cls, api_key: str, options: EquosOptions | None = None) -> "EquosClient":
        """
        Create a new Equos client instance.

        :param api_key: Your Equos API key
        :param options: Optional client configuration
        """
        return cls(api_key, options)

    @property
    def base_url(self) -> str:
        """
        Get the base URL used by this client.
        """
        return self._base_url
