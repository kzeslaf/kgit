# kgit

Docs about my git environment and wrapper over git command.

## TODO

* --verify-signatures?
* config option `merge.verifySignatures` (https://git-scm.com/docs/git-config)
* check in hook if `commit.gpgSign` is configured
* move `commit.gpgSign` from --global to repo config

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
