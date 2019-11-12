# kgit

Wrapper over git command.

## Hooks

To use hooks call following command:
```sh
git config --global core.hooksPath PATH_TO_HOOKS_DIR
```

Available hooks:
- [pre-commit hook](hooks/pre-commit): check if `user.name` and `user.email` are
  configured
