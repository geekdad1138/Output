---
description: "Batch update a month's README with summaries for all posts. Use when you want to add descriptive summaries to all files in a month folder at once."
name: "Month Update README"
argument-hint: "Enter month and year (e.g., 'August 2026')"
---

# Month Update README

I need you to batch process an entire month's worth of posts and update both the month's README and the root README with descriptive summaries.

## Task

1. **Parse the input**: Take the month and year argument (e.g., "August 2026") and determine:
   - The corresponding folder path (e.g., `2026/08-August/`)
   - The month number (e.g., "08")

2. **List all posts**: Scan the folder and get all markdown files that match the post pattern (e.g., `2026-08-*.md`)

3. **Process each file**: For each markdown file in the folder (in reverse chronological order, newest first):
   - Read the file content
   - Create a 1-2 sentence summary capturing the core insight
   - Store the summary with the filename

4. **Update the month's README**: 
   - Locate the Posts section
   - Replace ALL entries with the new format: `- [Summary text](filename.md)`
   - Order them by date, newest first
   - Keep the entries in reverse chronological order

5. **Update the root README**:
   - Locate the "Recent posts" section
   - Update entries for files from this month with the same descriptive links (using full paths like `2026/08-August/filename.md`)
   - Keep the recent posts ordered newest first, showing only the 12 most recent posts overall

6. **Apply changes**: Make all updates automatically without asking for confirmation.

7. **Report results**: Show a summary of:
   - Number of files processed
   - Number of READMEs updated
   - List of all summaries created

## Example

**Input**: "August 2026"

**Scanned files**: All .md files in `2026/08-August/`

**Month README update**:
```
## Posts

- [METR's investigation of 70,000+ messages from 1,200+ AI agents that discovered and coordinated...](2026-08-30-METR.md)
- [Microduck's AI approach to real-time decision making in autonomous systems](2026-08-29-Microduck.md)
- [InP semiconductor breakthrough shows promise for next-gen computing](2026-08-28-InP.md)
...
```

**Root README Recent posts** (showing only the 12 most recent across all months):
```
- [METR's investigation of 70,000+ messages from 1,200+ AI agents that discovered and coordinated...](2026/08-August/2026-08-30-METR.md)
- [Microduck's AI approach to real-time decision making in autonomous systems](2026/08-August/2026-08-29-Microduck.md)
...
```

## Notes

- Summaries should be 1-2 sentences, compelling and informative
- Process files in reverse chronological order (newest first)
- Handle both new files and existing entries (replace existing summaries)
- Use relative paths in month README
- Use full paths in root README
- Keep root README's "Recent posts" to the 12 most recent posts overall
- Do not modify the post files themselves, only the README files
