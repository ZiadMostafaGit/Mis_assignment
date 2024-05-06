document.addEventListener('DOMContentLoaded', function() {
    fetchMissingMedicines();
});

function fetchMissingMedicines() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/fetch_missing', true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            updateTable(data);
        } else {
            console.error('Request failed. Status:', xhr.status);
        }
    };
    xhr.onerror = function() {
        console.error('Request failed. Check your network connection.');
    };
    xhr.send();
}

function updateTable(data) {
    var tableBody = document.querySelector('table tbody');
    tableBody.innerHTML = ''; // Clear existing table data
    data.forEach(function(row) {
        var tr = document.createElement('tr');
        row.forEach(function(cellData) {
            var td = document.createElement('td');
            td.textContent = cellData;
            tr.appendChild(td);
        });
        tableBody.appendChild(tr);
    });
}
