#!/usr/bin/env sh
# Instalar (desde la raíz del repo):
#   chmod +x scripts/merci/pre-commit
#   ln -sf ../../scripts/merci/pre-commit .git/hooks/pre-commit
set -eu
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Automatización de Sitemap en cambios a public/
if git diff --cached --name-only --diff-filter=ACM | grep -q "^public/"; then
    echo "[Merci] Detectados cambios en public/, actualizando sitemap.xml..."
    python3 scripts/merci/merci_sitemap.py
    git add public/sitemap.xml
fi

# Ejecutar merci-audit.py sobre los archivos staged
exec python3 scripts/merci/merci-audit.py --git-staged
