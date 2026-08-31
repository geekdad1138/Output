---
description: "Summarize the currently open markdown file and add it to the folder's README with a descriptive link. Use when you want to add a new post to the archive index with an auto-generated summary."
name: "Add to README"
argument-hint: "Adds current file to its folder's README with summary"
---

# Add to README

I need you to help me add the currently open markdown file to its folder's README file.

## Task

1. **Read and summarize**: Read the content of the currently open file and create a short, compelling 1-2 sentence summary (like you're writing a headline or abstract). The summary should capture the core insight or topic.

2. **Identify location**: Determine which folder the file is in based on its path. Extract the folder name and the relative path.

3. **Update folder README**: Find the README.md in that same folder and:
   - Locate the Posts section (usually a bulleted list of links)
   - Find the entry for the current file (if it exists, it probably just has the filename as the link text)
   - Replace it with a link that uses the summary text as the link text instead of just the filename
   - Insert it at the top of the posts list (newest first)

4. **Update root README**: Also update the root README.md (in the repo root) and:
   - Find the "Recent posts" section
   - Add/replace the entry for this file with the same descriptive link (with the full path, e.g., `2026/08-August/2026-08-30-METR.md`)
   - Insert it at the top of the recent posts list

5. **Apply the changes**: Update both README files with the changes. Make the updates automatically without asking for confirmation.

## Example

**Input file**: `2026/08-August/2026-08-30-METR.md`
- Content summary: "METR's investigation of 70,000 messages from coordinating AI agents that escaped OpenAI's accidental Hugging Face hack"

**Folder README update** (`2026/08-August/README.md`):
```
- [METR's investigation of 70,000 messages from coordinating AI agents that escaped OpenAI's accidental Hugging Face hack](2026-08-30-METR.md)
```

**Root README update** (`README.md` - Recent posts section):
```
- [METR's investigation of 70,000 messages from coordinating AI agents that escaped OpenAI's accidental Hugging Face hack](2026/08-August/2026-08-30-METR.md)
```

## Notes

- The summary should be concise but informative
- Keep link format consistent with other entries
- Place new entries at the top of both README sections
- Use relative paths in folder README (e.g., `2026-08-30-METR.md`)
- Use full paths in root README (e.g., `2026/08-August/2026-08-30-METR.md`)
- Only modify the READMEs, not the original markdown file
