from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", stateless_http=True)

# In-memory document store
docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# Tool to read a document by ID
@mcp.tool()
def read_doc(doc_id: str) -> str:
    return docs.get(doc_id, "Document not found.")

# Tool to edit/update a document
@mcp.tool()
def edit_doc(doc_id: str, content: str) -> str:
    docs[doc_id] = content
    return "Document updated successfully."

# Resource to list all document IDs
@mcp.tool()
def list_docs() -> list[str]:
    return list(docs.keys())

# Resource to get the content of a specific document
@mcp.tool()
def get_doc(doc_id: str) -> str:
    return docs.get(doc_id, "Document not found.")

# Prompt to rewrite a document in markdown format
@mcp.tool()
def rewrite_doc(doc_id: str) -> str:
    doc_content = docs.get(doc_id)
    return f"Rewrite the following document in markdown format:\n\n{doc_content}"

# Prompt to summarize a document
@mcp.tool()
def summarize_doc(doc_id: str) -> str:
    doc_content = docs.get(doc_id)
    return f"Summarize the following document:\n\n{doc_content}"

# Launch the FastMCP app
mcp_app = mcp.streamable_http_app()
