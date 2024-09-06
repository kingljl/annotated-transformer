import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
    return chardet.detect(rawdata)['encoding']

# 检测文件编码
file_path = 'the_annotated_transformer.py'
encoding = detect_encoding(file_path)
print(f"Detected encoding: {encoding}")