window.onload = function() {
    var toggleSwitch = document.getElementById('toggle-switch');
    var rows = document.querySelectorAll('#tasks-table tr');
    
    toggleSwitch.addEventListener('change', function() {
        var isChecked = this.checked;
        for (var i = 0; i < rows.length; i++) {
            var ownerCell = rows[i].getElementsByTagName('td')[2];
            if (isChecked && ownerCell && ownerCell.textContent !== "{{ user.username }}") {
                rows[i].style.display = 'none';
            } else {
                rows[i].style.display = 'table-row';
            }
        }
    });
};