import pathlib

import cffi

# builder que para gerar o bind entre C e Python
ffibuilder = cffi.FFI()

# pega o arquivo header
this_dir = pathlib.Path().absolute()
h_file_name = this_dir / "calculations.h"
with open(h_file_name) as h_file:
    ffibuilder.cdef(h_file.read())

# seta o arquivo header e o ponto .c a se linkar
ffibuilder.set_source(
    "_calculations_cffi",
    '#include "calculations.h"',
    sources=["calculations.c"],
    include_dirs=[this_dir.as_posix()],
    extra_link_args=["-Wl,-rpath,."],
)

# compila o código C e gera a pasta Realise
# com o pacote e as funções
if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
