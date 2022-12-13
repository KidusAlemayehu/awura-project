document.querySelectorAll(".slide_container").forEach((carousel) => {
    const items = carousel.querySelectorAll(".slideitem");

    const buttons = document.querySelectorAll(".slide-nav");

    buttons.forEach((button, i) => {
        button.addEventListener("click", () => {
            // un-select all the items
            items.forEach((item) =>
                item.classList.remove("slideitem--selected")
            );
            buttons.forEach((button) =>
                button.classList.remove("btn-selected")
            );

            items[i].classList.add("slideitem--selected");
            button.classList.add("btn-selected");
        });
    });

    // Select the first item on page load
    items[0].classList.add("slidetem--selected");
    buttons[0].classList.add("btn-selected");
});