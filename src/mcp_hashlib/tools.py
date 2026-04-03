import hashlib
import io

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

app = Server("mcp-hashlib")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="hash_md5",
            description="Compute MD5 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "usedforsecurity": {
                        "type": "boolean",
                        "description": "Use for security purposes (default true)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha1",
            description="Compute SHA1 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "usedforsecurity": {
                        "type": "boolean",
                        "description": "Use for security purposes (default true)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha256",
            description="Compute SHA256 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "usedforsecurity": {
                        "type": "boolean",
                        "description": "Use for security purposes (default true)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha512",
            description="Compute SHA512 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "usedforsecurity": {
                        "type": "boolean",
                        "description": "Use for security purposes (default true)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha224",
            description="Compute SHA224 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "usedforsecurity": {
                        "type": "boolean",
                        "description": "Use for security purposes (default true)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha384",
            description="Compute SHA384 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "usedforsecurity": {
                        "type": "boolean",
                        "description": "Use for security purposes (default true)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha3_224",
            description="Compute SHA3-224 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"}
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha3_256",
            description="Compute SHA3-256 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"}
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha3_384",
            description="Compute SHA3-384 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"}
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_sha3_512",
            description="Compute SHA3-512 hash",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"}
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_blake2b",
            description="Compute BLAKE2b hash (512-bit)",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "digest_size": {
                        "type": "integer",
                        "description": "Digest size in bytes (default 64)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_blake2s",
            description="Compute BLAKE2s hash (256-bit)",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "digest_size": {
                        "type": "integer",
                        "description": "Digest size in bytes (default 32)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_shake_128",
            description="Compute SHAKE-128 XOF hash (variable length)",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "output_length": {
                        "type": "integer",
                        "description": "Output length in bytes (default 32)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_shake_256",
            description="Compute SHAKE-256 XOF hash (variable length)",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data to hash"},
                    "output_length": {
                        "type": "integer",
                        "description": "Output length in bytes (default 64)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_pbkdf2_hmac",
            description="PBKDF2-HMAC key derivation",
            inputSchema={
                "type": "object",
                "properties": {
                    "password": {
                        "type": "string",
                        "description": "Password to derive key from",
                    },
                    "salt": {"type": "string", "description": "Salt value"},
                    "iterations": {
                        "type": "integer",
                        "description": "Number of iterations (default 100000)",
                    },
                    "dklen": {
                        "type": "integer",
                        "description": "Derived key length (default 32)",
                    },
                    "hash_name": {
                        "type": "string",
                        "description": "Hash algorithm (default sha256)",
                    },
                },
                "required": ["password", "salt"],
            },
        ),
        Tool(
            name="hash_scrypt",
            description="Scrypt key derivation",
            inputSchema={
                "type": "object",
                "properties": {
                    "password": {
                        "type": "string",
                        "description": "Password to derive key from",
                    },
                    "salt": {"type": "string", "description": "Salt value"},
                    "n": {
                        "type": "integer",
                        "description": "CPU/memory cost parameter (default 16384)",
                    },
                    "r": {
                        "type": "integer",
                        "description": "Block size parameter (default 8)",
                    },
                    "p": {
                        "type": "integer",
                        "description": "Parallelization parameter (default 1)",
                    },
                    "dklen": {
                        "type": "integer",
                        "description": "Derived key length (default 32)",
                    },
                },
                "required": ["password", "salt"],
            },
        ),
        Tool(
            name="hash_file_digest",
            description="Compute hash of a file-like object",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "Data to hash (treated as file content)",
                    },
                    "algorithm": {
                        "type": "string",
                        "description": "Hash algorithm (default sha256)",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="hash_new",
            description="Create hash object using any available algorithm",
            inputSchema={
                "type": "object",
                "properties": {
                    "algorithm": {
                        "type": "string",
                        "description": "Algorithm name (e.g., md5, sha256, blake2b)",
                    },
                    "data": {"type": "string", "description": "Data to hash"},
                    "hex": {
                        "type": "boolean",
                        "description": "Return hex digest (default true)",
                    },
                },
                "required": ["algorithm", "data"],
            },
        ),
        Tool(
            name="hash_info",
            description="Get information about available hash algorithms",
            inputSchema={
                "type": "object",
                "properties": {
                    "info_type": {
                        "type": "string",
                        "enum": ["available", "guaranteed"],
                        "description": "Which algorithms to return",
                    }
                },
                "required": ["info_type"],
            },
        ),
        Tool(
            name="hash_update",
            description="Compute hash incrementally with multiple updates",
            inputSchema={
                "type": "object",
                "properties": {
                    "algorithm": {
                        "type": "string",
                        "description": "Hash algorithm (e.g., sha256, md5, blake2b)",
                    },
                    "data_parts": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of data strings to hash incrementally",
                    },
                    "hex": {
                        "type": "boolean",
                        "description": "Return hex digest (default true)",
                    },
                },
                "required": ["algorithm", "data_parts"],
            },
        ),
        Tool(
            name="hash_copy",
            description="Create a copy of a hash object",
            inputSchema={
                "type": "object",
                "properties": {
                    "algorithm": {"type": "string", "description": "Hash algorithm"},
                    "data": {"type": "string", "description": "Initial data to hash"},
                },
                "required": ["algorithm", "data"],
            },
        ),
        Tool(
            name="hash_properties",
            description="Get properties of a hash algorithm",
            inputSchema={
                "type": "object",
                "properties": {
                    "algorithm": {
                        "type": "string",
                        "description": "Hash algorithm name",
                    },
                },
                "required": ["algorithm"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: "dict[str, object]") -> list[TextContent]:
    if name == "hash_md5":
        data = arguments["data"].encode()
        usedforsecurity = arguments.get("usedforsecurity", True)
        h = hashlib.md5(data, usedforsecurity=usedforsecurity)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha1":
        data = arguments["data"].encode()
        usedforsecurity = arguments.get("usedforsecurity", True)
        h = hashlib.sha1(data, usedforsecurity=usedforsecurity)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha256":
        data = arguments["data"].encode()
        usedforsecurity = arguments.get("usedforsecurity", True)
        h = hashlib.sha256(data, usedforsecurity=usedforsecurity)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha512":
        data = arguments["data"].encode()
        usedforsecurity = arguments.get("usedforsecurity", True)
        h = hashlib.sha512(data, usedforsecurity=usedforsecurity)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha224":
        data = arguments["data"].encode()
        usedforsecurity = arguments.get("usedforsecurity", True)
        h = hashlib.sha224(data, usedforsecurity=usedforsecurity)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha384":
        data = arguments["data"].encode()
        usedforsecurity = arguments.get("usedforsecurity", True)
        h = hashlib.sha384(data, usedforsecurity=usedforsecurity)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha3_224":
        data = arguments["data"].encode()
        h = hashlib.sha3_224(data)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha3_256":
        data = arguments["data"].encode()
        h = hashlib.sha3_256(data)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha3_384":
        data = arguments["data"].encode()
        h = hashlib.sha3_384(data)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_sha3_512":
        data = arguments["data"].encode()
        h = hashlib.sha3_512(data)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_blake2b":
        data = arguments["data"].encode()
        digest_size = arguments.get("digest_size", 64)
        h = hashlib.blake2b(data, digest_size=digest_size)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_blake2s":
        data = arguments["data"].encode()
        digest_size = arguments.get("digest_size", 32)
        h = hashlib.blake2s(data, digest_size=digest_size)
        return [TextContent(type="text", text=h.hexdigest())]

    if name == "hash_shake_128":
        data = arguments["data"].encode()
        output_length = arguments.get("output_length", 32)
        h = hashlib.shake_128(data)
        return [TextContent(type="text", text=h.digest(output_length).hex())]

    if name == "hash_shake_256":
        data = arguments["data"].encode()
        output_length = arguments.get("output_length", 64)
        h = hashlib.shake_256(data)
        return [TextContent(type="text", text=h.digest(output_length).hex())]

    if name == "hash_pbkdf2_hmac":
        password = arguments["password"].encode()
        salt = arguments["salt"].encode()
        iterations = arguments.get("iterations", 100000)
        dklen = arguments.get("dklen", 32)
        hash_name = arguments.get("hash_name", "sha256")
        result = hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=dklen)
        return [TextContent(type="text", text=result.hex())]

    if name == "hash_scrypt":
        password = arguments["password"].encode()
        salt = arguments["salt"].encode()
        n = arguments.get("n", 16384)
        r = arguments.get("r", 8)
        p = arguments.get("p", 1)
        dklen = arguments.get("dklen", 32)
        result = hashlib.scrypt(password, salt=salt, n=n, r=r, p=p, dklen=dklen)
        return [TextContent(type="text", text=result.hex())]

    if name == "hash_file_digest":
        data = arguments["data"].encode()
        algorithm = arguments.get("algorithm", "sha256")
        result = hashlib.file_digest(io.BytesIO(data), algorithm)
        return [TextContent(type="text", text=result.hexdigest())]

    if name == "hash_new":
        algorithm = arguments["algorithm"]
        data = arguments["data"].encode()
        hex_output = arguments.get("hex", True)
        h = hashlib.new(algorithm, data)
        if hex_output:
            return [TextContent(type="text", text=h.hexdigest())]
        else:
            return [TextContent(type="text", text=h.digest().hex())]

    if name == "hash_info":
        info_type = arguments["info_type"]
        if info_type == "available":
            return [
                TextContent(
                    type="text", text=", ".join(sorted(hashlib.algorithms_available))
                )
            ]
        else:
            return [
                TextContent(
                    type="text", text=", ".join(sorted(hashlib.algorithms_guaranteed))
                )
            ]

    if name == "hash_update":
        algorithm = arguments["algorithm"]
        data_parts = arguments["data_parts"]
        hex_output = arguments.get("hex", True)
        h = hashlib.new(algorithm)
        for part in data_parts:
            h.update(part.encode())
        if hex_output:
            return [TextContent(type="text", text=h.hexdigest())]
        else:
            return [TextContent(type="text", text=h.digest().hex())]

    if name == "hash_copy":
        algorithm = arguments["algorithm"]
        data = arguments["data"].encode()
        h = hashlib.new(algorithm, data)
        h_copy = h.copy()
        return [TextContent(type="text", text=h_copy.hexdigest())]

    if name == "hash_properties":
        algorithm = arguments["algorithm"]
        h = hashlib.new(algorithm)
        import json

        props = {
            "name": h.name,
            "digest_size": h.digest_size,
            "block_size": h.block_size,
        }
        return [TextContent(type="text", text=json.dumps(props, indent=2))]

    raise ValueError(f"Unknown tool: {name}")


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


mcp = app
