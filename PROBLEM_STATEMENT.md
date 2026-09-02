# Payment Investigation Assistant

## Objective

Build a small AI-powered assistant for a bank's payment operations/compliance
team.

The assistant must answer natural-language payment-investigation questions by
combining:

- structured client data;
- structured payment data;
- policy/procedure documents;
- RAG;
- deterministic tools;
- an LLM/agent orchestration layer.

## Target architecture

```text
                 Investigation Question
                          |
                          v
                    LLM / AI Agent
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
    Client Tool      Payment Tools      Policy RAG
          |               |               |
          +---------------+---------------+
                          |
                          v
                       Evidence
                          |
                          v
                    LLM synthesis
                          |
                          v
                Grounded recommendation
                    + citations
```

## Example

Question:

> What review requirement applies to P50001 and why?

A strong assistant should:
1. retrieve P50001;
2. identify the client and relevant region;
3. retrieve applicable policy evidence;
4. check destination risk;
5. compare the transaction against deterministic thresholds;
6. produce a grounded recommendation;
7. cite the evidence.

## Critical banking reasoning principle

A policy trigger is **not automatically proof of suspicious activity**.

The assistant should distinguish:

- observed transaction facts;
- policy triggers;
- assumptions;
- missing evidence;
- recommended next action.

## Policy corpus

The corpus intentionally contains:
- global policy;
- regional procedures;
- high-risk jurisdiction list;
- investigation procedure;
- decoy administrative notes.

The assistant should retrieve relevant evidence instead of simply reading every
document or using the first search result.

## 60-minute constraint

Do not build an enterprise platform.

A small, reliable implementation with clear separation between:
RAG → tools → agent → grounded answer
is preferred.
