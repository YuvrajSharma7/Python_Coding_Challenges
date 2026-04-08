"""Core Caesar cipher logic (pure functions)."""

from caesar_constants import ALPHABET


def normalize_shift(shift: int) -> int:
    """Normalize shift to the alphabet length."""
    return shift % len(ALPHABET)


def caesar_transform(text: str, shift: int, mode: str) -> str:
    """Encode or decode text using a Caesar cipher.

    Behavior:
      - Preserves non-alphabet characters (spaces, digits, punctuation) unchanged.
      - Operates on lowercase a-z. Caller may .lower() first.

    Args:
        text: Input text.
        shift: Shift amount (any integer).
        mode: 'encode' or 'decode'.

    Returns:
        Transformed text.
    """
    shift = normalize_shift(shift)
    if mode == "decode":
        shift *= -1

    out = []
    n = len(ALPHABET)

    for ch in text:
        if ch in ALPHABET:
            idx = (ALPHABET.index(ch) + shift) % n
            out.append(ALPHABET[idx])
        else:
            out.append(ch)

    return "".join(out)


def brute_force_decode(cipher_text: str):
    """Try all possible shifts (0-25) to brute-force decode.

    Returns:
        List of tuples: (shift, decoded_text) where shift is the key used to decode.
    """
    results = []
    for shift in range(len(ALPHABET)):
        decoded = caesar_transform(cipher_text, shift, mode="decode")
        results.append((shift, decoded))
    return results
