document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('input[name="search"]');
    const searchForm = document.querySelector('.search-container form');
    const searchResults = document.getElementById('ttable');
    const searchh = document.getElementById('tttable');
    let totalSalesPrice = 0;
    let allMedicineData = [];
  
    function calculateTotalPrice() {
      totalSalesPrice = 0;
      displayedResults.forEach(result => {
        if (result.quantitySold && result.quantitySold > 0) {
          totalSalesPrice += result.quantitySold * result.price;
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
  
    function fetchMedicineData() {
      fetch('/search_sales', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ search_sales: '' })
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
  
    function search(query) {
      const results = searchMedicine(query);
      renderSearchResults(results);
    }
  
    function searchMedicine(query) {
      return allMedicineData.filter(medicine => medicine.name.toLowerCase().includes(query.toLowerCase()));
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
        increaseBtn.addEventListener('click', function () {
          result.quantitySold = (result.quantitySold || 0) + 1;
          row.querySelector('.quantity-sold').textContent = result.quantitySold;
          calculateTotalPrice();
        });
  
        const decreaseBtn = document.createElement('button');
        decreaseBtn.textContent = '-';
        decreaseBtn.addEventListener('click', function () {
          if (result.quantitySold && result.quantitySold > 0) {
            result.quantitySold--;
            row.querySelector('.quantity-sold').textContent = result.quantitySold;
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
    searchForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const query = searchInput.value.trim().toLowerCase();
    
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
    });


    
    const cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.addEventListener('click', function () {
      location.reload();
    });
  
    searchInput.addEventListener('keyup', function () {
      search(this.value);
    });
  
    fetchMedicineData();
  });