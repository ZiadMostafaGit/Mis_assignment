document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('input[name="search"]');
    const searchResults = document.getElementById('ttable');
    const searchh = document.getElementById('tttable');
    let totalSalesPrice = 0;
    let displayedResults = [];

    // Get Pharmacist ID and Customer ID from the HTML form
    const pharmacistIdInput = document.getElementById('Id');
    const customerIdInput = document.getElementById('Customer_id');

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
                <td>${result[3]}</td>
                <td style="display: flex; justify-content: space-between;">
                    <span class="quantity-sold">${result[4] || 0}</span>
                </td>
                <td>${result[2]}</td>
                <td>${result[6]}</td>
            `;

            const increaseBtn = document.createElement('button');
            increaseBtn.textContent = '+';
            increaseBtn.addEventListener('click', function () {
                console.log('Increase button clicked');
                const quantitySold = parseInt(result[4] || 0);
                result[4] = quantitySold + 1;
                row.querySelector('.quantity-sold').textContent = result[4];
                calculateTotalPrice();
            });

            const decreaseBtn = document.createElement('button');
            decreaseBtn.textContent = '-';
            decreaseBtn.addEventListener('click', function () {
                console.log('Decrease button clicked');
                const quantitySold = parseInt(result[4] || 0);
                if (quantitySold > 0) {
                    result[4] = quantitySold - 1;
                    row.querySelector('.quantity-sold').textContent = result[4];
                    calculateTotalPrice();
                }
            });

            const resetBtn = document.createElement('button');
            resetBtn.textContent = 'Reset';
            resetBtn.addEventListener('click', function () {
                const index = displayedResults.indexOf(result);
                if (index > -1) {
                    displayedResults.splice(index, 1);
                    renderSearchResults(displayedResults);
                    calculateTotalPrice();
                }
            });

            const buttonCell = document.createElement('td');
            buttonCell.appendChild(increaseBtn);
            buttonCell.appendChild(decreaseBtn);
            buttonCell.appendChild(resetBtn);
            row.appendChild(buttonCell);

            searchResults.appendChild(row);
        });
    }

    const saveSellBtn = document.getElementById('saveSellBtn');
    console.log("Save & Sell button:", saveSellBtn); // Check if the button element is correctly selected

    saveSellBtn.addEventListener('click', function () {
        console.log("Save & Sell button clicked"); // Check if the event listener is triggered
        const orderData = [];

        displayedResults.forEach(result => {
            const m_id = result[0]; // Assuming m_id is stored at index 0 of the result array
            const quantitySold = result[4] || 0; // Assuming quantity sold is stored at index 4 of the result array

            orderData.push({ m_id, quantitySold });
        });

        // Get the values of Pharmacist ID and Customer ID
        const c_p = parseInt(pharmacistIdInput.value);
        const p_id = parseInt(customerIdInput.value);

        // Send the orderData array along with Pharmacist ID and Customer ID to the backend endpoint
        fetch('/sell_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ c_p, p_id, orderData }),
        })
            .then(response => response.json())
            .then(data => {
                // Handle response from the backend if needed
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
});
