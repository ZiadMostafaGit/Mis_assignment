document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('input[name="search_purchases"]');
    const tableBody = document.querySelector('table tbody');

    function search(query) {
        // Clear the table body
        tableBody.innerHTML = '';

        // Clear the table body if the query is empty
        if (query.trim() === "") {
            return;
        }

        fetch('/search_purchases', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ search_purchases: query }),
        })
            .then(response => response.json())
            .then(data => {
                // Populate the table with search results
                data.forEach(medicine => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${medicine[0]}</td>
                        <td>${medicine[1]}</td>
                        <td>${medicine[2]}</td>
                        <td>${medicine[3]}</td>
                        <td>${medicine[4]}</td>
                        <td>${medicine[5]}</td>
                        <td>${medicine[6]}</td>
                    `;
                    tableBody.appendChild(row);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    searchInput.addEventListener('input', function () {
        search(this.value);
    });
});
