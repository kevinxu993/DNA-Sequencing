import a1

# just example genes and masks to test that the functions
# are returning the correct type
GENE1 = "A"
GENE2 = "A"
LIST1 = ["A"]
LIST2 = ["A"]
ANCHOR1 = "A"
ANCHOR2 = "A"
MASK1 = "A"

FILE_NAME = "a1_typechecker_file.txt"

# test that pair_genes returns a boolean
pair_genes_result = a1.pair_genes(GENE1, GENE2)
assert isinstance(pair_genes_result, bool), "pair_genes doesn't return a boolean"

# test that zip_length returns an int
zip_length_result = a1.zip_length(GENE1)
assert isinstance(zip_length_result, int), "zip_length doesn't return an int"

# test that splice_gene doesn't return anything
splice_gene_result = a1.splice_gene(LIST1, LIST2, ANCHOR1, ANCHOR2)
assert isinstance(splice_gene_result, type(None)), "splice_gene doesn't return a NoneType"

# check that match_mask returns an integer
match_mask_result = a1.match_mask(GENE1, MASK1)
assert isinstance(match_mask_result, int), "match_mask doesn't return an int"

# check that process_gene_file returns a tuple of ints
file_handle = open(FILE_NAME, 'r')
process_gene_file_result = a1.process_gene_file(file_handle, GENE1, MASK1)
file_handle.close()
result_tuple = isinstance(process_gene_file_result, tuple)
result_p = isinstance(process_gene_file_result[0], int)
result_m = isinstance(process_gene_file_result[1], int)
result_z = isinstance(process_gene_file_result[2], int)
result_types = result_tuple and result_p and result_m and result_z
assert result_types, "process_gene_file doesn't reutrn a tuple of ints"



print("Congratulations. If you are seeing this message (and no other errors)")
print("then you have correctly named functions which (at least in some instances)")
print("return the correct types.")
