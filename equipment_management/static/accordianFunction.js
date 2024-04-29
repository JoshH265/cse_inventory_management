// document.addEventListener('DOMContentLoaded', function() {
//     // Handle clicking on accordion items to show the accordion content
//     document.querySelectorAll('.accordion-item').forEach(function(item) {
//         item.addEventListener('click', function() {
//             // Close all other open accordions
//             document.querySelectorAll('.accordion-item').forEach(function(otherItem) {
//                 if (otherItem !== item) {
//                     var otherContent = otherItem.nextElementSibling;
//                     otherContent.style.display = "none";
//                 }
//             });

//             // Get the next element, which is the accordion content
//             var content = this.nextElementSibling;
//             // Show or hide the accordion content
//             content.style.display = content.style.display === "none" ? "table-row" : "none";
//         });
//     });

//     // Handle clicking on 'Cancel Changes' buttons to close the accordion content
//     document.querySelectorAll('.cancelchanges').forEach(function(button) {
//         button.addEventListener('click', function(event) {
//             event.preventDefault(); // Prevent the form from resetting
//             // Find the closest accordion content to this button
//             var content = this.closest('.accordian-content'); // Ensure the class name matches your HTML
//             // Hide the accordion content
//             content.style.display = 'none';
//             // Show the corresponding accordion item
//             var item = content.previousElementSibling;
//             item.style.display = 'table-row';
//         });
//     });
// });


document.addEventListener('DOMContentLoaded', function() {
    var accordionItems = document.querySelectorAll('.accordion-item');
    var accordionContents = document.querySelectorAll('.accordian-content');

    console.log("Number of accordion items:", accordionItems.length);

    // Handle clicking on accordion items to show the accordion content
    accordionItems.forEach(function(item) {
        item.addEventListener('click', function() {
            // Close all other open accordions
            accordionContents.forEach(function(content) {
                if (content !== item.nextElementSibling) {
                    content.style.display = 'none';
                }
            });

            // Get the next element, which is the accordion content
            var content = this.nextElementSibling;
            // Show or hide the accordion content
            content.style.display = content.style.display === 'none' ? 'table-row' : 'none';
        });
    });

    // Handle clicking on 'Cancel Changes' buttons to close the accordion content
    var cancelButtons = document.querySelectorAll('.cancelchanges');
    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the form from resetting
            // Find the closest accordion content to this button
            var content = this.closest('.accordian-content');
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