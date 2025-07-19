document.addEventListener('DOMContentLoaded', function() {
    // Обработчики для кнопок "Подробнее"
    document.querySelectorAll('.details-btn').forEach(button => {
        button.addEventListener('click', function() {
            const row = this.closest('tr');
            const machineId = row.cells[0].textContent;
            const machineName = row.cells[1].textContent;
            alert(`Подробная информация по автомату: ${machineName} (ID: ${machineId})`);
        });
    });
});