document.addEventListener('DOMContentLoaded', async function () {
            const ctx = document.getElementById('efficiencyChart').getContext('2d');

            try {
                // Эмуляция API запроса
                const mockApiResponse = () => {
                    return new Promise((resolve) => {
                        setTimeout(() => {
                            resolve({
                                labels: ['Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль'],
                                values: [75, 82, 68, 90, 85, 92]
                            });
                        }, 500);
                    });
                };

                // Замените на реальный запрос:
                // const response = await fetch('/api/efficiency');
                // const data = await response.json();
                const data = await mockApiResponse();

                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'Эффективность, %',
                            data: data.values,
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
                console.error('Ошибка загрузки данных:', error);
                document.querySelector('.chart-container').innerHTML = `
                    <div class="error-message">
                        Ошибка загрузки данных: ${error.message || 'Неизвестная ошибка'}
                    </div>
                `;
            }
        });
