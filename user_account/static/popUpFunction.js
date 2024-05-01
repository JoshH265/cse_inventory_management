// var cancelButton = document.getElementById("cancelEdit");

//     cancelButton.addEventListener('click', function(event){
//         event.preventDefault();
//         var accItem = this.closest('.accordian-content').previousElementSibling;
//         var accContent = this.closest('accordian-content');

//         accItem.style.display = "table-row";
//         accContent.style.display = "none";
//     });



// document.querySelectorAll('.extraBtn').forEach(function(button) {
//     button.addEventListener('click', function(event) {
//         document.querySelector('.bg-modal').style.display = 'flex';
//     });
// });

//password
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('myBtn').addEventListener('click', function() {
        document.querySelector('#password .modal-content').parentElement.style.display = 'flex';
    });
    
    document.querySelectorAll('#password .close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
});

//cr FAQ
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('myRBtn').addEventListener('click', function() {
        document.querySelector('#myHelp .modal-content').parentElement.style.display = 'flex';
    });
    
    document.querySelectorAll('#myHelp .close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
});

//cr extra info
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('extraBtn').addEventListener('click', function() {
        document.querySelector('#extra .modal-content').parentElement.style.display = 'flex';
    });
    
    document.querySelectorAll('#extra .close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
});

//rh FAQ
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btnHelpRH').addEventListener('click', function() {
        document.querySelector('#helpRH .modal-content').parentElement.style.display = 'flex';
    });
    
    document.querySelectorAll('#helpRH .close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
});

//rh extra info
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('RHextraBtn').addEventListener('click', function() {
        document.querySelector('#extraRH .modal-content').parentElement.style.display = 'flex';
    });
    
    document.querySelectorAll('#extraRH .close').forEach(function(closeBtn) {
        closeBtn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Event listener for "Extra Info" buttons
    document.querySelectorAll('.extraBtn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default form submission behavior
            document.querySelector('.bg-modal .modal-content').parentElement.style.display = 'flex';
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
    // document.querySelectorAll('.close').forEach(function(closeBtn) {
    //     closeBtn.addEventListener('click', function() {
    //         var bgModal = this.closest('.bg-modal');
    //         bgModal.style.display = 'none';

    //         var clearForm = bgModal.querySelector('input[type="reset"]');
    //         if (clearForm){
    //             clearForm.click();
    //         }
    //     });
    // });
});

// latest - works

// document.addEventListener('DOMContentLoaded', function() {
//     var extraButtons = document.getElementsByClassName('extraBtn');

//     for (var i = 0; i < extraButtons.length; i++) {
//         extraButtons[i].addEventListener('click', function(event) {
//             event.preventDefault(); // Prevent default form submission behavior
//             document.querySelector('.bg-modal').style.display = 'flex';
//         });
//     }

//     // Event listener for close button
//     document.querySelector('.close').addEventListener('click', function() {
//         document.querySelector('.bg-modal').style.display = 'none';
//     });
// });

// works

// document.addEventListener('DOMContentLoaded', function() {
//     document.body.addEventListener('click', function(event) {
//         // Check if the clicked element is an "Extra Info" button
//         if (event.target && event.target.classList.contains('extraBtn')) {
//             event.preventDefault(); // Prevent default form submission behavior
//             document.querySelector('.bg-modal').style.display = 'flex';
//         }

//         // Check if the clicked element is the close button
//         if (event.target && event.target.classList.contains('close')) {
//             document.querySelector('.bg-modal').style.display = 'none';
//         }
//     });
// });