<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php wp_title('|', true, 'right'); ?></title>
    
    <?php 
    // wp_head() es el anclaje obligatorio. 
    // Aquí aterrizará nuestro /assets/main.css gracias al functions.php
    wp_head(); 
    ?>
</head>
<body <?php body_class('theme-body'); ?>>

    <header class="header">
        <a href="/" class="header__brand">
            <img src="/assets/logo.webp" alt="mercedev.es" class="header__logo" width="150" height="auto">
        </a>
        <nav class="header__nav nav" aria-label="Navegación principal">
            <a href="/biblioteca" class="nav__link">Biblioteca</a>
            <a href="/blog" class="nav__link">Blog</a>
            <a href="/blog/category/art-de-cote" class="nav__link">Art de Coté</a>
            <a href="/tienda" class="nav__link">Tienda</a>
            <a href="/contacto" class="nav__link">Contacto</a>
        </nav>
    </header>

    <main class="main-content">
        <?php 
        if ( have_posts() ) :
        ?>
            
            <?php if ( is_singular() ) : ?>
                <!-- VISTA DE LECTURA (Artículo individual) -->
                <?php while ( have_posts() ) : the_post(); ?>
                    <article class="article">
                        <h1 class="article__title"><?php the_title(); ?></h1>
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
    </main>

    <!-- wp_footer() es obligatorio para scripts de cierre y barra de administración (si estás logueada) -->
    <?php wp_footer(); ?>
</body>
</html>