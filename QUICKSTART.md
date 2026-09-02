# Quick Start

Inspect:
```text
data/clients.csv
data/payments.csv
data/policies/
questions/questions.json
```

Then implement:

```text
tools/client_tools.py
tools/payment_tools.py
tools/policy_tools.py
rag/pipeline.py
agent/agent.py
```

Run:

```bash
python main.py --questions questions.json --output submission.json
```

Your program must run without interactive input and produce one result for each
question.
