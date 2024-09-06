from torchtext.datasets import Multi30k
train, val, test = Multi30k(root='.data',language_pair=("de", "en"))

# for de, en in train:
#     print(de)
#     print(en)
#     break

# for de, en in val:
#     print(de)
#     print(en)
#     break

for de, en in test:
    print(de)
    print(en)
    break