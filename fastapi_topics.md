As a **~3 years experienced developer**, interviewers usually expect you to know **FastAPI beyond basic CRUD**. You should be comfortable with architecture, async behavior, security, and production concerns.

Here’s a **structured list of FastAPI topics you should definitely know** 👇

---

# 1. FastAPI Fundamentals

These are expected basics.

* What **FastAPI** is and why it's fast
* ASGI vs WSGI
* Request handling
* Path parameters
* Query parameters
* Request body
* Response models
* Status codes
* Automatic docs (Swagger / ReDoc)

Also know how FastAPI uses **Pydantic** for validation.

---

# 2. Async Programming (Very Important)

FastAPI is built on **async architecture**.

You should understand:

* `async def` vs `def`
* `await`
* Non-blocking IO
* Event loop basics
* When to use sync vs async endpoints
* Background tasks
* Concurrency vs parallelism

FastAPI runs on **Starlette** and **Uvicorn**, so knowing their role helps.

---

# 3. Dependency Injection

FastAPI’s **dependency system** is heavily used.

Topics:

* `Depends()`
* Reusable dependencies
* Dependency chains
* Database session injection
* Authentication dependencies
* Caching dependencies

Example:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

# 4. Data Validation & Serialization

Using **Pydantic**

You should know:

* BaseModel
* Field validation
* Custom validators
* Nested models
* Optional fields
* Model inheritance
* Response models
* ORM mode

---

# 5. Database Integration

Common patterns with:

* **SQLAlchemy**
* **Alembic**

Topics:

* Session management
* CRUD pattern
* Async SQLAlchemy
* Database migrations
* Connection pooling

---

# 6. Authentication & Security

Very common interview topic.

You should know:

* OAuth2
* JWT authentication
* Password hashing
* API key authentication
* Role-based access

FastAPI utilities:

* `OAuth2PasswordBearer`
* Security dependencies

Libraries often used:

* **python-jose**
* **Passlib**

---

# 7. Middleware

Understand how middleware works.

Examples:

* Logging middleware
* CORS middleware
* Request timing
* Authentication middleware

Example:

```python
@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    return response
```

---

# 8. Background Tasks

Running tasks after response.

FastAPI feature:

```python
BackgroundTasks
```

Example uses:

* sending email
* processing files
* logging

---

# 9. Error Handling

Know how to handle errors properly.

Topics:

* `HTTPException`
* Custom exception handlers
* Validation errors

Example:

```python
raise HTTPException(status_code=404, detail="User not found")
```

---

# 10. API Versioning & Routing

For large projects:

* APIRouter
* Router prefixes
* Tags
* Versioning

Example:

```python
router = APIRouter(prefix="/users")
```

---

# 11. Testing FastAPI

Very important for mid-level developers.

Using:

* **pytest**
* **TestClient**

Topics:

* Unit testing endpoints
* Dependency overrides
* Mock database

---

# 12. Performance Optimization

You should know:

* async database calls
* caching
* response model optimization
* connection pooling
* streaming responses

Caching tools sometimes used:

* **Redis**

---

# 13. Deployment & Production

Important for experienced devs.

You should know:

* Running with **Uvicorn**
* Running with **Gunicorn**
* Dockerizing FastAPI apps
* Environment variables
* Logging
* Reverse proxy with **Nginx**

---

# 14. WebSockets

FastAPI also supports real-time communication.

Example uses:

* chat apps
* notifications
* live dashboards

Uses **Starlette** WebSocket support.

---

# 15. Project Architecture (Very Important for 3+ years dev)

Interviewers expect good structure.

Typical structure:

```
app/
  main.py
  routers/
  models/
  schemas/
  services/
  dependencies/
  core/
  db/
```

Concepts:

* separation of concerns
* service layer
* repository pattern
* clean architecture

---

✅ **If you know these topics well, you're already strong for mid-level FastAPI roles.**

---

💡 If you want, I can also show:

* **Top 25 FastAPI interview questions for 3+ years devs**
* **A production-level FastAPI project structure**
* **Advanced FastAPI topics (things most developers miss)**

These are the things that **actually differentiate strong backend developers in interviews.** 🚀
