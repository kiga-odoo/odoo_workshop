# Chapter 1: Architecture Overview

## 1. Multitier Application Architecture

Odoo is designed as a three-tier architecture separating concerns across tiers:

1. **Presentation Tier (Client / Frontend):**
   - Built with HTML5, CSS, and modern JavaScript using OWL (Odoo Web Library).
   - Uses the Material Symbols icon system for consistent, scalable UI iconography.
   - Responsible for rendering responsive user interfaces (forms, lists, kanban boards, graphs, pivot tables) and handling user events directly in web browsers.

2. **Logic Tier (Server / Backend):**
   - Written exclusively in Python.
   - Built on top of the Odoo ORM (Object-Relational Mapping) engine.
   - Houses all business logic, validation rules, automated workflows, computations, and API endpoints.

3. **Data Tier (Storage / Database):**
   - Powered by PostgreSQL as the relational database management system (RDBMS).
   - Responsible for durable persistence, ACID transactions, relational integrity, and indexing.

## 2. Odoo Modules & Addons

Everything in Odoo is packaged as modular units called **addons** or **modules**:
- Addons can be full-blown applications (flagged with `'application': True` in their manifest) or technical link modules.
- Addons can introduce completely new business objects or modify existing ones via inheritance.
- The server discovers addons configured via the `--addons-path` CLI option.

### Anatomy of an Odoo 20.0 Module

A standard Odoo 20.0 module follows this directory convention:

```text
estate/
├── models/             # Python business models (ORM classes)
│   ├── __init__.py
│   └── estate_property.py
├── views/              # View architectures and actions (XML)
│   ├── estate_property_views.xml
│   └── estate_menus.xml
├── security/           # Unified access control (ir.access.csv)
│   └── ir.access.csv
├── data/               # Initial or demo records (XML/CSV)
├── __init__.py         # Python package initialization
└── __manifest__.py     # Module metadata, dependencies, and file loading order
```

### Odoo 20.0 Security Model Note
Starting in Odoo 20.0, the framework unifies model access rights (`ir.model.access`) and record rules (`ir.rule`) into a streamlined model: `ir.access`. Security access control files are now named `security/ir.access.csv`.

## 3. Odoo Editions

- **Odoo Community**: The open-source core containing the server framework, base business apps, and PostgreSQL persistence.
- **Odoo Enterprise**: Shared-source modules providing extended apps, modern UI styling, and advanced workflows on top of the Community base.
