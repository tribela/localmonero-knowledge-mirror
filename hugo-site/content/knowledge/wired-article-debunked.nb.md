---
title: "Wired Magazine tar feil om Monero, her er hvorfor"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
På både personvern- og kryptovaluta-sfæren løper feilinformasjon ofte. Vi har [en artikkel som skisserer femten vanlige ukorrekte eller utdaterte antakelser om Monero](/knowledge/monero-myths-debunked), men vi ønsker å bruke tid på å ta opp en bestemt artikkel som ofte siteres og sirkuleres av Monero-skeptikere.

The Wired-publikasjonen la ut [en artikkel](https://www.wired.com/story/monero-privacy/) den 27. mars 2018, som i seg selv ble skrevet som svar på en annen fersk artikkel publisert av forskjellige akademikere med tittelen: "An Empirical Analysis av sporbarhet i Monero Blockchain".

Selv om avisen var medforfatter av enkeltpersoner med tydelig interessekonflikt (les: de er rådgivere for og har en eierandel i Zcash), ble avisen moderat godt mottatt av Monero-fellesskapet som bekrefter ting fellesskapet allerede har visst og skrevet om i deres egne Monero Research Lab-artikler ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) og [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), hvorav den tidligste ble publisert fire år tidligere. Det var imidlertid også flere frustrasjoner med det, hovedsakelig interessekonflikten, det faktum at problemene allerede var kjent, diskutert og – i noen tilfeller – utbedret, og den grove feilkarakteriseringen av Moneros personverngarantier på den tiden. Fellesskapet kommenterte fortrykket av verket, og mange av anbefalingene deres kom videre til den endelige artikkelen.

Men nøyaktig hva ble feilkarakterisert? Det faktum at Monero ikke hadde hatt feilene diskutert i avisen på over et år. Transaksjoner før 2017 var faktisk sårbare for en form for personvernlekkasje, men på publiseringstidspunktet hadde Monero tatt tak i de fleste bekymringene. For å være rettferdige overfor forfatterne, diskuterer de Moneros rettsmidler i liten grad, men ikke nok til å påvirke effekten det hadde på kryptovaluta-mediesyklusen på den tiden. Derav Wired-artikkelen.

Selv om vi kan undersøke den aktuelle Wired-artikkelen som et tidsskrift, og hvor sant eller usant det var på den tiden, inviterer det faktum at det fortsatt deles i dag som begrunnelse for hvorfor Moneros personverngarantier er svake, til en analyse. om hvordan stykket holder seg i nåtiden. Vi tar gjerne imot denne invitasjonen.

En rask lesing av artikkelen viser flere oppsiktsvekkende linjer, for eksempel "[Funnene] burde ikke bare bekymre noen som prøver å bruke Monero i dag" og hele tonen i artikkelen som postulerer forskningen som "ny", hovedsakelig basert på publikasjonen. Den akademiske artikkelen har i seg selv anbefalinger som å advare Monero-brukere om det potensielle kompromittering av deres anonymitet, til tross for at ikke bare disse diskusjonene hadde pågått siden 2014, men fellesskapets samlingsrop var at folk ikke skulle kjøpe Monero og at det var veldig eksperimentell.

Men hva med selve kritikken? Realiteten er at mange problemer med Monero som en personvernmynt enten ikke lenger gjelder Monero, eller deler bekymringer med personvernmynter som en kategori av blokkjedebaserte kryptovalutaer. La oss begynne å adressere disse.

En av de oftest siterte kritikkene av Monero er at på grunn av blokkjedens varighet og uforanderlighet, hvis en fremtidig teknologi skulle bryte personvernet, ville alle Moneros tidligere transaksjoner bli avslørt. Personvernet ditt har med andre ord en tikkende klokke.

Vi kan ikke understreke dette nok. Bokstavelig talt hver personvernmynt som bruker on-chain metoder for tilsløring og personvern har denne feilen, og likevel brukes den ofte mot Monero (ironisk nok mange ganger av konkurrerende personvernmynter med samme problem), og brukes også i denne artikkelen. Responsen på denne kritikken kan være overraskende for noen, men Monero kan faktisk være mindre sårbar enn andre personvernmynter for dette på grunn av det faktum at den har en flerstrenget tilnærming til personvern.

Monero skjuler utganger (sendere), beløp og mottakere gjennom tre forskjellige teknologier, henholdsvis ringsignaturer, RingCT og stealth-adresser. Av disse er ringsignaturer de svakeste og mest mottakelige for både moderne heuristikk og teoretiske, fremtidige, personvernbrytende teknologier. Dette har vært kjent for Monero-fellesskapet i årevis, og aktiv forskning pågår for å forbedre eller erstatte ringsignaturordningen fullstendig.

Men selv om ringsignaturen ble brutt helt, ville bare den sanne utgangen bli avslørt. IKKE avsenderen (som i individ), men utgangen. Å koble en utgang med en identitet er ikke umulig, men det vil kreve mer metadata og ressurser. Sammen med det faktum at RingCT og stealth-adressen IKKE vil bli avslørt, reduseres effekten ytterligere.

Det skal bemerkes at Wired-artikkelen på en lett måte diskuterer informasjonen ovenfor i delen der de henvendte seg til Riccardo 'fluffypony' Spagni for kommentar, men tiden som gis til den er kort, og ser nesten ut til å vinke bort. denne avgjørende informasjonen. Mangelen på forståelse er spesielt tydelig når man prøver å diskutere disse tingene med folk som deler artikkelen med vilje i moderne tid.

En annen kritikk som er mye vanskeligere å ta tak i, er hvordan omverdenen ser på Monero, og hvordan det henger sammen med hvordan samfunnet rundt Monero ser på mynten. For et eksempel på dette trenger ikke leserne se lenger enn tittelen på selve artikkelen: "The Dark Web's Favorite Currency Is Less Untraceable Than It Sees".

Enhver person som tilbringer betydelig tid i Monero-fellesskapet kan bekrefte det faktum at Monero-fellesskapet strekker seg langt for å vise hvor vanskelig ekte personvern er å oppnå, selv på bekostning av markedsførings- eller adopsjonsinnsats. Hvis fellesskapet gir rikelig med ressurser for å diskutere mynten og dens mangler nøyaktig, på et tidspunkt, blir uvitenheten feilen til brukeren som tror at mynten er alt de trenger for å være 100 % privat.

På dette tidspunktet bør det være tydelig at Monero-fellesskapet tar både personvernet og ærligheten om svakhetene og påfølgende forbedringer på alvor. Artikler, som den aktuelle, savner fullstendig denne innovasjonsånden i Monero. Den sammenligner Monero med mengden av andre kryptovalutaer som fremsetter grandiose påstander, kun med tanke på profitt og å tære på uutdannede investor-wannabes.

Virkeligheten kunne ikke vært mer annerledes. Monero er svært klar over sine svakheter, søker å fortsette å bygge for å forbedre dem, stramme opp løse ledd og oppnå det virkelige, men svært vanskelige målet om å gi verden en privat, ombyttbar kryptovaluta som kan brukes av alle, og gjøre alt på en måte som er rettferdig, desentralisert og fellesskapsdrevet. Kanskje det er på tide å legge vekk sensasjonaliteten og artikkeldelingen som et middel til å fjerne poser og promotere konkurrenter. Kanskje det er på tide å fortelle en ny historie.

Videre lesning