// DOM Elements
const searchForm = document.querySelector('#search-form');
const bookCards = document.querySelectorAll('.book-card');
const reserveButtons = document.querySelectorAll('.reserve-btn');

// Search Functionality
if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
        const searchType = document.querySelector('#search-type').value;
        const searchQuery = document.querySelector('#search-query').value;
        
        if (searchQuery.length < 3) {
            e.preventDefault();
            showAlert('Search query must be at least 3 characters long', 'error');
        }
    });
}

// Book Reservation
reserveButtons.forEach(button => {
    button.addEventListener('click', async (e) => {
        e.preventDefault();
        const bookId = button.dataset.bookId;
        
        try {
            const response = await fetch(`/books/reserve/${bookId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            const data = await response.json();
            
            if (data.success) {
                showAlert('Book reserved successfully!', 'success');
                updateBookStatus(bookId, 'reserved');
            } else {
                showAlert(data.message, 'error');
            }
        } catch (error) {
            showAlert('An error occurred', 'error');
        }
    });
});

// Alert System
function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    document.querySelector('.container').insertBefore(alertDiv, document.querySelector('.content'));
    
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// Book Status Update
function updateBookStatus(bookId, status) {
    const bookCard = document.querySelector(`[data-book-id="${bookId}"]`);
    const statusBadge = bookCard.querySelector('.status-badge');
    statusBadge.textContent = status;
    statusBadge.className = `status-badge status-${status}`;
}

// Form Validation
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => {
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            if (!field.value) {
                e.preventDefault();
                showAlert(`${field.name} is required`, 'error');
            }
        });
    });
});
