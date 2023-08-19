function saveCheckboxValues() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    let checkedValues = [];

    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            checkedValues.push(checkbox.id); /* Seçilen checkboxların id'leri kaydediliyor. 
            View tarafında tıklanan checkbox'lara erişebilmek adına name'lerin aynı olması gerekiyordu.
            Valueler eklendiğinde ise marka, model ve kategorilerin veritabanındaki id'leri aynı olduğunda seçilmeyen checkboxlarda işaretlenir. */ 
        }
    });

    localStorage.setItem('checkedValues', JSON.stringify(checkedValues));
}

function loadCheckboxValues() {
    const checkedValues = JSON.parse(localStorage.getItem('checkedValues'));

    if (checkedValues) {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(function (checkbox) { 
            if (checkedValues.includes(checkbox.id)) { /* Daha önce tıklanmış olan checkbox'lara erişiliyor ve sayfa üzerinde işaretleniyor. */
                checkbox.checked = true; 
            }
        });
    }
}

function UavFilter() {
    saveCheckboxValues();
}

$(document).ready(function() {
    loadCheckboxValues();
});
