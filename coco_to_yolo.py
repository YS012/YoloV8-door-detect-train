import json

# 读取 JSON 文件
with open('person_keypoints_default.json', 'r') as json_file:
    data = json.load(json_file)

# 遍历 images
for image in data['images']:
    image_id = image['id']
    filename = image['file_name']

    # 创建每个图像对应的 TXT 文件
    with open(f'{filename[:-4]}.txt', 'w') as txt_file:
        # 查找该图像对应的所有 annotations
        annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id]

        # 遍历该图像的所有 annotations，并将信息写入 TXT 文件
        for ann in annotations:
            category_id = ann['category_id'] - 1
            bbox = ann['bbox']
            keypoints = ann['keypoints']

            # 将信息写入 TXT 文件
            txt_file.write(f"{category_id} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} {' '.join(map(str, keypoints))}\n")
