document.addEventListener('DOMContentLoaded', function() {
    // Оригинальный код для подменю
    const submenuItems = document.querySelectorAll('.has-submenu');
    submenuItems.forEach(item => {
        const trigger = item.querySelector('a:first-child');
        const submenu = item.querySelector('.submenu');
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            submenuItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.submenu').classList.remove('active');
                }
            });
            item.classList.toggle('active');
            submenu.classList.toggle('active');
        });
    });
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.has-submenu')) {
            submenuItems.forEach(item => {
                item.classList.remove('active');
                item.querySelector('.submenu').classList.remove('active');
            });
        }
    });
    document.querySelectorAll('.submenu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const submenu = e.target.closest('.submenu');
            if (!submenu || !submenu.classList.contains('active')) {
                e.preventDefault();
            }
        });
    });

    // Новый код для фильтрации и сортировки
    const applyBtn = document.getElementById('apply-filters');
    const clearBtn = document.getElementById('clear-filters');
    const cards = document.querySelectorAll('.card');
    const totalInfo = document.querySelector('.total-info');
    
    // Применение фильтров
    applyBtn.addEventListener('click', function() {
        const statusFilter = document.getElementById('status-filter').value;
        const connectionFilter = document.getElementById('connection-filter').value;
        const cityFilter = document.getElementById('city-filter').value.toLowerCase();
        const sortBy = document.getElementById('sort-by').value;
        
        let visibleCards = [];
        
        cards.forEach(card => {
            const status = card.getAttribute('data-status');
            const connection = card.getAttribute('data-connection');
            const city = card.querySelector('.city').textContent.toLowerCase();
            const lastConnection = parseInt(card.querySelector('.last-connection').textContent);
            
            // Проверка фильтров
            const statusMatch = statusFilter === 'all' || status === statusFilter;
            const connectionMatch = connectionFilter === 'all' || connection === connectionFilter;
            const cityMatch = cityFilter === '' || city.includes(cityFilter);
            
            if (statusMatch && connectionMatch && cityMatch) {
                card.style.display = 'block';
                visibleCards.push(card);
            } else {
                card.style.display = 'none';
            }
        });
        
        // Сортировка
        visibleCards.sort((a, b) => {
            if (sortBy === 'name') {
                return a.querySelector('.card-title').textContent.localeCompare(
                    b.querySelector('.card-title').textContent
                );
            } else if (sortBy === 'status') {
                return a.getAttribute('data-status').localeCompare(b.getAttribute('data-status'));
            } else if (sortBy === 'connection') {
                const aTime = parseInt(a.querySelector('.last-connection').textContent);
                const bTime = parseInt(b.querySelector('.last-connection').textContent);
                return aTime - bTime;
            } else if (sortBy === 'city') {
                return a.querySelector('.city').textContent.localeCompare(
                    b.querySelector('.city').textContent
                );
            }
            return 0;
        });
        
        // Перестановка карточек
        const container = document.querySelector('.cards-container');
        visibleCards.forEach(card => {
            container.appendChild(card);
        });
        
        // Обновление итоговой информации
        const totalMoney = Array.from(visibleCards).reduce((sum, card) => {
            return sum + parseInt(card.querySelector('.money-value').textContent.replace(/\s/g, ''));
        }, 0);
        
        totalInfo.textContent = `Итого автоматов: ${visibleCards.length}. Денег в автоматах: ${totalMoney.toLocaleString('ru-RU')} р.`;
    });
    
    // Сброс фильтров
    clearBtn.addEventListener('click', function() {
        document.getElementById('status-filter').value = 'all';
        document.getElementById('connection-filter').value = 'all';
        document.getElementById('city-filter').value = '';
        document.getElementById('sort-by').value = 'name';
        
        cards.forEach(card => {
            card.style.display = 'block';
        });
        
        // Возврат к исходной сортировке
        const container = document.querySelector('.cards-container');
        const sortedCards = Array.from(cards).sort((a, b) => {
            return parseInt(a.getAttribute('data-id')) - parseInt(b.getAttribute('data-id'));
        });
        
        sortedCards.forEach(card => {
            container.appendChild(card);
        });
        
        // Обновление итоговой информации
        const totalMoney = Array.from(cards).reduce((sum, card) => {
            return sum + parseInt(card.querySelector('.money-value').textContent.replace(/\s/g, ''));
        }, 0);
        
        totalInfo.textContent = `Итого автоматов: ${cards.length}. Денег в автоматах: ${totalMoney.toLocaleString('ru-RU')} р.`;
    });
    
    // Инициализация при загрузке
    applyBtn.click();
});