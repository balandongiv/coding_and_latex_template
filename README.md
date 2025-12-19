You’re seeing `npm: command not found` / `npx: command not found`, which means **Node never got installed in the container** (so Gemini CLI can’t be installed either). In Codespaces/devcontainers this most often happens because:

- the container **wasn’t rebuilt** after you edited `devcontainer.json`, _or_
- relying on **nvm inside `onCreateCommand`** is brittle (PATH / shell init can differ, and if that step fails once, you’re left with no node/npm).

The most reliable fix: **install Node 20 using a Dev Container “feature”** (so `node/npm/npx` are always present), then install Gemini CLI in `postCreateCommand`.

### ✅ Drop-in `devcontainer.json` fix (recommended)

```jsonc
{
  "name": "LaTeX + Python + Node20 + Gemini (Codespaces)",
  "image": "mcr.microsoft.com/devcontainers/python:3.12-bookworm",

  "features": {
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },

  "containerEnv": {
    "PIP_DISABLE_PIP_VERSION_CHECK": "1"
  },

  "postCreateCommand": "bash -lc \"set -e; echo '== System packages (TeX) =='; sudo apt-get update; sudo apt-get install -y --no-install-recommends texlive-latex-recommended texlive-latex-extra texlive-xetex texlive-fonts-recommended latexmk biber chktex ca-certificates curl git; sudo apt-get clean; sudo rm -rf /var/lib/apt/lists/*; echo '== Python packages =='; python -m pip install --upgrade pip; pip install --no-cache-dir jupyter ipykernel numpy pandas matplotlib requests rich pytest black ruff; echo '== Node =='; node -v; npm -v; npx -v; echo '== Install Gemini CLI =='; npm install -g @google/gemini-cli; gemini --version\"",

  "customizations": {
    "vscode": {
      "extensions": [
        "James-Yu.latex-workshop",
        "ms-python.python",
        "ms-toolsai.jupyter",
        "charliermarsh.ruff",
        "ms-python.black-formatter",
        "esbenp.prettier-vscode",
        "streetsidesoftware.code-spell-checker"
      ],
      "settings": {
        "latex-workshop.view.pdf.viewer": "tab",
        "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",
        "latex-workshop.synctex.afterBuild.enabled": true,
        "latex-workshop.latex.outDir": "%DIR%/out",
        "latex-workshop.latex.tools": [
          {
            "name": "latexmk-xe",
            "command": "latexmk",
            "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "-xelatex",
              "-outdir=%OUTDIR%",
              "%DOC%"
            ]
          }
        ],
        "latex-workshop.latex.recipes": [
          { "name": "latexmk (XeLaTeX)", "tools": ["latexmk-xe"] }
        ],
        "latex-workshop.latex.autoBuild.run": "onSave",
        "editor.formatOnSave": true,
        "ruff.lint.run": "onSave",
        "editor.fontSize": 14,
        "editor.tabSize": 2,
        "files.autoSave": "onFocusChange"
      }
    }
  }
}
```

### Important: you must rebuild the container

After saving `devcontainer.json`:

- VS Code Command Palette → **“Dev Containers: Rebuild Container”**
- or in Codespaces: **Rebuild** (same idea)

### After rebuild, these should work

```bash
node -v
npm -v
npx -v
gemini --version
```

If you rebuild and `node -v` still fails, tell me what you see in **“Dev Containers” logs** during rebuild (the Node feature step will usually show clearly whether it ran).
