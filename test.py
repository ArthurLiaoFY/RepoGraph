# %%
import json
import uuid
from collections import defaultdict
from pprint import pprint
from typing import Any, Dict, List, Union

from pydantic import BaseModel

from utils.pycparser_tools import extract_ast_from_filepath, from_dict, generate_c_code


class Node(BaseModel):
    # ---------------------------
    uuid: uuid.UUID
    # ---------------------------
    rel_path: str
    fname: str
    # ---------------------------
    method: str
    name: Union[str, None] = None
    # ---------------------------
    code: str
    ast: Dict
    # ---------------------------
    line: int
    # ---------------------------


def search_node(node: Dict[str, Union[str, List, Dict]], node_type: str):
    for node_key, node_value in node.items():
        if node_key == "_nodetype" and node_value == node_type:
            print(node)

        elif isinstance(node_value, Dict):
            search_node(node=node_value, node_type=node_type)
        elif isinstance(node_value, List):
            for subnode in node_value:
                if isinstance(subnode, Dict):
                    search_node(node=subnode, node_type=node_type)
                else:
                    pass


def find_func_name(node: Dict[str, Union[str, List, Dict]]) -> Union[str, None]:
    match node["_nodetype"]:
        case "Decl":
            name = node.get("name")
        case "FuncDecl":
            name = node.get("type").get("declname")
        case "FuncDef":
            name = node.get("decl").get("name")
        case "Typedef":
            name = node.get("name")
        case _:
            name = None
    return name


# %%
repo_ast = extract_ast_from_filepath(
    aim_filepath=r"examples/c_files",
    fake_libc_include_path=r"-Iutils/fake_libc_include",
)

graph_nodes = {}
for filepath, file_content in repo_ast.items():
    print(filepath)
    print("len of ", len(file_content))
    for block in file_content:
        id = uuid.uuid4()
        graph_nodes[str(id)] = Node(
            uuid=id,
            rel_path=block["coord"].split(":")[0],
            name=find_func_name(block),
            fname=block["coord"].split(":")[0].split("/")[-1],
            code=generate_c_code(from_dict(block)),
            ast=block,
            line=block["coord"].split(":")[1],
            method=block["_nodetype"],
        )

graph_nodes[list(graph_nodes.keys())[0]]


set([v.method for v in graph_nodes.values()])


for v in graph_nodes.values():
    search_node(node=v.ast, node_type="Typedef")
