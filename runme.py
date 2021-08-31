import os, sys, struct, time, ssl, zlib, base64
def mv2tga(filename):
    with open(filename) as f:
        data=f.read()
    with open(os.path.splitext(filename)[0]+'.tga','wb') as f:
        f.write(zlib.decompress(base64.b64decode(data)))
def tga2mv(filename):
    with open(filename, 'rb') as f:
        data=f.read()
    with open(os.path.splitext(filename)[0]+'.txt', 'wb') as f:
        f.write(base64.b64encode(zlib.compress(data, 6))) # compress level is 0 to 9, 9 is best, 6 is the default (what nintendo apparently uses for miiverse posts)

if len(sys.argv) < 2:
    print(f"WaraWara Plaza Base64 Encoder\n\nUsage:\n  encoder.py <file name>\n\nExample:\n  encoder.py thisfile.tga - decodes and outputs a file named thisfile.txt")
else:
    file_ext = sys.argv[1][-3:]
    if file_ext == "txt":
        mv2tga(sys.argv[1])
    elif file_ext == "tga":
        tga2mv(sys.argv[1])
    else:
        print(f"Unknown file type. Must be either *.tga or *.txt")
