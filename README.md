# Checkov hard-fail

This action hard fails on given checks.

## Inputs

### `hard-fail-on`

**Required** Comma seperated list of controls that are not allowed to fail or skip.

### `path`

Path to check. Defaults to root.

### `skip-checks`

Comma seperated list of controls to skip.

## Example usage

```yaml
uses: sbkg0002/checkov-hard-fail-actio@main
with:
  hard-fail-on: 'CKV2_AWS_40,CKV_AWS_110'
  path: 'terraform/'
  skip-checks: 'CKV2_AWS_41,CKV_AWS_111'
```
