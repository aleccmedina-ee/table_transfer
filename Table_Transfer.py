from pycomm3 import LogixDriver

source_plc = input("Enter the IP to the PLC you wish to copy from: ")
source_plc = LogixDriver(source_plc)
source_plc.open()

source_tag = input("Enter the tag name you wish to copy: ")

source_tag=source_plc.read(source_tag)

destination_plc = input("Enter the IP to the PLC you wish to copy to: ")
destination_plc = LogixDriver(destination_plc)
destination_plc.open()

print(destination_plc.write(source_tag.tag, source_tag.value))