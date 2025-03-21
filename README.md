# Cortellis MCP Server

This MCP (Model Context Protocol) server provides an interface to search and explore the Cortellis database for drug-related information. It offers two main functionalities:
- Drug search with various filters
- Ontology/taxonomy term exploration

## Prerequisites

- Python 3.10 or higher
- uv package manager (recommended) or pip
- Cortellis API credentials

## Installation

1. Clone and install the package:
```bash
# Using uv (recommended)
uv pip install .

# Or using pip
pip install .
```

2. Set up your environment variables by creating a `.env` file:
```bash
CORTELLIS_USERNAME=your_username
CORTELLIS_PASSWORD=your_password
```

## Usage

The server provides two main functions:

### 1. Search Drugs

Search for drugs in the Cortellis database with various filters:
- Company
- Indication
- Action
- Phase
- Technology
- Drug name
- Country

Example usage:
```python
from cortellis_mcp import search_drugs

# Search for a specific drug
results = search_drugs(drug_name="semaglutide")

# Search with multiple filters
results = search_drugs(
    company="Novo Nordisk",
    indication="obesity",
    phase="L"  # Launched
)
```

### 2. Explore Ontology

Explore the ontology/taxonomy terms in the Cortellis database:
- Actions
- Indications
- Companies
- Drug names
- Targets
- Technologies

Example usage:
```python
from cortellis_mcp import explore_ontology

# Search for action terms
results = explore_ontology(action="glucagon")

# Search for indication terms
results = explore_ontology(indication="obesity")
```

## Development Status Codes

When searching for drugs, you can use the following phase codes:
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

## Using with Cursor IDE

To use this MCP server with Cursor IDE:

1. Install the server in your project:
```bash
uv pip install mcp-cortellis
```

2. Add the following to your `.cursor/settings.json`:
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

3. Restart Cursor IDE

Now you can use the Cortellis MCP commands directly in Cursor. Example prompts:

- "Search for drugs targeting obesity in phase 3"
- "Find all launched drugs by Novo Nordisk"
- "Explore ontology terms related to glucagon"

The MCP server will automatically handle the API calls and return the results in a structured format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
