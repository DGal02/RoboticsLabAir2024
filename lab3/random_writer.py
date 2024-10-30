import click
import time
import random
from datetime import datetime


@click.command()
@click.argument('file_path', type=click.Path())
@click.argument('interval', type=float)
def write_random_number(file_path, interval):
    """Aplikacja zapisująca losową liczbę i czas do pliku co N sekund."""
    print(f"Starting to write to {file_path} every {interval} seconds.")
    while True:
        random_number = random.random()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(file_path, 'a') as f:
            f.write(f"{current_time} - {random_number}\n")
        print(f"Wrote: {current_time} - {random_number}")
        time.sleep(interval)


if __name__ == '__main__':
    write_random_number()
