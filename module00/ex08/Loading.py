from time import sleep
from tqdm import tqdm
from ft_tqdm import ft_tqdm

for elem in ft_tqdm(range(0,666,1)):
    sleep(0.005)
print()
for elem in tqdm(range(0,666,1)):
    sleep(0.005)
print()
