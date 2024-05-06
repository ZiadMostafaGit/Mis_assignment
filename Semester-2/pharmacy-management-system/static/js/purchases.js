document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('input[name="search"]');
    const searchResults = document.getElementById('ttable');
    const searchh = document.getElementById('tttable');
    let displayedResults = [];

    // Get Pharmacist ID and Customer ID from the HTML form
    const pharmacistIdInput = document.getElementById('Id');
    const customerIdInput = document.getElementById('Customer_id');

    function search(query) {
        let table = "";

        // Clear the search results list if the query is empty
        if (query.trim() === "") {
            searchh.innerHTML = '';
            return;
        }

        fetch('/search_purchases', { // Assuming this is the endpoint for searching purchases
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ search_purchases: query }), // Adjust the key based on the backend requirement
        })
            .then(response => response.json())
            .then(data => {
                // Clear the search results list
                searchh.innerHTML = '';

                data.forEach(medicine => {
                    // Adjust to display only medicine name and price
                    table += `
                        <tr>
                            <td>${medicine.name}</td>
                            <td>${medicine.price}</td>
                            <td>
                                <button class="addBtn">Add</button>
                            </td>
                        </tr>
                    `;
                });

                searchh.innerHTML = table;
                const addBtns = document.querySelectorAll('.addBtn');
                addBtns.forEach((btn, index) => {
                    btn.addEventListener('click', function () {
                        displayedResults.push(data[index]);
                        renderSearchResults(displayedResults);
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
                <td>${result.name}</td>
                <td>${result.price}</td>
            `;

            searchResults.appendChild(row);
        });
    }

    const savePurchaseBtn = document.getElementById('savePurchaseBtn');
    savePurchaseBtn.addEventListener('click', function () {
        console.log("Save Purchase button clicked");

        // Get the values of Pharmacist ID and Customer ID
        const c_p = parseInt(pharmacistIdInput.value);
        const p_id = parseInt(customerIdInput.value);

        // Assuming displayedResults contain the selected purchases
        console.log("Selected purchases:", displayedResults);

        // You can proceed with saving the purchase data
    });

    const cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.addEventListener('click', function () {
        location.reload();
    });
});
