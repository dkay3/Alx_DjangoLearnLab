# Django Application Permissions and Groups

## Custom Permissions
- **Model:** Book
- **Permissions:**
  - `can_view`: Allows viewing of a book
  - `can_create`: Allows creation of a book
  - `can_edit`: Allows editing of a book
  - `can_delete`: Allows deletion of a book

## User Groups
- **Editors:** Can create and edit books
- **Viewers:** Can only view books
- **Admins:** Can view, create, edit, and delete books

## Enforcing Permissions
- Use the `@permission_required` decorator to enforce permissions on views.
- For class-based views, use `PermissionRequiredMixin`.

## Testing
- Create users and assign them to different groups.
- Verify access control by logging in as different users and testing their access.
