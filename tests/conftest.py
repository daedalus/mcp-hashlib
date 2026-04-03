import pytest

from mcp_hashlib.tools import app


@pytest.fixture
def mock_server():
    return app


@pytest.fixture
def sample_tools():
    return [
        "hash_md5",
        "hash_sha1",
        "hash_sha256",
        "hash_sha512",
        "hash_sha224",
        "hash_sha384",
        "hash_sha3_224",
        "hash_sha3_256",
        "hash_sha3_384",
        "hash_sha3_512",
        "hash_blake2b",
        "hash_blake2s",
        "hash_shake_128",
        "hash_shake_256",
        "hash_pbkdf2_hmac",
        "hash_scrypt",
        "hash_file_digest",
        "hash_new",
        "hash_info",
    ]
