# script: 301 Ops challenge class 11
# author: Paul Thomas
# date: 2-20-2023

import psutil

# Time spent by normal processes executing in user mode
user_time = psutil.cpu_times().user

# Time spent by processes executing in kernel mode
system_time = psutil.cpu_times().system

# Time when system was idle
idle_time = psutil.cpu_times().idle

# Time spent by priority processes executing in user mode
priority_user_time = psutil.cpu_times().nice

# Time spent waiting for I/O to complete.
io_wait_time = psutil.cpu_times().iowait

# Time spent for servicing hardware interrupts
hardware_interrupt_time = psutil.cpu_times().irq

# Time spent for servicing software interrupts
software_interrupt_time = psutil.cpu_times().softirq

# Time spent by other operating systems running in a virtualized environment
steal_time = psutil.cpu_times().steal

# Print the results
print("Time spent by normal processes executing in user mode: {:.2f} seconds".format(user_time))
print("Time spent by processes executing in kernel mode: {:.2f} seconds".format(system_time))
print("Time when system was idle: {:.2f} seconds".format(idle_time))
print("Time spent by priority processes executing in user mode: {:.2f} seconds".format(priority_user_time))
print("Time spent waiting for I/O to complete: {:.2f} seconds".format(io_wait_time))
print("Time spent for servicing hardware interrupts: {:.2f} seconds".format(hardware_interrupt_time))
print("Time spent for servicing software interrupts: {:.2f} seconds".format(software_interrupt_time))
print("Time spent by other operating systems running in a virtualized environment: {:.2f} seconds".format(steal_time))