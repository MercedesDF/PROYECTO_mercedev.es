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
}
// Enganchamos nuestra función de limpieza al momento exacto en que WP carga estilos, 
// dándole una prioridad de '100' para asegurarnos de que se ejecute al final y pise a los demás.
add_action('wp_enqueue_scripts', 'merci_limpiar_estilos_por_defecto', 100);

// =========================================================================
// 2. ENLACE CON EL NÚCLEO ESTÁTICO
// =========================================================================

function merci_cargar_assets_estaticos() {
    // WordPress es obstinado: si le damos una ruta que empieza por '/', le concatena 
    // el directorio del blog por defecto (ej. /blog/css/...).
    // Para forzar la salida a la raíz estática absoluta, construimos el esquema + host:
    $domain_root = (is_ssl() ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'];
    wp_enqueue_style('merci-core-styles', $domain_root . '/css/main.css', array(), '1.0.0', 'all');
}
add_action('wp_enqueue_scripts', 'merci_cargar_assets_estaticos');

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