# -*- coding: utf-8 -*-

name = "bat"

# Vendor packages: <vendor_version>+local.<our_version>
__version__ = "0.18.2"
version = __version__ + "+local.1.0.0"

description = "Vim-fork focused on extensibility and usability."

authors = ["sharkdp", "Joseph Yu"]

variants = [
    ["platform-linux", "arch-x86_64"],
    # ["platform-macos", "arch-x86_64"],
    # ["platform-windows", "arch-x86"],
    # ["platform-windows", "arch-x86_64"],
]

tools = ["bat"]
# @late()
# def tools():
#     import os
#     bin_path = os.path.join(str(this.root), 'bin')
#     executables = []
#     for item in os.listdir(bin_path):
#         path = os.path.join(bin_path, item)
#         if os.access(path, os.X_OK) and not os.path.isdir(path):
#             executables.append(item)
#     return executables

relocatable = True

build_command = r"""
set -euf -o pipefail

# Setup: curl "{CURL_FLAGS}" ...
# Show progress bar if output to terminal, else silence
declare -a CURL_FLAGS
CURL_FLAGS=("-L")
[ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")

FORK="https://github.com/sharkdp/bat"
URL="$FORK"/releases/download/"v{version}"
URL+=/bat-v{version}-"$REZ_ARCH_VERSION"-unknown-linux-musl.tar.gz

if [[ $REZ_BUILD_INSTALL -eq 1 ]]
then
    set -x
    curl "{CURL_FLAGS}" "$URL" \
    | tar --strip-components=1 -xz -C "$REZ_BUILD_INSTALL_PATH"
fi
""".format(
    version=__version__, CURL_FLAGS="${{CURL_FLAGS[@]}}"
)


def commands():
    """Commands to set up environment for ``rez env bat``"""
    env.PATH.append("{root}")
