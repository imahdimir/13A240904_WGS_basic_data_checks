"""


    """

import pandas as pd
from pandas_plink import read_plink

##

from A_PROJ.proj import DIR as D
from A_PROJ.proj import FILE_PATH as FP
from A_PROJ.proj import FILE_PATH_PAT as FPT
from A_PROJ.proj import VAR as V

##
def read_df_lift() :
    df = pd.read_parquet(FP.chr_pos_rsid_map)
    df = df.drop_duplicates(subset = ['chr' , 'pos'], keep = False)
    df = df.rename(columns = {'chr' : 'chrom'})
    return df

def read_hc_data_keep_one_individual(df_all, fp, iid) :
    df = pd.read_parquet(fp)

    msk = df[V.iid] == iid
    df = df[msk]
    assert df.shape[0] == 1

    df = df.iloc[:, 1:]

    df = df.T

    df = df.reset_index()

    df.columns = [V.rsid , V.imp_gt]

    df_all = pd.concat([df_all , df] , axis = 0)

    return df_all



##
def main():
    pass

    ##
    import pandas as pd
    from pandas_plink import read_plink

    # Load PLINK files
    (bim, fam, bed) = read_plink(FPT.iid_2723845.as_posix())

    # Extract SNP names and positions
    snps = bim[['snp', 'chrom', 'pos']]  # SNP name, chromosome, and position
    print(snps.head())

    ##
    # Extract sample IDs
    samples = fam[['iid']]  # Sample ID
    print(samples.head())

    ##
    # Extract genotype data
    genotypes = bed.compute() # Transpose to match SNPs as columns

    ##
    lift = read_df_lift()

    ##
    snps = snps.astype('string')

    snps = snps.merge(lift , on = ['chrom' , 'pos'] , how = 'left')
    print(snps.head())

    # there are some nan values in rsid column
    snps[V.rsid].isna().sum()

    ##
    snps[V.wgs_gt] = genotypes

    # now genotypes from WGS data for one individual is ready now I need to
    # find the genotype for the same individual from the imputed data

    ##

    # loop thorogh all the chromosomes and find the genotype for the individual
    # from the imputed data


    ##
    fp1 = FPT.hc_dta.format(1)
    print(fp1)

    df0 = pd.DataFrame()
    df1= read_hc_data_keep_one_individual(df0 , fp1)

    ##
    df_all = pd.DataFrame()
    for i in range(1 , 23) :
        print(i)
        fp = FPT.hc_dta.format(i)
        print(fp)
        df_all = read_hc_data_keep_one_individual(df_all , fp)

    ##
    snps = pd.merge(snps , df_all , on = V.rsid , how = 'left')

    ##
    snps1 = snps.dropna(subset = [V.rsid, V.wgs_gt, V.imp_gt])

    ##
    snps1[V.wgs_gt].corr(snps1[V.imp_gt])

    ##

    # another individual using the id inside the vcf file

    # 2443654

    ##
    snps[V.wgs_gt] = genotypes

    ##
    iid = '2443654'

    df_all = pd.DataFrame()
    for i in range(1 , 23) :
        print(i)
        fp = FPT.hc_dta.format(i)
        print(fp)
        df_all = read_hc_data_keep_one_individual(df_all , fp , iid)

    ##
    fp = '/disk/genetics2/ukb/orig/UKBv3/sample/ukb11425_imp_chr1_22_v3_s487395.sample'

    df = pd.read_csv(fp, sep = ' ', header = 0, low_memory = False)

    ##
    iid = '2443654'

    df['ID_1'].eq(iid).sum()

    ##
    df['ID_2'].eq(iid).sum()

    ##



    ##






    ##






    ##




    ##


    ##




    ##



    ##


    ##


    ##


    ##

##

def read_bim_merge_with_lift(bim_fn , df_lift) :
    df = pd.read_csv(bim_fn , sep = '\t' , header = None)

    df = df[[0 , 3]]

    df.columns = ['chr' , 'pos']

    df = df.astype('string')

    df_cols = pd.merge(df , df_lift , on = ['chr' , 'pos'] , how = 'left')

    return df_cols

def save_gt(bim_fn , df_cols) :
    bed_fn = '/homes/nber/mahdimir/bed_files_converted_2_csv/' + Path(bim_fn).with_suffix(
            '.csv').name

    df_gt = pd.read_csv(bed_fn)

    df_gt.columns = df_cols['rsid']

    df_gt = df_gt.loc[: , df_gt.columns.notna()]

    df_gt = df_gt.loc[: , ~ df_gt.columns.duplicated()]

    od = '/var/genetics/ws/mahdimir/local/prj_data/1174_verify_all_individual_IDs_are_available/med/gt_by_individual/'

    fo = od + Path(bim_fn).with_suffix('.p').name
    print(fo)

    df_gt.to_parquet(fo , index = False)

    return df_gt

def job(bim_fn) :
    df_cols = read_bim_merge_with_lift(bim_fn , LIFT)
    df_gt = save_gt(bim_fn , df_cols)

def main() :
    # get_all_bim_files in the folder
    bims = Path('/homes/nber/mahdimir/plink_out/').rglob('*.bim')

    b = list(bims)

    print(len(b))

    with Pool(20) as p :
        print(20)
        p.map(job , b)

if __name__ == '__main__' :
    main()

##
