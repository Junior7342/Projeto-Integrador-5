document.addEventListener('DOMContentLoaded', function() {
    var contentContainer = document.getElementById('welcome');
    if (contentContainer) {
        contentContainer.classList.add('visible');
    }

    var contentSearch = document.getElementById('search');
    if (contentSearch) {
        contentSearch.classList.add('visible');
    }

    var artistsImages = document.getElementById('art');
    if (artistsImages) {
        var imgElements = artistsImages.querySelectorAll('.a-img');
        imgElements.forEach(function(img) {
            img.classList.add('visible');
        });
    }
});
