# %%
import os

from clang.cindex import Index


def parse_repo(repo_path):
    result = {}
    index = Index.create()
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".c") or file.endswith(".h"):
                filepath = os.path.join(root, file)
                print(f"Parsing {filepath}")
                result[filepath] = index.parse(filepath, args=["-Iinclude", "-std=c11"])
                # 分析 translation unit 的 AST
                # ...
    return result


result = parse_repo("./DPS-2000AB-8A_APP_fullcode_1")

# %%
result['./DPS-2000AB-8A_APP_fullcode_1/p33FJ64GS606.h']
# %%
