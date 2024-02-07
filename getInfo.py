import GPUtil
import psutil

import cpuinfo


def get_system_and_gpu_info():
    # 获取CPU型号
    cpu_model = cpuinfo.get_cpu_info()['brand_raw']
    # 获取CPU核心数
    cpu_cores = psutil.cpu_count(logical=False)
    # 获取系统内存总量，单位为字节
    total_memory = psutil.virtual_memory().total / (1024 ** 3)

    # 使用GPUtil获取GPU信息
    gpu_info = []
    try:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_details = {
                "name": gpu.name,
                "memory_total": gpu.memoryTotal
            }
            gpu_info.append(gpu_details)
    except Exception as e:
        print(str(e))

    # 打印信息（或根据需要返回）
    # print(f"CPU Model: {cpu_model}")
    # print(f"CPU Physical Cores: {cpu_cores}")
    # print(f"Total System Memory: {total_memory} GB")
    # for index, gpu in enumerate(gpu_info, start=1):
    #     print(f"GPU {index}: Name - {gpu['name']}, Total Memory - {gpu['memory_total']} MB")

    return cpu_model, cpu_cores, total_memory, gpu_info


def get_realtime_usage_info():
    # CPU实时占用率
    cpu_usage = psutil.cpu_percent(interval=1) / 100

    # 内存占用信息
    memory_info = psutil.virtual_memory()
    used_memory = memory_info.used / (1024 ** 3)  # 转换为GB

    # GPU信息
    gpus_usage = []
    try:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_usage = {
                "name": gpu.name,
                "load": gpu.load,  # GPU占用率
                "memory_used": gpu.memoryUsed,  # 显存占用大小
                "memory_usage": gpu.memoryUsed / gpu.memoryTotal
            }
            gpus_usage.append(gpu_usage)
    except Exception as e:
        print(f"Failed to get GPU usage: {str(e)}")
        # gpus_usage.append({"error": str(e)})

    # 打印信息（或根据需要返回）
    # print(f"CPU Usage: {cpu_usage * 100}%")
    # print(f"Used Memory: {used_memory:.2f} GB")
    # for gpu_usage in gpu_usages:
    #     print(
    #         f"GPU {gpu_usage['name']}: Load: {gpu_usage['load']}, Memory Used: {gpu_usage['memory_used']} MB, "
    #         f"Memory Usage: {gpu_usage['memory_usage'] * 100:.2f}%")

    return cpu_usage, used_memory, gpus_usage


if __name__ == "__main__":
    get_system_and_gpu_info()
    get_realtime_usage_info()
