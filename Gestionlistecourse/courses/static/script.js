// script.js
document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.querySelector('.add-button');
    
    // Animation du bouton "Ajouter un article"
    addButton.addEventListener('mouseover', function() {
        addButton.style.backgroundColor = '#218838';
    });

    addButton.addEventListener('mouseout', function() {
        addButton.style.backgroundColor = '#28a745';
    });
});
