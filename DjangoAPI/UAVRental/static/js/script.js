function saveCheckboxValues() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    let checkedValues = [];

    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            checkedValues.push(checkbox.id);
        }
    });

    localStorage.setItem('checkedValues', JSON.stringify(checkedValues));
}

function loadCheckboxValues() {
    const checkedValues = JSON.parse(localStorage.getItem('checkedValues'));

    if (checkedValues) {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(function (checkbox) {
            if (checkedValues.includes(checkbox.id)) {
                checkbox.checked = true;
            }
        });
    }
}

function UavFilter() {
    saveCheckboxValues();
}

$( document ).ready(function() {
    loadCheckboxValues();
});
