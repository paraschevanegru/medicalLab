INSERT INTO pacienti VALUES (NULL, 'Maria', 6150501220018, TO_DATE('01.05.2015', 'DD.MM.YYYY'), '0747454541', 'maria@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Stefan', 5110123220021, TO_DATE('23.01.2011', 'DD.MM.YYYY'), '0747434342', 'stefan@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Tudor', 1991114220036, TO_DATE('14.12.1999', 'DD.MM.YYYY'), '0747454543', 'tudor@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Madalina',2700311220047 , TO_DATE('12.03.1970', 'DD.MM.YYYY'), '0747434344', 'madalina@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Mihaela',2860921220052 , TO_DATE('21.09.1986', 'DD.MM.YYYY'), '0747454545', 'mihaela@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Matei', 5001202220065, TO_DATE('02.12.2000', 'DD.MM.YYYY'), '0747434346', 'stefan@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Luca', 5030715220079, TO_DATE('15.07.2003', 'DD.MM.YYYY'), '0747454547', 'luca@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Anca', 2901009220086, TO_DATE('09.10.1990', 'DD.MM.YYYY'), '0747434348', 'anca@ceva.com' );
INSERT INTO pacienti VALUES (NULL, 'Robert', 1891030220035, TO_DATE('30.10.1989', 'DD.MM.YYYY'), '0747434348', 'robert@ceva.com' );
SELECT * FROM pacienti;


INSERT INTO asistenti VALUES (NULL, 100, 'Mihai', '0747454541', 'mihai@ceva.com' );
INSERT INTO asistenti VALUES (NULL, 102, 'Alex', '0747454549', 'alex@ceva.com' );
INSERT INTO asistenti VALUES (NULL, 103, 'Sofia', '0788857542', 'sofia@ceva.com' );
INSERT INTO asistenti VALUES (NULL, 104, 'Teodora', '0747484545', 'teodora@ceva.com' );
INSERT INTO asistenti VALUES (NULL, 105, 'Ioan', '0747384545', 'ioan@ceva.com' );
INSERT INTO asistenti VALUES (NULL, 106, 'Maria', '0739984545', 'maria@ceva.com' );
SELECT * FROM asistenti;

