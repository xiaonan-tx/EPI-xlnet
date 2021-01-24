with open("./fine_tuning_data/asTSV/1kmer_tsv_data/GM12878/GM12878_enhancer_te.tsv", "r") as f:
    en_samples = f.readlines()
f.close()

with open("./fine_tuning_data/asTSV/1kmer_tsv_data/GM12878/GM12878_promoter_te.tsv", "r") as f:
    pr_samples = f.readlines()
f.close()

with open("./fine_tuning_data/asTSV/1kmer_tsv_data/GM12878/dev.tsv", "w") as f:
    for (en_line, pro_line) in zip(en_samples,pr_samples):
        label = en_line.split('\t')[1]
        enhancer = en_line.split('\t')[3].replace('\n', '')
        promoter = pro_line.split("\t")[3]
        merged_en_pr_line = "train\t" + label + '\t' + enhancer + '\t' + promoter
        # print(merged_en_pr_line.split("\t"))
        f.write(merged_en_pr_line)
        # break
f.close()
