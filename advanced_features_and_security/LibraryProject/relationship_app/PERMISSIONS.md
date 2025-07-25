# Permissions Overview

## Custom Permissions (Book Model)
- `can_view`: View book list/details.
- `can_create`: Add new books.
- `can_edit`: Modify book entries.
- `can_delete`: Remove books.

## Groups
| Group    | Permissions                   |
|----------|-------------------------------|
| Viewers  | can_view                      |
| Editors  | can_view, can_create, can_edit|
| Admins   | All permissions               |