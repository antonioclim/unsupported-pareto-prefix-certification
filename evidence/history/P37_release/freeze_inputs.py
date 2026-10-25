#!/usr/bin/env python3
"""Maintainer-only release snapshot; never used to repair a failed check.

Run after an explained and reviewed edit to the current package. This records
the actual bytes; it is not a mathematical validation or an end-user command.
The original P31 and P24 manifests remain immutable under evidence/ and legacy/.
"""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'frozen_manifest.json'

def main():
    files=[]
    for p in sorted(ROOT.rglob('*')):
        relative=p.relative_to(ROOT)
        if not p.is_file() or relative.parts[0]=='results':continue
        if p==TARGET or '__pycache__' in relative.parts or any(s.startswith('.') for s in relative.parts):continue
        if p.is_symlink():raise ValueError('Symlink not permitted in frozen payload: '+str(relative))
        files.append({'path':relative.as_posix(),'bytes':p.stat().st_size,
                      'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    manifest={'schema':'p33-review-companion-frozen-v1',
              'created_at_utc':datetime.now(timezone.utc).isoformat(),
              'purpose':'Identity of reviewed current sources and retained evidence; not proof of theorems.',
              'excluded':'results/ contains execution reports, not frozen inputs.',
              'files':files}
    TARGET.write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'status':'SNAPSHOT_WRITTEN','frozen_files':len(files),
                      'manifest_sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest()}))

if __name__=='__main__':main()
