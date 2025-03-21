# Cortellis MCP Server

This MCP (Model Context Protocol) server provides an interface to search and explore the Cortellis database for drug-related information. It offers two main functionalities:
- Drug search with various filters
- Ontology/taxonomy term exploration

## Prerequisites

- Python 3.10 or higher
- uv package manager (recommended) or pip
- Cortellis API credentials

## Installation

### Local Installation (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/uh-joan/mcp-cortellis.git
cd mcp-cortellis
```

2. Install the package:
```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
uv pip install -e .

# Or using pip
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
pip install -e .
```

3. Set up your environment variables:
```bash
# In your .env file
CORTELLIS_USERNAME=your_username
CORTELLIS_PASSWORD=your_password
```

### Alternative: Install from GitHub

If you just want to use the package without development:

```bash
# Using uv
uv pip install git+https://github.com/uh-joan/mcp-cortellis.git

# Or using pip
pip install git+https://github.com/uh-joan/mcp-cortellis.git
```

## Using with Cursor IDE

Add the following to your `.cursor/settings.json`:
```json
{
  "mcps": {
    "cortellis": {
      "command": ["python", "-m", "cortellis_mcp"],
      "env": {
        "CORTELLIS_USERNAME": "your_username",
        "CORTELLIS_PASSWORD": "your_password"
      }
    }
  }
}
```

After restarting Cursor, you can use natural language prompts like:
- "Search for drugs targeting obesity in phase 3"
- "Find all launched drugs by Novo Nordisk"
- "Explore ontology terms related to glucagon"

## Quick Start

```python
from cortellis_mcp import search_drugs, explore_ontology

# Search for Phase 3 obesity drugs
results = search_drugs(
    indication="obesity",
    phase="C3"  # Phase 3 Clinical
)

# Explore ontology terms
terms = explore_ontology(
    category="indication",
    term="diabetes"
)
```

Check the [examples](examples/) directory for more usage examples.

## API Reference

See the [API documentation](docs/API.md) for detailed function references.

### Development Status Codes

When searching for drugs, you can use these phase codes:
- `S`: Suspended
- `DR`: Discovery/Preclinical
- `CU`: Clinical (unknown phase)
- `C1`: Phase 1 Clinical
- `C2`: Phase 2 Clinical
- `C3`: Phase 3 Clinical
- `PR`: Pre-registration
- `R`: Registered
- `L`: Launched
- `OL`: Outlicensed
- `NDR`: No Development Reported
- `DX`: Discontinued
- `W`: Withdrawn

## Development

For development work, follow the [Local Installation](#local-installation-recommended) instructions above, which will install the package in editable mode (`-e` flag).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
