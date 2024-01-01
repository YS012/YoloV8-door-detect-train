import os


def process_txt_file(file_path, w, h):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        values = list(map(float, line.split()))

        # 第一个数和5个之后每三个数中的最后一个数转换为整数
        values[0] = int(values[0])
        for i in range(5, len(values), 3):
            values[i + 2] = int(values[i + 2])

        # 第2、4个数除以w、h并保留6位小数，其他数保持不变
        values[1] = round(values[1] / w, 6)
        values[3] = round(values[3] / w, 6)
        values[2] = round(values[2] / h, 6)
        values[4] = round(values[4] / h, 6)

        for i in range(5, len(values), 3):
            values[i] = round(values[i] / w, 6)
            values[i + 1] = round(values[i + 1] / h, 6)

        # 将处理后的行添加到列表中
        processed_lines.append(values)

    # 将处理后的结果写回文件
    with open(file_path, 'w') as file:
        for line in processed_lines:
            file.write(' '.join(map(str, line)) + '\n')


# 假设w和h为图片的宽度和高度
image_width = 1920
image_height = 1080

# 更改为您的文件夹路径
folder_path = 'D:\\Python\\yolov8_demo\\datasets\\my_pos\\labels\\train'

# 获取文件夹中的所有 TXT 文件
txt_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

for file_path in txt_files:
    process_txt_file(file_path, image_width, image_height)
