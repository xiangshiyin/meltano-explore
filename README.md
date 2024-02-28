**Table of Contents**
- [meltano-explore](#meltano-explore)
  - [Environment setup](#environment-setup)
  - [Examples:](#examples)
  - [Build a customized extractor](#build-a-customized-extractor)


# meltano-explore
Learn about Meltano usage

## Environment setup
1. Install `poetry` [[reference](https://python-poetry.org/docs/#installation)]
2. Run `poetry add meltano` (clean install with `poetry`)
3. Run `mkdir projects` (create the projects folder)
4. Run `cd projects`
5. Run `meltano init .`
<details>
<summary>Output</summary>

```
❯ meltano init .                                                                                                         (base)
Creating .meltano folder
created .meltano in /Users/xiangshiyin/Documents/Learning/meltano-explore/projects/.meltano
Creating project files...
   |-- meltano.yml
   |-- README.md
   |-- requirements.txt
   |-- output/.gitignore
   |-- .gitignore
   |-- extract/.gitkeep
   |-- load/.gitkeep
   |-- transform/.gitkeep
   |-- analyze/.gitkeep
   |-- notebook/.gitkeep
   |-- orchestrate/.gitkeep
Creating system database...  Done!



                          ████   █████
                         ░░███  ░░███
 █████████████    ██████  ░███  ███████    ██████   ████████    ██████
░░███░░███░░███  ███░░███ ░███ ░░░███░    ░░░░░███ ░░███░░███  ███░░███
 ░███ ░███ ░███ ░███████  ░███   ░███      ███████  ░███ ░███ ░███ ░███
 ░███ ░███ ░███ ░███░░░   ░███   ░███ ███ ███░░███  ░███ ░███ ░███ ░███
 █████░███ █████░░██████  █████  ░░█████ ░░████████ ████ █████░░██████
░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░    ░░░░░   ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░



Your project has been created!

Meltano Environments initialized with dev, staging, and prod.
To learn more about Environments visit: https://docs.meltano.com/concepts/environments

Next steps:
  Visit https://docs.meltano.com/getting-started/part1 to learn where to go from here
```

</details>

6. Run `meltano add extractor tap-google-sheets` to add an extractor tap
<details>
<summary>Output</summary>

```
❯ meltano add extractor tap-google-sheets                                                                                (base)
2024-02-28T04:50:05.574072Z [warning  ] `kind: password` is deprecated for setting definitions in favour of `sensitive: true`, and is currently in use by the following settings of extractor 'tap-google-sheets': 'oauth_credentials.client_id', 'oauth_credentials.client_secret', 'oauth_credentials.refresh_token', 'sheet_id'. Please open an issue or pull request to update the plugin definition on Meltano Hub at https://github.com/meltano/hub/blob/main/_data/meltano/extractors/tap-google-sheets/matatika.yml.
Added extractor 'tap-google-sheets' to your project
Variant:	matatika (default)
Repository:	https://github.com/Matatika/tap-google-sheets
Documentation:	https://hub.meltano.com/extractors/tap-google-sheets--matatika

Installing extractor 'tap-google-sheets'...
Installed extractor 'tap-google-sheets'

To learn more about extractor 'tap-google-sheets', visit https://hub.meltano.com/extractors/tap-google-sheets--matatika
```

</details>

7. Run `meltano remove extractor tap-google-sheets` to remove the extractor tap
<details>
<summary>Output</summary>

```
❯ meltano remove extractor tap-google-sheets                                                                             (base)

Removing extractor 'tap-google-sheets'...

2024-02-28T05:15:21.179487Z [warning  ] `kind: password` is deprecated for setting definitions in favour of `sensitive: true`, and is currently in use by the following settings of extractor 'tap-google-sheets': 'oauth_credentials.client_id', 'oauth_credentials.client_secret', 'oauth_credentials.refresh_token', 'sheet_id'. Please open an issue or pull request to update the plugin definition on Meltano Hub at https://github.com/meltano/hub/blob/main/_data/meltano/extractors/tap-google-sheets/matatika.yml.
Reset extractor 'tap-google-sheets' plugin settings in the system database
Removed extractor 'tap-google-sheets' from meltano.yml
Removed extractor 'tap-google-sheets' from .meltano/extractors
Removed extractor 'tap-google-sheets' from plugins/extractors/tap-google-sheets*.lock
```

</details>

## Examples:
## Build a customized extractor
https://docs.meltano.com/tutorials/custom-extractor

