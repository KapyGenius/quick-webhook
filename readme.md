# FastAPI Webhook

This is a FastAPI-based webhook application that accepts POST requests and forwards the data to Formspark. The Formspark ID is stored as an environment variable.

## Features

- Accepts any POST request payload.
- Forwards the data to a Formspark endpoint.
- Dockerized for easy deployment.

---

## Prerequisites

- Python 3.10+
- Docker (optional, for containerized deployment)
- Formspark account (for the Formspark ID)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KapyGenius/quick-webhook.git
cd quick-webhook
```