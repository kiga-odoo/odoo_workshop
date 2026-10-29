# Odoo Technical Training - Server Framework 101 (Odoo 20.0)

Welcome to the Odoo Server Framework 101 workshop repository, updated for **Odoo 20.0**!

This repository contains the training code and step-by-step solutions for the official [Odoo Server Framework 101 Tutorial](https://www.odoo.com/documentation/master/developer/tutorials/server_framework_101.html).

## Repository Architecture

- `main`: Clean starting branch containing only base setup files (`.gitignore`, `README.md`).
- `solution`: Step-by-step reference solutions for each chapter.
- Tags: `chapter-1` through `chapter-15` tag each chapter's commit on the `solution` branch.

## Key Changes in Odoo 20.0

1. **Unified Security Model (`ir.access.csv`)**:
   - In Odoo 20.0, `ir.model.access` and `ir.rule` have been consolidated into `ir.access`.
   - Security access control is defined in `security/ir.access.csv`.
   - The CSV format uses: `id,name,model_id,group_id/id,operation,domain`.
   - `model_id` uses the model name directly (`estate.property`, not `model_estate_property`).
   - `operation` specifies allowed operations via flags: `crud` (Create, Read, Update, Delete).

2. **Material Symbols Icons**:
   - Odoo 20.0 adopts Google Material Symbols in place of legacy FontAwesome icons (`fa-*`).
   - For example: `icon="check"`, `icon="close"`, and `icon="attach_money"`.

3. **Modern View and Constraint Syntax**:
   - Tabular views use the `<list>` element instead of legacy `<tree>`.
   - Model constraints are declared with `models.Constraint` rather than `_sql_constraints`.
   - Standard Python 3 UTF-8 default encoding (omitting legacy `# -*- coding: utf-8 -*-` headers).

## How to Follow the Workshop on Main

Students remain on the `main` branch. If stuck or wishing to review the official solution for any chapter, cherry-pick the respective chapter tag:

```bash
git checkout main

# Chapter 1: Architecture Overview
git cherry-pick chapter-1

# Chapter 2: A New Application (estate manifest & package)
git cherry-pick chapter-2

# Chapter 3: Models And Basic Fields (estate.property model)
git cherry-pick chapter-3

# Chapter 4: Security - A Brief Introduction (Odoo 20.0 ir.access.csv)
git cherry-pick chapter-4

# Chapter 5: Finally, Some UI To Play With (actions, menus, defaults, reserved fields)
git cherry-pick chapter-5

# Chapter 6: Basic Views (list, form, search views)
git cherry-pick chapter-6

# Chapter 7: Relations Between Models (types, tags, offers, partner & user relations)
git cherry-pick chapter-7

# Chapter 8: Computed Fields And Onchanges (total area, best offer, deadlines, onchange)
git cherry-pick chapter-8

# Chapter 9: Ready For Some Action? (state transitions, buttons, offer acceptance)
git cherry-pick chapter-9

# Chapter 10: Constraints (SQL constraints and Python validation)
git cherry-pick chapter-10

# Chapter 11: Add The Sprinkles (widgets, colors, order, invisible, stat buttons)
git cherry-pick chapter-11

# Chapter 12: Inheritance (CRUD override ondelete/create, res.users model & view extension)
git cherry-pick chapter-12

# Chapter 13: Interact With Other Modules (estate_account link module, invoice creation)
git cherry-pick chapter-13

# Chapter 14: A Brief History Of QWeb (Kanban card view with conditional pricing)
git cherry-pick chapter-14

# Chapter 15: The Final Word (guidelines review, clean code formatting)
git cherry-pick chapter-15
```

## Modules Included

- `estate`: Real estate advertisement and management application.
- `estate_account`: Link addon integrating real estate sales with customer invoicing.
