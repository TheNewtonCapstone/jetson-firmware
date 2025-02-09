#!/usr/bin/env bash
ROOT="$(dirname "$(readlink -f "$0")")"

# Export environment variables for paths
export NEWTON_ROOT="${ROOT}"
export JETSON_CONTAINERS_PATH="${ROOT}/lib/jetson-containers"
export PYTHONPATH="${ROOT}/:${PYTHONPATH}"
VENV_PATH="$ROOT"/.venv

echo $ROOT
INSTALL_PREFIX="/usr/local/bin"

# Make newton executable and create symlink
chmod +x "$ROOT/newton"
sudo ln -sf "$ROOT/newton" "$INSTALL_PREFIX/newton"
source "$VENV_PATH"/bin/activate
