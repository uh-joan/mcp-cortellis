FROM python:3.10-slim

WORKDIR /app

# Install uv for better dependency management
RUN pip install uv

# Copy only the necessary files
COPY pyproject.toml .
COPY README.md .
COPY LICENSE .
COPY cortellis_mcp ./cortellis_mcp

# Install dependencies and the package
RUN uv pip install .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the MCP server
CMD ["python", "-m", "cortellis_mcp"] 