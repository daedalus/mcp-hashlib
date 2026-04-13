name: mcp-hashlib
description: >
  MCP server exposing hashlib functionality (MD5, SHA, BLAKE2, SHA3, PBKDF2, scrypt).
  Triggers on: hash, hashing, md5, sha256, crypto, cryptographic, key derivation, pbkdf2, blake2.
---

# mcp-hashlib Skill

MCP server that exposes Python's hashlib functionality to LLMs via the Model Context Protocol.

## Usage

When the user asks about:
- Computing hashes (MD5, SHA1, SHA256, SHA512, SHA224, SHA384)
- BLAKE2 hashes (blake2b, blake2s)
- SHA3 hashes (sha3_224, sha3_256, sha3_384, sha3_512)
- XOF hashes (shake_128, shake_256)
- Key derivation (pbkdf2_hmac, scrypt)
- Hash file-like objects
- Getting algorithm information

The MCP server provides tools for all these operations.

## Examples

- "Compute SHA256 hash of this string"
- "What hash algorithms are available?"
- "Generate a PBKDF2 key with 100k iterations"
- "Hash this data using blake2b"
- "How do I use hashlib for key derivation?"

## Tools

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
- `hash_blake2b` - BLAKE2b hash
- `hash_blake2s` - BLAKE2s hash
- `hash_shake_128` - SHAKE-128 XOF
- `hash_shake_256` - SHAKE-256 XOF
- `hash_pbkdf2_hmac` - PBKDF2-HMAC key derivation
- `hash_scrypt` - Scrypt key derivation
- `hash_file_digest` - Hash file-like object
- `hash_new` - Create hash with any algorithm
- `hash_info` - Get algorithm info
- `hash_update` - Incremental hashing
- `hash_copy` - Copy hash object
- `hash_properties` - Get algorithm properties