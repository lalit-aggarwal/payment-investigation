"""
Policy retrieval tool interfaces.

The agent should use these methods to obtain policy evidence rather than
opening policy files directly.

The implementation should preserve the source document name so that the final
assistant can cite the evidence.
"""


def search_policy(
    query: str,
    top_k: int = 5,
) -> list[dict]:
    """
    Retrieve policy evidence relevant to a natural-language query.

    Parameters
    ----------
    query:
        Example:
        ``"high value payment enhanced review threshold"``.

    top_k:
        Maximum number of results.

    Returns
    -------
    list[dict]
        Suggested result:

        {
            "source": "global_payment_policy.md",
            "text": "...relevant passage...",
            "score": 0.91
        }

    Implementation
    --------------
    Connect this method to ``rag/pipeline.py``.
    """
    pass


def get_policy_document(source: str) -> dict:
    """
    OPTIONAL: Retrieve a complete policy document by source name.

    Useful after the agent has already identified the relevant document.
    """
    pass
