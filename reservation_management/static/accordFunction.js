document.addEventListener('DOMContentLoaded', () => {
    const tables = document.querySelectorAll('table');
    const transitionDuration = 200; // Duration in milliseconds

    tables.forEach(table => {
        table.addEventListener('click', (event) => {
            const target = event.target;
            const isTrigger = target.closest('.accordion-trigger');
            const isButton = target.classList.contains('cancel-btn') || target.classList.contains('save-btn');

            if (isTrigger) {
                const parentRow = isTrigger;
                const accordionContent = parentRow.nextElementSibling;

                // If the accordion is being opened
                if (accordionContent.classList.contains('hidden')) {
                    // Remove 'hidden' class after a slight delay to start the transition
                    setTimeout(() => {
                        accordionContent.classList.remove('hidden');
                    }, 20);
                    // Add 'active' class to apply the transition effect
                    accordionContent.classList.add('active');
                    parentRow.classList.add('hidden'); // Hide the parent row immediately
                }
                // If the accordion is being closed
                else {
                    // Remove 'active' class to end the transition
                    accordionContent.classList.remove('active');
                    // Add 'hidden' class after the transition has completed
                    setTimeout(() => {
                        accordionContent.classList.add('hidden');
                    }, transitionDuration);
                    parentRow.classList.remove('hidden'); // Show the parent row immediately
                }
            } else if (isButton && target.classList.contains('cancel-btn')) {
                const accordionContent = target.closest('.accordion-content');
                const parentRow = accordionContent.previousElementSibling;
                // Remove 'active' class and add 'hidden' with a delay
                accordionContent.classList.remove('active');
                setTimeout(() => {
                    accordionContent.classList.add('hidden');
                }, transitionDuration);
                parentRow.classList.remove('hidden'); // Show the parent row immediately
            }
        });
    });
});