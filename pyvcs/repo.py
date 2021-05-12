import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    pyvcs_dir = os.environ.get("GIT_DIR", default=".pyvcs")
    curr_dir = pathlib.Path(workdir)
    while str(curr_dir.absolute()) != "/":
        if (curr_dir / pyvcs_dir).exists():
            return curr_dir / pyvcs_dir
        curr_dir = curr_dir.parent
    if (curr_dir / pyvcs_dir).exists():
        return curr_dir / pyvcs_dir
    raise Exception("Not a git repository")



def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    pyvcs_dir = os.environ.get("GIT_DIR", default=".pyvcs")
    curr_path = pathlib.Path(workdir)
    if not curr_path.is_dir():
        raise Exception(f"{workdir} is not a directory")
    os.makedirs(curr_path / pyvcs_dir / "refs" / "heads")
    os.makedirs(curr_path / pyvcs_dir / "refs" / "tags")
    os.makedirs(curr_path / pyvcs_dir / "objects")
    with open(curr_path / pyvcs_dir / 'HEAD', 'w') as file:
        file.write("ref: refs/heads/master\n")
    with open(curr_path / pyvcs_dir / 'config', 'w') as file:
        file.write("[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n")
    with open(curr_path / pyvcs_dir / 'description', 'w') as file:
        file.write("Unnamed pyvcs repository.\n")
    return curr_path / pyvcs_dir

