# %%
import json
import uuid
from collections import defaultdict
from pprint import pprint

from pydantic import BaseModel

from utils.pycparser_tools import extract_ast_from_filepath, from_dict, generate_c_code

repo_ast = extract_ast_from_filepath(
    aim_filepath=r"examples/c_files",
    fake_libc_include_path=r"-Iutils/fake_libc_include",
)


# %%
class Node(BaseModel):
    uuid: uuid.UUID
    rel_path: str
    fname: str
    code: str
    ast: dict
    line: int
    method: str


# %%
# result
graph_nodes = {}
for filepath, file_content in repo_ast.items():
    print(filepath)
    for block in file_content:
        id = uuid.uuid4()
        graph_nodes[str(id)] = Node(
            uuid=id,
            rel_path=block["coord"].split(":")[0],
            fname=block["coord"].split(":")[0].split("/")[-1],
            code=generate_c_code(from_dict(block)),
            ast=block,
            line=block["coord"].split(":")[1],
            method=block["_nodetype"],
        )

        # print(generate_c_code(from_dict(block)))
    # break

#     result = defaultdict(list)

# for element in data["ext"]:
#     result[element["_nodetype"]].append(element)
# a2.append()
# %%

pprint(graph_nodes[list(graph_nodes.keys())[0]])
# %%
result.keys()
# %%
pprint(result["FuncDef"][0].keys())
# %%
for i in range(len(result["FuncDef"])):
    pprint(result["FuncDef"][i]["decl"]["name"])
    for block_item in result["FuncDef"][i]["body"]["block_items"]:
        if block_item["_nodetype"] == "FuncCall":
            pprint(block_item["name"]["name"])
    print("*" * 10)

# %%
for func in from_dict(data).ext:
    pprint(func.decl)
    print(generate_c_code(func))
    print("*" * 50)
# %%
Node(
    uuid=UUID("dc5e4765-756e-40ef-852d-0edf02771f38"),
    rel_path="examples/c_files/basic.c",
    fname="basic.c",
    code="int foo()\n{\n}\n\n",
    ast={
        "_nodetype": "FuncDef",
        "coord": "examples/c_files/basic.c:1:5",
        "decl": {
            "_nodetype": "Decl",
            "name": "foo",
            "quals": [],
            "align": [],
            "storage": [],
            "funcspec": [],
            "coord": "examples/c_files/basic.c:1:5",
            "type": {
                "_nodetype": "FuncDecl",
                "coord": "examples/c_files/basic.c:1:5",
                "type": {
                    "_nodetype": "TypeDecl",
                    "declname": "foo",
                    "quals": [],
                    "align": None,
                    "coord": "examples/c_files/basic.c:1:5",
                    "type": {
                        "_nodetype": "IdentifierType",
                        "names": ["int"],
                        "coord": "examples/c_files/basic.c:1:1",
                    },
                },
                "args": None,
            },
            "bitsize": None,
            "init": None,
        },
        "body": {
            "_nodetype": "Compound",
            "coord": "examples/c_files/basic.c:1:1",
            "block_items": None,
        },
        "param_decls": None,
    },
    line=1,
    method="FuncDef",
)
