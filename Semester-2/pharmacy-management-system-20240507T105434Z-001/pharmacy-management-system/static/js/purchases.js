document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('input[name="search_purchases"]');
    const searchResults = document.getElementById('ttable');
    const searchh = document.getElementById('tttable');
    let totalSalesPrice = 0;
    let displayedResults = [];

    function calculateTotalPrice() {
        totalSalesPrice = 0;
        displayedResults.forEach(result => {
            if (result[4] && result[4] > 0) {
                totalSalesPrice += (result[4] * result[2]);
            }
        });

        const totalPriceElement = document.getElementById('totalPrice');
        if (totalPriceElement) {
            totalPriceElement.textContent = `Total Price: $${totalSalesPrice.toFixed(2)}`;
        }
    }

    function search(query) {
        let table = "";

        // Clear the search results list if the query is empty
        if (query.trim() === "") {
            searchh.innerHTML = '';
            return;
        }

        fetch('/search_sales', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ search_sales: query }),
        })
            .then(response => response.json())
            .then(data => {
                // Clear the search results list
                searchh.innerHTML = '';

                data.forEach(medicine => {
                    table += `
                        <tr>
                            <td>${medicine[0]}</td>
                            <td>${medicine[1]}</td>
                            <td>${medicine[3]}</td>
                            <td style="display: flex; justify-content: space-between;">
                                <span class="quantity-sold">${medicine[4] || 0}</span>
                            </td>
                            <td>${medicine[2]}</td>
                            <td>${medicine[6]}</td>
                            <td>
                                <button class="addBtn">Add</button>
                            </td>
                        </tr>
                    `;
                });

                searchh.innerHTML = table;
                calculateTotalPrice();
                const addBtns = document.querySelectorAll('.addBtn');
                addBtns.forEach((btn, index) => {
                    btn.addEventListener('click', function () {
                        displayedResults.push(data[index]);
                        renderSearchResults(displayedResults);
                        calculateTotalPrice();
                    });
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    searchInput.addEventListener('keyup', function () {
        search(this.value);
    });

    function renderSearchResults(results) {
        searchResults.innerHTML = '';

        results.forEach(result => {
            const row = document.createElement('tr');
            row.innerHTML = `
            <td>${result[0]}</td>
            <td>${result[1]}</td>
            <td> <input type="number" class="quantity-input" onkeyup="calculateTotal()"></td>
            <td> <input type="number" class="supply-price-input" onkeyup="calculateTotal()"></td>
            <td>${result[2]}</td>
            <td><input type="date" class="expiration-date-input"></td>
            `;

            searchResults.appendChild(row);
        });
    }

    const supplierIdInput = document.querySelector('input[placeholder="Supplier-ID"]');
    const saveSellBtn = document.getElementById('saveSellBtn');

    saveSellBtn.addEventListener('click', function () {
        const supplierID = supplierIdInput.value;
        const purchaseOrderData = [];
    
        // Get all rows in the table body
        const rows = document.querySelectorAll('table tbody tr');
    
        // Loop through each row
        rows.forEach(row => {
            const medicineId = row.querySelector('td:first-child').textContent;
            const quantity = row.querySelector('.quantity-input').value;
            const purchasePrice = row.querySelector('.supply-price-input').value;
            let expireDateInput = row.querySelector('.expiration-date-input');
            let expireDate = expireDateInput.value;
    
            // Parse the expiration date value
            let parsedDate = new Date(expireDate);
            
            // Format the expiration date as 'mm/yyyy'
            let formattedExpireDate = `${parsedDate.getMonth() + 1}/${parsedDate.getFullYear()}`;
    
            // Create an object for this medicine
            const medicine = { medicineId, quantity, purchasePrice, expireDate: formattedExpireDate };
    
            // Add the medicine object to the purchaseOrderData array
            purchaseOrderData.push(medicine);
        });
    
        // Send the purchase order data to the backend
        fetch('/api/purchase_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ supplier_id: supplierID, purchaseOrderData }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the backend
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    

    const cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.addEventListener('click', function () {
        location.reload();
    });

    function calculateTotal() {
        // Get all rows in the table body
        const rows = document.querySelectorAll('table tbody tr');

        let totalPrice = 0;

        // Loop through each row
        rows.forEach(row => {
            // Get quantity and supply price input elements
            const quantityInput = row.querySelector('.quantity-input');
            const supplyPriceInput = row.querySelector('.supply-price-input');

            // Get the values from the input elements
            const quantity = parseFloat(quantityInput.value) || 0;
            const supplyPrice = parseFloat(supplyPriceInput.value) || 0;

            // Calculate the total price for this row
            const rowTotalPrice = quantity * supplyPrice;

            // Add the row total to the overall total price
            totalPrice += rowTotalPrice;
        });

        // Update the total price display
        const totalPriceElement = document.getElementById('totalPrice');
        totalPriceElement.textContent = `Total Price: $${totalPrice.toFixed(2)}`;
    }
});