## Release Information

- Version: 1.0
- Status: Initial Release
- Features:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Power calculation

## Git Hooks

A pre-commit hook automatically runs tests before committing changes.

## Gitflow Workflow Implemented

This project demonstrates the Gitflow branching strategy using a Python calculator application.

### Workflow Steps
1. Created the main and develop branches.
2. Created a feature branch to implement the power function.
3. Created and merged a Pull Request into develop.
4. Prepared release version 1.0.
5. Created a hotfix branch to fix the division error message.
6. Merged the hotfix into main and develop.
7. Created release tags v1.0 and v1.0.1.
8. Configured a pre-commit hook to execute tests before commits.
9. Implemented GitHub Actions for automated testing.

### Testing
- Framework: Pytest
- Total test cases: 6
- Test status: All 6 tests passed.

### Tools Used
- Python
- Git and GitHub
- GitHub Actions
- Pytest
- VS Code