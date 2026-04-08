"""CLI wrapper for Caesar cipher program.

Run:
  python caesar_cli.py

Features:
  - encode / decode
  - brute-force decode (try all shifts)
  - text input or file input/output
"""

from caesar_art import LOGO, SUBTITLE
from caesar_constants import MODES, SOURCES
from caesar_core import caesar_transform, brute_force_decode
from caesar_io import read_text_file, write_text_file


def read_mode() -> str:
    while True:
        mode = input("Choose mode (encode / decode / bruteforce): ").strip().lower()
        if mode in MODES:
            return mode
        print("❌ Invalid mode. Please type encode, decode, or bruteforce.")


def read_source() -> str:
    while True:
        src = input("Source (text / file): ").strip().lower()
        if src in SOURCES:
            return src
        print("❌ Invalid source. Please type text or file.")


def read_shift() -> int:
    while True:
        raw = input("Type the shift number: ").strip()
        try:
            return int(raw)
        except ValueError:
            print("❌ Please enter a valid integer shift (e.g., 3).")


def read_text() -> str:
    return input("Type your message: ").rstrip("").lower()


def read_file_path(prompt: str) -> str:
    return input(prompt).strip()


def want_continue() -> bool:
    again = input("Do you want to continue? (y/n): ").strip().lower()
    return again == "y"


def handle_encode_decode(source: str, mode: str) -> None:
    shift = read_shift()

    try:
        if source == "text":
            text = read_text()
            result = caesar_transform(text, shift, mode)
            print(f"\n✅ The {mode}d text is: {result}")
            return

        # file mode
        in_path = read_file_path("Input file path: ")
        out_path = read_file_path("Output file path: ")

        content = read_text_file(in_path).lower()
        result = caesar_transform(content, shift, mode)
        write_text_file(out_path, result)

        print(f"\n✅ Done. Wrote {mode}d output to: {out_path}")

    except FileNotFoundError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Error: {e}")


def handle_bruteforce(source: str) -> None:
    if source == "text":
        cipher_text = read_text()
    else:
        in_path = read_file_path("Input file path (ciphertext): ")
        cipher_text = read_text_file(in_path).lower()

    results = brute_force_decode(cipher_text)

    print("🔎 Brute-force results (shift -> decoded):")
    for shift, decoded in results:
        print(f"[{shift:02d}] {decoded}")

    # Optional save to file
    save = input("Save all results to a file? (y/n): ").strip().lower()
    if save == "y":
        out_path = read_file_path("Output file path: ")
        blob = "".join([f"[{s:02d}] {d}" for s, d in results]) + ""
        write_text_file(out_path, blob)
        print(f"✅ Saved brute-force results to: {out_path}")


def main() -> None:
    print(LOGO)
    print(SUBTITLE)
    print("-" * len(SUBTITLE))

    while True:
        mode = read_mode()
        source = read_source()

        if mode in {"encode", "decode"}:
            handle_encode_decode(source, mode)
        else:
            handle_bruteforce(source)

        if not want_continue():
            break


if __name__ == "__main__":
    main()
