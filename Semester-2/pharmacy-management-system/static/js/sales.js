document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('input[name="search"]');
    const searchForm = document.querySelector('.search-container form');
    const searchResults = document.getElementById('search-results');
    const selectedMedicinesList = document.getElementById('selected-medicines');
    let totalSalesPrice = 0;
    let allMedicineData = [];

    function calculateTotalPrice() {
        totalSalesPrice = 0;
        selectedMedicines.forEach(medicine => {
            if (medicine.quantitySold && medicine.quantitySold > 0) {
                totalSalesPrice += medicine.quantitySold * medicine.price;
            }
        });

        const totalPriceElement = document.getElementById('totalPrice');
        if (totalPriceElement) {
            totalPriceElement.textContent = `Total Price: $${totalSalesPrice.toFixed(2)}`;
        }
    }

    searchResults.addEventListener('click', function (event) {
        const target = event.target;
        if (target.tagName === 'BUTTON') {
            const row = target.closest('tr');
            const index = Array.from(row.parentNode.children).indexOf(row);
            const result = displayedResults[index];
            if (result) {
                if (target.textContent === '+') {
                    result.quantitySold = (result.quantitySold || 0) + 1;
                } else if (target.textContent === '-') {
                    if (result.quantitySold && result.quantitySold > 0) {
                        result.quantitySold--;
                    }
                } else if (target.textContent === 'Reset') {
                    const index = displayedResults.indexOf(result);
                    if (index > -1) {
                        displayedResults.splice(index, 1);
                        renderSearchResults(displayedResults);
                        calculateTotalPrice();
                    }
                }
                renderSearchResults(displayedResults);
                calculateTotalPrice();
            }
        }
    });

    let displayedResults = [];

    function fetchMedicineData(query) {
        fetch('/search_sales', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ search_sales: query })
        })
        .then(response => response.json())
        .then(data => {
            allMedicineData = data;
            renderSearchResults(allMedicineData);
            calculateTotalPrice();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    function renderSearchResults(results) {
        searchResults.innerHTML = '';
        results.forEach(result => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${result.id}</td>
                <td>${result.name}</td>
                <td>${result.quantity}</td>
                <td style="display: flex; justify-content: space-between;">
                    <span class="quantity-sold">${result.quantitySold || 0}</span>
                </td>
                <td>${result.price}</td>
                <td>${result.expiryDate}</td>
            `;
            const increaseBtn = document.createElement('button');
            increaseBtn.textContent = '+';
            const decreaseBtn = document.createElement('button');
            decreaseBtn.textContent = '-';
            const resetBtn = document.createElement('button');
            resetBtn.textContent = 'Reset';
            const buttonCell = document.createElement('td');
            buttonCell.appendChild(increaseBtn);
            buttonCell.appendChild(decreaseBtn);
            buttonCell.appendChild(resetBtn);
            row.appendChild(buttonCell);
            searchResults.appendChild(row);
        });
    }

    searchForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const query = searchInput.value.trim().toLowerCase();
        fetchMedicineData(query);
    });

    const cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.addEventListener('click', function () {
        location.reload();
    });

    searchInput.addEventListener('keyup', function () {
        const query = this.value.trim().toLowerCase();
        fetchMedicineData(query);
    });

    const selectedMedicines = [];

    function renderSelectedMedicines() {
        selectedMedicinesList.innerHTML = '';
        selectedMedicines.forEach(medicine => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${medicine.id}</td>
                <td>${medicine.name}</td>
                <td>${medicine.quantity}</td>
                <td style="display: flex; justify-content: space-between;">
                    <span class="quantity-sold">${medicine.quantitySold || 0}</span>
                </td>
                <td>${medicine.price}</td>
                <td>${medicine.expiryDate}</td>
            `;
            selectedMedicinesList.appendChild(row);
        });
    }

    // Event delegation for buttons
    searchResults.addEventListener('click', function (event) {
        const target = event.target;
        if (target.classList.contains('add-btn')) {
            const row = target.closest('tr');
            const index = Array.from(row.parentNode.children).indexOf(row);
            const selectedMedicine = displayedResults[index];
            if (selectedMedicine) {
                selectedMedicines.push(selectedMedicine);
                renderSelectedMedicines();
                calculateTotalPrice();
            }
        }
    });

    // You can continue with your other functionalities such as selling the selected medicines.
});
