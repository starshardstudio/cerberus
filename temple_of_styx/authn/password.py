import argon2

a2ph = argon2.PasswordHasher(
    time_cost=argon2.DEFAULT_TIME_COST,
    memory_cost=argon2.DEFAULT_MEMORY_COST,
    parallelism=argon2.DEFAULT_PARALLELISM,
    hash_len=argon2.DEFAULT_HASH_LENGTH,
    salt_len=argon2.DEFAULT_RANDOM_SALT_LENGTH,
)
"""
:mod:`argon2` password hasher, configured and available for usage elsewhere in the project.
"""

__all__ = (
    "a2ph",
)
