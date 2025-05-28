
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kyan_cosplay"
    )

# ========== Login ==========

class MainMenu(tk.Tk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title(f"Kyan Cosplay - Menú Principal ({user[2].upper()})")
        self.geometry("900x500")
        self.resizable(False, False)
        tk.Label(self, text=f"Bienvenido, {user[1]} ({user[2]})", font=("Arial", 14)).pack(pady=10)

        # Frame principal para los menús en horizontal
        main_frame = tk.Frame(self)
        main_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Menú de Gestión (columna izquierda)
        gestion_frame = tk.LabelFrame(main_frame, text="Menú de Gestión", padx=10, pady=10)
        gestion_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        tk.Button(gestion_frame, text="Gestión de Clientes", width=25, command=self.gestion_clientes).pack(pady=2)
        tk.Button(gestion_frame, text="Gestión de Productos", width=25, command=self.gestion_productos).pack(pady=2)
        tk.Button(gestion_frame, text="Gestión de Talleres", width=25, command=self.gestion_talleres).pack(pady=2)
        tk.Button(gestion_frame, text="Gestión de Eventos", width=25, command=self.gestion_eventos).pack(pady=2)
        tk.Button(gestion_frame, text="Gestión de Proveedores", width=25, command=self.gestion_proveedores).pack(pady=2)
        tk.Button(gestion_frame, text="Gestión de Empresa", width=25, command=self.gestion_empresa).pack(pady=2)
        tk.Button(gestion_frame, text="Facturación y Abonos", width=25, command=self.gestion_facturas).pack(pady=2)
        tk.Button(gestion_frame, text="Pedidos de Compra", width=25, command=self.not_implemented).pack(pady=2)
        tk.Button(gestion_frame, text="Registrar Usuario", width=25, command=self.not_implemented).pack(pady=2)

        # Menú de Consultas (columna derecha)
        consultas_frame = tk.LabelFrame(main_frame, text="Menú de Consultas", padx=10, pady=10)
        consultas_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        tk.Button(consultas_frame, text="Ver Clientes", width=25, command=self.consulta_clientes).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Productos", width=25, command=self.consulta_productos).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Talleres", width=25, command=self.consulta_talleres).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Eventos", width=25, command=self.consulta_eventos).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Proveedores", width=25, command=self.consulta_proveedores).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Empresa", width=25, command=self.consulta_empresa).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Compras", width=25, command=self.not_implemented).pack(pady=2)
        tk.Button(consultas_frame, text="Ver Facturas", width=25, command=self.consulta_facturas).pack(pady=2)
        tk.Button(consultas_frame, text="Estadísticas", width=25, command=self.abrir_estadisticas).pack(pady=2)

        # Ajuste de expansión de columnas
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Cerrar sesión
        tk.Button(self, text="Cerrar Sesión", width=30, command=self.cerrar_sesion).pack(pady=15)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_sesion)

    def cerrar_sesion(self):
        self.destroy()
        LoginWindow().mainloop()

    # Gestión
    def gestion_clientes(self):
        ClientesWindow(self.user, modo_consulta=False)

    def gestion_productos(self):
        ProductosWindow(self.user, modo_consulta=False)
    
    def gestion_talleres(self):
        TalleresWindow(self.user, modo_consulta=False)
    
    def gestion_eventos(self):
        EventosWindow(self.user, modo_consulta=False)

    def gestion_proveedores(self):
        ProveedoresWindow(self.user, modo_consulta=False)

    def gestion_empresa(self):
        EmpresaWindow(self.user, modo_consulta=False)

    def gestion_facturas(self):
        FacturasWindow(self.user, modo_consulta=False)

    # Consultas
    def consulta_clientes(self):
        ClientesWindow(self.user, modo_consulta=True)

    def consulta_productos(self):
        ProductosWindow(self.user, modo_consulta=True)
    
    def consulta_talleres(self):
        TalleresWindow(self.user, modo_consulta=True)
    
    def consulta_eventos(self):
        EventosWindow(self.user, modo_consulta=True)

    def consulta_proveedores(self):
        ProveedoresWindow(self.user, modo_consulta=True)

    def consulta_empresa(self):
        EmpresaWindow(self.user, modo_consulta=True)

    def consulta_facturas(self):
        FacturasWindow(self.user, modo_consulta=True)

    def abrir_estadisticas(self):
        EstadisticasMenuWindow(self.user)


    def not_implemented(self):
        messagebox.showinfo("No implementado", "Esta sección aún no está implementada")



class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kyan Cosplay - Login")
        self.geometry("400x250")
        self.resizable(False, False)

        tk.Label(self, text="Usuario:", font=("Arial", 12)).pack(pady=10)
        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Contraseña:", font=("Arial", 12)).pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Iniciar sesión", command=self.login, font=("Arial", 12)).pack(pady=20)

        self.username_entry.focus_set()
        self.bind('<Return>', lambda event: self.login())

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not username or not password:
            messagebox.showwarning("Faltan datos", "Introduce usuario y contraseña.")
            return

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, username, rol FROM usuarios WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        db.close()
        if user:
            self.destroy()
            MainMenu(user).mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")



class ClientesWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Clientes" if modo_consulta else "Gestión de Clientes")
        self.geometry("900x600")
        self.minsize(700, 400)
        self.resizable(True, True)
        self.modo_consulta = modo_consulta

        # --- Formulario de entrada/edición ---
        form_frame = tk.LabelFrame(self, text="Formulario Cliente")
        form_frame.pack(fill=tk.X, padx=10, pady=5, anchor="n")

        self.campos = ["Nombre", "Apellidos", "Teléfono", "Email"]
        self.entries = {}
        # Primera fila: Nombre, Apellidos, Teléfono, Email
        for i, campo in enumerate(self.campos):
            tk.Label(form_frame, text=campo + ":").grid(row=0, column=i*2, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=0, column=i*2+1, padx=5, pady=3, sticky="we")
            self.entries[campo] = entry

        # Segunda fila: DNI (ocupa toda la fila)
        tk.Label(form_frame, text="DNI:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
        entry_dni = tk.Entry(form_frame, width=22)
        entry_dni.grid(row=1, column=1, padx=5, pady=3, sticky="we")
        self.entries["DNI"] = entry_dni

        # Hacer columnas expandibles
        for i in range(8):
            form_frame.grid_columnconfigure(i, weight=1)

        # --- Botones de acción ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.btn_add = tk.Button(btn_frame, text="Añadir", command=self.agregar_cliente)
        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_cliente)
        self.btn_clear = tk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        self.btn_edit.pack(side=tk.LEFT, padx=5)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=5)

        # --- Tabla de clientes ---
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree = ttk.Treeview(table_frame, columns=("ID", "Nombre", "Apellidos", "Teléfono", "Email", "DNI"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.cargar_clientes()

        if self.modo_consulta:
            self.btn_add.config(state="disabled")
            self.btn_edit.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")

    def cargar_clientes(self):
        db = get_db()
        cursor = db.cursor()
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT id, Nombre, Apellidos, telefono, email, dni FROM clientes")
        for cliente in cursor.fetchall():
            self.tree.insert("", tk.END, values=cliente)
        cursor.close()
        db.close()

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            cliente = self.tree.item(selected[0])["values"]
            for i, campo in enumerate(["Nombre", "Apellidos", "Teléfono", "Email", "DNI"]):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, cliente[i+1])

    def agregar_cliente(self):
        datos = [self.entries[campo].get() for campo in ["Nombre", "Apellidos", "Teléfono", "Email", "DNI"]]
        if not all(datos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO clientes (Nombre, Apellidos, telefono, email, dni) VALUES (%s, %s, %s, %s, %s)",
            tuple(datos)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_clientes()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Cliente añadido correctamente.")

    def editar_cliente(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un cliente para editar.")
            return
        cliente = self.tree.item(selected[0])["values"]
        nuevos = [self.entries[campo].get() for campo in ["Nombre", "Apellidos", "Teléfono", "Email", "DNI"]]
        if not all(nuevos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE clientes SET Nombre=%s, Apellidos=%s, telefono=%s, email=%s, dni=%s WHERE id=%s",
            tuple(nuevos) + (cliente[0],)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_clientes()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")



# ========== Gestión y Consulta de Productos ==========
class ProductosWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Productos" if modo_consulta else "Gestión de Productos")
        self.geometry("900x400")
        self.resizable(False, False)
        self.modo_consulta = modo_consulta
        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"),
            show="headings"
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        if not modo_consulta:
            tk.Button(btn_frame, text="Añadir", command=self.agregar_producto).pack(side=tk.LEFT, padx=5)
            tk.Button(btn_frame, text="Editar", command=self.editar_producto).pack(side=tk.LEFT, padx=5)
            tk.Button(btn_frame, text="Eliminar", command=self.eliminar_producto).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Actualizar", command=self.cargar_productos).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.LEFT, padx=5)
        self.cargar_productos()

    def cargar_productos(self):
        db = get_db()
        cursor = db.cursor()
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT id, tipodeproducto, codigoproducto, precio, iva, stock, descuento, descripcion FROM productos")
        for producto in cursor.fetchall():
            self.tree.insert("", tk.END, values=producto)
        cursor.close()
        db.close()

    def agregar_producto(self):
        campos = ["Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"]
        datos = []
        for campo in campos:
            valor = simpledialog.askstring("Nuevo Producto", f"{campo}:")
            if valor is None:
                return
            datos.append(valor)
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO productos (tipodeproducto, codigoproducto, precio, iva, stock, descuento, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            tuple(datos)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_productos()
        messagebox.showinfo("Éxito", "Producto añadido correctamente.")

    def editar_producto(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un producto para editar.")
            return
        producto = self.tree.item(selected[0])["values"]
        campos = ["Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"]
        nuevos = []
        for i, campo in enumerate(campos):
            valor = simpledialog.askstring("Editar Producto", f"{campo}:", initialvalue=producto[i+1])
            if valor is None:
                return
            nuevos.append(valor)
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE productos SET tipodeproducto=%s, codigoproducto=%s, precio=%s, iva=%s, stock=%s, descuento=%s, descripcion=%s WHERE id=%s",
            tuple(nuevos) + (producto[0],)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_productos()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")

    def eliminar_producto(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un producto para eliminar.")
            return
        producto = self.tree.item(selected[0])["values"]
        if messagebox.askyesno("Confirmar", f"¿Eliminar producto {producto[2]}?"):
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM productos WHERE id = %s", (producto[0],))
            db.commit()
            cursor.close()
            db.close()
            self.cargar_productos()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")


# ========== Gestión y Consulta de Productos ==========
class ProductosWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Productos" if modo_consulta else "Gestión de Productos")
        self.geometry("1100x600")
        self.minsize(900, 400)
        self.resizable(True, True)
        self.modo_consulta = modo_consulta

        # --- Formulario de entrada/edición ---
        form_frame = tk.LabelFrame(self, text="Formulario Producto")
        form_frame.pack(fill=tk.X, padx=10, pady=5, anchor="n")

        self.campos = [
            ("Tipo", 0, 0), ("Código", 0, 2), ("Precio", 0, 4), ("IVA", 0, 6),
            ("Stock", 1, 0), ("Descuento", 1, 2), ("Descripción", 1, 4)
        ]
        self.entries = {}
        for campo, row, col in self.campos:
            tk.Label(form_frame, text=campo + ":").grid(row=row, column=col, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=row, column=col+1, padx=5, pady=3, sticky="we")
            self.entries[campo] = entry

        # Hacer columnas expandibles
        for i in range(8):
            form_frame.grid_columnconfigure(i, weight=1)

        # --- Botones de acción ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.btn_add = tk.Button(btn_frame, text="Añadir", command=self.agregar_producto)
        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_producto)
        self.btn_clear = tk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        self.btn_edit.pack(side=tk.LEFT, padx=5)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=5)

        # --- Tabla de productos ---
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"),
            show="headings"
        )
        for col, width in zip(self.tree["columns"], [60, 120, 120, 90, 60, 80, 90, 300]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.cargar_productos()

        if self.modo_consulta:
            self.btn_add.config(state="disabled")
            self.btn_edit.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")

    def cargar_productos(self):
        db = get_db()
        cursor = db.cursor()
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT id, tipodeproducto, codigoproducto, precio, iva, stock, descuento, descripcion FROM productos")
        for producto in cursor.fetchall():
            self.tree.insert("", tk.END, values=producto)
        cursor.close()
        db.close()

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            producto = self.tree.item(selected[0])["values"]
            for i, campo in enumerate(["Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"]):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, producto[i+1])

    def agregar_producto(self):
        datos = [self.entries[campo].get() for campo in ["Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"]]
        if not all(datos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO productos (tipodeproducto, codigoproducto, precio, iva, stock, descuento, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            tuple(datos)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_productos()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Producto añadido correctamente.")

    def editar_producto(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un producto para editar.")
            return
        producto = self.tree.item(selected[0])["values"]
        nuevos = [self.entries[campo].get() for campo in ["Tipo", "Código", "Precio", "IVA", "Stock", "Descuento", "Descripción"]]
        if not all(nuevos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE productos SET tipodeproducto=%s, codigoproducto=%s, precio=%s, iva=%s, stock=%s, descuento=%s, descripcion=%s WHERE id=%s",
            tuple(nuevos) + (producto[0],)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_productos()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")



# ========== Gestión y Consulta de Talleres ==========
class TalleresWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Talleres" if modo_consulta else "Gestión de Talleres")
        self.geometry("1100x600")
        self.minsize(900, 400)
        self.resizable(True, True)
        self.modo_consulta = modo_consulta

        # --- Formulario de entrada/edición ---
        form_frame = tk.LabelFrame(self, text="Formulario Taller")
        form_frame.pack(fill=tk.X, padx=10, pady=5, anchor="n")

        self.campos = [
            ("Nombre", 0, 0), ("Día (YYYY-MM-DD)", 0, 2), ("Hora (HH:MM:SS)", 0, 4), ("Plazas Totales", 0, 6),
            ("Precio", 1, 0), ("IVA", 1, 2), ("Descuento", 1, 4)
        ]
        self.entries = {}
        for campo, row, col in self.campos:
            tk.Label(form_frame, text=campo + ":").grid(row=row, column=col, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=row, column=col+1, padx=5, pady=3, sticky="we")
            self.entries[campo] = entry

        for i in range(8):
            form_frame.grid_columnconfigure(i, weight=1)

        # --- Botones de acción ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.btn_add = tk.Button(btn_frame, text="Añadir", command=self.agregar_taller)
        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_taller)
        self.btn_clear = tk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        self.btn_edit.pack(side=tk.LEFT, padx=5)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=5)

        # --- Tabla de talleres ---
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Nombre", "Día", "Hora", "Plazas Totales", "Precio", "IVA", "Descuento"),
            show="headings"
        )
        for col, width in zip(self.tree["columns"], [60, 180, 120, 100, 120, 90, 60, 90]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.cargar_talleres()

        if self.modo_consulta:
            self.btn_add.config(state="disabled")
            self.btn_edit.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")

    def cargar_talleres(self):
        db = get_db()
        cursor = db.cursor()
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT id, nombretaller, dia, hora, plazastotales, precio, iva, descuento FROM talleres")
        for taller in cursor.fetchall():
            self.tree.insert("", tk.END, values=taller)
        cursor.close()
        db.close()

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            taller = self.tree.item(selected[0])["values"]
            for i, campo in enumerate(["Nombre", "Día (YYYY-MM-DD)", "Hora (HH:MM:SS)", "Plazas Totales", "Precio", "IVA", "Descuento"]):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, taller[i+1])

    def agregar_taller(self):
        datos = [self.entries[campo].get() for campo in ["Nombre", "Día (YYYY-MM-DD)", "Hora (HH:MM:SS)", "Plazas Totales", "Precio", "IVA", "Descuento"]]
        if not all(datos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO talleres (nombretaller, dia, hora, plazastotales, precio, iva, descuento) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            tuple(datos)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_talleres()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Taller añadido correctamente.")

    def editar_taller(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un taller para editar.")
            return
        taller = self.tree.item(selected[0])["values"]
        nuevos = [self.entries[campo].get() for campo in ["Nombre", "Día (YYYY-MM-DD)", "Hora (HH:MM:SS)", "Plazas Totales", "Precio", "IVA", "Descuento"]]
        if not all(nuevos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE talleres SET nombretaller=%s, dia=%s, hora=%s, plazastotales=%s, precio=%s, iva=%s, descuento=%s WHERE id=%s",
            tuple(nuevos) + (taller[0],)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_talleres()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Taller actualizado correctamente.")

# ========== Gestión y Consulta de Eventos ==========
class EventosWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Eventos" if modo_consulta else "Gestión de Eventos")
        self.geometry("900x500")
        self.minsize(700, 400)
        self.resizable(True, True)
        self.modo_consulta = modo_consulta

        # --- Formulario de entrada/edición ---
        form_frame = tk.LabelFrame(self, text="Formulario Evento")
        form_frame.pack(fill=tk.X, padx=10, pady=5, anchor="n")

        self.campos = [
            ("Nombre", 0, 0), ("Fecha (YYYY-MM-DD)", 0, 2), ("Horario (HH:MM:SS)", 0, 4),
            ("Precio", 1, 0), ("IVA", 1, 2)
        ]
        self.entries = {}
        for campo, row, col in self.campos:
            tk.Label(form_frame, text=campo + ":").grid(row=row, column=col, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=row, column=col+1, padx=5, pady=3, sticky="we")
            self.entries[campo] = entry

        for i in range(6):
            form_frame.grid_columnconfigure(i, weight=1)

        # --- Botones de acción ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.btn_add = tk.Button(btn_frame, text="Añadir", command=self.agregar_evento)
        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_evento)
        self.btn_clear = tk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        self.btn_edit.pack(side=tk.LEFT, padx=5)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=5)

        # --- Tabla de eventos ---
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Nombre", "Fecha", "Horario", "Precio", "IVA"),
            show="headings"
        )
        for col, width in zip(self.tree["columns"], [60, 180, 120, 100, 90, 60]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.cargar_eventos()

        if self.modo_consulta:
            self.btn_add.config(state="disabled")
            self.btn_edit.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")

    def cargar_eventos(self):
        db = get_db()
        cursor = db.cursor()
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT id, nombre, fecha, horario, precio, iva FROM eventos")
        for evento in cursor.fetchall():
            self.tree.insert("", tk.END, values=evento)
        cursor.close()
        db.close()

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            evento = self.tree.item(selected[0])["values"]
            for i, campo in enumerate(["Nombre", "Fecha (YYYY-MM-DD)", "Horario (HH:MM:SS)", "Precio", "IVA"]):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, evento[i+1])

    def agregar_evento(self):
        datos = [self.entries[campo].get() for campo in ["Nombre", "Fecha (YYYY-MM-DD)", "Horario (HH:MM:SS)", "Precio", "IVA"]]
        if not all(datos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO eventos (nombre, fecha, horario, precio, iva) VALUES (%s, %s, %s, %s, %s)",
            tuple(datos)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_eventos()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Evento añadido correctamente.")

    def editar_evento(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un evento para editar.")
            return
        evento = self.tree.item(selected[0])["values"]
        nuevos = [self.entries[campo].get() for campo in ["Nombre", "Fecha (YYYY-MM-DD)", "Horario (HH:MM:SS)", "Precio", "IVA"]]
        if not all(nuevos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE eventos SET nombre=%s, fecha=%s, horario=%s, precio=%s, iva=%s WHERE id=%s",
            tuple(nuevos) + (evento[0],)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_eventos()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Evento actualizado correctamente.")

class ProveedoresWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Proveedores" if modo_consulta else "Gestión de Proveedores")
        self.geometry("1200x600")
        self.minsize(1000, 400)
        self.resizable(True, True)
        self.modo_consulta = modo_consulta

        # --- Formulario de entrada/edición ---
        form_frame = tk.LabelFrame(self, text="Formulario Proveedor")
        form_frame.pack(fill=tk.X, padx=10, pady=5, anchor="n")

        self.campos = [
            ("Nombre y Apellidos", 0, 0), ("Razón Social", 0, 2), ("Dirección", 0, 4), ("Email", 0, 6),
            ("Teléfono", 1, 0), ("CIF", 1, 2), ("Cuenta Bancaria", 1, 4), ("IVA", 1, 6),
            ("Medio de Pago", 2, 0), ("Moneda", 2, 2)
        ]
        self.entries = {}
        for campo, row, col in self.campos:
            tk.Label(form_frame, text=campo + ":").grid(row=row, column=col, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=row, column=col+1, padx=5, pady=3, sticky="we")
            self.entries[campo] = entry

        for i in range(8):
            form_frame.grid_columnconfigure(i, weight=1)

        # --- Botones de acción ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.btn_add = tk.Button(btn_frame, text="Añadir", command=self.agregar_proveedor)
        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_proveedor)
        self.btn_clear = tk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario)
        self.btn_add.pack(side=tk.LEFT, padx=5)
        self.btn_edit.pack(side=tk.LEFT, padx=5)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=5)

        # --- Tabla de proveedores ---
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Nombre y Apellidos", "Razón Social", "Dirección", "Email", "Teléfono", "CIF", "Cuenta Bancaria", "IVA", "Medio de Pago", "Moneda"),
            show="headings"
        )
        for col, width in zip(self.tree["columns"], [60, 150, 150, 180, 150, 100, 100, 150, 60, 120, 80]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.cargar_proveedores()

        if self.modo_consulta:
            self.btn_add.config(state="disabled")
            self.btn_edit.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")

    def cargar_proveedores(self):
        db = get_db()
        cursor = db.cursor()
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT id, nombreapellidos, razonsocial, direccion, email, telefono, cif, cuentabancaria, iva, mediodepago, moneda FROM proveedores")
        for proveedor in cursor.fetchall():
            self.tree.insert("", tk.END, values=proveedor)
        cursor.close()
        db.close()

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            proveedor = self.tree.item(selected[0])["values"]
            for i, campo in enumerate([
                "Nombre y Apellidos", "Razón Social", "Dirección", "Email", "Teléfono",
                "CIF", "Cuenta Bancaria", "IVA", "Medio de Pago", "Moneda"
            ]):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, proveedor[i+1])

    def agregar_proveedor(self):
        datos = [self.entries[campo].get() for campo in [
            "Nombre y Apellidos", "Razón Social", "Dirección", "Email", "Teléfono",
            "CIF", "Cuenta Bancaria", "IVA", "Medio de Pago", "Moneda"
        ]]
        if not all(datos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO proveedores (nombreapellidos, razonsocial, direccion, email, telefono, cif, cuentabancaria, iva, mediodepago, moneda) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(datos)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_proveedores()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Proveedor añadido correctamente.")

    def editar_proveedor(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un proveedor para editar.")
            return
        proveedor = self.tree.item(selected[0])["values"]
        nuevos = [self.entries[campo].get() for campo in [
            "Nombre y Apellidos", "Razón Social", "Dirección", "Email", "Teléfono",
            "CIF", "Cuenta Bancaria", "IVA", "Medio de Pago", "Moneda"
        ]]
        if not all(nuevos):
            messagebox.showwarning("Faltan datos", "Completa todos los campos.")
            return
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE proveedores SET nombreapellidos=%s, razonsocial=%s, direccion=%s, email=%s, telefono=%s, cif=%s, cuentabancaria=%s, iva=%s, mediodepago=%s, moneda=%s WHERE id=%s",
            tuple(nuevos) + (proveedor[0],)
        )
        db.commit()
        cursor.close()
        db.close()
        self.cargar_proveedores()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")


# ========== Gestión y Consulta de Empresa ==========
class EmpresaWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Empresa" if modo_consulta else "Gestión de Empresa")
        self.geometry("700x400")
        self.resizable(False, False)
        self.modo_consulta = modo_consulta

        # Campos de la empresa
        self.campos = [
            "Nombre", "Dirección", "Teléfono", "Email", "CIF",
            "Código Postal", "Población", "Cuenta Bancaria", "Forma de Pago"
        ]
        self.entries = {}

        # Frame de formulario
        form_frame = tk.Frame(self)
        form_frame.pack(pady=20)

        for i, campo in enumerate(self.campos):
            tk.Label(form_frame, text=campo + ":").grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[campo] = entry

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        if not modo_consulta:
            tk.Button(btn_frame, text="Guardar", command=self.guardar_empresa).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.LEFT, padx=5)

        self.cargar_empresa()

        if modo_consulta:
            for entry in self.entries.values():
                entry.config(state="readonly")

    def cargar_empresa(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT nombre, direccion, telefono, email, cif, codigopostal, poblacion, cuentabancaria, formapago FROM empresa LIMIT 1")
        empresa = cursor.fetchone()
        if empresa:
            for i, campo in enumerate(self.campos):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, empresa[i])
        cursor.close()
        db.close()

    def guardar_empresa(self):
        valores = [self.entries[campo].get() for campo in self.campos]
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id FROM empresa LIMIT 1")
        empresa = cursor.fetchone()
        if empresa:
            cursor.execute(
                "UPDATE empresa SET nombre=%s, direccion=%s, telefono=%s, email=%s, cif=%s, codigopostal=%s, poblacion=%s, cuentabancaria=%s, formapago=%s WHERE id=%s",
                tuple(valores) + (empresa[0],)
            )
        else:
            cursor.execute(
                "INSERT INTO empresa (nombre, direccion, telefono, email, cif, codigopostal, poblacion, cuentabancaria, formapago) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                tuple(valores)
            )
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Éxito", "Datos de empresa guardados correctamente.")


class FacturasWindow(tk.Toplevel):
    def __init__(self, user, modo_consulta=False):
        super().__init__()
        self.title("Facturación y Abonos" if not modo_consulta else "Consulta de Facturas")
        self.geometry("1200x700")
        self.resizable(True, True)
        self.modo_consulta = modo_consulta

        # --- Variables de cabecera ---
        self.tipo_dest_var = tk.StringVar(value="cliente")
        self.destinatario_var = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.direccion_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.doc_var = tk.StringVar()
        self.forma_pago_var = tk.StringVar()
        self.observaciones_var = tk.StringVar()

        # --- Frame Cabecera ---
        cabecera = tk.LabelFrame(self, text="Cabecera de Factura")
        cabecera.pack(fill=tk.X, padx=10, pady=5)

        # Tipo destinatario
        tk.Label(cabecera, text="Tipo:").grid(row=0, column=0, sticky="e")
        tk.Radiobutton(cabecera, text="Cliente", variable=self.tipo_dest_var, value="cliente", command=self.actualizar_lista_destinatarios).grid(row=0, column=1)
        tk.Radiobutton(cabecera, text="Proveedor", variable=self.tipo_dest_var, value="proveedor", command=self.actualizar_lista_destinatarios).grid(row=0, column=2)

        # Destinatario
        tk.Label(cabecera, text="Destinatario:").grid(row=0, column=3, sticky="e")
        self.combo_dest = ttk.Combobox(cabecera, textvariable=self.destinatario_var, width=40, state="readonly")
        self.combo_dest.grid(row=0, column=4, padx=5)
        self.combo_dest.bind("<<ComboboxSelected>>", self.cargar_datos_destinatario)

        # Fecha
        tk.Label(cabecera, text="Fecha (YYYY-MM-DD):").grid(row=0, column=5, sticky="e")
        self.fecha_entry = tk.Entry(cabecera, textvariable=self.fecha_var, width=12)
        self.fecha_entry.grid(row=0, column=6, padx=5)
        from datetime import date
        self.fecha_var.set(str(date.today()))

        # Dirección, Email, Teléfono, Documento (SOLO VISUALIZACIÓN)
        tk.Label(cabecera, text="Dirección:").grid(row=1, column=0, sticky="e")
        self.entry_direccion = tk.Entry(cabecera, textvariable=self.direccion_var, width=40, state="readonly")
        self.entry_direccion.grid(row=1, column=1, columnspan=2, padx=5)
        tk.Label(cabecera, text="Email:").grid(row=1, column=3, sticky="e")
        self.entry_email = tk.Entry(cabecera, textvariable=self.email_var, width=30, state="readonly")
        self.entry_email.grid(row=1, column=4, padx=5)
        tk.Label(cabecera, text="Teléfono:").grid(row=1, column=5, sticky="e")
        self.entry_telefono = tk.Entry(cabecera, textvariable=self.telefono_var, width=15, state="readonly")
        self.entry_telefono.grid(row=1, column=6, padx=5)
        tk.Label(cabecera, text="DNI/CIF:").grid(row=2, column=0, sticky="e")
        self.entry_doc = tk.Entry(cabecera, textvariable=self.doc_var, width=20, state="readonly")
        self.entry_doc.grid(row=2, column=1, padx=5)

        # Forma de pago y observaciones (EDITABLES)
        tk.Label(cabecera, text="Forma de Pago:").grid(row=2, column=2, sticky="e")
        tk.Entry(cabecera, textvariable=self.forma_pago_var, width=20).grid(row=2, column=3, padx=5)
        tk.Label(cabecera, text="Observaciones:").grid(row=2, column=4, sticky="e")
        tk.Entry(cabecera, textvariable=self.observaciones_var, width=40).grid(row=2, column=5, columnspan=2, padx=5)

        # --- Frame Líneas de Factura ---
        lineas_frame = tk.LabelFrame(self, text="Líneas de Factura")
        lineas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Tabla de líneas
        self.lineas_tree = ttk.Treeview(lineas_frame, columns=("Producto", "Descripción", "Cantidad", "Precio", "IVA", "Descuento", "Total línea"), show="headings", height=8)
        for col in self.lineas_tree["columns"]:
            self.lineas_tree.heading(col, text=col)
            self.lineas_tree.column(col, width=120)
        self.lineas_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Scrollbar
        scrollbar = ttk.Scrollbar(lineas_frame, orient="vertical", command=self.lineas_tree.yview)
        self.lineas_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Frame para añadir línea
        add_linea_frame = tk.Frame(lineas_frame)
        add_linea_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Selección de producto
        tk.Label(add_linea_frame, text="Producto:").pack()
        self.producto_var = tk.StringVar()
        self.combo_producto = ttk.Combobox(add_linea_frame, textvariable=self.producto_var, width=30, state="readonly")
        self.combo_producto.pack()
        self.combo_producto.bind("<<ComboboxSelected>>", self.autocompletar_producto)

        tk.Label(add_linea_frame, text="Cantidad:").pack()
        self.cantidad_var = tk.StringVar(value="1")
        tk.Entry(add_linea_frame, textvariable=self.cantidad_var, width=10).pack()

        tk.Label(add_linea_frame, text="Precio:").pack()
        self.precio_var = tk.StringVar()
        tk.Entry(add_linea_frame, textvariable=self.precio_var, width=10, state="readonly").pack()

        tk.Label(add_linea_frame, text="IVA (%):").pack()
        self.iva_var = tk.StringVar()
        tk.Entry(add_linea_frame, textvariable=self.iva_var, width=10, state="readonly").pack()

        tk.Label(add_linea_frame, text="Descuento (%):").pack()
        self.descuento_var = tk.StringVar(value="0")
        tk.Entry(add_linea_frame, textvariable=self.descuento_var, width=10, state="readonly").pack()

        tk.Button(add_linea_frame, text="Añadir línea", command=self.agregar_linea).pack(pady=10)
        tk.Button(add_linea_frame, text="Eliminar línea seleccionada", command=self.eliminar_linea).pack(pady=2)

        # --- Botones de acción ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        self.btn_guardar = tk.Button(btn_frame, text="Guardar Factura", command=self.guardar_factura)
        self.btn_guardar.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=5)

        # --- Inicialización ---
        self.productos_db = []
        self.lineas = []
        self.actualizar_lista_destinatarios()
        self.cargar_productos()

        # Seleccionar automáticamente el primer destinatario si hay datos
        if self.combo_dest["values"]:
            self.combo_dest.current(0)
            self.cargar_datos_destinatario()

        # Seleccionar automáticamente el primer producto si hay datos
        if self.combo_producto["values"]:
            self.combo_producto.current(0)
            self.autocompletar_producto()

        if self.modo_consulta:
            self.btn_guardar.config(state="disabled")
            for widget in cabecera.winfo_children():
                widget.config(state="disabled")
            for widget in add_linea_frame.winfo_children():
                widget.config(state="disabled")

    def actualizar_lista_destinatarios(self):
        db = get_db()
        cursor = db.cursor()
        if self.tipo_dest_var.get() == "cliente":
            cursor.execute("SELECT id, Nombre, Apellidos, direccion, email, telefono, dni FROM clientes")
            self.destinatarios = cursor.fetchall()
            lista = [f"{c[0]} - {c[1]} {c[2]}" for c in self.destinatarios]
        else:
            cursor.execute("SELECT id, razonsocial, direccion, email, telefono, cif FROM proveedores")
            self.destinatarios = cursor.fetchall()
            lista = [f"{p[0]} - {p[1]}" for p in self.destinatarios]
        self.combo_dest["values"] = lista
        # Selecciona automáticamente el primero si hay datos
        if lista:
            self.combo_dest.current(0)
            self.cargar_datos_destinatario()
        else:
            self.combo_dest.set("")
            self.direccion_var.set("")
            self.email_var.set("")
            self.telefono_var.set("")
            self.doc_var.set("")
        cursor.close()
        db.close()

    def cargar_datos_destinatario(self, event=None):
        idx = self.combo_dest.current()
        if idx == -1 or not self.destinatarios:
            return
        datos = self.destinatarios[idx]
        if self.tipo_dest_var.get() == "cliente":
            self.direccion_var.set(datos[3])
            self.email_var.set(datos[4])
            self.telefono_var.set(datos[5])
            self.doc_var.set(datos[6])
        else:
            self.direccion_var.set(datos[2])
            self.email_var.set(datos[3])
            self.telefono_var.set(datos[4])
            self.doc_var.set(datos[5])

    def cargar_productos(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, descripcion, precio, iva, descuento FROM productos")
        self.productos_db = cursor.fetchall()
        lista = [f"{p[0]} - {p[1]}" for p in self.productos_db]
        self.combo_producto["values"] = lista
        # Selecciona automáticamente el primero si hay datos
        if lista:
            self.combo_producto.current(0)
            self.autocompletar_producto()
        else:
            self.combo_producto.set("")
            self.precio_var.set("")
            self.iva_var.set("")
            self.descuento_var.set("")
        cursor.close()
        db.close()

    def autocompletar_producto(self, event=None):
        idx = self.combo_producto.current()
        if idx == -1 or not self.productos_db:
            return
        prod = self.productos_db[idx]
        self.precio_var.set(str(prod[2]))
        self.iva_var.set(str(prod[3]))
        self.descuento_var.set(str(prod[4]))

    def agregar_linea(self):
        idx = self.combo_producto.current()
        if idx == -1 or not self.productos_db:
            messagebox.showwarning("Producto", "Selecciona un producto.")
            return
        prod = self.productos_db[idx]
        try:
            cantidad = float(self.cantidad_var.get())
            precio = float(self.precio_var.get())
            iva = float(self.iva_var.get())
            descuento = float(self.descuento_var.get())
        except Exception:
            messagebox.showwarning("Datos", "Cantidad, precio, IVA y descuento deben ser numéricos.")
            return
        precio_desc = precio * (1 - descuento/100)
        total_linea = round(precio_desc * cantidad * (1 + iva/100), 2)
        self.lineas.append({
            "id_producto": prod[0],
            "descripcion": prod[1],
            "cantidad": cantidad,
            "precio": precio,
            "iva": iva,
            "descuento": descuento,
            "total_linea": total_linea
        })
        self.lineas_tree.insert("", tk.END, values=(prod[0], prod[1], cantidad, precio, iva, descuento, total_linea))

    def eliminar_linea(self):
        selected = self.lineas_tree.selection()
        if not selected:
            return
        idx = self.lineas_tree.index(selected[0])
        self.lineas_tree.delete(selected[0])
        del self.lineas[idx]

    def guardar_factura(self):
        # Validación de cabecera
        if not self.combo_dest.get():
            messagebox.showwarning("Faltan datos", "Selecciona un destinatario.")
            return
        if not self.fecha_var.get():
            messagebox.showwarning("Faltan datos", "Introduce la fecha.")
            return
        if not self.lineas:
            messagebox.showwarning("Faltan datos", "Añade al menos una línea de producto.")
            return

        db = get_db()
        cursor = db.cursor()
        # Calcular siguiente número de factura
        cursor.execute("SELECT MAX(numfac) FROM cabfac")
        max_numfac = cursor.fetchone()[0]
        numfac = (max_numfac or 0) + 1

        # Insertar cabecera
        tipo_dest = self.tipo_dest_var.get()
        idcliente = None
        idproveedor = None
        if tipo_dest == "cliente":
            idcliente = self.destinatarios[self.combo_dest.current()][0]
        else:
            idproveedor = self.destinatarios[self.combo_dest.current()][0]

        cursor.execute("""
            INSERT INTO cabfac (
                numfac, tipo_destinatario, idcliente, idproveedor,
                nombre_destinatario, direccion_destinatario, email_destinatario, telefono_destinatario, doc_destinatario,
                fecha, tipo, formapago, observaciones
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            numfac,
            tipo_dest,
            idcliente,
            idproveedor,
            self.combo_dest.get(),
            self.direccion_var.get(),
            self.email_var.get(),
            self.telefono_var.get(),
            self.doc_var.get(),
            self.fecha_var.get(),
            "F",
            self.forma_pago_var.get(),
            self.observaciones_var.get()
        ))
        db.commit()

        # Insertar líneas
        for l in self.lineas:
            cursor.execute("""
                INSERT INTO linfac (numfac, id_producto, descripcion, precio, unidad, iva, descuento, total_linea)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                numfac, l["id_producto"], l["descripcion"], l["precio"],
                l["cantidad"], l["iva"], l["descuento"], l["total_linea"]
            ))
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Éxito", f"Factura {numfac} guardada correctamente.")
        self.destroy()

class EstadisticasMenuWindow(tk.Toplevel):
    def __init__(self, user):
        super().__init__()
        self.title("Estadísticas")
        self.geometry("900x600")
        self.user = user

        # Notebook para pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear pestañas para cada estadística
        self.tabs = []
        for i, nombre in enumerate([
            "Productos más vendidos (TOP 10)",
            "Total de clientes y listado",
            "Proveedores por compras realizadas",
            "Productos con menos stock (TOP 10)",
            "Ventas por mes (últimos 12 meses)",
            "Clientes que más compran (TOP 10)",
            "Proveedores con mejor precio medio"
        ]):
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=f"{i+1}. {nombre}")
            self.tabs.append(frame)

        # Llamar a los métodos de carga de datos
        self.cargar_productos_mas_vendidos(self.tabs[0])
        self.cargar_clientes_listado(self.tabs[1])
        self.cargar_proveedores_por_compras(self.tabs[2])
        self.cargar_productos_menos_stock(self.tabs[3])
        self.cargar_ventas_por_mes(self.tabs[4])
        self.cargar_clientes_mas_compran(self.tabs[5])
        self.cargar_proveedores_mejor_precio(self.tabs[6])

    def cargar_productos_mas_vendidos(self, frame):
        tree = ttk.Treeview(frame, columns=("Descripción", "Total Vendido"), show="headings")
        tree.heading("Descripción", text="Descripción")
        tree.heading("Total Vendido", text="Total Vendido")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT pr.descripcion, SUM(l.unidad) as total_vendido
            FROM linfac l
            JOIN productos pr ON l.id_producto = pr.id
            GROUP BY l.id_producto
            ORDER BY total_vendido DESC
            LIMIT 10
        """)
        for desc, total in cursor.fetchall():
            tree.insert("", tk.END, values=(desc, total))
        cursor.close()
        db.close()

    def cargar_clientes_listado(self, frame):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM clientes")
        nclientes = cursor.fetchone()[0]
        label = tk.Label(frame, text=f"Total de clientes registrados: {nclientes}", font=("Arial", 12, "bold"))
        label.pack(pady=10)
        tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Apellidos", "Email"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        cursor.execute("SELECT id, Nombre, Apellidos, email FROM clientes ORDER BY id")
        for c in cursor.fetchall():
            tree.insert("", tk.END, values=c)
        cursor.close()
        db.close()

    def cargar_proveedores_por_compras(self, frame):
        tree = ttk.Treeview(frame, columns=("ID", "Razón Social", "Compras Realizadas"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.razonsocial, COUNT(c.id) as compras_realizadas
            FROM proveedores p
            LEFT JOIN compras c ON p.id = c.id_proveedor
            GROUP BY p.id
            ORDER BY compras_realizadas DESC
        """)
        for pid, nombre, compras in cursor.fetchall():
            tree.insert("", tk.END, values=(pid, nombre, compras))
        cursor.close()
        db.close()

    def cargar_productos_menos_stock(self, frame):
        tree = ttk.Treeview(frame, columns=("Descripción", "Stock"), show="headings")
        tree.heading("Descripción", text="Descripción")
        tree.heading("Stock", text="Stock")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT descripcion, stock
            FROM productos
            ORDER BY stock ASC
            LIMIT 10
        """)
        for desc, stock in cursor.fetchall():
            tree.insert("", tk.END, values=(desc, stock))
        cursor.close()
        db.close()

    def cargar_ventas_por_mes(self, frame):
        tree = ttk.Treeview(frame, columns=("Mes", "Total Ventas (€)"), show="headings")
        tree.heading("Mes", text="Mes")
        tree.heading("Total Ventas (€)", text="Total Ventas (€)")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT DATE_FORMAT(cabfac.fecha, '%Y-%m') as mes, SUM(linfac.total_linea) as total_ventas
            FROM cabfac
            JOIN linfac ON cabfac.numfac = linfac.numfac
            WHERE cabfac.tipo = 'F'
            GROUP BY mes
            ORDER BY mes DESC
            LIMIT 12
        """)
        for mes, total in cursor.fetchall():
            tree.insert("", tk.END, values=(mes, f"{total:.2f}"))
        cursor.close()
        db.close()

    def cargar_clientes_mas_compran(self, frame):
        tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Apellidos", "Total Gastado (€)"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT c.id, c.Nombre, c.Apellidos, SUM(linfac.total_linea) as total_gastado
            FROM cabfac
            JOIN clientes c ON cabfac.idcliente = c.id
            JOIN linfac ON cabfac.numfac = linfac.numfac
            WHERE cabfac.tipo = 'F'
            GROUP BY c.id
            ORDER BY total_gastado DESC
            LIMIT 10
        """)
        for cid, nombre, apellidos, total in cursor.fetchall():
            tree.insert("", tk.END, values=(cid, nombre, apellidos, f"{total:.2f}"))
        cursor.close()
        db.close()

    def cargar_proveedores_mejor_precio(self, frame):
        tree = ttk.Treeview(frame, columns=("ID", "Razón Social", "Precio Medio (€)"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.razonsocial, AVG(d.precio_unitario) as precio_medio
            FROM compras_detalle d
            JOIN compras c ON d.id_compra = c.id
            JOIN proveedores p ON c.id_proveedor = p.id
            GROUP BY p.id
            HAVING COUNT(d.id) > 0
            ORDER BY precio_medio ASC
            LIMIT 10
        """)
        for pid, nombre, precio in cursor.fetchall():
            tree.insert("", tk.END, values=(pid, nombre, f"{precio:.2f}"))
        cursor.close()
        db.close()


# ========== Punto de entrada ==========
if __name__ == "__main__":
    LoginWindow().mainloop()
