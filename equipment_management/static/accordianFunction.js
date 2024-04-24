function toggleAccordion(button) {
    var contentRow = button.parentNode.parentNode.nextElementSibling; // Get the next row (content) of the clicked button
    contentRow.style.display = contentRow.style.display === 'none' ? 'table-row' : 'none'; // Toggle the display property
}
// function toggleAccordion(button) {
//     var contentRow = button.parentNode.parentNode.nextElementSibling; // Get the next row (content) of the clicked button
//     var itemRow = button.parentNode.parentNode; // Get the current row (accordion item) of the clicked button

//     if (contentRow.style.display === 'none') {
//         contentRow.style.display = 'table-row'; // Show the content row
//         itemRow.style.display = 'none'; // Hide the item row
//     } else {
//         contentRow.style.display = 'none'; // Hide the content row
//         itemRow.style.display = 'table-row'; // Show the item row
//     }
// }