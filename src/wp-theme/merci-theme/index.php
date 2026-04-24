<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Favicon explícito para la capa dinámica -->
    <link rel="icon" href="/favicon.ico?v=3" type="image/x-icon">

    <?php 
    // wp_head() es el anclaje obligatorio. 
    // Aquí aterrizará nuestro /assets/main.css gracias al functions.php
    wp_head(); 
    ?>
</head>
<body <?php body_class('theme-body'); ?>>

    <header class="header" id="top" tabindex="-1">
        <a href="#main" class="skip-link">Saltar al contenido principal</a>
        <a href="/" class="header__brand">
            <img src="/assets/logo.webp?v=2" alt="{{DOMINIO}}" class="header__logo" width="263" height="65">
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

    <main class="main" id="main" tabindex="-1">
        <?php 
        // 1. Inyección de Cabeceras Estilo "Boilerplate" para Vistas Dinámicas
        $header_title = '';
        $header_desc = '';

        if ( is_category('art-de-cote') ) {
            $header_title = 'Art de Coté';
            $header_desc = 'Repositorio de hallazgos y herramientas colaterales. I+D puro convertido en activos técnicos reutilizables.';
        } elseif ( is_page('tienda') || (function_exists('is_shop') && is_shop()) ) {
            $header_title = 'Tienda';
            $header_desc = 'Catálogo de recursos, herramientas y merchandising oficial del entorno Merci Boilerplate.';
        } elseif ( is_home() || is_archive() ) {
            $header_title = 'Blog';
            $header_desc = 'Bitácora cronológica, diario de desarrollo y artículos generales del ecosistema.';
        }

        if ( $header_title ) : 
        ?>
            <section class="hero">
                <h1 class="hero__title"><?php echo $header_title; ?></h1>
                <p class="hero__subtitle"><?php echo $header_desc; ?></p>
            </section>
        <?php endif; ?>

        <!-- Atomización definitiva: Usamos el componente estructural genérico -->
        <section class="section">
        <?php 
        // 2. Bucle principal de contenido (The Loop)
        if ( have_posts() ) :
        ?>
            
            <?php if ( is_singular() ) : ?>
                <!-- VISTA DE LECTURA (Artículo individual) -->
                <?php while ( have_posts() ) : the_post(); ?>
                    <article class="article">
                        <?php if ( ! $header_title ) : ?>
                            <h1 class="article__title"><?php the_title(); ?></h1>
                        <?php endif; ?>
                        <div class="article__content">
                            <?php the_content(); ?>
                        </div>
                    </article>
                <?php endwhile; ?>
            <?php else : ?>
                <!-- VISTA DE LISTADO (Grid y Tarjetas) -->
                <div class="grid">
                    <?php while ( have_posts() ) : the_post(); ?>
                        <article class="card card--booklet">
                            <h2 class="card__title">
                                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                            </h2>
                            <div class="card__meta">
                                <?php echo get_the_date(); ?> | <?php the_category(', '); ?>
                            </div>
                            <div class="card__content">
                                <?php the_excerpt(); ?>
                            </div>
                        </article>
                    <?php endwhile; ?>
                </div>
            <?php endif; ?>

        <?php 
        else : 
            echo '<p>No se encontraron artículos.</p>';
        endif; 
        // Fin de "The Loop"
        ?>
        </section>
    </main>

    <footer class="footer">
        <p class="footer__text">
            &copy; 2026 <strong>{{DOMINIO}}</strong> — Base de código abierto bajo Licencia MIT.
            <span style="margin: 0 1rem;">|</span> <a href="#top" style="color: inherit; text-decoration: underline;">↑ Volver arriba</a>
        </p>
    </footer>

    <!-- wp_footer() es obligatorio para scripts de cierre y barra de administración (si estás logueada) -->
    <?php wp_footer(); ?>
</body>
</html>