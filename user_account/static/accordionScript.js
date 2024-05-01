document.addEventListener('DOMContentLoaded', function() {
    var accItem = document.querySelectorAll('.accordion-item');

    accItem.forEach(function(item) {
        item.addEventListener('click', function() {
            // Get the next element in the DOM after the current accordion item
            var content = this.nextElementSibling;

            // Get the number of columns from the first row of the table
            var columnCount = this.closest('table').querySelector('tr:first-child').children.length;

            // Toggle the 'accordion-content' visibility and the 'accordion-item' itself
            if (content.style.display !== "table-row") {
                // Set the colspan attribute to match the number of columns
                content.querySelector('td').setAttribute('colspan', columnCount);
                
                content.style.display = "table-row"; // Show the accordion content
                this.style.display = "none"; // Hide the accordion item
            } else {
                content.style.display = "none"; // Hide the accordion content
                this.style.display = "table-row"; // Show the accordion item
            }
        });
    });
});
function toggleAcc() {
    var accItem = document.querySelectorAll('.accordion-item');

    accItem.forEach(function(item) {
        var content = item.nextElementSibling;
        item.style.display = "table-row";
        content.style.display = "none";
    });
}