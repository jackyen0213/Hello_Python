
import os
import re
import shutil
import time
import datetime
import subprocess

def parse_modify_file(filename):
    filename_out = filename + "_new"
    filename_bak = filename + "_bak"

    with open(filename, "r") as fp, open(filename_out, "w") as out_fp:
        lines = fp.readlines()

        pat = re.compile(r'-lNPI')

        for line in lines:
            if re.search(pat, line):
                print("\t$(LD) -o $@ $(OBJS) -L$(NPI_L1_DIR) -L$(NPI_LIB) -ldl -lpthread -lrt -lNPI -lnpiL1 -lz", file=out_fp)
            else:
                print(f"{line}", file=out_fp, end="")

    shutil.copy(filename, filename_bak)
    shutil.move(filename_out, filename)


def walk_dir(root_dir):
    for cur_dir, sub_dirs, files in os.walk(root_dir):
        print(f"Current dir: {cur_dir}");

        for a_file in files:
            if a_file == "Makefile":
                abs_filename = os.path.join(cur_dir, a_file)
                print(f"a_file = {abs_filename}")
                parse_modify_file(abs_filename)

        for sub_dir in sub_dirs:
            walk_dir(sub_dir)


def main():
    path = '/My_Libraries';

    walk_dir(path)


if __name__ == "__main__":
    main()

