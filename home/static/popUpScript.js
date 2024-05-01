document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('helpBtn').addEventListener('click', function() {
        document.querySelector('.bg-modal .helpInfo').parentElement.style.display = 'flex';
    });
    
    document.querySelectorAll('.bg-modal .close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            this.closest('.bg-modal').style.display = 'none';
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {  
    document.querySelectorAll('.extraBtn').forEach(function(extraBtn) {
        extraBtn.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default form submission behavior
            var modalContent = this.closest('.accordian-content').querySelector('.bg-modal .modal-content');
            modalContent.parentElement.style.display = 'flex';
        });
    });

    // Event listener for "Add Button" buttons
    document.querySelectorAll('.addBtn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default form submission behavior
            document.querySelector('.bg-modal .create-record').parentElement.style.display = 'flex';
        });
    });

    // Event listener for close buttons
    document.querySelectorAll('.close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            var bgModal = this.closest('.bg-modal');
            bgModal.style.display = 'none';

            var clearForm = bgModal.querySelector('input[type="reset"]');
            if (clearForm){
                clearForm.click();
            }
        });
    });
});