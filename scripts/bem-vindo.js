document.addEventListener('DOMContentLoaded', function () {
    // Adiciona a classe 'visible-content' aos elementos desejados
    function addVisibleClass(elementId) {
        var element = document.getElementById(elementId);
        if (element) {
            element.classList.add('visible-content');
        }
    }

    addVisibleClass('welcome');
    addVisibleClass('search');

    var artistsImages = document.getElementById('art');
    if (artistsImages) {
        var imgElements = artistsImages.querySelectorAll('.a-img');
        imgElements.forEach(function (img) {
            img.classList.add('visible-content');
        });
    }

    var mobileMenuIcon = document.getElementById('mobile-menu-icon');
    var mobileMenu = document.querySelector('.mobile-menu');

    if (mobileMenuIcon && mobileMenu) {
        // Alterna a visibilidade do menu móvel
        mobileMenuIcon.addEventListener('click', function () {
            if (mobileMenu.style.display === 'flex') {
                mobileMenu.style.display = 'none';
            } else {
                mobileMenu.style.display = 'flex';
            }
        });

        // Fecha o menu ao clicar fora dele
        document.addEventListener('click', function (event) {
            var isClickInsideMobileMenu = mobileMenu.contains(event.target);
            var isClickInsideMobileMenuIcon = mobileMenuIcon.contains(event.target);

            if (!isClickInsideMobileMenu && !isClickInsideMobileMenuIcon) {
                mobileMenu.style.display = 'none';
            }
        });
    }
});
