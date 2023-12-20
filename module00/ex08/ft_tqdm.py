import os

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    progress_width = (int(os.get_terminal_size().columns)) // 3
    def print_progress(iteration):
        percentage = int(iteration / total * 100)
        filled_length = int(progress_width * iteration // total)
        time_estimate = round((iteration / total) * 2)
        speed = iteration / 2 - 4.5
        bar = f"{int(percentage)}%|{'=' * filled_length}{'-' * (progress_width - filled_length)}>| {iteration}/{total} [00:0{time_estimate}<00:00, {speed:.1f}it/s]"
        print(f"\r{bar}", end='' ,flush=True)
    for i, item in enumerate(lst, 1):
        yield item
        print_progress(i)
