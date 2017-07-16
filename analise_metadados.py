import pandas as pd

from file_util import FileUtil
from metrics_util import MetricsUtil
import time
import os
from collections import defaultdict

directory = "/Users/lucas/PycharmProjects/software-architecture-github-file-crawler/output_metadata/"
# read the list of files
file_list = map(lambda f: directory + "/" + f, os.listdir(directory))

flang = open("dados_meta/language.csv", "w")
fsize = open("dados_meta/size.csv", "w")
fstars = open("dados_meta/stars.csv", "w")

max_stars, repo_stars = 0, None
max_size, repo_size = 0, None

flang.write("stars\n")
fsize.write("stars\n")
fstars.write("stars\n")

erros = 0

langs = defaultdict(int)

for file in file_list:
    with open(file) as f:
        try:
            language, size, stars = f.readline().split(",")

            size = int(size)
            stars = int(stars)

            if size > max_size:
                max_size = size
                repo_size = file

            if stars > max_stars:
                max_stars = stars
                repo_stars = file

            langs[language] += 1

            flang.write("%s\n" % language)
            fsize.write("%s\n" % size)
            fstars.write("%s\n" % stars)
        except Exception:
            erros += 1

flang.close()
fsize.close()
fstars.close()


fdist = open("dados_meta/lang_dist.csv", "w")

fdist.write("lang,total\n")

for l in langs:
    fdist.write("%s,%s\n" % (l, langs[l]))

fdist.close()

print max_size
print repo_size

print "\n"

print max_stars
print repo_stars

# print erros
