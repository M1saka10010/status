from datetime import datetime

import getInfo


class Info:
    def __init__(self):
        cpu_model, cpu_cores, total_memory, gpu_info = getInfo.get_system_and_gpu_info()
        self.cpu_model = cpu_model
        self.cpu_cores = cpu_cores
        self.total_memory = total_memory
        self.gpus_info = gpu_info
        self.cpu_usage = None
        self.used_memory = None
        self.gpus_usage = None
        self.last_update_time = None

    def get_realtime_usage_info(self):
        # 获取实时使用信息
        cpu_usage, used_memory, gpus_usage = getInfo.get_realtime_usage_info()
        self.cpu_usage = cpu_usage
        self.used_memory = used_memory
        self.gpus_usage = gpus_usage
        self.last_update_time = datetime.now()

        return self.cpu_usage, self.used_memory, self.gpus_usage

    async def get_system_status(self):
        if self.last_update_time is None or (datetime.now() - self.last_update_time).seconds > 3:
            self.get_realtime_usage_info()
        system_status = {
            'cpu_model': self.cpu_model,
            'cpu_cores': self.cpu_cores,
            'cpu_usage': self.cpu_usage,
            'total_memory': self.total_memory,
            'used_memory': self.used_memory,
            'memory_usage': self.used_memory / self.total_memory,
            'gpus_info': self.gpus_info,
            'gpus_usage': self.gpus_usage
        }

        return system_status


if __name__ == '__main__':
    info = Info()
    print(info.get_system_status())
