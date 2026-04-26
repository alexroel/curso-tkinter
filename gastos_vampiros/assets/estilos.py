# ─── Paleta de 7 colores ─────────────────────────────────────────────────────
BG_MAIN    = "#EEE9FE"   # Fondo principal lavanda suave
BG_WHITE    = "#FCFCFD"   # Tarjetas y superficies blancas
ACCENT     = "#7C4DFF"   # Púrpura vibrante — color principal
GREEN      = "#00C9A7"   # Verde menta — acciones positivas
CORAL      = "#FF6B6B"   # Coral — acciones destructivas / alertas
TEXT_DARK  = "#06040D"   # Texto principal oscuro
TEXT_LIGHT = "#FAFAFA"   # Texto secundario, placeholders, bordes, sombras

# Colores derivados
ACCENT_HOVER   = "#651FFF"   # Acento más oscuro para hover
GREEN_HOVER    = "#00B396"   # Verde más oscuro para hover
CORAL_HOVER    = "#E55A5A"   # Coral más oscuro para hover
BG_ENTRY       = "#F0ECFA"   # Fondo sutil para entradas de texto
BORDER_LIGHT   = "#D8D3E8"   # Borde suave para entradas


def aplicar_estilos(style):
    """
    Configura todos los estilos ttk para la aplicación Gastos Vampiro.
    Recibe una instancia de ttk.Style ya creada.
    """

    style.theme_use("clam")

    # ── Frame principal (fondo general) ──────────────────────────────────
    style.configure("Main.TFrame", background=BG_MAIN)

    # ── Header ───────────────────────────────────────────────────────────
    style.configure(
        "Header.TFrame",
        background=ACCENT,
    )

    style.configure(
        "HeaderTitle.TLabel",
        background=ACCENT,
        foreground=BG_ENTRY,
        font=("Segoe UI", 30, "bold"),
    )

    style.configure(
        "HeaderSubTitle.TLabel",
        background=ACCENT,
        foreground=TEXT_LIGHT,
        font=("Segoe UI", 14),
    )

    # ── Tarjeta / Card (formulario, resumen, etc.) ───────────────────────
    style.configure(
        "Card.TFrame",
        background=BG_WHITE,
    )

    # ── Formulario ───────────────────────────────────────────────────────
    style.configure(
        "Card.TLabelframe",
        background=BG_MAIN,
        foreground=TEXT_DARK,
        font=("Segoe UI", 12, "bold"),
        borderwidth=0,
        # relief="groove",
    )

    style.configure(
        "Card.TLabelframe.Label",
        background=BG_MAIN,
        foreground=ACCENT,
        font=("Segoe UI", 12, "bold"),
    )

    style.configure(
        "Card.TLabel",
        background=BG_MAIN,
        foreground=TEXT_DARK,
        font=("Segoe UI", 11),
    )

    style.configure(
        "CardLight.TLabel",
        background=BG_MAIN,
        foreground=TEXT_LIGHT,
        font=("Segoe UI", 10),
    )

    # ── Entradas de texto ────────────────────────────────────────────────
    style.configure(
        "Card.TEntry",
        fieldbackground=BG_WHITE,
        foreground=TEXT_DARK,
        bordercolor=BORDER_LIGHT,
        lightcolor=BORDER_LIGHT,
        darkcolor=BORDER_LIGHT,
        font=("Segoe UI", 12),
        padding=(8, 6),
    )

    style.map(
        "Card.TEntry",
        bordercolor=[("focus", ACCENT)],
        lightcolor=[("focus", ACCENT)],
    )

    # ── Botón Acento (Agregar) ───────────────────────────────────────────
    style.configure(
        "Accent.TButton",
        background=ACCENT,
        foreground="#FFFFFF",
        font=("Segoe UI", 12, "bold"),
        padding=(16, 8),
        borderwidth=0,
    )

    style.map(
        "Accent.TButton",
        background=[("active", ACCENT_HOVER), ("pressed", ACCENT_HOVER)],
        foreground=[("active", "#FFFFFF")],
    )

    # ── Botón Peligro (Eliminar) ─────────────────────────────────────────
    style.configure(
        "Danger.TButton",
        background=CORAL,
        foreground="#FFFFFF",
        font=("Segoe UI", 12, "bold"),
        padding=(16, 8),
        borderwidth=0,
    )

    style.map(
        "Danger.TButton",
        background=[("active", CORAL_HOVER), ("pressed", CORAL_HOVER)],
        foreground=[("active", "#FFFFFF")],
    )

    # ── Botón Secundario (Exportar PDF) ──────────────────────────────────
    style.configure(
        "Secondary.TButton",
        background=GREEN,
        foreground="#FFFFFF",
        font=("Segoe UI", 12, "bold"),
        padding=(16, 8),
        borderwidth=0,
        cursor="hand2",
    )

    style.map(
        "Secondary.TButton",
        background=[("active", GREEN_HOVER), ("pressed", GREEN_HOVER)],
        foreground=[("active", "#FFFFFF")],
    )

    # ── Labels generales sobre fondo principal ───────────────────────────
    style.configure(
        "Main.TLabel",
        background=BG_MAIN,
        foreground=TEXT_DARK,
        font=("Segoe UI", 12),
    )

    style.configure(
        "MainBold.TLabel",
        background=BG_MAIN,
        foreground=TEXT_DARK,
        font=("Segoe UI", 12, "bold"),
    )

    style.configure(
        "TotalLabel.TLabel",
        background=BG_MAIN,
        foreground=ACCENT,
        font=("Segoe UI", 14, "bold"),
    )

    style.configure(
        "Anual.TLabel",
        background=BG_MAIN,
        foreground=TEXT_DARK,
        font=("Segoe UI", 10),
    )

    # ── Treeview (tabla) ─────────────────────────────────────────────────
    style.configure(
        "Treeview",
        background=BG_WHITE,
        foreground=TEXT_DARK,
        fieldbackground=BG_WHITE,
        rowheight=32,
        font=("Segoe UI", 12),
    )

    style.configure(
        "Treeview.Heading",
        background=BG_MAIN,
        foreground=TEXT_DARK,
        font=("Segoe UI", 11, "bold"),
        relief="flat",
    )

    style.map(
        "Treeview",
        background=[("selected", ACCENT)],
        foreground=[("selected", "#FFFFFF")],
    )

    # ── Scrollbar ────────────────────────────────────────────────────────
    style.configure(
        "Vertical.TScrollbar",
        background=BORDER_LIGHT,       # Color del thumb (barra)
        troughcolor=BG_WHITE,          # Fondo del track
        borderwidth=0,
        arrowsize=14,
    )

    style.map(
        "Vertical.TScrollbar",
        background=[
            ("active", ACCENT),        # Hover sobre el thumb
            ("pressed", ACCENT_HOVER), # Click sobre el thumb
        ],
    )
