# SPEC.md — mcp-hashlib

## Purpose

An MCP server that exposes hashlib functionality to LLMs, providing cryptographic hashing and key derivation operations via the Model Context Protocol.

## Scope

**In scope:**
- All standard hash algorithms (md5, sha1, sha224, sha256, sha384, sha512)
- BLAKE2 (blake2b, blake2s)
- SHA3 (sha3_224, sha3_256, sha3_384, sha3_512)
- XOF hashes (shake_128, shake_256)
- Key derivation functions (pbkdf2_hmac, scrypt)
- Algorithm info (algorithms_available, algorithms_guaranteed)
- Hash object operations (update, copy, properties)
- File-like object hashing (file_digest)

**Not in scope:**
- Custom hash algorithms beyond what's in hashlib
- HMAC constructions (use pbkdf2_hmac)
- Encryption/decryption

## Public API / Interface

### Tools (MCP)

| Tool Name | Description | Parameters |
|-----------|-------------|------------|
| `hash_md5` | Compute MD5 hash | `data: str`, `usedforsecurity: bool` |
| `hash_sha1` | Compute SHA1 hash | `data: str`, `usedforsecurity: bool` |
| `hash_sha256` | Compute SHA256 hash | `data: str`, `usedforsecurity: bool` |
| `hash_sha512` | Compute SHA512 hash | `data: str`, `usedforsecurity: bool` |
| `hash_sha224` | Compute SHA224 hash | `data: str`, `usedforsecurity: bool` |
| `hash_sha384` | Compute SHA384 hash | `data: str`, `usedforsecurity: bool` |
| `hash_sha3_224` | Compute SHA3-224 hash | `data: str` |
| `hash_sha3_256` | Compute SHA3-256 hash | `data: str` |
| `hash_sha3_384` | Compute SHA3-384 hash | `data: str` |
| `hash_sha3_512` | Compute SHA3-512 hash | `data: str` |
| `hash_blake2b` | Compute BLAKE2b hash | `data: str`, `digest_size: int` |
| `hash_blake2s` | Compute BLAKE2s hash | `data: str`, `digest_size: int` |
| `hash_shake_128` | Compute SHAKE-128 XOF | `data: str`, `output_length: int` |
| `hash_shake_256` | Compute SHAKE-256 XOF | `data: str`, `output_length: int` |
| `hash_pbkdf2_hmac` | PBKDF2-HMAC key derivation | `password: str`, `salt: str`, `iterations: int`, `dklen: int`, `hash_name: str` |
| `hash_scrypt` | Scrypt key derivation | `password: str`, `salt: str`, `n: int`, `r: int`, `p: int`, `dklen: int` |
| `hash_file_digest` | Hash file-like object | `data: str`, `algorithm: str` |
| `hash_new` | Create hash with any algorithm | `algorithm: str`, `data: str`, `hex: bool` |
| `hash_info` | Get algorithm info | `info_type: "available" \| "guaranteed"` |
| `hash_update` | Incremental hashing | `algorithm: str`, `data_parts: list[str]`, `hex: bool` |
| `hash_copy` | Copy hash object | `algorithm: str`, `data: str` |
| `hash_properties` | Get algorithm properties | `algorithm: str` |

All tools return hex-encoded string output.

## Edge Cases

1. **Empty data**: All hash functions should handle empty string input
2. **Unknown algorithm**: hash_new should raise ValueError for invalid algorithm names
3. **XOF output length**: shake functions require positive output_length
4. **Large iterations**: pbkdf2_hmac with high iteration count may be slow
5. **Invalid key derivation parameters**: scrypt with invalid n/r/p values should raise error
6. **Binary data handling**: All tools accept string input encoded as UTF-8

## Performance & Constraints

- Pure stdlib hashlib (no external dependencies for hashing)
- MCP server using stdio transport
- Python 3.11+ required