import codecs
import os

def remove_first_line(fname):
    """ Removing first line of file """
    with codecs.open(fname, 'r', 'utf-8') as fin:
        data = fin.read().splitlines(True)
    with codecs.open('temp_file.tsv', 'w','utf-8') as fout:
        fout.writelines(data[1:])

    fin.close()
    fout.close()
    # Delete original file and rename temp file to original name
    os.remove(fname)
    os.rename('temp_file.tsv',fname)

def analyze_input_files(name_file,title_file,known_for_file):
    """ Create properly formatted name and known_for files ready to import to database.
        Because of errors in imgb Database function also need to check if all tconst mentioned
        in "actor known for movies" list really exists."""

    tconst_set = set()

    remove_first_line(title_file)
    title_in = codecs.open(title_file,'r','utf-8')
    title_table = title_in.read().splitlines(True)
    title_in.close()

    #Prepare set of tconst values from title table
    for t in title_table:
        r = t.rstrip().split("\t")
        tconst_set.add(r[0])

    remove_first_line(name_file)
    f_in = codecs.open(name_file, 'r','utf-8')
    f_out_name = codecs.open('name_temp.tsv', 'w','utf-8')
    f_out_relation = codecs.open(known_for_file, 'w','utf-8')
    table = f_in.read().splitlines(True)

    for i in table:
        k = i.rstrip().split("\t")
        line_for_name = "\t".join(k[:-1]) + "\n"
        f_out_name.write(line_for_name)

        actor_relations = k[-1].split(",")
        for relation in actor_relations:
            if relation in tconst_set:
                line_for_relation = k[0] + "\t" + relation + "\n"
                f_out_relation.write(line_for_relation)

    f_in.close()
    f_out_name.close()
    f_out_relation.close()

    # Delete original file and rename temp file to original name
    os.remove(name_file)
    os.rename('name_temp.tsv',name_file)
