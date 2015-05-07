#!/usr/local/bin/python3

import hashlib, os, sys, time

def sort_files(dir):
    stack = [dir]
    result = {'files' : [], 'sysfiles' : [], 'links' : []}
    while stack:
        dir = stack.pop()
        for f in os.listdir(dir):
            n = os.path.join(dir, f)
            if f[0] == ".":
                 result['sysfiles'].append(n)
            elif os.path.islink(n):
                 result['links'].append(n)
            elif os.path.isdir(n):
                stack.append(n)
            else:
                result['files'].append(n)
    return result

def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename,'rb') as f: 
        for chunk in iter(lambda: f.read(128*md5.block_size), b''): 
             md5.update(chunk)
    return md5.hexdigest()

def analyze_file(f):
    checksum = md5sum(f)
    size_bytes = os.path.getsize(f)
    size_mb = round(size_bytes/(2**20), 4)
    size_gb = round(size_bytes/(2**30), 4)
    create_time = time.ctime(os.stat(f).st_birthtime)
    mod_time = time.ctime(os.path.getmtime(f))
    return [f, checksum, size_bytes, size_mb, size_gb, create_time, mod_time]
    
def report(data):
    print("\nFILES:")
    for f in data['files']:
        h = md5sum(f)
        print(f, "\t", h)
    print("\nSYSTEM FILES:")
    for s in data['sysfiles']:
        print(s)
    print("\nLINKS:") 
    for l in data['links']:
        print(l)

def main():
    dir_to_check = sys.argv[1]
    allfiles = sort_files(dir_to_check)
    for f in allfiles['files']:
        row = analyze_file(f)
        print("\t".join(map(lambda i: str(i), row)))

main()
