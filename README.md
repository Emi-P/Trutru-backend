## Levantar el server
Parado en el directorio base ejecutar:

 ``` uvicorn main:app --reload ``` 




## 🧠 Conceptos clave / Estructura de archivos

### GameState
El **GameState** representa el estado completo de una partida en un momento dado.

Incluye, por ejemplo:
- jugadores
- cartas en mano de cada jugador
- cartas en la mesa
- turno actual
- nivel de truco cantado
- puntajes parciales de la partida

📌 **Regla fundamental**:  
El `GameState` **no tiene lógica**, solo datos.  
Es la **única fuente de verdad** del juego.

---

### Acción
Una **acción** es lo que un jugador intenta hacer.

Ejemplos:
- jugar una carta
- cantar truco
- aceptar / rechazar
- irse al mazo

Las acciones:
- vienen del cliente
- no garantizan ser válidas por lo que el motor debe validarlas
- deben ser evaluadas por el motor del juego

---

### GameEngine
El **GameEngine** es el cerebro del juego.

Responsabilidades:
- validar si una acción es legal según el GameState actual
- aplicar las reglas del truco
- generar un **nuevo GameState válido**

📌 Es el **único componente autorizado** a modificar el estado del juego.

---

### GameManager
El **GameManager** es el gestor de partidas activas que existen en el servido.

Responsabilidades:
- mantener todas las partidas en memoria
- mapear `game_id → GameState`
- recibir acciones desde la capa de transporte
- delegar la lógica al `GameEngine`
- actualizar el estado y notificar a los jugadores

📌 Vive mientras el proceso esté activo.

---

## 📂 Detalle de carpetas y archivos

### `app/main.py`
Punto de entrada del backend.

- Inicializa FastAPI
- Crea la instancia global del `GameManager`
- Registra routers HTTP y WebSockets
- Define eventos de startup / shutdown

---

### `app/dependencies.py`
Dependencias compartidas.

- acceso a recursos globales
- autenticación (futuro)
- helpers para inyección de dependencias

No contiene lógica de juego.

---

### `app/routers/`
Endpoints HTTP (REST).

- **No contienen lógica de juego**
- Se usan para:
  - crear partidas
  - unirse a partidas
  - login / usuarios
  - ranking

Archivos:
- `games.py` → operaciones sobre partidas
- `users.py` → usuarios y auth

---

### `app/ws/`
WebSockets para tiempo real.

- Reciben acciones de los jugadores
- Mantienen la conexión viva
- Delegan todo al `GameManager`

Archivo:
- `game.py` → `/ws/game/{game_id}`

---

### `app/game/` — Dominio del juego

Contiene **toda la lógica del truco**.

Nada fuera de este módulo debería conocer las reglas.

#### `state.py`
- Define la estructura del `GameState`
- Solo datos
- Sin validaciones

#### `actions.py`
- Define las acciones posibles del juego
- Contrato entre cliente y servidor
- No aplica reglas

#### `engine.py`
- Implementa las reglas del truco
- Valida acciones
- Produce nuevos estados

---

### `app/services/`

#### `game_manager.py`
- Mantiene las partidas activas en memoria
- Garantiza acceso controlado al estado
- Es la fachada entre transporte y dominio

---

### `app/models/`
Modelos de base de datos (ORM).

- usuarios
- partidas finalizadas
- ranking

📌 No se usan para el estado vivo del juego.

---

### `app/schemas/`
Schemas Pydantic.

- Validan input/output DE LA API
- Separan API pública de modelos internos

---

### `app/db/`
Configuración de base de datos.

- db engine
- sesión
- conexión

---

### `tests/`
Tests automatizados.

- tests del engine
- tests de transiciones de estado
- tests de flujo de acciones

---
