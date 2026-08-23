import os
import cv2
import easyocr

# ========== 全局路径配置==========
# CCPD原始数据集路径
data_dir = r"C:\Users\23924\Desktop\Experiment\CCPD2020"
# 预处理后图片输出路径
output_dir = r"C:\Users\23924\PycharmProjects\pythonProject\Experience\Experience2\data\processed"
# 结果日志保存路径
result_dir = r"C:\Users\23924\PycharmProjects\pythonProject\Experience\Experience2\results"

os.makedirs(output_dir, exist_ok=True)
os.makedirs(result_dir, exist_ok=True)

# 全局初始化OCR模型（只加载一次，大幅提升批量处理速度）
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)


# ========== 1：批量图片预处理 ==========
def batch_preprocess(img_count=1000):

    img_list = [f for f in os.listdir(data_dir) if f.endswith(".jpg")]
    print(f"找到原始图片总数: {len(img_list)}，本次处理前 {img_count} 张")

    for idx, img_name in enumerate(img_list[:img_count]):
        img_path = os.path.join(data_dir, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        # 预处理流水线：统一尺寸 → 可按需加灰度、去噪、超分辨率
        img_resized = cv2.resize(img, (640, 320))  # 统一尺寸
        # img_denoise = cv2.fastNlMeansDenoisingColored(img_resized)  # 去噪（可选，会变慢）

        # 保存预处理结果
        cv2.imwrite(os.path.join(output_dir, img_name), img_resized)

        if (idx + 1) % 100 == 0:
            print(f"已处理 {idx + 1} 张")

    print(f"批量预处理完成，结果已保存至: {output_dir}")


# ========== 2：车牌识别核心 ==========
def recognize_plate(img):
    """单张图片车牌识别"""
    result = reader.readtext(img, detail=0)
    return result[0] if result else ""


def multi_frame_vote(frame_list):
    """
    多帧投票纠错机制
    """
    votes = {}
    for frame in frame_list:
        text = recognize_plate(frame)
        if not text:
            continue
        votes[text] = votes.get(text, 0) + 1
    if not votes:
        return ""
    return max(votes.items(), key=lambda x: x[1])[0]


# ========== 主流程：预处理 → 识别测试 ==========
if __name__ == "__main__":
    # 第一步：执行批量预处理
    batch_preprocess(img_count=100)  # 先测试100张，没问题再改大

    # 第二步：单张图片识别测试
    processed_imgs = [f for f in os.listdir(output_dir) if f.endswith(".jpg")]
    if processed_imgs:
        test_img_path = os.path.join(output_dir, processed_imgs[0])
        test_img = cv2.imread(test_img_path)
        result = recognize_plate(test_img)
        print(f"\n 单张测试识别结果: {result}")
        print(f"测试图片文件名: {processed_imgs[0]}")
