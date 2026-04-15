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
        <!-- Enlace de retorno al núcleo estático -->
        <a href="/" class="header__brand">mercedev.es</a>
        <nav class="header__nav" aria-label="Navegación del Blog">
            <a href="/blog" class="header__link">Biblioteca Dinámica</a>
        </nav>
    </header>

    <main class="main-content">
        <?php 
        // Inicio de "The Loop" de WordPress
        if ( have_posts() ) : 
            while ( have_posts() ) : the_post(); 
        ?>
            
            <!-- Estructura BEM para el artículo dinámico -->
            <article class="article">
                <h1 class="article__title"><?php the_title(); ?></h1>
                
                <div class="article__content">
                    <?php the_content(); ?>
                </div>
            </article>

        <?php 
            endwhile; 
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