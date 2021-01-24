spm_train \
    --input=./pre_train_data_128/txt/EP_pre_train_data_128_1kmer.txt \
    --model_prefix=./xlnet_EPI_cased_L-12_H-768_A-12/spm.cased.EPI \
    --shuffle_input_sentence \
    --character_coverage=1 \
    --control_symbols=\<cls\>,\<sep\>,\<pad\>,\<mask\>,\<eod\> \
    --user_defined_symbols=\<eop\> \
    --vocab_size=15