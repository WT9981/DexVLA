import subprocess

# requirements.txt 路径
requirements_file = "D:\\FutureSpace\\Project\\DexVLA\\requirements.txt"

with open(requirements_file, "r", encoding="utf-8") as f:
    for line in f:
        package = line.strip()
        if not package or package.startswith("#"):
            continue  # 跳过空行和注释

        print(f"\n📦 正在安装: {package}")
        try:
            subprocess.check_call(["pip", "install", package, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
            print(f"✅ 成功安装: {package}")
        except subprocess.CalledProcessError:
            print(f"❌ 安装失败，跳过: {package}")
