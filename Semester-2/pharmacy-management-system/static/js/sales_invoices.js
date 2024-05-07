// sales_invoices.js

// Function to fetch sales invoices from the backend
function fetchSalesInvoices() {
    return fetch('/api/sales_invoices')
        .then(response => response.json())
        .then(data => {
            populateTable(data); // Call function to populate table with fetched data
        })
        .catch(error => {
            console.error('Error fetching sales invoices:', error);
        });
}

// Function to populate the table with fetched data
function populateTable(data) {
    const tableBody = document.querySelector('table tbody');
    tableBody.innerHTML = ''; // Clear existing table rows

    data.forEach(invoice => {
        invoice[4].forEach(medicine => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${invoice[0]}</td>
                <td>${invoice[1]}</td>
                <td>${invoice[2]}</td>
                <td>${medicine[0]}</td>
                <td>${medicine[1]}</td>
                <td>${medicine[2]}</td>
                <td>Unit</td>
                <td>${medicine[1] * medicine[2]}</td>
                <td>${invoice[3]}</td>
            `;
            tableBody.appendChild(row);
        });
    });
}

// Call the function to fetch sales invoices when the page loads
document.addEventListener('DOMContentLoaded', function() {
    fetchSalesInvoices();
});
