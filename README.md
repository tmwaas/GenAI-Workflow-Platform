# GenAI Workflow Platform (Azure AKS)

A cloud-native GenAI-ready platform built to demonstrate **production-grade software engineering**, **DevOps automation**, and **scalable GenAI architecture**. The platform is validated using an **enterprise banking use case**, but intentionally designed as **reusable building blocks** rather than a one-off GenAI demo.

- Cloud-native GenAI-ready platform deployed on Azure Kubernetes Service (AKS)
- Microservices architecture with API Gateway and RAG Service (FastAPI)
- Infrastructure provisioned using Terraform and containerized with Docker
- Designed for enterprise banking environments with security and scalability in mind
- Ready to integrate Azure OpenAI and vector search (RAG) without redesign

---

## Why This Project Matters

This repository is designed to showcase how **GenAI workloads can be integrated responsibly into enterprise environments** such as banking:

- API-first, cloud-native architecture
- Clear separation of concerns between platform and GenAI logic
- Designed for regulated environments (security, RBAC, auditability)
- Ready for Azure OpenAI, RAG, and agentic workflows without redesign

---

## Key Capabilities

- Cloud-native GenAI platform on **Azure Kubernetes Service (AKS)**
- **API Gateway + RAG Service** (FastAPI microservices)
- Infrastructure as Code using **Terraform**
- Containerized workloads with **Docker**
- Designed for **Azure DevOps CI/CD pipelines**
- Extensible to **RAG pipelines and agentic workflows**

---

## Key Objectives

- Build a reusable GenAI platform using cloud-native patterns
- Separate application concerns from GenAI logic
- Demonstrate secure, scalable deployment on Azure Kubernetes Service (AKS)
- Enable future integration with Azure OpenAI and vector search (RAG)

---

## Architecture Overview

The platform is built using a cloud-native microservices architecture deployed on
Azure Kubernetes Service (AKS). The design focuses on separation of concerns,
scalability, and future-proof GenAI integration.

![Architecture Diagram](docs/architecture_diagram.png)

### Architecture Flow

1. **Client / User**
   - Sends requests to the platform via a REST API.

2. **API Gateway (FastAPI)**
   - Validates incoming requests.
   - Acts as a stable API contract for consumers.
   - Routes requests to downstream GenAI services.

3. **RAG Service (FastAPI)**
   - Encapsulates all Retrieval-Augmented Generation logic.
   - Currently returns simulated responses due to sandbox constraints.
   - Designed to integrate Azure OpenAI embeddings and vector search without impacting clients.

4. **Azure Kubernetes Service (AKS)**
   - Hosts all microservices as containerized workloads.
   - Enables independent scaling of API Gateway and RAG Service.

5. **Supporting Azure Services**
   - **Azure Container Registry (ACR)** for private container images.
   - **Azure AI Search** reserved for vector-based retrieval.
   - Infrastructure provisioned using **Terraform**.

This architecture allows GenAI capabilities to evolve independently while maintaining
a stable and secure platform for enterprise banking use cases.

**Core components:**

- **API Gateway**
  - Python FastAPI service
  - Validates requests and exposes a stable API contract
- **RAG Service**
  - Dedicated service for Retrieval-Augmented Generation logic
  - Currently simulated due to Azure Sandbox constraints
  - Designed to plug in Azure OpenAI + embeddings without redesign
- **Infrastructure**
  - Azure Kubernetes Service (AKS)
  - Azure Container Registry (ACR)
  - Azure AI Search (ready for vector search)
  - Provisioned using Terraform

The separation between API Gateway and RAG Service ensures that GenAI logic
can evolve independently without impacting consumers.

---

## RAG Examples (Conceptual & Practical)

```text
rag/examples/
├── langchain_rag_example.py
└── llamaindex_rag_example.py
```

Demonstrates:
- Chunking and embedding
- Vector retrieval
- Prompt augmentation

---

## Agentic Workflow Examples

```text
agentic/examples/
├── loan_approval_agent.py
├── multi_agent_finance.py
├── crewai_summary_agent.py
```

Demonstrates:
- Agent roles
- Multi-step workflows
- Orchestration concepts

---

## ☁️ Cloud & DevOps Stack

- Azure Kubernetes Service (AKS)
- Terraform (Infrastructure as Code)
- Docker & Kubernetes
- Azure Container Registry (ACR)
- Python (FastAPI)
- Microservices architecture
- Designed to integrate with Azure DevOps CI/CD pipelines

---

## 📁 Repository Structure

```text
genai-workflow-platform/
├── infra/
│   └── terraform/        # Azure infrastructure (AKS, Search, etc.)
├── services/
│   ├── api-gateway/      # FastAPI API Gateway
│   ├── rag-service/      # RAG service (simulated)
│   └── agent-service/   # Reserved for agentic workflows
├── rag/
│   └── examples/                  # RAG framework examples (conceptual)
│       ├── langchain_rag_example.py
│       └── llamaindex_rag_example.py│
├── agentic/
│   └── examples/                  # Agentic workflow examples
│       ├── loan_approval_agent.py
│       ├── multi_agent_finance.py
│       └── crewai_summary_agent.py
├── k8s/                  # Kubernetes manifests
├── docs/                 # Architecture & design notes
└── README.md
```

## Repository Structure Philosophy

This repository intentionally separates:

- **Production services** (`services/`) used in deployment on AKS
- **GenAI pattern exploration** (`rag/examples`, `agentic/examples`)
- **Infrastructure and platform concerns** (`infra/`, `k8s/`)

This approach allows GenAI capabilities to evolve independently
without impacting API contracts or production workloads.

---

## Deployment & Demo (Quick Start)

```bash
# --- Deployment (High Level) ---
terraform init
terraform apply
kubectl apply -f k8s/

# --- Demo (Local Port Forward) ---
kubectl port-forward deployment/api-gateway 8000:8000

# --- Call API ---
curl --get \
  --data-urlencode "question=Explain SME loan approval process" \
  http://localhost:8000/ask

# --- Example response ---
# {
#   "question": "Explain SME loan approval process",
#   "answer": "SME loan approval typically involves an initial risk assessment, credit scoring, compliance checks, and final approval by a credit committee.",
#   "source": "internal-policy-documents (simulated)"
# }
```

## Security & Constraints

- Infrastructure is provisioned using Infrastructure as Code
- Private container images stored in ACR
- Kubernetes imagePullSecrets used due to limited RBAC permissions
- GenAI responses are simulated in sandbox environments

## GenAI Upgrade Path

The current implementation simulates RAG behavior due to Azure Sandbox limitations.

In a full production setup:

- Azure OpenAI embeddings can be enabled
- Azure AI Search can be used as a vector database
- No changes are required to the API Gateway or client integrations

This design ensures low-risk evolution from prototype to production.
