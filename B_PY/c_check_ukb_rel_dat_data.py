"""

    """


import pandas as pd

import sys
from pathlib import Path


sys.path.append(Path.cwd().as_posix())

from a_proj.proj import VAR as V



def check_whether_iids_of_wgs_are_present_in_rel_file():
    pass

    ##
    fn = '/Users/mmir/Downloads/temp_4_sftp_2_server/all_WGS_filenames.txt'

    df_wgs = pd.read_csv(fn, header = None)

    ##
    df_wgs[V.iid] = df_wgs[0].str.split('_')
    df_wgs[V.iid] = df_wgs[V.iid].apply(lambda x: x[0])

    ##
    df_wgs = df_wgs[[V.iid]]

    ##
    df_wgs = df_wgs.drop_duplicates()

    ##
    df_wgs = df_wgs.astype('string')

    ##

    ##
    fn = '/Users/mmir/Downloads/temp_4_sftp_2_server/1.dat'
    df_rel = pd.read_csv(fn, sep = '\s')

    ##
    df_rel = df_rel[[V.id1, V.id2]]

    ##
    df_rel = df_rel.astype('string')

    ##
    df_rel = df_rel.rename(columns = {V.id1 : V.iid})

    ##
    df_rel_2 = df_rel[[V.id2]]
    df_rel_2 = df_rel_2.rename(columns = {V.id2 : V.iid})

    ##
    df_rel = df_rel.drop(columns = V.id2)

    ##
    df_rel_all = pd.concat([df_rel, df_rel_2])

    ##


    ##
    df_merge = pd.merge(df_wgs , df_rel , how= 'outer' , indicator = True)

    ##
    df_not_both = df_merge[df_merge['_merge'].ne('both')]

    ##
    assert df_not_both.empty


##
