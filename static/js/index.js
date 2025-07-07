document.addEventListener('DOMContentLoaded', function() {
    // График эффективности сети (уменьшенный)
    const efficiencyCtx = document.getElementById('efficiencyChart');
    
    try {
        // Данные для эффективности сети
        const efficiencyData = {
            labels: ['Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль'],
            values: [75, 82, 68, 90, 85, 92]
        };

        new Chart(efficiencyCtx, {
            type: 'line',
            data: {
                labels: efficiencyData.labels,
                datasets: [{
                    label: 'Эффективность, %',
                    data: efficiencyData.values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 3,
                    pointBackgroundColor: '#fff',
                    pointBorderWidth: 2,
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        padding: 12,
                        callbacks: {
                            label: function(context) {
                                return ` ${context.parsed.y}%`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        min: 50,
                        max: 100,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        },
                        ticks: {
                            callback: function(value) {
                                return value + '%';
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });

    } catch (error) {
        console.error('Ошибка загрузки данных эффективности:', error);
        efficiencyCtx.closest('.chart-container').innerHTML = `
            <div class="error-message">
                Ошибка: ${error.message || 'Неизвестная ошибка'}
            </div>
        `;
    }

    // График состояния сети (увеличенный, без подписей)
    const statusCtx = document.getElementById('networkStatusChart');
    const statusContainer = statusCtx.closest('.chart-container');
    
    // Создаем элемент для всплывающей подсказки
    const tooltip = document.createElement('div');
    tooltip.className = 'status-tooltip';
    statusContainer.appendChild(tooltip);
    
    // Статусы для подсказок
    const statusInfo = {
        working: {
            name: 'Работает',
            description: 'Автоматы в нормальном режиме'
        },
        warning: {
            name: 'Предупреждение',
            description: 'Требуется внимание'
        },
        critical: {
            name: 'Критично',
            description: 'Требуется срочное вмешательство'
        }
    };
    
    // Данные для состояния сети
    const statusData = {
        working: 85,
        warning: 10,
        critical: 5
    };

    try {
        // Обновляем центральный текст
        document.getElementById('statusCenterText').innerHTML = `
            <div class="total-percent">${statusData.working}%</div>
        `;

        const statusChart = new Chart(statusCtx, {
            type: 'doughnut',
            data: {
                labels: [],
                datasets: [{
                    data: [
                        statusData.working, 
                        statusData.warning, 
                        statusData.critical
                    ],
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(255, 99, 132, 0.8)'
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(255, 99, 132, 1)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: false
                    }
                },
                onHover: (event, chartElements) => {
                    // При наведении на сегмент
                    if (chartElements.length > 0) {
                        const index = chartElements[0].index;
                        let status, value, name;
                        
                        switch(index) {
                            case 0:
                                status = 'working';
                                value = statusData.working;
                                name = statusInfo.working.name;
                                break;
                            case 1:
                                status = 'warning';
                                value = statusData.warning;
                                name = statusInfo.warning.name;
                                break;
                            case 2:
                                status = 'critical';
                                value = statusData.critical;
                                name = statusInfo.critical.name;
                                break;
                        }
                        
                        // Показываем подсказку
                        tooltip.innerHTML = `
                            <div><strong>${name}: ${value}%</strong></div>
                            <div>${statusInfo[status].description}</div>
                        `;
                        tooltip.classList.add('show');
                        
                        // Позиционируем подсказку
                        const rect = statusCtx.getBoundingClientRect();
                        const x = event.clientX - rect.left;
                        const y = event.clientY - rect.top;
                        
                        tooltip.style.left = x + 'px';
                        tooltip.style.top = y + 'px';
                        
                        // Увеличиваем процент в центре
                        const percentElement = document.querySelector('.total-percent');
                        percentElement.textContent = value + '%';
                        percentElement.style.color = index === 0 ? 
                            'rgba(75, 192, 192, 1)' : 
                            index === 1 ? 
                            'rgba(255, 206, 86, 1)' : 
                            'rgba(255, 99, 132, 1)';
                    } else {
                        // Когда курсор убран
                        tooltip.classList.remove('show');
                        
                        // Восстанавливаем исходный процент
                        const percentElement = document.querySelector('.total-percent');
                        percentElement.textContent = statusData.working + '%';
                        percentElement.style.color = 'rgba(75, 192, 192, 1)';
                    }
                }
            }
        });

        // Обработчик движения мыши
        statusCtx.addEventListener('mousemove', (e) => {
            if (!tooltip.classList.contains('show')) return;
            
            const rect = statusCtx.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            tooltip.style.left = x + 'px';
            tooltip.style.top = y + 'px';
        });
        
        // Скрываем подсказку при уходе с графика
        statusContainer.addEventListener('mouseleave', () => {
            tooltip.classList.remove('show');
            
            // Восстанавливаем исходный процент
            const percentElement = document.querySelector('.total-percent');
            percentElement.textContent = statusData.working + '%';
            percentElement.style.color = 'rgba(75, 192, 192, 1)';
        });

    } catch (error) {
        console.error('Ошибка загрузки данных состояния:', error);
        statusCtx.closest('.chart-container').innerHTML = `
            <div class="error-message">
                Ошибка: ${error.message || 'Неизвестная ошибка'}
            </div>
        `;
    }
});