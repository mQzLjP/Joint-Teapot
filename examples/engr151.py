import re
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, TypeVar

from joint_teapot import Teapot, logger


class ENGR151Teapot(Teapot):
    def archive_repos(self, regex: str) -> None:
        print(f"Archiving repos with name matching {regex}")
        for repo_name in self.gitea.get_all_repo_names():
            if re.match(regex, repo_name):
                print(f"Archived {repo_name}")
                self.gitea.repository_api.repo_edit(
                    self.gitea.org_name, repo_name, body={"archived": True}
                )
            else:
                print(f"Skipped {repo_name}")


if __name__ == "__main__":
    teapot = ENGR151Teapot()
    teapot.archive_repos(".*-p1")
