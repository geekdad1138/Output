from pathlib import Path
import os
import re

root = Path(r"c:\Users\dave\Documents\GitHub\Output")
year_dir = root / "2026"

month_names = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

def human_title(path: Path) -> str:
    name = path.stem
    parts = name.split("-", 3)
    if len(parts) >= 4 and re.fullmatch(r"\d{4}", parts[0]):
        return " ".join(parts[3:]).replace("-", " ")
    return path.stem.replace("-", " ")


def relative_link(target: Path, source_dir: Path) -> str:
    return os.path.relpath(target, source_dir).replace("\\", "/")


month_dirs = sorted(
    [p for p in year_dir.iterdir() if p.is_dir() and re.fullmatch(r"\d{2}-[A-Za-z]+", p.name)],
    key=lambda p: p.name,
)

all_posts = []
for month_dir in month_dirs:
    for path in sorted(month_dir.glob("*.md"), key=lambda p: p.name, reverse=True):
        if path.name == "README.md":
            continue
        all_posts.append((path.name, path))
all_posts.sort(key=lambda item: item[0], reverse=True)

# Create year index
year_lines = [
    "# 2026 Archive",
    "",
    "This is the main index for the 2026 writing archive. It gives you a quick way to jump into a specific month or browse the latest posts.",
    "",
    "## Quick links",
    "",
    "- [Back to repository home](../README.md)",
    "- [Browse by month](#browse-by-month)",
    "- [Recent posts](#recent-posts)",
    "",
    "## Browse by month",
    "",
    "| Month | Posts |",
    "| --- | ---: |",
]
for month_dir in month_dirs:
    month_no = month_dir.name.split("-", 1)[0]
    month_label = month_names.get(month_no, month_dir.name.split("-", 1)[1])
    entries = sorted([p for p in month_dir.glob("*.md") if p.name != "README.md"], key=lambda p: p.name, reverse=True)
    year_lines.append(f"| [{month_label}]({month_dir.name}/README.md) | {len(entries)} |")

year_lines.extend(["", "## Recent posts", ""])
for _, path in all_posts[:15]:
    rel = relative_link(path, year_dir)
    year_lines.append(f"- [{human_title(path)}]({rel})")
(year_dir / "README.md").write_text("\n".join(year_lines) + "\n", encoding="utf-8")

# Create month indexes
for month_dir in month_dirs:
    month_no = month_dir.name.split("-", 1)[0]
    month_label = month_names.get(month_no, month_dir.name.split("-", 1)[1])
    entries = sorted([p for p in month_dir.glob("*.md") if p.name != "README.md"], key=lambda p: p.name, reverse=True)
    month_lines = [
        f"# {month_label} 2026",
        "",
        f"Archive for {month_label} in 2026.",
        "",
        "- [Back to 2026 archive](../README.md)",
        "",
        "## Posts",
        "",
    ]
    if entries:
        for path in entries:
            title = human_title(path)
            rel = relative_link(path, month_dir)
            month_lines.append(f"- [{title}]({rel})")
    else:
        month_lines.append("No posts published in this month yet.")
    (month_dir / "README.md").write_text("\n".join(month_lines) + "\n", encoding="utf-8")

# Create root README
root_lines = [
    "# Output 🚀",
    "",
    "> `stdout` for my professional insights, technical perspectives, and public commentary.",
    "",
    "This repository is a permanent archive of the writing I publish publicly across LinkedIn and other channels. The goal is simple: keep ideas discoverable and searchable long after a social feed has moved on.",
    "",
    "## Quick navigation",
    "",
    "- [Browse the 2026 archive](./2026/README.md)",
    "- [Open the latest month index](./2026/07-July/README.md)",
    "- [Find me on LinkedIn](https://www.linkedin.com/in/daveabraham/)",
    "",
    "## Browse by month",
    "",
    "| Month | Posts |",
    "| --- | ---: |",
]
for month_dir in month_dirs:
    month_no = month_dir.name.split("-", 1)[0]
    month_label = month_names.get(month_no, month_dir.name.split("-", 1)[1])
    entries = sorted([p for p in month_dir.glob("*.md") if p.name != "README.md"], key=lambda p: p.name, reverse=True)
    root_lines.append(f"| [{month_label}]({month_dir.relative_to(root).as_posix()}/README.md) | {len(entries)} |")
root_lines.extend(["", "## Recent posts", ""])
for _, path in all_posts[:12]:
    rel = relative_link(path, root)
    root_lines.append(f"- [{human_title(path)}]({rel})")
root_lines.extend(["", "This archive is intentionally lightweight so it can be browsed quickly from GitHub, cloned for reference, or linked to from other places.", ""])
(root / "README.md").write_text("\n".join(root_lines) + "\n", encoding="utf-8")
