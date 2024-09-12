cd /var/genetics/ws/mahdimir/projects_data/24Q3/13A240904_WGS_basic_data_checks/med/plink_out_converted_2_bed_sorted_2723845_24053_0_0.dragen.hard-filtered.vcf.filtered.vcf
f1="/var/genetics/ws/mahdimir/projects_data/24Q3/13A240904_WGS_basic_data_checks/inp/sorted_2723845_24053_0_0.dragen.hard-filtered.vcf.filtered.vcf"
plink2 --max-alleles 2 --vcf $f1 --make-bed --out 2723845 --allow-extra-chr


