"""

    Project-wide constants, directories, and file paths, file path patterns.

    """

from pathlib import Path

PROJ_DATA = Path(
    '/var/genetics/ws/mahdimir/projects_data/24Q3/13A240904_WGS_basic_data_checks')

class Directory :
    p = PROJ_DATA

    inp = p / 'inp'
    med = p / 'med'
    # out = p / 'out'

    # one individual data
    iid_2723845 = med / 'iid_2723845'

    # imputed hard call data, from 2A240317_UKB_imputed_gt_corr/med/hc_dta
    hc_dta = inp / 'hc_dta'


DIR = Directory()
D = DIR

class FilePath :
    d = Directory()

    chr_pos_rsid_map = d.inp / 'chr_pos_rsid_map.parquet'  # src: '/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair/inp/chr_pos_rsid_map.p'



FILE_PATH = FilePath()
FP = FILE_PATH

class FilePathPattern :
    d = Directory()

    # one idividual data, bed, bim, fam prefix
    iid_2723845 = d.iid_2723845 / '2723845'

    # imputed hard call data
    hc_dta = (d.hc_dta / 'chr{}.prq').as_posix()



FILE_PATH_PAT = FilePathPattern()
FPT = FILE_PATH_PAT

class Var :
    rsid = 'rsid'
    iid = 'IID'
    wgs_gt = 'wgs_gt'
    imp_gt = 'imp_gt'

VAR = Var()
V = VAR
