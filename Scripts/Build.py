#!/usr/bin/env python3
"""
Script de automação de compilação otimizada para o DitDash.
Suporta passagem de argumentos via linha de comando.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run_command(cmd, env=None):
    print(f"[BUILD] Executando: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env)
    if result.returncode != 0:
        print(f"[ERRO] Falha na execução do comando. Código de saída: {result.returncode}")
        sys.exit(result.returncode)


def setup_isolated_venv(venv_dir: Path) -> Path:
    """Cria um ambiente virtual isolado para garantir o menor tamanho de build."""
    if venv_dir.exists():
        shutil.rmtree(venv_dir, ignore_errors=True)

    print(f"[BUILD] Criando ambiente virtual limpo em {venv_dir.name}...")
    subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)

    if sys.platform == "win32":
        pip_exe = venv_dir / "Scripts" / "pip.exe"
        pyinstaller_exe = venv_dir / "Scripts" / "pyinstaller.exe"
    else:
        pip_exe = venv_dir / "bin" / "pip"
        pyinstaller_exe = venv_dir / "bin" / "pyinstaller"

    print("[BUILD] Instalando o PyInstaller no ambiente isolado...")
    subprocess.run([str(pip_exe), "install", "--quiet", "--upgrade", "pip"], check=True)
    subprocess.run([str(pip_exe), "install", "--quiet", "pyinstaller"], check=True)

    return pyinstaller_exe


def clean_artifacts(root_dir: Path, name: str):
    """Remove pastas temporárias de compilação."""
    print("[BUILD] Limpando arquivos temporários...")
    for folder in ["build", ".build_venv"]:
        path = root_dir / folder
        if path.exists():
            shutil.rmtree(path, ignore_errors=True)

    spec_file = root_dir / f"{name}.spec"
    if spec_file.exists():
        spec_file.unlink()


def main():
    parser = argparse.ArgumentParser(
        description="Utilitário avançado de compilação para o DitDash"
    )
    parser.add_argument(
        "--source",
        type=str,
        default="src/DitDash.py",
        help="Caminho do código-fonte (Padrão: src/DitDash.py)"
    )
    parser.add_argument(
        "--name",
        type=str,
        default="DitDash",
        help="Nome final do arquivo executável (Padrão: DitDash)"
    )
    parser.add_argument(
        "--icon",
        type=str,
        default="assets/icon.ico",
        help="Caminho para o ícone .ico (Padrão: assets/icon.ico)"
    )
    parser.add_argument(
        "--arch",
        type=str,
        choices=["x86_64", "x86", "arm64", "universal2"],
        help="Arquitetura do sistema alvo (Suportado conforme o SO hospedeiro)"
    )
    parser.add_argument(
        "--isolated",
        action="store_true",
        help="Gera o executável utilizando um venv limpo para reduzir o tamanho do arquivo"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Limpa compilações anteriores antes de iniciar"
    )

    args = parser.parse_args()

    root_dir = Path(__file__).parent.parent.resolve()
    source_path = root_dir / args.source
    icon_path = root_dir / args.icon

    if not source_path.exists():
        print(f"[ERRO] O arquivo fonte '{args.source}' não foi encontrado.")
        sys.exit(1)

    if args.clean and (root_dir / "dist").exists():
        shutil.rmtree(root_dir / "dist", ignore_errors=True)

    # Seleção do binário do PyInstaller
    if args.isolated:
        venv_dir = root_dir / ".build_venv"
        pyinstaller_bin = setup_isolated_venv(venv_dir)
    else:
        pyinstaller_bin = Path("pyinstaller")

    # Construção dos parâmetros de compilação
    cmd = [
        str(pyinstaller_bin),
        "--onefile",
        "--clean",
        f"--name={args.name}"
    ]

    if icon_path.exists():
        cmd.append(f"--icon={str(icon_path)}")
    else:
        print(f"[AVISO] Ícone não encontrado em '{args.icon}'. O build continuará sem ícone.")

    if args.arch:
        cmd.append(f"--target-architecture={args.arch}")

    # Exclusão de módulos irrelevantes para minimizar o tamanho
    excluded_modules = [
        "tkinter", "unittest", "email", "http", "xml",
        "asyncio", "pydoc", "multiprocessing", "urllib",
        "sqlite3", "ctypes", "logging"
    ]
    for module in excluded_modules:
        cmd.append(f"--exclude-module={module}")

    cmd.append(str(source_path))

    # Executa o processo de build
    run_command(cmd)

    # Limpeza pós-compilação
    clean_artifacts(root_dir, args.name)

    print("\n==================================================")
    print(f" COMPILAÇÃO CONCLUÍDA COM SUCESSO")
    print(f" Executável gerado em: {root_dir / 'dist'}")
    print("==================================================\n")


if __name__ == "__main__":
    main()