INSERT INTO programari VALUES (NULL, 140121, TO_DATE('14.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 5030715220079), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 100));
INSERT INTO programari VALUES (NULL, 230121, TO_DATE('23.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 5001202220065), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 100));
INSERT INTO programari VALUES (NULL, 240121, TO_DATE('24.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 5110123220021), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 104));
INSERT INTO programari VALUES (NULL, 140121, TO_DATE('14.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 2860921220052), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 105));
INSERT INTO programari VALUES (NULL, 140121, TO_DATE('14.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 1991114220036), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 104));
INSERT INTO programari VALUES (NULL, 110121, TO_DATE('11.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 6150501220018), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 103));
INSERT INTO programari VALUES (NULL, 100121, TO_DATE('10.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 2700311220047), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 103));
INSERT INTO programari VALUES (NULL, 190121, TO_DATE('19.01.2021', 'DD.MM.YYYY'), (SELECT id_pacient FROM pacienti WHERE cnp = 2901009220086), ( SELECT id_asistent FROM asistenti WHERE cod_asistent = 102));
--INSERT INTO programari VALUES (NULL, 190121, TO_DATE('19.01.2021', 'DD.MM.YYYY'), );--
SELECT * FROM programari;

INSERT INTO laboranti VALUES (NULL, 101, 'Andreea', 'Chimist', '0788867542', 'andreea@ceva.com' );
INSERT INTO laboranti VALUES (NULL, 105, 'Andrei', 'Biochimist', '0789867542', 'andrei@ceva.com' );
INSERT INTO laboranti VALUES (NULL, 106, 'Cosmin', 'Biochimist', '0747463545', 'cosmin@ceva.com' );
INSERT INTO laboranti VALUES (NULL, 107, 'Gabriela', 'Biolog Medical', '0778867542', 'gabriela@ceva.com' );
INSERT INTO laboranti VALUES (NULL, 109, 'Eduard', 'Chimist', '0778367542', 'eduard@ceva.com' );
INSERT INTO laboranti VALUES (NULL, 103, 'Andreea', 'Biochimist', '0778388542', 'andreea@ceva.com' );
SELECT * FROM laboranti;


INSERT INTO tipuri_teste VALUES (NULL, 'Hematologie');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Biochimie');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Biologie moleculara');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Microbiologie');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Markeri endocrini');
INSERT INTO tipuri_teste VALUES (NULL, 'Alergologie');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Citogenetica');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Histopatologie');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Imunologie');
INSERT INTO tipuri_teste (denumire_tip_test) VALUES ('Toxicologie');
SELECT * FROM tipuri_teste;


INSERT INTO Teste VALUES (NULL, 'Concentrat leucocitar', 50, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Hematologie'));
INSERT INTO detalii_teste values(teste_id_test_seq.currval,'absente elemente celulare anormale','-' ,'examinare microscopică');

INSERT INTO Teste VALUES (NULL, 'Calciu ionic', 16, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Biochimie'));
INSERT INTO detalii_teste values(teste_id_test_seq.currval,'3.60-5.20','mg/dl','spectrofotometrie');

INSERT INTO Teste VALUES (NULL, 'FT4 (Tiroxina liberă)', 47, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Markeri endocrini'));
INSERT INTO detalii_teste values(teste_id_test_seq.currval,'0.89-1.76','ng/dL','electrochemiluminiscenţă ');

INSERT INTO Teste VALUES (NULL, 'ARN Viral SARS-CoV-2', 285, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Biologie moleculara'));
INSERT INTO detalii_teste values(teste_id_test_seq.currval,'Nedetectabil (Negativ)', '-','RT-PCR');

INSERT INTO Teste VALUES (NULL, 'Sideremie(Fier seric)', 16, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Biochimie'));
INSERT INTO detalii_teste values(teste_id_test_seq.currval,'50.00-170.00','ug/dl','spectrofotometrie');

INSERT INTO Teste VALUES (NULL, 'Exsudat faringian pentru fuzospirili', 34, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Microbiologie'));
INSERT INTO detalii_teste values(teste_id_test_seq.currval,' absenti fusospirili', '-','examen microscopic');

INSERT INTO Teste VALUES (NULL, 'Celule lupice', 50, DEFAULT, (SELECT id_tip_test FROM tipuri_teste WHERE denumire_tip_test ='Hematologie'));

SELECT * FROM teste;
SELECT * FROM detalii_teste;

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+2,
( SELECT id_pacient FROM pacienti WHERE cnp = 5110123220021),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 100),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 109),
( SELECT id_test FROM teste WHERE nume_test='Sideremie(Fier seric)'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+2,
( SELECT id_pacient FROM pacienti WHERE cnp = 5030715220079),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 100),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 101),
( SELECT id_test FROM teste WHERE nume_test='Calciu ionic'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+2,
( SELECT id_pacient FROM pacienti WHERE cnp = 2700311220047),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 104),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 107),
( SELECT id_test FROM teste WHERE nume_test='Exsudat faringian pentru fuzospirili'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+1,
( SELECT id_pacient FROM pacienti WHERE cnp = 5001202220065),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 105),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 101),
( SELECT id_test FROM teste WHERE nume_test='FT4 (Tiroxina liberă)'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+1,
( SELECT id_pacient FROM pacienti WHERE cnp = 2901009220086),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 104),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 109),
( SELECT id_test FROM teste WHERE nume_test='Concentrat leucocitar'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+2,
( SELECT id_pacient FROM pacienti WHERE cnp = 2860921220052),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 103),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 106),
( SELECT id_test FROM teste WHERE nume_test='ARN Viral SARS-CoV-2'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+1,
( SELECT id_pacient FROM pacienti WHERE cnp = 1991114220036),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 103),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 105),
( SELECT id_test FROM teste WHERE nume_test='ARN Viral SARS-CoV-2'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+1,
( SELECT id_pacient FROM pacienti WHERE cnp = 6150501220018),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 100),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 107),
( SELECT id_test FROM teste WHERE nume_test='Calciu ionic'));

INSERT INTO teste_efectuate values (NULL, SYSDATE, SYSDATE+1,
( SELECT id_pacient FROM pacienti WHERE cnp = 6150501220018),
( SELECT id_asistent FROM asistenti WHERE cod_asistent = 102),
( SELECT id_laborant FROM laboranti WHERE cod_laborant = 105),
( SELECT id_test FROM teste WHERE nume_test='ARN Viral SARS-CoV-2'));

SELECT * FROM teste_efectuate;


INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'39.49',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 5110123220021 AND t.id_pacient = p.id_pacient));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'1.15',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 5001202220065 AND t.id_pacient = p.id_pacient));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'4.25',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 5030715220079 AND t.id_pacient = p.id_pacient));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+3,'Nedetectabil',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 2860921220052 AND t.id_pacient = p.id_pacient));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+3,'Nedetectabil',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 1991114220036 AND t.id_pacient = p.id_pacient));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'3.15',
(SELECT t.id_test_efectuat FROM teste_efectuate t, teste ts, pacienti p 
WHERE p.cnp = 6150501220018 
AND t.id_pacient = p.id_pacient 
AND ts.nume_test = 'Calciu ionic' 
AND t.id_test = ts.id_test ));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'Detectat',
(SELECT t.id_test_efectuat FROM teste_efectuate t, teste ts, pacienti p 
WHERE p.cnp = 6150501220018 
AND t.id_pacient = p.id_pacient 
AND ts.nume_test = 'ARN Viral SARS-CoV-2' 
AND t.id_test = ts.id_test ));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'prezenti fusospirili',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 2700311220047 AND t.id_pacient = p.id_pacient));
INSERT INTO buletine_teste VALUES (NULL, SYSDATE+2,'absente',(SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = 2901009220086 AND t.id_pacient = p.id_pacient));

SELECT * FROM buletine_teste;
    
INSERT INTO plati VALUES (NULL, SYSDATE,16, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 5030715220079));
INSERT INTO plati VALUES (NULL, SYSDATE,47, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 5001202220065));
INSERT INTO plati VALUES (NULL, SYSDATE,16, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 5110123220021));
INSERT INTO plati VALUES (NULL, SYSDATE,285, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 2860921220052));
INSERT INTO plati VALUES (NULL, SYSDATE,285, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 1991114220036));
INSERT INTO plati VALUES (NULL, SYSDATE,301, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 6150501220018));
INSERT INTO plati VALUES (NULL, SYSDATE,34, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 2700311220047));
INSERT INTO plati VALUES (NULL, SYSDATE,50, DEFAULT, (SELECT id_pacient FROM pacienti WHERE cnp = 2901009220086));

SELECT * FROM plati;


COMMIT;



