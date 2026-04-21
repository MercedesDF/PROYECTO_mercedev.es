<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php wp_title('|', true, 'right'); ?></title>
    <link rel="icon" href="/favicon.ico?v=3" type="image/x-icon">
    <?php wp_head(); ?>
</head>
<body <?php body_class('theme-body'); ?>>
    <header class="header">
        <a href="/" class="header__brand">
            <img src="/assets/logo.webp?v=2" alt="mercedev.es" class="header__logo" width="150" height="auto">
        </a>
        <button class="header__toggle" id="menu-toggle" aria-label="Abrir menú" aria-expanded="false">
            <span class="header__toggle-icon"></span>
        </button>
        <nav class="header__nav nav" id="main-nav" aria-label="Navegación principal">
            <a href="/" class="nav__link">Home</a>
            <a href="/biblioteca" class="nav__link">Biblioteca</a>
            <a href="/blog" class="nav__link">Blog</a>
            <a href="/blog/category/art-de-cote" class="nav__link">Art de Coté</a>
            <a href="/blog/tienda" class="nav__link">Tienda</a>
            <a href="/contacto" class="nav__link">Contacto</a>
        </nav>
    </header>

    <main class="main">
        <section class="hero">
            <h1 class="hero__title">Tienda</h1>
            <p class="hero__subtitle">Catálogo de recursos, herramientas y merchandising oficial del entorno Merci Boilerplate.</p>
        </section>

        <section class="section">
            <?php 
            // Esta es la función mágica: renderiza los productos, pero dentro de NUESTRA estructura.
            woocommerce_content(); 
            ?>
        </section>
    </main>

    <footer class="footer">
        <p class="footer__text">&copy; 2026 <strong>mercedev.es</strong> — Base de código abierto bajo Licencia MIT.</p>
    </footer>

    <?php wp_footer(); ?>
</body>
</html>