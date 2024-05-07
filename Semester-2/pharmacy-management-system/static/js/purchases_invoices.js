// Function to populate the table with fetched data
function populateTable(data) {
    const tableBody = document.querySelector('table tbody');
    tableBody.innerHTML = ''; // Clear existing table rows

    data.forEach(invoice => {
        invoice[3].forEach(medicine => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${invoice[0]}</td>
                <td>${invoice[1]}</td>
                <td>${invoice[2]}</td>
                <td>${medicine[0]}</td>
                <td>${medicine[1]}</td>
                <td>${medicine[2]}</td>
                <td>${medicine[3]}</td>
                <td>${medicine[4]}</td>
            `;
            tableBody.appendChild(row);
        });
    });
}

// Call the function to fetch purchase invoices when the page loads
document.addEventListener('DOMContentLoaded', function() {
    fetchPurchaseInvoices();
});

// Function to fetch purchase invoices
function fetchPurchaseInvoices() {
    fetch('/api/purchase_invoices')
        .then(response => response.json())
        .then(data => populateTable(data))
        .catch(error => console.error('Error fetching purchase invoices:', error));
}
