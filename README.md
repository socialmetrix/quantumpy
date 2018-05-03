# Quantumpy

An ultra simple wrapper for the [Socialmetrix](https://www.socialmetrix.com/) Quantum API, with basic functionality

## Usage

You will need an active account and your API Secret to authenticate. Check the [official documentation](https://socialmetrix.github.io/quantum-api-docs/#getting-your-api-secret) to obtain yours.

```python
from quantumpy import QuantumAPI

# Initialize connection with the api, providing your api_secret
api_secret = '1357c94eccd047b78e66ebe78675d3dfd27be69f'
q = QuantumAPI(api_secret)

# Get all projects associated with account
projects = q.get_projects()
for project in projects:
  print(project['name'])
```

## Installation

```bash
git checkout https://github.com/socialmetrix/quantumpy.git quantumpy
cd quantumpy
pip install --upgrade --force-reinstall -e .
pip show quantumpy
```

## API Documentation

Original API docs are [available here](https://socialmetrix.github.io/quantum-api-docs/)
