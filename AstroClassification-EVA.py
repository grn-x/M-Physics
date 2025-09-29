from graphviz import Digraph

# Mindmap im Rahmen der Astro-EVA-Aufgabe
#dot = Digraph("Planeten-System")
#dot.attr(size="12", dpi="300", rankdir="TB")  # Top-Bottom Layout

dot = Digraph("Planeten-System", engine="neato")
dot.attr(size="10", dpi="300",
         overlap="false",
         splines="true",
         nodesep="0.1", ranksep="0.1")

dot.attr('node', fontsize='14')
dot.attr('edge', fontsize='12')


# Root
dot.node("Himmelskörper", "Klassifizierung von Himmelskörpern")

# -----------------------------
# Kategorie: Planeten-System
# -----------------------------
dot.node("PlanetenGruppe", "Planeten-System")
dot.edge("Himmelskörper", "PlanetenGruppe")

# Planeten
planet_def = "Körper im Umlauf um Stern; hydrostatisches Gleichgewicht; Bahn bereinigt"
dot.node("Planet", "Planeten")
dot.edge("PlanetenGruppe", "Planet")
dot.node("PlanetInfo", planet_def, shape="note")
dot.edge("Planet", "PlanetInfo")

# Monde
moon_def = "Natürliche Satelliten; Umlauf um Planeten"
dot.node("Mond", "Monde")
dot.edge("PlanetenGruppe", "Mond")
dot.node("MondInfo", moon_def, shape="note")
dot.edge("Mond", "MondInfo")

# Zwergplaneten
zp_def = "Hydrostatisches Gleichgewicht, aber Bahn nicht bereinigt"
dot.node("Zwergplanet", "Zwergplaneten")
dot.edge("PlanetenGruppe", "Zwergplanet")
dot.node("ZwergInfo", zp_def, shape="note")
dot.edge("Zwergplanet", "ZwergInfo")

# -----------------------------
# Kategorie: Kleine Körper
# -----------------------------
dot.node("KleineKörper", "Kleine Körper")
dot.edge("Himmelskörper", "KleineKörper")

# Asteroiden
asteroid_def = "Meist felsig; wenige km – 1000 km groß"
dot.node("Asteroid", "Asteroiden")
dot.edge("KleineKörper", "Asteroid")
dot.node("AsteroidInfo", asteroid_def, shape="note")
dot.edge("Asteroid", "AsteroidInfo")

# Kometen
komet_def = "Eisreich; entwickeln Schweif nahe der Sonne"
dot.node("Komet", "Kometen")
dot.edge("KleineKörper", "Komet")
dot.node("KometInfo", komet_def, shape="note")
dot.edge("Komet", "KometInfo")

# Meteoroiden
met_def = "Kleine Fragmente (<1 m) von Asteroiden/Kometen"
dot.node("Meteoroid", "Meteoroiden")
dot.edge("KleineKörper", "Meteoroid")
dot.node("MetInfo", met_def, shape="note")
dot.edge("Meteoroid", "MetInfo")

# Meteorite
met2_def = "Meteoroiden, die Erdoberfläche erreichen"
dot.node("Meteorit", "Meteorite")
dot.edge("KleineKörper", "Meteorit")
dot.node("Met2Info", met2_def, shape="note")
dot.edge("Meteorit", "Met2Info")

# -----------------------------
# Kategorie: Räumlicher Aufbau
# -----------------------------
dot.node("Raum", "Räumlicher Aufbau des Sonnensystems")
dot.edge("Himmelskörper", "Raum")

agb_def = "Zwischen Mars & Jupiter"
dot.node("Asteroidengürtel", "Asteroidengürtel")
dot.edge("Raum", "Asteroidengürtel")
dot.node("AGBInfo", agb_def, shape="note")
dot.edge("Asteroidengürtel", "AGBInfo")

kg_def = "Jenseits von Neptun; viele transneptunische Objekte"
dot.node("Kuipergürtel", "Kuipergürtel")
dot.edge("Raum", "Kuipergürtel")
dot.node("KGInfo", kg_def, shape="note")
dot.edge("Kuipergürtel", "KGInfo")

ow_def = "Hypothetische Kugelwolke aus Milliarden Kometenkernen"
dot.node("Oort", "Oortsche Wolke")
dot.edge("Raum", "Oort")
dot.node("OWInfo", ow_def, shape="note")
dot.edge("Oort", "OWInfo")

# -----------------------------
# Kategorie: Interstellare Objekte
# -----------------------------
dot.node("InterObj", "Interstellare Objekte")
dot.edge("Himmelskörper", "InterObj")

inter_def = "Durchqueren Sonnensystem, Ursprung außerhalb"
dot.node("InterInfo", inter_def, shape="note")
dot.edge("InterObj", "InterInfo")

# -----------------------------
# Kategorie: Habitable Zone
# -----------------------------
dot.node("HabZone", "Habitable Zone")
dot.edge("Himmelskörper", "HabZone")
hab_def = "Abstand zum Stern, in dem Wasser flüssig existieren kann"
dot.node("HabInfo", hab_def, shape="note")
dot.edge("HabZone", "HabInfo")



dot.render("assets/AstroClassification", format="png", cleanup=True)
