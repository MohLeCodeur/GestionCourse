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
// script.js
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const confirmDelete = confirm('Êtes-vous sûr de vouloir supprimer cet article ?');
            if (!confirmDelete) {
                event.preventDefault();  // Annule la suppression si l'utilisateur clique sur "Non"
            }
        });
    });
});

// script.js
document.addEventListener('DOMContentLoaded', function() {
    const markButtons = document.querySelectorAll('.mark-button');

    markButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const confirmMark = confirm('Êtes-vous sûr de vouloir marquer cet article comme acheté/non acheté ?');
            if (!confirmMark) {
                event.preventDefault();  // Annule l'action si l'utilisateur clique sur "Non"
            }
        });
    });
});