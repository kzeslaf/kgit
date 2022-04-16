# kgit

Docs about my git environment and wrapper over git command.

## How to set up my environment

### Global configuration

Install hooks:
```
git config --global core.hooksPath PATH_TO_HOOKS_DIR
```

### Repository configuration

Set local config options:

* `user.name`
* `user.email`
* `commit.gpgSign`
* `merge.verifySignatures`

## Hooks

To install hooks call following command:
```sh
git config --global core.hooksPath PATH_TO_HOOKS_DIR
```

### Available hooks

- [pre-commit hook](hooks/pre-commit)
    - check if `user.name`, `user.email`, `commit.gpgSign` and
  `merge.verifySignatures` are configured

## Links

* [Git Tools - Signing Your Work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)
