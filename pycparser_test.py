import json
import os
from collections import defaultdict

from utils.pycparser_tools import parse_file, to_dict


def extract_filepath_c_files_ast(
    aim_filepath: str, fake_libc_include_path: str
) -> dict[list]:
    result = defaultdict(list)

    for dirpath, dirnames, filenames in os.walk(aim_filepath):
        for file in filenames:
            if file.endswith(".c"):
                full_path = os.path.join(dirpath, file)
                print(full_path)

                ast = parse_file(
                    full_path,
                    use_cpp=True,
                    cpp_path="gcc",
                    cpp_args=["-E", fake_libc_include_path],
                )
                for func in ast.ext:
                    result[full_path].append(to_dict(func))
    return result


# %%
