document.addEventListener('DOMContentLoaded', function() {
    var accordionItems = document.querySelectorAll('.accordion-item');
    var accordionContents = document.querySelectorAll('.accordian-content');

    // Handle clicking on accordion items to show the accordion content


    accordionItems.forEach(function(item) {
        item.addEventListener('click', function() {
            // Toggle only the clicked accordion item and its content
            var content = this.nextElementSibling;

            // If the clicked content is already displayed, hide it and show the item
            if (content.style.display === 'table-row') {
                content.style.display = 'none';
                this.style.display = 'table-row';  // Make sure the item row is shown
            } else {
                // Otherwise, hide all other content rows and display the clicked content
                accordionContents.forEach(function(otherContent) {
                    otherContent.style.display = 'none';
                    // Also, ensure other accordion items are visible
                    if (otherContent.previousElementSibling) {
                        otherContent.previousElementSibling.style.display = 'table-row';
                    }
                });
                content.style.display = 'table-row';
                this.style.display = 'none';  // Hide the clicked item row
            }
        });
    });
    
    // Handle clicking on 'Cancel Changes' buttons to close the accordion content
    var cancelButtons = document.querySelectorAll('.cancelchanges');
    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the form from resetting
            // Find the closest accordion content to this button
            var content = this.closest('.accordian-content');

            var form = content.querySelector('form');
            form.reset();
            // Hide the accordion content
            content.style.display = 'none';
            // Show the corresponding accordion item
            var item = content.previousElementSibling;
            item.style.display = 'table-row';
        });
    });

    // Check the number of accordion items and enable scrolling if there are more than 5
    var table = document.querySelector('.InnerPanel');
    if (accordionItems.length > 5) {
        console.log("More than 5 accordion items. Adding scroll class.");
        table.classList.add('scroll');
    }
});