document.addEventListener('DOMContentLoaded', function() {
    // График эффективности сети
    const efficiencyCtx = document.getElementById('efficiencyChart');
    
    try {
        const efficiencyData = {
            labels: ['Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль'],
            values: [75, 82, 68, 90, 85, 92]
        };

        if (efficiencyCtx) {
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
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12,
                            callbacks: { label: ctx => ` ${ctx.parsed.y}%` }
                        }
                    },
                    scales: {
                        y: {
                            min: 50, max: 100,
                            grid: { color: 'rgba(0, 0, 0, 0.05)' },
                            ticks: { callback: value => value + '%' }
                        },
                        x: { grid: { display: false } }
                    }
                }
            });
        }

    } catch (error) {
        console.error('Ошибка эффективности:', error);
        const container = document.querySelector('#efficiencyChart')?.closest('.chart-container');
        if (container) container.innerHTML = `<div class="error">Ошибка: ${error.message}</div>`;
    }

    // График состояния сети
    const statusCtx = document.getElementById('networkStatusChart');
    const statusContainer = statusCtx?.closest('.chart-container');
    
    if (statusContainer) {
        const tooltip = document.createElement('div');
        tooltip.className = 'status-tooltip';
        statusContainer.appendChild(tooltip);
        
        const statusInfo = {
            working: { name: 'Работает', description: 'Автоматы в нормальном режиме' },
            warning: { name: 'Предупреждение', description: 'Требуется внимание' },
            critical: { name: 'Критично', description: 'Требуется срочное вмешательство' }
        };
        
        const statusData = { working: 85, warning: 10, critical: 5 };

        try {
            const centerText = document.getElementById('statusCenterText');
            if (centerText) {
                centerText.innerHTML = `<div class="total-percent">${statusData.working}%</div>`;
            }

            const statusChart = new Chart(statusCtx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: [statusData.working, statusData.warning, statusData.critical],
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
                    plugins: { legend: { display: false }, tooltip: { enabled: false } },
                    onHover: (event, chartElements) => {
                        if (chartElements.length > 0) {
                            const index = chartElements[0].index;
                            let status, value, name;
                            
                            switch(index) {
                                case 0: status = 'working'; value = statusData.working; name = statusInfo.working.name; break;
                                case 1: status = 'warning'; value = statusData.warning; name = statusInfo.warning.name; break;
                                case 2: status = 'critical'; value = statusData.critical; name = statusInfo.critical.name; break;
                            }
                            
                            tooltip.innerHTML = `<div><strong>${name}: ${value}%</strong></div><div>${statusInfo[status].description}</div>`;
                            tooltip.classList.add('show');
                            
                            const rect = statusCtx.getBoundingClientRect();
                            tooltip.style.left = (event.clientX - rect.left) + 'px';
                            tooltip.style.top = (event.clientY - rect.top) + 'px';
                            
                            if (centerText) {
                                const percentElement = centerText.querySelector('.total-percent');
                                if (percentElement) {
                                    percentElement.textContent = value + '%';
                                    percentElement.style.color = 
                                        index === 0 ? 'rgba(75, 192, 192, 1)' : 
                                        index === 1 ? 'rgba(255, 206, 86, 1)' : 
                                        'rgba(255, 99, 132, 1)';
                                }
                            }
                        } else {
                            tooltip.classList.remove('show');
                            if (centerText) {
                                const percentElement = centerText.querySelector('.total-percent');
                                if (percentElement) {
                                    percentElement.textContent = statusData.working + '%';
                                    percentElement.style.color = 'rgba(75, 192, 192, 1)';
                                }
                            }
                        }
                    }
                }
            });

            statusCtx.addEventListener('mousemove', (e) => {
                if (!tooltip.classList.contains('show')) return;
                const rect = statusCtx.getBoundingClientRect();
                tooltip.style.left = (e.clientX - rect.left) + 'px';
                tooltip.style.top = (e.clientY - rect.top) + 'px';
            });
            
            statusContainer.addEventListener('mouseleave', () => {
                tooltip.classList.remove('show');
                if (centerText) {
                    const percentElement = centerText.querySelector('.total-percent');
                    if (percentElement) {
                        percentElement.textContent = statusData.working + '%';
                        percentElement.style.color = 'rgba(75, 192, 192, 1)';
                    }
                }
            });

        } catch (error) {
            console.error('Ошибка состояния:', error);
            statusContainer.innerHTML = `<div class="error">Ошибка: ${error.message}</div>`;
        }
    }

    // График продаж с кнопками переключения
    try {
        const salesData = {
            days: ['01.07', '02.07', '03.07', '04.07', '05.07', '06.07', '07.07', '08.07', '09.07', '10.07'],
            amount: [12000, 14500, 13200, 15600, 14200, 16300, 13800, 15200, 14700, 16000],
            quantity: [45, 52, 48, 57, 51, 58, 49, 55, 53, 59]
        };

        function initSalesChart(type = 'amount') {
            const ctx = document.getElementById('salesChart');
            if (!ctx) return;
            
            if (window.salesChartInstance) {
                window.salesChartInstance.destroy();
            }
            
            const isAmount = type === 'amount';
            const label = isAmount ? 'Сумма продаж, руб' : 'Количество продаж';
            const data = isAmount ? salesData.amount : salesData.quantity;
            const borderColor = isAmount ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 159, 64, 1)';
            const backgroundColor = isAmount ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 159, 64, 0.2)';
            
            window.salesChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: salesData.days,
                    datasets: [{
                        label: label,
                        data: data,
                        backgroundColor: backgroundColor,
                        borderColor: borderColor,
                        borderWidth: 2,
                        borderRadius: 5,
                        barThickness: 20
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return isAmount 
                                        ? `${context.parsed.y} руб` 
                                        : `${context.parsed.y} шт`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: { color: 'rgba(255, 255, 255, 0.1)' },
                            ticks: {
                                color: '#fff',
                                callback: function(value) {
                                    return isAmount 
                                        ? `${value/1000} тыс` 
                                        : value;
                                }
                            }
                        },
                        x: {
                            grid: { display: false },
                            ticks: { color: '#fff' }
                        }
                    }
                }
            });
        }

        // Обработчики кнопок
        document.querySelectorAll('.sales-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.sales-btn').forEach(b => {
                    b.classList.remove('active');
                });
                this.classList.add('active');
                initSalesChart(this.dataset.type);
            });
        });

        // Инициализация первого графика
        initSalesChart();

    } catch (error) {
        console.error('Ошибка продаж:', error);
        const container = document.querySelector('#salesChart')?.closest('.chart-container');
        if (container) container.innerHTML = `<div class="error">Ошибка: ${error.message}</div>`;
    }
});