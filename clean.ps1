
"D:\Development\simple-cloud-kit-oss\.venvs\sck-core-docs-ix2_KQRo-py3.13\Scripts\Activate.ps1" `
   && Get-ChildItem -Path "docs\technical_reference" -Recurse -Directory -Name "_autosummary" | `
   ForEach-Object { Remove-Item -Path "docs\technical_reference\$_" -Recurse -Force }
