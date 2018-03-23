function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
} 


var input = document.querySelector('#file-input');

// Hide the input (type="file") element because we can't control style
input.style.opacity = 0;

// Update the readonly filename textbox when input(type="file") changes
input.addEventListener('change', function() {
    document
        .getElementById("import-filename")
        .value = input.files[0].name 
            + " (size: " + returnFileSize(input.files[0].size) + ")";
});

function returnFileSize(number) {
    if (number < 1024) {
        return number + 'bytes';
    } else if (number > 1024 && number < 1048576) {
        return (number/1024).toFixed(1) + 'KB';
    } else if (number > 1048576) {
        return (number/1048576).toFixed(1) + 'MB';
    }
}

