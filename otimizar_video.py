import subprocess
import sys
import os

def check_ffmpeg():
    """Verifica se o FFmpeg está instalado no sistema."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def optimize_mp4(input_path, output_path, crf=24, preset="medium"):
    """
    Otimiza o arquivo MP4 para a Web.
    - H.264 (libx264)
    - AAC Audio
    - Faststart (permite o vídeo começar a tocar antes do download completo)
    - CRF 24 (Bom equilíbrio de qualidade e tamanho. Quanto maior, menor o arquivo)
    """
    print(f"-> Otimizando MP4: {input_path}...")
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-c:v", "libx264",
        "-crf", str(crf),
        "-preset", preset,
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        output_path
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ MP4 Otimizado salvo em: {output_path}")

def convert_to_webm(input_path, output_path, crf=30, bitrate="0"):
    """
    Converte o vídeo para o formato WebM (VP9).
    - VP9 (libvpx-vp9)
    - Opus Audio
    - CRF 30 (padrão recomendado para VP9 Web)
    """
    print(f"-> Convertendo para WebM (VP9): {input_path}...")
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-c:v", "libvpx-vp9",
        "-crf", str(crf),
        "-b:v", bitrate,
        "-c:a", "libopus",
        "-b:a", "128k",
        output_path
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ WebM salvo em: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python otimizar_video.py <caminho_do_video.mp4>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
        sys.exit(1)

    if not check_ffmpeg():
        print("Erro: O FFmpeg não foi encontrado no sistema.")
        print("Instale o FFmpeg (ex: 'sudo apt install ffmpeg' ou 'brew install ffmpeg') para rodar este script.")
        sys.exit(1)

    base_name, _ = os.path.splitext(input_file)
    output_mp4 = f"{base_name}_otimizado.mp4"
    output_webm = f"{base_name}.webm"

    try:
        # 1. Gerar MP4 Leve para Web
        optimize_mp4(input_file, output_mp4)
        
        # 2. Gerar versão WebM (VP9)
        convert_to_webm(input_file, output_webm)

        print("\n✨ Processo concluído com sucesso!")
        print(f"1. MP4 Leve: {output_mp4}")
        print(f"2. WebM:     {output_webm}")

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro durante a conversão: {e}")

if __name__ == "__main__":
    main()
