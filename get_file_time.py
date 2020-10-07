
import os
import time
import datetime
import subprocess

def walk_dir(root_dir, f, baseline_timestamp):
    for cur_dir, sub_dirs, files in os.walk(root_dir):
        #print(f"Current dir: {cur_dir}");

        for a_file in files:
            abs_path_file = os.path.join(os.path.abspath(cur_dir), a_file)
            #print(f"a file= {os.path.join(os.path.abspath(cur_dir), a_file)}")
            try:
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(abs_path_file)
            except:
                pass
            else:
                # mtime is the timestamp of the file
                if mtime < baseline_timestamp :
                    print(f"{time.ctime(mtime)} : {abs_path_file}", sep='\n', file=f)
                    #subprocess.run(['touch', abs_path_file])

        for sub_dir in sub_dirs:
            walk_dir(sub_dir, f, baseline_timestamp)


def main():
    baseline_dt = datetime.datetime.strptime('2018-07-01 12:00:00', '%Y-%m-%d %H:%M:%S')
    baseline_timestamp = time.mktime(baseline_dt.timetuple()) + 1e-6 * baseline_dt.microsecond
    print(f"baseline_time= {time.ctime(baseline_timestamp)}, {baseline_timestamp}")

    path1 = '/jackyen0213';
    path2 = '/jackyen0213/Case'

    with open('old_file.txt', 'w') as f:    
        walk_dir(path2, f, baseline_timestamp)


if __name__ == "__main__":
    main()
