document.addEventListener('DOMContentLoaded', function() {
    fetchData();
});

function fetchData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/fetch_data?table=Medicine', true);
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

        var m_id = document.createElement('td');
        m_id.textContent = row['M_ID'];
        tr.appendChild(m_id);

        var m_name = document.createElement('td');
        m_name.textContent = row['M_Name'];
        tr.appendChild(m_name);

        var unit_price = document.createElement('td');
        unit_price.textContent = row['Unit_Price'];
        tr.appendChild(unit_price);

        var quantity = document.createElement('td');
        quantity.textContent = row['Quantity'];
        tr.appendChild(quantity);

        var units = document.createElement('td');
        units.textContent = row['Units'];
        tr.appendChild(units);

        var category = document.createElement('td');
        category.textContent = row['Category'];
        tr.appendChild(category);

        var expire_date = document.createElement('td');
        expire_date.textContent = row['Expire_Date'];
        tr.appendChild(expire_date);

        tableBody.appendChild(tr);
    });
}