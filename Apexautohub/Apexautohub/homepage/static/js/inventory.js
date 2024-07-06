// your-js-file.js

// Function to animate car list items
function animateCarListItems() {
    const carListItems = document.querySelectorAll('ul li');

    carListItems.forEach((carItem, index) => {
        carItem.style.animation = `fadeInUp 0.5s ease ${index / 5}s both`;
    });
}

// Function to handle clicks on car list items
function handleCarItemClick(event) {
    const carName = event.target.textContent;

    // Redirect to the individual car page
    window.location.href = `${carName.toLowerCase()}.html`;
}

// Function to add hover effect on car list items
function addHoverEffect(carItem) {
    carItem.addEventListener('mouseover', () => {
        carItem.style.transform = 'scale(1.05)';
    });

    carItem.addEventListener('mouseout', () => {
        carItem.style.transform = 'scale(1)';
    });
}

document.addEventListener('DOMContentLoaded', () => {
    animateCarListItems();

    const carListItems = document.querySelectorAll('ul li');
    carListItems.forEach((carItem) => {
        addHoverEffect(carItem);
        carItem.addEventListener('click', handleCarItemClick);
    });
});

