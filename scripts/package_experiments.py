"""Atualiza hashes e ZIPs dos experimentos com a biblioteca padrão do Python."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]

for experiment in sorted((ROOT / 'experiments').iterdir()):
    if not experiment.is_dir():
        continue
    archive = experiment / (experiment.name + '.zip')
    manifest = experiment / 'SHA256SUMS.txt'
    files = sorted(p for p in experiment.rglob('*') if p.is_file() and p not in (archive, manifest))
    manifest.write_bytes(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(experiment).as_posix() + '\n' for p in files).encode('utf-8'))
    files = sorted(files + [manifest])
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for file in files:
            entry = zipfile.ZipInfo(experiment.name + '/' + file.relative_to(experiment).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            output.writestr(entry, file.read_bytes())
    with zipfile.ZipFile(archive) as check:
        assert check.testzip() is None
        assert len(check.namelist()) == len(files)
    print(f'{experiment.name}: {len(files)} arquivos; ZIP {archive.stat().st_size:,} bytes; SHA-256 {hashlib.sha256(archive.read_bytes()).hexdigest()}')
