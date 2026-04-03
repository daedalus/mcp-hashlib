import hashlib

import pytest

from mcp_hashlib.tools import call_tool


@pytest.mark.asyncio
async def test_hash_md5():
    result = await call_tool("hash_md5", {"data": "hello"})
    assert result[0].text == hashlib.md5(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_sha256():
    result = await call_tool("hash_sha256", {"data": "hello"})
    assert result[0].text == hashlib.sha256(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_sha512():
    result = await call_tool("hash_sha512", {"data": "hello"})
    assert result[0].text == hashlib.sha512(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_blake2b():
    result = await call_tool("hash_blake2b", {"data": "hello"})
    assert result[0].text == hashlib.blake2b(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_blake2s():
    result = await call_tool("hash_blake2s", {"data": "hello"})
    assert result[0].text == hashlib.blake2s(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_sha3_256():
    result = await call_tool("hash_sha3_256", {"data": "hello"})
    assert result[0].text == hashlib.sha3_256(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_shake_256():
    result = await call_tool("hash_shake_256", {"data": "hello", "output_length": 32})
    h = hashlib.shake_256(b"hello")
    expected = h.digest(32).hex()
    assert result[0].text == expected


@pytest.mark.asyncio
async def test_hash_pbkdf2_hmac():
    result = await call_tool(
        "hash_pbkdf2_hmac",
        {"password": "password", "salt": "salt", "iterations": 1000, "dklen": 32},
    )
    expected = hashlib.pbkdf2_hmac("sha256", b"password", b"salt", 1000, dklen=32).hex()
    assert result[0].text == expected


@pytest.mark.asyncio
async def test_hash_scrypt():
    result = await call_tool(
        "hash_scrypt",
        {
            "password": "password",
            "salt": "salt",
            "n": 1024,
            "r": 8,
            "p": 1,
            "dklen": 32,
        },
    )
    expected = hashlib.scrypt(
        b"password", salt=b"salt", n=1024, r=8, p=1, dklen=32
    ).hex()
    assert result[0].text == expected


@pytest.mark.asyncio
async def test_hash_file_digest():
    result = await call_tool(
        "hash_file_digest", {"data": "hello", "algorithm": "sha256"}
    )
    import io

    expected = hashlib.file_digest(io.BytesIO(b"hello"), "sha256").hexdigest()
    assert result[0].text == expected


@pytest.mark.asyncio
async def test_hash_new():
    result = await call_tool("hash_new", {"algorithm": "sha256", "data": "hello"})
    assert result[0].text == hashlib.sha256(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_new_hex_false():
    result = await call_tool(
        "hash_new", {"algorithm": "sha256", "data": "hello", "hex": False}
    )
    assert result[0].text == hashlib.sha256(b"hello").digest().hex()


@pytest.mark.asyncio
async def test_hash_new_all_algorithms():
    available = hashlib.algorithms_available
    for algo in ["md5-sha1", "ripemd160", "sha512_224", "sha512_256", "sm3"]:
        if algo in available:
            result = await call_tool("hash_new", {"algorithm": algo, "data": "test"})
            expected = hashlib.new(algo, b"test").hexdigest()
            assert result[0].text == expected, f"Failed for {algo}"


@pytest.mark.asyncio
async def test_hash_info_shows_all():
    result = await call_tool("hash_info", {"info_type": "available"})
    algos = result[0].text.split(", ")
    assert "md5" in algos
    assert "sha256" in algos


@pytest.mark.asyncio
async def test_hash_info_guaranteed():
    result = await call_tool("hash_info", {"info_type": "guaranteed"})
    algos = result[0].text.split(", ")
    assert "md5" in algos
    assert "sha256" in algos


@pytest.mark.asyncio
async def test_hash_update():
    result = await call_tool(
        "hash_update", {"algorithm": "sha256", "data_parts": ["hello", "world"]}
    )
    h = hashlib.sha256()
    h.update(b"hello")
    h.update(b"world")
    assert result[0].text == h.hexdigest()


@pytest.mark.asyncio
async def test_hash_copy():
    result = await call_tool("hash_copy", {"algorithm": "sha256", "data": "hello"})
    assert result[0].text == hashlib.sha256(b"hello").hexdigest()


@pytest.mark.asyncio
async def test_hash_properties():
    import json

    result = await call_tool("hash_properties", {"algorithm": "sha256"})
    props = json.loads(result[0].text)
    assert props["name"] == "sha256"
    assert props["digest_size"] == 32
    assert props["block_size"] == 64


@pytest.mark.asyncio
async def test_unknown_tool():
    with pytest.raises(ValueError):
        await call_tool("unknown_tool", {})
