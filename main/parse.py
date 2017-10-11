from refextract import extract_references_from_file
from os import path
from glob import glob
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

list_of_pdfs = find_ext("PDFS_to_PROCESS","pdf")

for pdf in list_of_pdfs:
    reference = extract_references_from_file(pdf)
    with open('drop_these_into_anystyledotio.txt','a') as biblio:
        for dictn in reference:
            raw = dictn['raw_ref']
            try:
                biblio.write("{}\n".format(str("".join(raw))))
            except UnicodeEncodeError:
                biblio.write("{}\n".format(raw))
            else:
                biblio.write("{}\n".format(raw))
            # r = dict((k, v[0]) for k, v in dictn.iteritems() if v)
            # biblio.write("{}\n".format(r))



