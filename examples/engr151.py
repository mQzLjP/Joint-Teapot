import argparse
import re

from joint_teapot import Teapot


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
    parser = argparse.ArgumentParser(description="ENGR151 Teapot Utility")
    subparsers = parser.add_subparsers(dest="command")

    archive_parser = subparsers.add_parser(
        "archive-repos", help="Archive repositories matching a regex pattern."
    )
    archive_parser.add_argument(
        "regex", type=str, help="The regex pattern to match repository names."
    )

    args = parser.parse_args()

    teapot = ENGR151Teapot()

    if args.command == "archive-repos":
        teapot.archive_repos(args.regex)
    else:
        parser.print_help()
