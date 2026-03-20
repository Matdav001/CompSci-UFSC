# Libraries imports
from pathlib import Path

# Variables names
SOURCE_DIR = Path(".")
OUTPUT_FILE = Path.cwd().name + ".py"
CURRENT_FILE = Path(__file__).name  # this script

# Gets the files names and sorts them
python_files = sorted(
    [
        p for p in SOURCE_DIR.glob("*.py")
        if p.name not in {OUTPUT_FILE, CURRENT_FILE}
    ],
    key=lambda p: p.name
)

#
# Makes a separating line, for the end and start, like this:
# ============== EXERCISE: 01-01 ==============#
# ==================== END ====================#
#
def make_line(text: str, width: int = 45):
    text = f" {text} "
    remaining = width - len(text)
    left = remaining // 2
    right = remaining - left
    return f"# {'=' * left}{text}{'=' * right}"

#
# Prints to output file and comments all exercises
#
with open(OUTPUT_FILE,"w", encoding="utf-8") as out:
    _ = out.write("#\n#\n")
    _ = out.write(f"# {Path.cwd().name}\n")
    _ = out.write("#\n#\n\n")
    for file_path in python_files:
        clean_name = file_path.name.split(".", 1)[0]
        header = make_line(f"EXERCISE: {clean_name}")
        footer = make_line("END")
        _ = out.write("'''\n#\n")
        _ = out.write(header)
        _ = out.write("#\n")
        _ = out.write(file_path.read_text(encoding="utf-8"))
        _ = out.write("\n#\n")
        _ = out.write(footer)
        _ = out.write("#\n'''\n\n\n")

# Prints when finished
print(f"Wrote {OUTPUT_FILE}")
