import argparse
import Codificador, Decodificador

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="comando", required=True)

    p_esc = sub.add_parser("esconderMensagem")
    p_esc.add_argument("imagem")
    p_esc.add_argument("mensagem")

    p_ler = sub.add_parser("lerMensagem")
    p_ler.add_argument("imagem")

    args = parser.parse_args()

    if args.comando == "esconderMensagem":
        Codificador.EsconderPorLSB(args.mensagem, args.imagem)
    elif args.comando == "lerMensagem":
        Decodificador.LerMensagemPorLSB(args.imagem)
    else:
        print("Comando inválido. Use 'esconderMensagem' ou 'lerMensagem'.")