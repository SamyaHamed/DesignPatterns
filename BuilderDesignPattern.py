class Computer:
    def __init__(self):
        self.cpu =None
        self.memory =None
        self.disk =None
        self.gpu = None
        self.os = None


    def __str__(self):
        return(
            f" Computer("f"CPU = {self.cpu},"f"memory = {self.memory},"
            f"disk = {self.disk},"f"os={self.os},"f"gpu={self.gpu})"
        )

class ComputerBuilder:
    def __init__ (self):
        self.computer = Computer()

    def set_cpu(self,cpu):
        self.computer.cpu = cpu
        return self

    def set_memory(self,memory):
        self.computer.memory = memory
        return self

    def set_disk(self,disk):
        self.computer.disk = disk
        return self

    def set_os(self,os):
        self.computer.os = os
        return self

    def set_gpu(self,gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


gaming_pc = (ComputerBuilder()
             .set_cpu("Intel i9")
             .set_os("linux")
             .set_memory("64")
             .set_disk("64")
             .set_gpu("RTX 4080")
             .build())

office_computer = (ComputerBuilder()
                   .set_cpu("Intel i9")
                   .set_os("windows")
                   .build())


print("gaming_computer:")
print(gaming_pc)
print("\n")
print("office_computer:")
print(office_computer)

