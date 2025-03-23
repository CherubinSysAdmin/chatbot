#!/usr/bin/env python3

import logging
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token Telegram
TOKEN = 'TON_BOT_TOKEN_ICI'

# Liste des services à surveiller
SERVICES = ["apache2", "ssh", "vsftpd", "samba", "bind9", "isc-dhcp-server", "postfix", "shellinabox"]

# Fonction pour exécuter une commande shell
def execute_command(command: str) -> str:
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Erreur: {e.output.strip()}"

# Vérifier l'état des services (actifs, inactifs)
async def check_services(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    results = {service: execute_command(f"systemctl is-active {service}") for service in SERVICES}
    active_services = [f"✅ {srv}" for srv, status in results.items() if status == "active"]
    inactive_services = [f"❌ {srv}" for srv, status in results.items() if status != "active"]

    response = "**📌 État des services :**\n\n"
    response += "**🔹 Actifs :**\n" + ("\n".join(active_services) if active_services else "Aucun service actif.") + "\n\n"
    response += "**🔻 Inactifs :**\n" + ("\n".join(inactive_services) if inactive_services else "Aucun service inactif.")
    
    await update.message.reply_text(response)

# Vérifier un service spécifique
async def check_service_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        service = context.args[0]
        status = execute_command(f"systemctl is-active {service}")
        await update.message.reply_text(f"Service `{service}` : {status}")
    else:
        await update.message.reply_text("Usage : /check_service [nom_du_service]")

# Redémarrer un service
async def restart_service(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        service = context.args[0]
        execute_command(f"sudo systemctl restart {service}")
        status = execute_command(f"systemctl is-active {service}")
        await update.message.reply_text(f"Service `{service}` redémarré.\nStatut actuel : {status}")
    else:
        await update.message.reply_text("Usage : /restart [nom_du_service]")

# Stopper un service
async def stop_service(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        service = context.args[0]
        execute_command(f"sudo systemctl stop {service}")
        status = execute_command(f"systemctl is-active {service}")
        await update.message.reply_text(f"Service `{service}` arrêté.\nStatut actuel : {status}")
    else:
        await update.message.reply_text("Usage : /stop_service [nom_du_service]")

# Vérifier l'utilisation de la mémoire
async def memory_usage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = execute_command("free -h")
    await update.message.reply_text(f"📊 **Utilisation de la mémoire :**\n```\n{result}\n```")

# Vérifier l'utilisation du CPU
async def cpu_usage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = execute_command("top -bn1 | grep 'Cpu(s)'")
    await update.message.reply_text(f"⚙️ **Utilisation du CPU :**\n```\n{result}\n```")

# Redémarrer le serveur
async def restart_server(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("⚠️ **Le serveur va redémarrer...**")
    execute_command("sudo reboot")

# Fonction principale
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Ajout des commandes
    application.add_handler(CommandHandler("check_services", check_services))
    application.add_handler(CommandHandler("check_service", check_service_status))
    application.add_handler(CommandHandler("restart", restart_service))
    application.add_handler(CommandHandler("stop_service", stop_service))
    application.add_handler(CommandHandler("memory", memory_usage))
    application.add_handler(CommandHandler("cpu", cpu_usage))
    application.add_handler(CommandHandler("restart_server", restart_server))

    # Démarrer le bot
    application.run_polling()

if __name__ == "__main__":
    main()