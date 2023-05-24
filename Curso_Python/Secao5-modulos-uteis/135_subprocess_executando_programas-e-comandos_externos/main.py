import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

saida = proc.stdout
saida = saida.replace('icmp_seq', 'Pedro')
print(saida)
