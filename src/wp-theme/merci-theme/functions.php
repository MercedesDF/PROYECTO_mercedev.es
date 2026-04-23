<?php
/**
 * Merci Theme - functions.php
 * Escudo de rendimiento y enlazador de assets estáticos (Fase 4.2).
 * 
 * NOTA ARQUITECTÓNICA: Este archivo tiene la responsabilidad exclusiva 
 * de bloquear la inyección de código basura de WP (WordPress) y enlazar 
 * el CSS compilado del núcleo estático.
 */

// =========================================================================
// 1. LIMPIEZA DE CABECERA (Bloqueo de código basura)
// =========================================================================

// Eliminar el soporte nativo de emojis (inyecta JS y CSS innecesario en el DOM)
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');

/**
 * Función para desencolar (dequeue) estilos masivos que WP inyecta por defecto.
 */
function merci_limpiar_estilos_por_defecto() {
    // Elimina el CSS de la librería de bloques (Gutenberg)
    wp_dequeue_style('wp-block-library');
    wp_dequeue_style('wp-block-library-theme');
    // Elimina el CSS de variables globales (theme.json inyectado en línea)
    wp_dequeue_style('global-styles');
    // Elimina estilos clásicos residuales
    wp_dequeue_style('classic-theme-styles');
}
// Enganchamos nuestra función de limpieza al momento exacto en que WP carga estilos, 
// dándole una prioridad de '100' para asegurarnos de que se ejecute al final y pise a los demás.
add_action('wp_enqueue_scripts', 'merci_limpiar_estilos_por_defecto', 100);

// Eliminar la inyección forzada del motor de global-styles en línea
remove_action('wp_enqueue_scripts', 'wp_enqueue_global_styles');
remove_action('wp_body_open', 'wp_enqueue_global_styles');

// =========================================================================
// 2. ENLACE CON EL NÚCLEO ESTÁTICO
// =========================================================================

function merci_cargar_assets_estaticos() {
    // Obtenemos la URL oficial y segura de WordPress (ej. https://mercedev.es/blog o http://localhost/blog).
    // Al usar home_url(), esquivamos la inyección del puerto interno 8080 que Varnish hace en $_SERVER['HTTP_HOST'].
    // Luego, eliminamos el sufijo '/blog' para apuntar a la raíz estática pública.
    $domain_root = preg_replace('#/blog/?$#', '', home_url());
    wp_enqueue_style('merci-core-styles', $domain_root . '/css/main.css', array(), '1.0.1', 'all');
    // Encolar el JavaScript unificado (el filtro de defer lo procesará automáticamente)
    wp_enqueue_script('merci-core-js', $domain_root . '/js/main.js', array(), '1.0.0', true);
}
add_action('wp_enqueue_scripts', 'merci_cargar_assets_estaticos');

// =========================================================================
// 2.5 RENDIMIENTO: CARGA DIFERIDA DE SCRIPTS (Fase 4.4)
// =========================================================================

// Forzar atributo 'defer' en todos los scripts del frontend para no bloquear el renderizado
function merci_defer_js_frontend($tag, $handle) {
    // No tocar los scripts si estamos en el panel de administración
    if (is_admin() || strpos($tag, ' defer') !== false) {
        return $tag;
    }
    // Reemplazar ' src' por ' defer src'
    return str_replace(' src', ' defer src', $tag);
}
add_filter('script_loader_tag', 'merci_defer_js_frontend', 10, 2);

// =========================================================================
// 3. WOOCOMMERCE EN MODO CATÁLOGO (Fase 4.3)
// =========================================================================

// Declarar soporte básico para evitar que WP/WooCommerce lance errores
function merci_woocommerce_support() {
    add_theme_support('woocommerce');
}
add_action('after_setup_theme', 'merci_woocommerce_support');

// Escudo de rendimiento: Eliminar botones de "Añadir al carrito"
remove_action('woocommerce_after_shop_loop_item', 'woocommerce_template_loop_add_to_cart', 10);
remove_action('woocommerce_single_product_summary', 'woocommerce_template_single_add_to_cart', 30);

// Desencolar scripts pesados del carrito (AJAX) que WC inyecta globalmente
function merci_limpiar_scripts_wc() {
    wp_dequeue_script('wc-cart-fragments');
}
add_action('wp_enqueue_scripts', 'merci_limpiar_scripts_wc', 100);

// Desencolar ABSOLUTAMENTE TODO el CSS por defecto de WooCommerce
add_filter( 'woocommerce_enqueue_styles', '__return_empty_array' );

// =========================================================================
// 4. HARDENING Y SEGURIDAD (Fase 5.2)
// =========================================================================

// Ocultar la versión exacta de WordPress (Security by Obscurity)
remove_action('wp_head', 'wp_generator');

// Eliminar enlaces a manifiestos no utilizados (Windows Live Writer y RSD)
remove_action('wp_head', 'wlwmanifest_link');
remove_action('wp_head', 'rsd_link');

// Desactivar la API XML-RPC (Cierra un vector crítico de ataques de fuerza bruta)
add_filter('xmlrpc_enabled', '__return_false');

// Ofuscar mensajes de error en el inicio de sesión (Evita enumeración de usuarios)
function merci_ofuscar_errores_login() {
    return 'Credenciales incorrectas.';
}
add_filter('login_errors', 'merci_ofuscar_errores_login');

// =========================================================================
// 5. AUTO-CONFIGURACIÓN DEL BOILERPLATE (Infraestructura como Código)
// =========================================================================

function merci_boilerplate_auto_setup() {
    // 1. Configurar Enlaces Permanentes (Permalinks) a "Nombre de la entrada"
    if (get_option('permalink_structure') !== '/%postname%/') {
        global $wp_rewrite;
        update_option('permalink_structure', '/%postname%/');
        $wp_rewrite->set_permalink_structure('/%postname%/');
        $wp_rewrite->flush_rules();
    }

    // 2. Autocrear las categorías requeridas por el enrutamiento del menú
    if (!term_exists('fichas', 'category')) {
        wp_insert_term('Fichas Técnicas', 'category', array('slug' => 'fichas'));
    }
    if (!term_exists('art-de-cote', 'category')) {
        wp_insert_term('Art de Coté', 'category', array('slug' => 'art-de-cote'));
    }

    // 3. Purgar contenido basura por defecto ("¡Hola, mundo!" y "Página de ejemplo")
    // Localizamos los posts por su ID habitual en instalaciones nuevas y validamos su slug
    $default_post = get_post(1);
    if ($default_post && in_array($default_post->post_name, array('hola-mundo', 'hello-world'))) {
        wp_delete_post(1, true); // true = forzar borrado sin pasar por la papelera
    }
    $default_page = get_post(2);
    if ($default_page && in_array($default_page->post_name, array('pagina-ejemplo', 'pagina-de-ejemplo', 'sample-page'))) {
        wp_delete_post(2, true);
    }
}
add_action('init', 'merci_boilerplate_auto_setup');