# Equos Python SDK
[Equos.ai](https://www.equos.ai) official Python SDK.

## Prerequisites
- Go to [Equos Studio](https://studio.equos.ai).
- Create an organization.
- Create an API Key.

## Installation
```bash
pip install equos
```

## Features

- Official Python SDK for [Equos.ai](https://www.equos.ai)
- High-level `EquosClient` grouped by resource (`brains`, `characters`, `faces`, `voices`, `conversations`, `knowledge_bases`, `organizations`, `tokens`, `health`)
- Sync and async variants for every endpoint
- Type-safe generated models for all request / response bodies
- Escape hatch to the low-level generated client for full `httpx` customization

## Quick Start

```python
import os
from equos import EquosClient

client = EquosClient(api_key=os.environ["EQUOS_API_KEY"])

# Health check
print(client.health.check())

# List the first 20 brains
print(client.brains.list())
```

You don't have an API key? [Create one here](https://studio.equos.ai).

## Configuration

By default the client targets `https://api.equos.ai`. Override the endpoint via `EquosOptions`:

```python
from equos import EquosClient, EquosOptions

client = EquosClient(
    api_key=os.environ["EQUOS_API_KEY"],
    options=EquosOptions(endpoint="https://develop-api.equos.ai"),
)
```

## API Groups

Every group is available on the `EquosClient` instance. Each method has an async counterpart suffixed with `_async`.

### `client.brains`
| Method | Description |
|---|---|
| `list(take=20, skip=0, client_query=UNSET)` | List brains |
| `get(id)` | Get a brain by id |
| `create(body)` | Create a brain (`CreateEquosBrainRequest`) |
| `update(id, body)` | Update a brain (`CreateEquosBrainRequest`) |
| `delete(id)` | Delete a brain |

### `client.characters`
| Method | Description |
|---|---|
| `list(take=20, skip=0, client_query=UNSET)` | List characters |
| `get(id)` | Get a character |
| `create(body)` | Create a character (`CreateEquosCharacterRequest`) |
| `update(id, body)` | Update a character (`UpdateEquosCharacterRequest`) |
| `delete(id)` | Delete a character |

### `client.faces`
| Method | Description |
|---|---|
| `list(take=20, skip=0, client_query=UNSET)` | List faces |
| `get(id)` | Get a face |
| `create(body)` | Create a face (`CreateEquosFaceRequest`) |
| `delete(id)` | Delete a face |

### `client.voices`
| Method | Description |
|---|---|
| `list(take=20, skip=0, client_query=UNSET)` | List voices |
| `get(id)` | Get a voice |
| `create(body)` | Create a voice (`CreateEquosVoiceRequest`) |
| `update(id, body)` | Update a voice (`CreateEquosVoiceRequest`) |
| `delete(id)` | Delete a voice |

### `client.conversations`
| Method | Description |
|---|---|
| `list(take=20, skip=0, client_query=UNSET)` | List conversations |
| `get(id)` | Get a conversation |
| `start(body)` | Start a conversation (`CreateEquosConversationRequest`) |
| `stop(id)` | Stop a conversation |

### `client.knowledge_bases`
| Method | Description |
|---|---|
| `list(take=20, skip=0, client_query=UNSET)` | List knowledge bases |
| `get(id)` | Get a knowledge base |
| `create(body)` | Create a knowledge base (`CreateKnowledgeBaseRequest`) |
| `delete(id)` | Delete a knowledge base |
| `add_document(id, body)` | Add a document (`CreateDocumentRequest`) |
| `index_document(id, doc)` | Index a document |
| `delete_document(id, doc)` | Delete a document |

### `client.organizations`
| Method | Description |
|---|---|
| `get_freemium_usage()` | Get the freemium usage for the current org |

### `client.tokens`
| Method | Description |
|---|---|
| `create(body)` | Create a short-lived access token (`CreateEquosTokenRequest`) |

### `client.health`
| Method | Description |
|---|---|
| `check()` | Health check |

## Examples

### Create and Fetch a Brain
```python
from equos import EquosClient
from equos.models import CreateEquosBrainRequest

client = EquosClient(api_key="YOUR_API_KEY")

created = client.brains.create(CreateEquosBrainRequest(name="My Brain"))
print(created.id, created.name)

fetched = client.brains.get(created.id)
print(fetched)
```

### Start a Conversation
```python
from equos import EquosClient
from equos.models import CreateEquosConversationRequest

client = EquosClient(api_key="YOUR_API_KEY")

conversation = client.conversations.start(
    CreateEquosConversationRequest(character_id="chr_...")
)
print(conversation.id, conversation.token)
```

### Async Usage
Every method has an `_async` variant that returns a coroutine:
```python
import asyncio
from equos import EquosClient

async def main():
    client = EquosClient(api_key="YOUR_API_KEY")
    brains = await client.brains.list_async(take=50)
    print(brains)

asyncio.run(main())
```

### Pagination and Filtering
`list*` endpoints accept `take`, `skip`, and `client_query`:
```python
page = client.characters.list(take=50, skip=0, client_query="external-user-123")
```

## Models and Types

All generated request / response models are re-exported for convenience:

```python
from equos.models import (
    CreateEquosBrainRequest,
    CreateEquosCharacterRequest,
    CreateEquosConversationRequest,
    CreateEquosFaceRequest,
    CreateEquosVoiceRequest,
    CreateKnowledgeBaseRequest,
    CreateDocumentRequest,
    CreateEquosTokenRequest,
    # ...and all response models
)

from equos.types import UNSET, Unset, Response
```

## Low-Level Client

For fine-grained control or endpoints not yet surfaced on `EquosClient`, use the generated client directly:

```python
from equos.client import AuthenticatedClient
from equos.client.api.brain import get_brain

auth_client = AuthenticatedClient(
    base_url="https://api.equos.ai",
    token="YOUR_API_KEY",
    auth_header_name="x-api-key",
    prefix="",
)

with auth_client as c:
    brain = get_brain.sync(id="brain_id", client=c)
    print(brain)
```

Each generated endpoint module exposes four callables:
- `sync(...)` — parsed response, or `None`
- `sync_detailed(...)` — `Response[Parsed]` with status / headers / content
- `asyncio(...)` / `asyncio_detailed(...)` — async variants

### Advanced `httpx` Customization
```python
import httpx
from equos.client import AuthenticatedClient

auth_client = AuthenticatedClient(
    base_url="https://api.equos.ai",
    token="YOUR_API_KEY",
    auth_header_name="x-api-key",
    prefix="",
    httpx_args={"timeout": 30.0, "proxies": "http://localhost:8030"},
)

# Or swap in your own httpx.Client
auth_client.set_httpx_client(httpx.Client(base_url="https://api.equos.ai"))
```

## Changelog

See [Releases](https://github.com/EquosAI/equos-python-sdk/releases) for version history.

## Other Equos SDKs

| SDK | Platform | Package |
|-----|----------|---------|
| **@equos/browser-sdk** | Browser (vanilla JS/TS) | [npm](https://www.npmjs.com/package/@equos/browser-sdk) |
| **@equos/react** | Browser (React) | [npm](https://www.npmjs.com/package/@equos/react) |
| **@equos/node-sdk** | Node.js (server-side only) | [npm](https://www.npmjs.com/package/@equos/node-sdk) |
| **equos** | Python (server-side only) | [PyPI](https://pypi.org/project/equos/) |

## Reach Us

- Equos Slack Community: [Join Equos Community Slack](https://join.slack.com/t/equosaicommunity/shared_invite/zt-3d8oy19au-jZpsJB0i~gdL0jbDswdzzQ)
- Support: [Support Form](https://docs.google.com/forms/d/e/1FAIpQLSdoK7LvORdQf7KOQKvhhlESStJcKc3bDB9HPsEet6LuOmVUfQ/viewform)

## Documentation

- Official Documentation: [https://docs.equos.ai](https://docs.equos.ai)
- Equos NodeJS Examples: [https://github.com/EquosAI/equos-examples/tree/main/examples/equos-nextjs-integration](https://github.com/EquosAI/equos-examples/tree/main/examples/equos-nextjs-integration)
- Equos React Examples: [https://github.com/EquosAI/equos-examples/blob/main/examples/equos-react-integration/README.md](https://github.com/EquosAI/equos-examples/blob/main/examples/equos-react-integration/README.md)

## Authors

- [Loïc Combis](https://www.linkedin.com/in/lo%C3%AFc-combis-a211a813a/)
