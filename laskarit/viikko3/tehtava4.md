```mermaid
 sequenceDiagram
	main->>laitehallinto: HKLLaitehallinto()
	laitehallinto-->>laitehallinto: lataajat=[]
	laitehallinto-->>laitehallinto: lukijat=[]
	main->>rautatietori: Lataajalaite()
	main->>ratikka6: Lukijalaite()
	main->>bussi244: Lukijalaite()
	main->>laitehallinto: lisaa_lataaja(rautatietori)
	laitehallinto-->>laitehallinto: lataajat=[rautatietori]
	main->>laitehallinto: lisaa_lukija(ratikka6)
	laitehallinto-->>laitehallinto: lukijat=[ratikka6]
	main->>laitehallinto: lisaa_lukija(bussi244)
	laitehallinto-->>laitehallinto: lukijat=[ratikka6, bussi244]
	main->>lippu_luukku: Kioski()
	main->>kallen_kortti: osta_matkakortti("Kalle")
	kallen_kortti->>lippu_luukku: Matkakortti("Kalle")
	lippu_luukku-->>kallen_kortti("Kalle")
	Note right of kallen_kortti: Omistaja=Kalle\npvm=0\nkk=0\narvo=0
	main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
	rautatietori-->>rautatietori: lataa_arvoa(kallen_kortti, 3)
	rautatietori->>kallen_kortti: kasvata_arvoa(3)
	main-->ratikka6: osta_lippu(kallen_kortti, 0)
	ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
	main-->bussi244: osta_lippu(kallen_kortti, 2)
	bussi244->>kallen_kortti: vahenna_arvoa(3.5)
	kallen_kortti->>bussi244: False
