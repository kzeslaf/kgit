# kgit

My _git_ configuration and tools.

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
    - check if `user.name`, `user.email`, `user.signingkey`, `commit.gpgSign`
      and `merge.verifySignatures` are configured

## Links

* [Git Tools - Signing Your Work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)
* [Kernel Maintainer PGP guide](https://www.kernel.org/doc/html/latest/process/maintainer-pgp-guide.html)
