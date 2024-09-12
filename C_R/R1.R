list.of.packages <- c("data.table", "dplyr", "magrittr", "tidyverse", "plinkFile", "genio", "arrow")
lapply(list.of.packages, library, character.only = TRUE)


fp1 <- "/Users/mmir/Downloads/temp/sibs_model_data.parquet" # src: genetics:/09A240711_verify_all_individual_IDs_are_available/med

df <- read_parquet(fp1)


# Calculate column-wise averages
averages <- colMeans(df[, c("g1", "g2", "g1_hat", "g2_hat")])

# Convert the averages to a data frame with a single row
average_df <- as.data.frame(t(averages))

# Print the result in a nice wide format
print(average_df, row.names = FALSE)


