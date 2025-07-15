import subprocess
import os
from collections import defaultdict


def get_git_contributions(repo_path, author_name):
    """Получает статистику по коммитам указанного автора"""
    os.chdir(repo_path)

    # Получаем все коммиты автора
    commits = subprocess.check_output(
        ['git', 'log', '--author=' + author_name, '--pretty=%H'],
        text=True
    ).splitlines()

    # Собираем статистику по файлам
    file_stats = defaultdict(lambda: {'added': 0, 'removed': 0})
    total_added = 0
    total_removed = 0

    for commit in commits:
        # Получаем изменения для каждого коммита
        diff = subprocess.check_output(
            ['git', 'show', '--numstat', '--pretty=', commit],
            text=True
        )

        # Обрабатываем изменения
        for line in diff.split('\n'):
            if not line or '\t' not in line:
                continue

            added, removed, filename = line.split('\t', 2)

            # Пропускаем переименования
            if added == '-' and removed == '-':
                continue

            try:
                added = int(added) if added.isdigit() else 0
                removed = int(removed) if removed.isdigit() else 0

                file_stats[filename]['added'] += added
                file_stats[filename]['removed'] += removed
                total_added += added
                total_removed += removed
            except ValueError:
                continue

    return {
        'file_stats': dict(file_stats),
        'total_added': total_added,
        'total_removed': total_removed,
        'net_lines': total_added - total_removed,
        'commit_count': len(commits)
    }


if __name__ == "__main__":
    # Укажите путь к репозиторию
    repo_path = r"C:\Users\Home\Desktop\franchisor_vending_machines"

    # Укажите ваше имя/email в Git
    # (то, что используется в коммитах)
    your_git_author = "kontaurova0306@gmail.com"  # Замените на ваше имя

    if not os.path.exists(repo_path):
        print(f"❌ Репозиторий '{repo_path}' не найден!")
        exit(1)

    print("\n" + "="*50)
    print(f"🔄 Анализ коммитов автора '{your_git_author}'...")
    print("="*50 + "\n")

    stats = get_git_contributions(repo_path, your_git_author)

    print("Общая статистика")
    print(f"• Всего коммитов: {stats['commit_count']}")
    print(f"• Добавлено строк: {stats['total_added']}")
    print(f"• Удалено строк: {stats['total_removed']}")
    print(f"• Результат (добавлено минус удалено): {stats['net_lines']}")

    print("\n🔍 Статистика по файлам:")
    for filename, changes in stats['file_stats'].items():
        print(f"▸ {filename}: +{changes['added']}/-{changes['removed']} \
              (итого: {changes['added'] - changes['removed']})")

    print("\n" + "="*50)
