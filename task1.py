import os
import shutil
import sys
import argparse


def copy_files(src, dest):
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isdir(item_path):
            # Рекурсивний виклик для піддиректорій
            copy_files(item_path, dest)
        else:
            # Визначаємо розширення файла та створюємо відповідну піддиректорію
            extension = os.path.splitext(item)[1][1:]
            if extension:
                dest_dir = os.path.join(dest, extension)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.copy(item_path, dest_dir)


def main():
    parser = argparse.ArgumentParser(description='Копіює файли у нову директорію, сортуючи їх за розширенням.')
    parser.add_argument('source_directory', help='Шлях до вихідної директорії')
    parser.add_argument('destination_directory', nargs='?', default='dist',
                        help='Шлях до директорії призначення (за замовчуванням "dist")')

    args = parser.parse_args()

    src_dir = args.source_directory
    dest_dir = args.destination_directory

    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує.")
        sys.exit(1)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    try:
        copy_files(src_dir, dest_dir)
    except Exception as e:
        print(f"Помилка: {e}")
        sys.exit(1)

    print(f"Файли були успішно скопійовані з {src_dir} в {dest_dir}")


if __name__ == "__main__":
    main()
