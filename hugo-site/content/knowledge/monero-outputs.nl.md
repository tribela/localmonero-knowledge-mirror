---
title: "Monero-Outputs uitgelegd"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero gebruikt, net als andere cryptocurrencies, outputs als een middel om fondsen te verantwoorden. Veel crypto-savvy gebruikers hebben deze term waarschijnlijk al eerder gehoord, maar niet iedereen begrijpt wat ze bedoelen of hoe ze werken. Zoals onderzocht in ons [artikel over ringhandtekeningen ](/knowledge/ring-signatures), zijn outputs de daadwerkelijke eenheden die op de blockchain worden uitgewisseld tussen partijen die transacties uitvoeren. Vergelijkbaar met een dollarbiljet, maar het bedrag is niet in een vaste coupure.

Als u $ 16 krijgt voor een baan, ontvangt u mogelijk een biljet van één dollar, een biljet van vijf dollar en een biljet van tien dollar. U heeft $ 16, maar u heeft ook drie verschillende rekeningen in uw portefeuille. Als u iemand 6 dollar wilt betalen, kunt u de 5 en de 1 gebruiken, maar als u iemand $ 8 wilt betalen, kunt u alleen de $ 10 gebruiken en krijgt u $ 2 terug als wisselgeld. Ten slotte, als u iemand $ 14 zou willen betalen, zou u alle drie de biljetten moeten gebruiken en zou u $ 2 als wisselgeld terugkrijgen, maar voor een korte tijd, als u alle drie de rekeningen overhandigt, heeft u geen geld in uw portefeuille totdat u het wisselgeld terug krijgt.

Monero werkt op dezelfde manier. Stel dat u een winkel runt en drie verschillende artikelen verkoopt. U ontvangt misschien 1,5 XMR, 2,25 XMR en 5,25 XMR voor een totaal van 9 XMR, maar u heeft ook drie verschillende outputs in uw portefeuille met de eerder vermelde coupures. Net als met de dollars, wilt u misschien iemand 3 XMR betalen. U kunt alleen de 5,25 XMR-uitvoer gebruiken en 2,25 XMR terugkrijgen als wisselgeld, of u kunt de 1,5 en 2,25 XMR-uitvoer combineren en 0,75 XMR terugkrijgen als wisselgeld.

Maar zodra u de transactie verzendt, worden de uitgangen die u wel gebruikt in een "vergrendelde" toestand gezet, wat betekent dat ze ontoegankelijk zijn totdat u het wisselgeld terugkrijgt. Het protocol ontgrendelt het geld (d.w.z. geeft u het wisselgeld terug) na 10 bevestigingen, of ongeveer 20 minuten. Net zoals wanneer u de dollarbiljetten uit uw portefeuille overhandigt, kunt u het geld niet gebruiken totdat u het wisselgeld terugkrijgt van de kassier, uw Monero is ontoegankelijk totdat u het wisselgeld terugkrijgt.

Laten we teruggaan naar het voorbeeld van het sturen van 3 XMR naar iemand, en u gebruikt de 5,25 XMR-uitvoer. Nu, terwijl u wacht op uw 1,75 XMR terug in wisselgeld, kunt u het niet gebruiken. Deze 1.75 XMR is niet toegankelijk voor u. Maar u kunt nog steeds de 1,5 XMR- en 2,25 XMR-uitgangen gebruiken, aangezien deze niet zijn uitgegeven. Om terug te gaan naar het voorbeeld van de dollar: als u iemand $ 8 heeft betaald, zoals in het vorige voorbeeld, zou u de $ 2 die u terug verwacht niet in wisselgeld kunnen gebruiken totdat het aan u wordt gegeven, maar in dit voorbeeld heeft u nog steeds een biljet van $ 10 die ongebruikt in uw portefeuille zit. Dit kan nog steeds worden gebruikt om te kopen wat u maar wilt terwijl u wacht op het wisselgeld. Hetzelfde geldt voor Monero.

Dit is vaak een punt van verwarring voor nieuwe Monero-gebruikers. Vaak heeft een gebruiker slechts één output in zijn portefeuille, ontvangen van een transactie of vriend. Laten we zeggen dat deze output 20 XMR is. Ze hebben geen andere output in hun portefeuille. Ze willen nu een donatie doen aan twee van hun favoriete goede doelen. Ze sturen 5 XMR naar het eerste goede doel en zijn dan in de war, want hoewel ze nog 15 XMR over zouden moeten hebben, kunnen ze niet meteen de volgende donatie naar het tweede goede doel sturen. Zoals u misschien al geraden heeft, komt dit omdat de 15 XMR is vergrendeld. Het kan pas worden uitgegeven als het als wisselgeld is teruggegeven (10 bevestigingen of ongeveer 20 minuten). Nadat hun geld is ontgrendeld, kunnen ze hun tweede donatie sturen.

Om het punt nog eens te herhalen, ze zouden dit probleem niet hebben gehad als ze in plaats daarvan meerdere uitgangen hadden gehad, zoals twee 10 XMR-uitgangen of iets dergelijks. Ze zouden beide donaties direct na elkaar kunnen verzenden, omdat de eerste donatie een van de 10 XMR-outputs zou gebruiken (en 10 bevestigingen zou wachten om 5 XMR als wisselgeld terug te ontvangen), en de tweede donatie zou de andere 10 XMR output gebruiken.

Sommige cryptocurrency-portefeuilles hebben een functie die 'outputbeheer' wordt genoemd, waarmee een gebruiker eenvoudig kan zien welke output ze momenteel hebben (naast zijn totale som), en stelt hun in staat om te kiezen welke ze willen gebruiken wanneer ze hun cryptocurrency uitgeven.

Vanaf nu doet de GUI van Monero automatisch output-selectie voor gebruikers, aangezien gebruikers die hun eigen output selecteren vaak leidt tot verwarring of, in sommige gevallen, schending van de privacy. Er zijn echter portefeuilles in aanbouw, zoals het nieuwe Feather-portefeuille project, die deze functies voor output-beheer zullen bevatten.

We hebben veel gesproken over het verzendende gedeelte, maar er gebeurt iets fascinerends aan de ontvangende kant. Terugkomend op ons voorbeeld van het sturen van 3 XMR naar iemand en het gebruik van uw 1,5 XMR- en 2,25 XMR-outputs in de transactie (terwijl u 0,75 XMR als wisselgeld verwacht), ontvangt de ontvanger NIET twee outputs van 1,5 XMR en 2,25 XMR. In plaats daarvan ontvangen ze EEN 3 XMR-uitvoer.

Op de achtergrond combineert het protocol alle outputs die gebruikt worden voor uitgaven, en geeft de ontvanger één output van het betaalde bedrag, en stuurt één wisselgeldoutput terug naar de afzender. De afzender krijgt dus ook één output als wisselgeld terug, ongeacht of hij twee, drie of tien outputs heeft gebruikt om de transactie te verzenden.

We hopen dat dit wat verwarring heeft weggenomen over outputs en hoe de interne boekhouding van het protocol werkt, evenals het veelvoorkomende probleem van verwarring bij geblokkeerde fondsen. In een ander artikel zullen we onderzoeken hoe u uw outputs kunt beheren om de kans te minimaliseren dat u moet wachten op ontgrendeld geld voordat u toekomstige transacties verzendt.

Verder lezen