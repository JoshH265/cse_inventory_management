// document.addEventListener('DOMContentLoaded', function() {
//     // Handle clicking on accordion items to show the accordion content
//     document.querySelectorAll('.accordion-item').forEach(function(item) {
//         item.addEventListener('click', function() {
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
