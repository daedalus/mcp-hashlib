import hashlib
import io
from typing import Any

from fastmcp import FastMCP

server = FastMCP("mcp-hashlib")


@server.tool()
def hash_md5(data: str, usedforsecurity: bool = True) -> str:
    """Compute MD5 hash"""
    h = hashlib.md5(data.encode(), usedforsecurity=usedforsecurity)
    return h.hexdigest()


@server.tool()
def hash_sha1(data: str, usedforsecurity: bool = True) -> str:
    """Compute SHA1 hash"""
    h = hashlib.sha1(data.encode(), usedforsecurity=usedforsecurity)
    return h.hexdigest()


@server.tool()
def hash_sha256(data: str, usedforsecurity: bool = True) -> str:
    """Compute SHA256 hash"""
    h = hashlib.sha256(data.encode(), usedforsecurity=usedforsecurity)
    return h.hexdigest()


@server.tool()
def hash_sha512(data: str, usedforsecurity: bool = True) -> str:
    """Compute SHA512 hash"""
    h = hashlib.sha512(data.encode(), usedforsecurity=usedforsecurity)
    return h.hexdigest()


@server.tool()
def hash_sha224(data: str, usedforsecurity: bool = True) -> str:
    """Compute SHA224 hash"""
    h = hashlib.sha224(data.encode(), usedforsecurity=usedforsecurity)
    return h.hexdigest()


@server.tool()
def hash_sha384(data: str, usedforsecurity: bool = True) -> str:
    """Compute SHA384 hash"""
    h = hashlib.sha384(data.encode(), usedforsecurity=usedforsecurity)
    return h.hexdigest()


@server.tool()
def hash_sha3_224(data: str) -> str:
    """Compute SHA3-224 hash"""
    h = hashlib.sha3_224(data.encode())
    return h.hexdigest()


@server.tool()
def hash_sha3_256(data: str) -> str:
    """Compute SHA3-256 hash"""
    h = hashlib.sha3_256(data.encode())
    return h.hexdigest()


@server.tool()
def hash_sha3_384(data: str) -> str:
    """Compute SHA3-384 hash"""
    h = hashlib.sha3_384(data.encode())
    return h.hexdigest()


@server.tool()
def hash_sha3_512(data: str) -> str:
    """Compute SHA3-512 hash"""
    h = hashlib.sha3_512(data.encode())
    return h.hexdigest()


@server.tool()
def hash_blake2b(data: str, digest_size: int = 64) -> str:
    """Compute BLAKE2b hash (512-bit)"""
    h = hashlib.blake2b(data.encode(), digest_size=digest_size)
    return h.hexdigest()


@server.tool()
def hash_blake2s(data: str, digest_size: int = 32) -> str:
    """Compute BLAKE2s hash (256-bit)"""
    h = hashlib.blake2s(data.encode(), digest_size=digest_size)
    return h.hexdigest()


@server.tool()
def hash_shake_128(data: str, output_length: int = 32) -> str:
    """Compute SHAKE-128 XOF hash (variable length)"""
    h = hashlib.shake_128(data.encode())
    return h.digest(output_length).hex()


@server.tool()
def hash_shake_256(data: str, output_length: int = 64) -> str:
    """Compute SHAKE-256 XOF hash (variable length)"""
    h = hashlib.shake_256(data.encode())
    return h.digest(output_length).hex()


@server.tool()
def hash_pbkdf2_hmac(
    password: str,
    salt: str,
    iterations: int = 100000,
    dklen: int = 32,
    hash_name: str = "sha256",
) -> str:
    """PBKDF2-HMAC key derivation"""
    result = hashlib.pbkdf2_hmac(
        hash_name,
        password.encode(),
        salt.encode(),
        iterations,
        dklen=dklen,
    )
    return result.hex()


@server.tool()
def hash_scrypt(
    password: str,
    salt: str,
    n: int = 16384,
    r: int = 8,
    p: int = 1,
    dklen: int = 32,
) -> str:
    """Scrypt key derivation"""
    result = hashlib.scrypt(
        password.encode(),
        salt=salt.encode(),
        n=n,
        r=r,
        p=p,
        dklen=dklen,
    )
    return result.hex()


@server.tool()
def hash_file_digest(data: str, algorithm: str = "sha256") -> str:
    """Compute hash of a file-like object"""
    result = hashlib.file_digest(io.BytesIO(data.encode()), algorithm)
    return result.hexdigest()


@server.tool()
def hash_new(algorithm: str, data: str, hex: bool = True) -> str:
    """Create hash object using any available algorithm"""
    h = hashlib.new(algorithm, data.encode())
    if hex:
        return h.hexdigest()
    else:
        return h.digest().hex()


@server.tool()
def hash_info(info_type: str = "available") -> str:
    """Get information about available hash algorithms"""
    if info_type == "available":
        return ", ".join(sorted(hashlib.algorithms_available))
    else:
        return ", ".join(sorted(hashlib.algorithms_guaranteed))


@server.tool()
def hash_update(algorithm: str, data_parts: list[str], hex: bool = True) -> str:
    """Compute hash incrementally with multiple updates"""
    h = hashlib.new(algorithm)
    for part in data_parts:
        h.update(part.encode())
    if hex:
        return h.hexdigest()
    else:
        return h.digest().hex()


@server.tool()
def hash_copy(algorithm: str, data: str) -> str:
    """Create a copy of a hash object"""
    h = hashlib.new(algorithm, data.encode())
    h_copy = h.copy()
    return h_copy.hexdigest()


@server.tool()
def hash_properties(algorithm: str) -> str:
    """Get properties of a hash algorithm"""
    import json

    h = hashlib.new(algorithm)
    props = {
        "name": h.name,
        "digest_size": h.digest_size,
        "block_size": h.block_size,
    }
    return json.dumps(props, indent=2)


def main() -> None:
    server.run()


mcp = server


async def call_tool(name: str, arguments: dict[str, Any]) -> list[Any]:
    """Call an MCP tool by name with arguments.

    Args:
        name: The name of the tool to call.
        arguments: Dictionary of arguments to pass to the tool.

    Returns:
        A list of text content results from the tool call.
    """
    try:
        result = await server.call_tool(name, arguments)
        return result.content
    except Exception as e:
        if "not found" in str(e).lower() or "unknown" in str(e).lower():
            raise ValueError(f"Unknown tool: {name}") from e
        raise
