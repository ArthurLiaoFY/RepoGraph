# %%
from repograph.utils import create_structure

a = create_structure(directory_path="/Users/wr80340/WorkSpace/wafer_overlay")
# %%
a.keys()
# %%
a["common"].keys()
# %%
a["common"]["plot_fn.py"]
# %%
from repograph.construct_graph import CodeGraph

code_graph = CodeGraph(root="/Users/wr80340/WorkSpace/wafer_overlay")
chat_fnames_new = code_graph.find_files(["/Users/wr80340/WorkSpace/wafer_overlay"])

# %%
from tree_sitter_languages import get_language, get_parser

example = """
#!shebang
# License blah blah (Apache 2.0)
"This is a module docstring."

a = 1

'''This
is
not
a
multiline
comment.'''

b = 2

class Test:
    "This is a class docstring."

    'This is bogus.'

    def test(self):
        "This is a function docstring."

        "Please, no."

        return 1

c = 3
"""
language = get_language()
parser = get_parser("python")
# %%
tree = parser.parse(example.encode())
node = tree.root_node
print(node.sexp())
