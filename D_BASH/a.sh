pyenv activate dx
dx login


dx run --instance-type mem1_ssd1_v2_x2 app-cloud_workstation

dx ssh job-GqJ3fP8JzVpg26jX3f919Qg9


dx select --level VIEW

unset DX_WORKSPACE_ID
dx cd $DX_PROJECT_CONTEXT_ID:

# download sorted_vcfs.tar.gz
dx download file-GqFkpy8JzVpb8qQJp1KJ9Jvy
tar -xzvf sorted_vcfs.tar.gz

