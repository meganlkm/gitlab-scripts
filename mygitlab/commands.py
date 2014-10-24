""" gitlab commands """

from config import Config
conf = Config()


def cmd_router(prog=None, **kwargs):
    """ command router """


def cat_file_from_obj(args):
    """ cat-file-from-obj """


def create_project(args):
    """ create-project """


def get_group(args):
    """ get-group """
    # stuff


def merge_request(args):
    """ merge request """
    #stuff

# class Commands(conf):

#     """ Config for mygitlab """

#     def __init__(self):
#         """ Commands::init """

#     def cmd_router(self, prog=None, **kwargs):
#         """ command router """

#     def _cat_file_from_obj(self, args):
#         """ cat-file-from-obj """
#         # usage() {
#         #     echo "$(tput bold)Usage:$(tput sgr0)"
#         #     echo "  cat-file-from-sha [options]"
#         #     echo "$(tput bold)Options:$(tput sgr0)"
#         #     echo "  -f file path/name"
#         #     echo "  -r repository"
#         #     echo "  -s sha to show (default is HEAD)"
#         #     exit 1
#         # }

#         # repo= file=
#         # sha=HEAD

#         # while getopts r:s:f: opt; do
#         #     case $opt in
#         #         f) file=${OPTARG} ;;
#         #         r) repo=${OPTARG} ;;
#         #         s) sha=${OPTARG} ;;
#         #         *) usage ;;
#         #     esac
#         # done

#         # if [[ $repo == '' ||
#         #       $sha == '' ||
#         #       $file == ''
#         #     ]]; then
#         #     usage
#         # fi

#         # git clone --bare ${repo} ${TMP_DIR} > /dev/null 2>&1
#         # cd ${TMP_DIR}
#         # git cat-file -p $(git ls-tree ${sha} ${file} | cut -d " " -f 3 | cut -f 1)
#         # cd ${BASE_DIR} && rm -rf ${TMP_DIR}
