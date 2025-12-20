# Git Reset Cheat Sheet (Beginner-Friendly, Real-World Workflow)

Here’s a beginner-friendly, “real life” scenario that fits all 4 reset types, with **the same common steps first**, then “which reset to pick” depending on what happened.

---

## Scenario (your workflow)

You work on **different computers / Codespaces** and sometimes let **Codex / Gemini CLI** make changes automatically.

Example:

* On Computer A / Codespace A, you made a couple commits on `main`.
* On Computer B / Codespace B, you (or Codex/Gemini) also made commits on `main`.
* Now your current workspace feels “messy”: commits are wrong order, or automation committed something you don’t want, or you pulled and got conflicts.
* You decide: “I want my branch to go back to an earlier commit, and then decide what to keep.”

---

## Common steps (do these before choosing Soft/Mixed/Hard/Keep)

### 0) Safety check (especially with automation + multiple machines)

**Goal:** don’t lose work you didn’t mean to lose.

In VS Code:

1. Open **Source Control** (Ctrl+Shift+G)
2. Look for:

   * **Staged Changes**
   * **Changes**
   * anything you care about

If there are important changes you might want later, do **one** of these:

**Option A — Commit a safety snapshot (easy for beginners)**

* Click **+** to stage everything → write message like `WIP safety snapshot` → **Commit**

  * (You can undo/clean later.)

**Option B — Stash (cleaner)**

* Source Control `…` → **Stash** → **Stash Changes**

  * This hides local changes so resets are safer.

---

### 1) Make sure you’re on the right branch

* Bottom-left status bar: confirm it says `main` (or the branch you intend).

---

### 2) Get the latest remote info (important when you use multiple computers)

Terminal:

```bash
git fetch --all --prune
```

This updates your view of `origin/main` without changing files.

---

### 3) Open history and choose the “good” commit

In VS Code:

* Source Control → **Graph / History**
* Find a commit you trust (example: “before Codex/Gemini made weird changes” or “last known good build”).

---

### 4) Start reset (the same UI for all 4)

In VS Code:

* **Right-click** that commit → **Reset current branch to this commit…**
* Now you see the dialog with: **Soft / Mixed / Hard / Keep**

At this point, the *only difference* is which option you pick.

---

## How beginners choose the right option (based on common situations)

### A) You want to “rewind commits” but keep ALL code changes ready to recommit

**Typical when:** automation created multiple commits and you want to squash/rewrite them.

✅ Pick **Soft**

* Result: files unchanged, changes become **staged**
* Then you can make **one clean commit**.

Terminal equivalent:

```bash
git reset --soft <commit>
```

---

### B) You want to “rewind commits” but keep changes as normal edits (not staged)

**Typical when:** you want to re-check what changed, run tests, stage selectively.

✅ Pick **Mixed**

* Result: files unchanged, changes become **unstaged**

Terminal:

```bash
git reset --mixed <commit>
# or: git reset <commit>
```

---

### C) You want to throw away local work and go back exactly (clean slate)

**Typical when:** Codex/Gemini generated junk edits, or you don’t care about local changes.

⚠️ Pick **Hard**

* Result: working files revert; uncommitted changes lost

Terminal:

```bash
git reset --hard <commit>
```

---

### D) You want to rewind commits BUT protect your current local edits

**Typical when:** you have local uncommitted work in this Codespace/computer, and you don’t want it overwritten.

✅ Pick **Keep**

* Result: reset only if it won’t clobber your edits (otherwise it fails safely)

Terminal:

```bash
git reset --keep <commit>
```

---

## After reset (common “finish” steps)

No matter which type you chose:

1. **Run your build/tests**
2. If you used stash:

   * Source Control `…` → **Stash → Apply Stash**
3. If you plan to sync to GitHub and you reset history **on a branch that was already pushed**:

   * You may need:

     ```bash
     git push --force-with-lease
     ```
   * (Only do this if you understand you’re rewriting the branch history on remote.)

---

## A simple rule for your specific workflow (multi-machine + AI automation)

* If you’re unsure: **Mixed** is the safest “I want to inspect and keep my changes” choice.
* If you have local edits you must not lose: **Keep**
* If you’re cleaning up automation commits into one commit: **Soft**
* If you want to completely discard local mess: **Hard**

If you tell me which of these is your current case:

1. “automation made bad commits”, 2) “I need to keep local edits”, 3) “I want clean slate”
   …I’ll recommend the exact reset type and the exact VS Code clicks + terminal commands to finish cleanly.

---

## Check that installs succeeded (after rebuilding the container)

**Important:** you must rebuild the container after saving `devcontainer.json`.

In VS Code:

* Command Palette → **Dev Containers: Rebuild Container**

In Codespaces:

* **Rebuild** (same idea)

After the rebuild, confirm these commands work:

```bash
node -v
npm -v
npx -v
gemini --version
```

If you rebuild and `node -v` still fails, check the **Dev Containers** logs during rebuild.
The Node feature step will usually show clearly whether it ran.
