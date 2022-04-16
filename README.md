# kgit

Docs about my git environment and wrapper over git command.

## How to set up my environment

1. `git config --global commit.gpgSign true`
2. `git config --global core.hooksPath PATH_TO_HOOKS_DIR`

## Hooks

To use hooks call following command:
```sh
git config --global core.hooksPath PATH_TO_HOOKS_DIR
```

### Available hooks

- [pre-commit hook](hooks/pre-commit): check if `user.name` and `user.email` are
  configured

## Links

* [Git Tools - Signing Your Work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)
