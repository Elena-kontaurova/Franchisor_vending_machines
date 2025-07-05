document.addEventListener('DOMContentLoaded', function() {
    const submenuItems = document.querySelectorAll('.has-submenu');

    submenuItems.forEach(item => {
        const trigger = item.querySelector('a:first-child');
        const submenu = item.querySelector('.submenu');

        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            // Закрываем все другие подменю
            submenuItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.submenu').classList.remove('active');
                }
            });

            // Переключаем текущее подменю
            item.classList.toggle('active');
            submenu.classList.toggle('active');
        });
    });

    // Закрытие подменю при клике вне его области
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.has-submenu')) {
            submenuItems.forEach(item => {
                item.classList.remove('active');
                item.querySelector('.submenu').classList.remove('active');
            });
        }
    });

    // Отключение кликов на ссылках в скрытом подменю
    document.querySelectorAll('.submenu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const submenu = e.target.closest('.submenu');
            if (!submenu || !submenu.classList.contains('active')) {
                e.preventDefault(); // Запрещаем переход, если подменю скрыто
            }
        });
    });
});