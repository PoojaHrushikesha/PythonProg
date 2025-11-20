
import argparse
import secrets
import string
import math
import sys

try:
    import pyperclip
    PYPERCLIP_AVAILABLE = True
except Exception:
    PYPERCLIP_AVAILABLE = False

def build_charset(use_lower, use_upper, use_digits, use_symbols):
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        # A conservative set of symbols typically allowed in passwords
        charset += "!@#$%^&*()-_=+[]{};:,.<>/?"
    return charset

def generate_password(length, charset):
    if not charset:
        raise ValueError("Character set is empty. Enable at least one category.")
    return ''.join(secrets.choice(charset) for _ in range(length))

def estimate_entropy(length, charset_size):
    # entropy bits = length * log2(charset_size)
    if charset_size <= 0:
        return 0.0
    return length * math.log2(charset_size)

def strength_label(entropy_bits):
    # Rough guideline:
    #  <28 bits — Very Weak
    #  28–35 — Weak
    #  36–59 — Reasonable
    #  60–127 — Strong
    #  128+ — Very Strong
    if entropy_bits < 28:
        return "Very Weak"
    if entropy_bits < 36:
        return "Weak"
    if entropy_bits < 60:
        return "Reasonable"
    if entropy_bits < 128:
        return "Strong"
    return "Very Strong"

def parse_args():
    p = argparse.ArgumentParser(description="Secure Password Generator")
    p.add_argument("-l", "--length", type=int, default=16, help="Password length (default 16)")
    p.add_argument("--no-lower", dest="lower", action="store_false", help="Exclude lowercase letters")
    p.add_argument("--no-upper", dest="upper", action="store_false", help="Exclude uppercase letters")
    p.add_argument("--no-digits", dest="digits", action="store_false", help="Exclude digits")
    p.add_argument("--no-symbols", dest="symbols", action="store_false", help="Exclude symbols")
    p.add_argument("-s", "--save", nargs="?", const="password.txt", metavar="FILE",
                   help="Save password to a file (default filename 'password.txt' if flag used without value)")
    p.add_argument("--copy", action="store_true", help="Copy password to clipboard (requires pyperclip)")
    p.add_argument("--count", type=int, default=1, help="Generate this many passwords (default 1)")
    p.add_argument("--show-charset", action="store_true", help="Print the charset used (for debugging)")
    return p.parse_args()

def interactive_if_needed(args):
    # If the user runs without flags and from a TTY, offer interactive prompts
    if sys.stdin.isatty() and len(sys.argv) == 1:
        print("Interactive Password Generator (press Enter to accept defaults)\n")
        try:
            inp = input(f"Password length [{args.length}]: ").strip()
            if inp:
                args.length = int(inp)
            def ask_bool(prompt, default):
                r = input(f"{prompt} [{'Y' if default else 'N'}]: ").strip().lower()
                if not r:
                    return default
                return r[0] in ("y", "1", "t")
            args.lower = ask_bool("Include lowercase?", args.lower)
            args.upper = ask_bool("Include uppercase?", args.upper)
            args.digits = ask_bool("Include digits?", args.digits)
            args.symbols = ask_bool("Include symbols?", args.symbols)
            inp = input(f"How many passwords to generate [{args.count}]: ").strip()
            if inp:
                args.count = int(inp)
            inp = input("Save to file? (enter filename or leave blank): ").strip()
            if inp:
                args.save = inp
            if PYPERCLIP_AVAILABLE:
                args.copy = ask_bool("Copy each password to clipboard?", args.copy)
            else:
                print("(pyperclip not available — clipboard copy disabled)")
        except KeyboardInterrupt:
            print("\nCancelled.")
            sys.exit(1)

def main():
    args = parse_args()
    # Default booleans True unless explicitly turned off
    # argparse set up default True for lower/upper/digits/symbols unless flags used
    if not hasattr(args, "lower"):
        args.lower = True
    if not hasattr(args, "upper"):
        args.upper = True
    if not hasattr(args, "digits"):
        args.digits = True
    if not hasattr(args, "symbols"):
        args.symbols = True

    # If run interactively with no flags, let user change options
    interactive_if_needed(args)

    # Validate length and count
    if args.length <= 0:
        print("Error: length must be positive.")
        sys.exit(2)
    if args.count <= 0:
        print("Error: count must be positive.")
        sys.exit(2)

    charset = build_charset(args.lower, args.upper, args.digits, args.symbols)

    if not charset:
        print("Error: No character categories selected. Enable at least one of lowercase/uppercase/digits/symbols.")
        sys.exit(2)

    if args.show_charset:
        print("Charset used:", charset)
        print("Charset size:", len(set(charset)))

    generated = []
    for i in range(args.count):
        pw = generate_password(args.length, charset)
        entropy = estimate_entropy(args.length, len(set(charset)))
        label = strength_label(entropy)

        header = f"Password #{i+1}:"
        print(header)
        print(pw)
        print(f"Length: {args.length} | Charset size: {len(set(charset))} | Entropy: {entropy:.1f} bits | Strength: {label}")
        print("-" * max(40, len(header)))

        generated.append(pw)

        if args.copy:
            if not PYPERCLIP_AVAILABLE:
                print("Warning: pyperclip not installed — cannot copy to clipboard.")
            else:
                try:
                    pyperclip.copy(pw)
                    print("(Copied to clipboard)")
                except Exception as e:
                    print("Warning: Failed to copy to clipboard:", e)

    if args.save:
        try:
            with open(args.save, "a", encoding="utf-8") as f:
                for pw in generated:
                    f.write(pw + "\n")
            print(f"Saved {len(generated)} password(s) to '{args.save}'")
        except Exception as e:
            print("Error: Could not save to file:", e)

if __name__ == "__main__":
    main()
