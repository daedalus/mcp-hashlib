# mcp-hashlib

An MCP server that exposes hashlib functionality to LLMs.

[![PyPI](https://img.shields.io/pypi/v/mcp-hashlib.svg)](https://pypi.org/project/mcp-hashlib/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-hashlib.svg)](https://pypi.org/project/mcp-hashlib/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

mcp-name: io.github.daedalus/mcp-hashlib

## Install

```bash
pip install mcp-hashlib
```

## Usage

```python
from mcp_hashlib import mcp, main
```

## Available Tools

The MCP server exposes the following hashlib functions:

- `hash_md5` - MD5 hash
- `hash_sha1` - SHA1 hash
- `hash_sha256` - SHA256 hash
- `hash_sha512` - SHA512 hash
- `hash_sha224` - SHA224 hash
- `hash_sha384` - SHA384 hash
- `hash_sha3_224` - SHA3-224 hash
- `hash_sha3_256` - SHA3-256 hash
- `hash_sha3_384` - SHA3-384 hash
- `hash_sha3_512` - SHA3-512 hash
- `hash_blake2b` - BLAKE2b hash (512-bit)
- `hash_blake2s` - BLAKE2s hash (256-bit)
- `hash_shake_128` - SHAKE-128 XOF hash
- `hash_shake_256` - SHAKE-256 XOF hash
- `hash_pbkdf2_hmac` - PBKDF2-HMAC key derivation
- `hash_scrypt` - Scrypt key derivation
- `hash_file_digest` - Hash file-like object
- `hash_new` - Create hash with any available algorithm
- `hash_info` - Get algorithm info
- `hash_update` - Incremental hashing
- `hash_copy` - Copy hash object
- `hash_properties` - Get algorithm properties

## Development

```bash
git clone https://github.com/daedalus/mcp-hashlib.git
cd mcp-hashlib
pip install -e ".[test]"

# run tests
pytest

# format
ruff format src/ tests/

# lint
ruff check src/ tests/

# type check
mypy src/
```