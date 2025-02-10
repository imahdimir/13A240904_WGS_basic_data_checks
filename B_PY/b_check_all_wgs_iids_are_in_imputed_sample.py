"""

    """


import pandas as pd

import sys
from pathlib import Path

from pandas.io.sas.sas_constants import column_type_offset


##
sys.path.append(Path.cwd().as_posix())

from a_proj.proj import VAR as V

##
def check_all_wgs_iids_are_in_imputed_data_iids():
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

    ##
    fn = '/Users/mmir/Downloads/temp_4_sftp_2_server/1.txt'
    df_imp = pd.read_csv(fn, sep = '\s')
    df_imp = df_imp.iloc[1:]

    ##
    df_imp = df_imp[[V.id_1, V.id_2]]

    ##
    df_imp = df_imp.astype('string')

    ##
    assert df_imp[V.id_1].eq(df_imp[V.id_2]).all()

    ##
    df_imp = df_imp.rename(columns = {V.id_1 : V.iid})
    df_imp = df_imp.drop(columns = V.id_2)

    ##
    df_merge = pd.merge(df_wgs, df_imp, how='outer', indicator = True)

    ##
    df_not_both = df_merge[df_merge['_merge'].ne('both')]

    ##
    df_merge1 = pd.merge(df_wgs, df_imp, how='left', indicator = True)

    ##
    df_not_both_1 = df_merge1[df_merge1['_merge'].ne('both')]

    ##





    ##








    ##


    ##






##
