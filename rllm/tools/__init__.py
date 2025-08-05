from rllm.tools.code_tools import (
    PythonInterpreter,
)
from rllm.tools.registry import ToolRegistry
from rllm.tools.request_manager import (
    ToolRequestManager, 
    BaseScheduler, 
    FIFOScheduler,
    ToolManagerRegistry,
    tool_manager_registry,
    get_tool_manager,
    submit_tool_request
)
from rllm.tools.web_tools import (
    FirecrawlTool,
    GoogleSearchTool,
    TavilyExtractTool,
    TavilySearchTool,
)

# Define default tools dict
DEFAULT_TOOLS = {
    "python": PythonInterpreter,
    "google_search": GoogleSearchTool,
    "firecrawl": FirecrawlTool,
    "tavily-extract": TavilyExtractTool,
    "tavily-search": TavilySearchTool,
}

# Create the singleton registry instance and register all default tools
tool_registry = ToolRegistry()
tool_registry.register_all(DEFAULT_TOOLS)

__all__ = [
    "PythonInterpreter",
    "LocalRetrievalTool",
    "GoogleSearchTool",
    "FirecrawlTool",
    "TavilyExtractTool",
    "TavilySearchTool",
    "ToolRegistry",
    "tool_registry",
    "ToolRequestManager",
    "BaseScheduler",
    "FIFOScheduler",
    "ToolManagerRegistry",
    "tool_manager_registry",
    "get_tool_manager",
    "submit_tool_request",
]
