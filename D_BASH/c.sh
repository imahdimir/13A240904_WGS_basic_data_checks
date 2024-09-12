pyenv activate dx
dx login


dx run --instance-type mem1_ssd1_v2_x2 app-cloud_workstation

dx ssh job-GqJ3fP8JzVpg26jX3f919Qg9


dx select --level VIEW

unset DX_WORKSPACE_ID
dx cd $DX_PROJECT_CONTEXT_ID:

# download filtered.tar.gz # filtered is out put of tabix, filtering so many individuals
dx download file-Gp9f0x8JzVpx4xKyQ446qFgB
mkdir wgs_VCFs
tar -xzvf filtered.tar.gz -C ./wgs_VCFs/



vcf_data = allel.read_vcf('1600005_24053_0_0.dragen.hard-filtered.vcf.gz', fields=['variants/ID', 'calldata/GT'])


from cyvcf2 import VCF

vcf_reader = VCF('1600005_24053_0_0.dragen.hard-filtered.vcf.gz')


# Extract SNP IDs from the VCF file
snp_ids = [variant.ID for variant in vcf_reader if variant.ID is not None]

# Print the SNP IDs
print(snp_ids)

