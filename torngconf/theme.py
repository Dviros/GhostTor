#!/usr/bin/python3

class color:
    BLUE = '\033[94m'
    CYAN = '\033[36m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'
    
class icon:
    success = color.GREEN+'[*]'+color.END
    process = color.CYAN+'[+]'+color.END
    info = color.YELLOW+'[i]'+color.END
    error = color.RED+'[!]'+color.END
    question = color.BLUE+'[?]'+color.END

class English:
    options = "OPTIONS"
    downloading = icon.process + "Downloading {}..."
    installing = icon.process + " Installing {}..."
    install_pls = icon.error + " Please install {} please"
    uninstalling = icon.process + " Uninstalling Tor..."
    uninstalled = icon.success + " GhostTor has been uninstalled"
    installed = icon.success + " {} has been installed"
    already_installed = icon.info + " {} is already installed"
    description = """GhostTor - Make all your internet traffic anonymized through Tor proxy
Rewritten from GhostTor with Python 3"""
    root_please = icon.error + " You must be root, use 'sudo GhostTor'"
    sorry_windows = icon.error + " Sorry, GhostTor is not designed for Windows 😛 Use Tor Browser pls"
    sorry_some_os = """I'm sorry, you have to install Tor and macchanger from source by yourself :v I'm too lazy
Tor: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Sorry BSD user, I'm still trying to find way to fully support for BSD"
    current_language = icon.info + " The current display language: "
    language_list = icon.info + """ List of languages:
    1. English
    3. German"""
    choose_your_lang = icon.question + " Choose your language (1-3): "
    wanna_change_lang = icon.question + " Wanna change the display language? (y/n): "
    wanna_uninstall = icon.question + " Wanna uninstall GhostTor (y/n): "
    invalid_choice = icon.error + " Invalid choice"
    country_id = "COUNTRY ISO CODE"
    help_help = "Show this help message and exit"
    privoxy_help = "Connecting to Tor with Privoxy - Enhance your privacy"
    start_help = "Start connecting to Tor"
    stop_help = "Stop connecting to Tor"
    circuit_help = "Renew the current Tor circuit"
    id_help = "Connect to Tor exit node of a specific country. Go to CountryCode.org to search country ISO code"
    update_help = "Check for update"
    no_delay_help = "Disable delay time"
    changemac_help = "Randomly change MAC address. Use 'ifconfig' to show interface devices"
    language_help = "Change the display language. English is the default"
    language_list_help = "Show the available languages list"
    checkip_help = "Check your current IPv4 address"
    dns_help = "Use this to fix DNS when website address can't be resolved"
    done = color.GREEN+ " Done"+color.END
    disable_ipv6_info = icon.info + color.BOLD + " For security reason, GhostTor is gonna disable IPv6 to prevent IPv6 leaks (it happened to me lmao)" + color.END
    iptables_info = icon.info + """ Non-Tor traffic will be blocked by iptables
    Some apps may not be able to connect to the Internet"""
    block_bittorrent = icon.info + """ For the goodness of Tor network, BitTorrent traffic will be blocked by iptables
    with your torrent client :'("""
    applying_language = icon.process + " Applying display language..."
    checking_update = icon.process + " Checking GhostTor update..."
    outofdate = icon.error + " Your GhostTor is out-of-date"
    uptodate = icon.success + " Your GhostTor is up-to-date"
    wanna_update = icon.question + " Wanna update your GhostTor (y/n): "
    updating = icon.process + " Updating GhostTor to {}..."
    already_configured = icon.info + " {} file is already configured"
    configuring = icon.process + " Configuring {} file..."
    restoring_configuration = icon.process + " Restoring {} configuration..."
    ipv6_already_disabled = icon.info + " IPv6 is already disabled"
    disabling_ipv6 = icon.process + " Disabling IPv6..."
    stopping_tor = icon.process + " Stopping Tor service..."
    starting_tor = icon.process + " Starting new Tor service..."
    changing_tor_circuit = icon.process + " Changing Tor circuit..."
    setting_iptables = icon.process + " Setting up iptables rules..."
    flushing_iptables = icon.process + " Flushing iptables, resetting to default..."
    checking_ip = icon.process + " Checking your current IP..."
    fixing_dns = icon.process + " Fixing your DNS problem..."
    your_ip = icon.info + " Your current {} address: "
    checking_tor = icon.process + " Checking Tor connection..."
    tor_success = icon.success + " Congratulations! You've been connecting to Tor {}"
    tor_failed = icon.error + " The connecting process to Tor has failed"
    tor_disconnected = icon.success + " You've been disconnecting from Tor"
    try_again = icon.question + " Wanna try again (y/n): "
    restarting_network = icon.process + " Restarting NetworkManager..."
    changing_mac = icon.process + " Changing your current MAC address..."
    mac_changed = icon.success + " You MAC address has been changed"
    ifconfig_tip = icon.info + color.BOLD + " You can use 'ifconfig' to show interface devices" + color.END
    id_tip = icon.info + color.BOLD + " You can go to https://CountryCode.org to search country ISO code" + color.END
    torghostng_tip = icon.info + color.BOLD + " You can run GhostTor with '{}'"
    dns_tip = icon.info + " If you have problem with resolving website address, use '--dns' to fix it"
    interface_error = icon.error + " There is no interface named {}. Changing failed"
    video_tutorials = icon.info + """ If you have any questions, take a look at GhostTor Tutorial Videos here: """+ color.BOLD +"""https://bit.ly/34TNglL"""+ color.END +"""
    You will love it, i think :D"""
    

