import pathlib

import cffi

ffibuilder = cffi.FFI()

this_dir = pathlib.Path().absolute()
h_file_name = this_dir / "calculations.h"
with open(h_file_name) as h_file:
    ffibuilder.cdef(h_file.read())

ffibuilder.set_source(
    "_calculations_cffi",
    # Since you're calling a fully-built library directly, no custom source
    # is necessary. You need to include the .h files, though, because behind
    # the scenes cffi generates a .c file that contains a Python-friendly
    # wrapper around each of the functions.
    '#include "calculations.h"',
    # The important thing is to include the pre-built lib in the list of
    # libraries you're linking against:
    sources=["calculations.c"],
    include_dirs=[this_dir.as_posix()],
    extra_link_args=["-Wl,-rpath,."],
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
