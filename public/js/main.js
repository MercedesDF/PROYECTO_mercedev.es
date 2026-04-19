/**
 * main.js - Lógica del Frontend (Vanilla JS)
 * Control del menú hamburguesa y utilidades de UI.
 */

document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const mainNav = document.getElementById('main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            // Alternar estado de accesibilidad y clases BEM
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !isExpanded);
            menuToggle.classList.toggle('is-active');
            mainNav.classList.toggle('is-active');
        });
    }
});