class German(English):
    options = "OPTIONEN"
    downloading = icon.process + "Herunterladen {}..."
    installing = icon.process + " Installieren {}..."
    uninstalling = icon.process + " GhostTor wird deinstalliert..."
    uninstalled = icon.success + " GhostTor wurde deinstalliert"
    installed = icon.success + " {} wurde installiert"
    already_installed = icon.info + " {} ist schon installiert"
    description = """GhostTor - Anonymisiere all deinen Internetverkehr druch Tor
neu programmiert ausgehend von TorGhost mit Python 3"""
    root_please = icon.error + " Du must root sein, benutze 'sudo GhostTor'"
    sorry_windows = icon.error + " Entschuldigung, GhostTor ist nicht kompatibel mit Windows 😛 Bitte benutze den Tor Browser"
    sorry_some_os = """Entschuldigung, aber du musst Tor und macchanger von dem Quellcode selber installieren :v Ich bin zu faul dafür
Tor: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Sorry BSD user, I'm still trying to find way that GhostTor can fully support for BSD"
    current_language = icon.info + " The current display language: "
    language_list = icon.info + """ List of languages:
    1. English
    2. Vietnamese
    3. German"""
    choose_your_lang = icon.question + " Ändere deine Sprache (1-3): "
    wanna_change_lang = icon.question + " Willst du deine Sprache ändern? (y/n): "
    wanna_uninstall = icon.question + " Möchtest du D4NG3R.HOST deinstallieren? (y/n): "
    invalid_choice = icon.error + " Falsche auswahl"
    country_id = "ISO Abkürzung des Landes"
    help_help = "Zeige diese hilfe Nachricht und schließen"
    privoxy_help = "Verbinen zum Tor Netzwerk mit Privoxy - Verbessere deine Privatsphäre"
    start_help = "Starte die Verbindung zu Tor"
    stop_help = "Stoppe die Verbindung zu Tor"
    circuit_help = "Erneuere die aktuelle Tor Verbindung"
    id_help = "Verbinde dich mit einem Tor-Ausgang in einem spezifischen Land. Gehe zu CountryCode.org und suche den Land ISO code."
    update_help = "Suche nach neuen Versionen"
    no_delay_help = "Schalte die Verzögerungszeit aus"
    changemac_help = "Ändere deine MAC Adresse zufällig. Benutze 'ifconfig' um Geräteinterfaces anzuzeigen"
    language_help = "Ändere die Anzeigesprache. Englisch ist der Standart"
    language_list_help = "Zeige mögliche Sprachauswahlen"
    checkip_help = "Teste deine aktuelle IPV4 Adresse"
    dns_help = "Benutze diese option um DNS zu reparieren wenn eine Website Adresse nicht aufgelöst werden kann"
    done = color.GREEN+ " Fertig"+color.END
    disable_ipv6_info = icon.info + color.BOLD + " Aus Sicherheitsgründen schaltet GhostTor IPv6 Verkehr aus, um IPv6 Lecks zu verhindern" + color.END
    iptables_info = icon.info + """ Nicht-Tor Verkehr wird von iptables blockiert.
    Manche Anwendungen werden sich nicht mit dem Internet verbinden können"""
    block_bittorrent = icon.info + """ Um das Tor-Netzwerk nicht unnötig zu belasten, wird BitTorrent Verkehr von iptables blockiert."""
    applying_language = icon.process + " Anzeigesprache wird geändert..."
    checking_update = icon.process + " Prüfen auf neue Versionen von GhostTor..."
    outofdate = icon.error + " Es gibt neue Versionen von GhostTor"
    uptodate = icon.success + " Deine Verison von GhostTor is aktuell"
    wanna_update = icon.question + " Möchtest du GhostTor aktualisieren? (y/n): "
    updating = icon.process + " D4NG3R.HOST wird aktualisiert zur Verison {}..."
    already_configured = icon.info + " {} ist bereits konfiguriert"
    configuring = icon.process + " Konfigurieren von {} ..."
    restoring_configuration = icon.process + " Wiederherstellen der Konfiguration {}..."
    ipv6_already_disabled = icon.info + " IPv6 ist bereits ausgeschaltet"
    disabling_ipv6 = icon.process + " Ausschalten von IPv6..."
    stopping_tor = icon.process + " Tor Dienst wird gestoppt..."
    starting_tor = icon.process + " Tor Dienst wird gestartet..."
    changing_tor_circuit = icon.process + " Änderung des Tor-Pfades..."
    setting_iptables = icon.process + " Einstellen der iptables Regeln..."
    flushing_iptables = icon.process + " Aktualisieren von iptables, zurücksetzen auf Standarteinstellungen..."
    checking_ip = icon.process + " Testen deiner aktuellen IP..."
    fixing_dns = icon.process + " Reparieren deines DNS Problems..."
    your_ip = icon.info + " Deine aktuelle {} Adresse: "
    checking_tor = icon.process + " Testen deiner Tor Verbindung..."
    tor_success = icon.success + " Erfolg! Du bist nun zu Tor verbunden {}"
    tor_failed = icon.error + " Dein Verbindungsprozess zu Tor ist fehlgeschlagen"
    tor_disconnected = icon.success + " Deine Verbindung zu Tor wurde getrennt"
    try_again = icon.question + " Möchtest du es erneut probieren (y/n): "
    restarting_network = icon.process + " Neustarten des NetworkManager..."
    changing_mac = icon.process + " Änderung deiner aktuellen MAC Adresse..."
    mac_changed = icon.success + " Deine Mac Adresse wurde geändert"
    ifconfig_tip = icon.info + color.BOLD + " Du kannst 'ifconfig' benutzen um Netzwerkadapter anzuzeigen" + color.END
    id_tip = icon.info + color.BOLD + " Du kannst zu https://CountryCode.org gehen um Länder ISO codes zu finden" + color.END
    torghostng_tip = icon.info + color.BOLD + " Du kannst GhostTor mit '{}' starten"
    dns_tip = icon.info + " Wenn du Probleme hast mit DNS, kannst du '--dns' benutzen um das Problem zu lösen"
    interface_error = icon.error + " Es existiert kein Netzwerkadapter namens {}. Änderung fehlgeschlagen"
    video_tutorials = icon.info + """ Wenn du Fragen hast, kannst du dir GhostTor Tutorial Videos hier anschauen: """+ color.BOLD +"""https://bit.ly/34TN"""+ color.END +"""
    Ich denke die sollten dir gefallen:D"""
    
the_banner = color.GREEN + """ 

   ▄▄▄  █                      ▄   ▄▄▄▄▄▄▄
 ▄▀   ▀ █ ▄▄    ▄▄▄    ▄▄▄   ▄▄█▄▄    █     ▄▄▄    ▄ ▄▄
 █   ▄▄ █▀  █  █▀ ▀█  █   ▀    █      █    █▀ ▀█   █▀  ▀
 █    █ █   █  █   █   ▀▀▀▄    █      █    █   █   █
  ▀▄▄▄▀ █   █  ▀█▄█▀  ▀▄▄▄▀    ▀▄▄    █    ▀█▄█▀   █
 
             Create by TR0J4N3R & D4NG3Rv2 
 
 YouTube: https://www.youtube.com/channel/UCjw4sunOoXDiT0DJNSz6HBw
 Instagram: https://www.instagram.com/TR0J4N3R/
 Discord: https://discord.gg/JkgbXuHYAt


               """ + color.END
