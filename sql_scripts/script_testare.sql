--Adaugati coloana metoda_recoltare in tabela detalii_teste, de tip varchar(40)--
ALTER TABLE detalii_teste
ADD(metoda_recoltare varchar(40));

--In tabela detalii_teste modificati metoda_recoltarii--
UPDATE detalii_teste
SET metoda_recoltare = 'exsudat nazofaringian și faringian'
WHERE id_test = '4';

--In tabela asistenti modificati in Marian numele asistentului care are codul 103--
UPDATE asistenti
SET nume_asistent = 'Marian', email = 'marian@ceva.com'
WHERE cod_asistent = 103;

--In tabela teste modificati pretul testului 'Calciu ionic' sa fie de 2 ori mai mare--
UPDATE teste
SET pret_test = pret_test * 2
WHERE nume_test = 'Calciu ionic';

--In tabela teste modificati pretul testului 'ARN Viral SARS-CoV-2' astfel incat sa fie aplicata o reducere de 5%--
UPDATE teste
SET pret_test = pret_test - pret_test*5/100
WHERE nume_test = 'ARN Viral SARS-CoV-2';

--Sa se afiseze pacientii, testul pe care l-au efectuat si pretul testului--
SELECT p.nume_pacient, t.nume_test, t.pret_test
FROM teste_efectuate e, teste t, pacienti p
WHERE e.id_test = t.id_test
AND p.id_pacient = e.id_pacient;

--Sa se afiseze pacientii, testul pe care l-au efectuat si de asemenea rezultatul si intervalul de referinta--
SELECT p.nume_pacient, t.nume_test, b.rezultat, d.interval_referinta
FROM teste_efectuate e, teste t, pacienti p, detalii_teste d, buletine_teste b
WHERE e.id_test = t.id_test 
AND d.id_test =  t.id_test
AND p.id_pacient = e.id_pacient
AND b.id_test_efectuat = e.id_test_efectuat;

--Sa se afiseze informatiile de pe buletinul de test al pacientului Maria--
SELECT p.nume_pacient, t.nume_test, r.rezultat, d.unitate_masura, d.interval_referinta, d.metoda_prelucrare
FROM pacienti p, teste t, teste_efectuate e, buletine_teste r, detalii_teste d
WHERE  e.id_pacient=p.id_pacient
AND t.id_test=e.id_test
AND d.id_test = e.id_test
AND p.cnp= 6150501220018
AND r.id_test_efectuat = e.id_test_efectuat; 

--Ce teste a efectuat pacientul cu cnp-ul 6150501220018 v1?--    
SELECT p.nume_pacient, t.nume_test
FROM pacienti p, teste t, teste_efectuate e
WHERE  e.id_pacient=p.id_pacient
AND t.id_test=e.id_test
AND p.cnp = 6150501220018;

--Ce teste a efectuat pacientul cu cnp-ul 6150501220018 v2?--
SELECT p.nume_pacient, t.nume_test
FROM pacienti p
JOIN teste_efectuate e on e.id_pacient=p.id_pacient 
JOIN teste t on t.id_test=e.id_test
WHERE p.cnp = 6150501220018;  

-- Ce teste a efectuat pacientul cu cnp-ul 2901009220086 si pretul acestora--
SELECT p.nume_pacient, t.nume_test,t.pret_test
FROM pacienti p, teste t, teste_efectuate e
WHERE t.id_test=e.id_test
AND p.cnp = 2901009220086
AND e.id_pacient=p.id_pacient;

--Care este testul cu pretul cel mai mare--
SELECT nume_test
FROM teste
WHERE pret_test=(SELECT max(pret_test) FROM teste);

--Sa se afiseze pacientii care au efectuat testul ARN Viral SARS-CoV-2--
SELECT p.nume_pacient, t.nume_test
FROM pacienti p, teste t, teste_efectuate e
WHERE t.id_test=e.id_test
AND p.id_pacient = e.id_pacient
AND t.nume_test = 'ARN Viral SARS-CoV-2';

--Sa se specifice numarul de teste efectuate de fiecare asistent--
SELECT a.nume_asistent, COUNT(e.id_test_efectuat)
FROM asistenti a,  teste_efectuate e
WHERE a.id_asistent = e.id_asistent
GROUP BY a.nume_asistent,e.id_asistent;

--Sa se specifice numarul de teste prelucrate de fiecare laborant--
SELECT l.nume_laborant, COUNT(e.id_test_efectuat)
FROM laboranti l,  teste_efectuate e
WHERE l.id_laborant = e.id_laborant
GROUP BY l.nume_laborant,e.id_laborant;

--Care sunt testele la care s-a folosit ca si metoda de prelucrare spectrofotometria?--
SELECT t.nume_test, d.metoda_prelucrare
FROM teste t, detalii_teste d
WHERE t.id_test = d.id_test
AND d.metoda_prelucrare = 'spectrofotometrie';

--Total incasari pentru data curenta--
SELECT SUM(total_plata) total_incasari
FROM plati;

--Total plata pentru fiecare pacient--
SELECT pa.nume_pacient,p.total_plata
FROM pacienti pa, plati p
WHERE pa.id_pacient = p.id_pacient;

--Cate teste negative avem pentru testul ARN Viral SARS-CoV-2? --
SELECT nume_test,COUNT(rezultat) AS Teste_negative
FROM teste, buletine_teste
WHERE rezultat = 'Nedetectabil'
AND nume_test = 'ARN Viral SARS-CoV-2'
GROUP BY nume_test;

--Cate teste pozitive avem pentru testul ARN Viral SARS-CoV-2?--
SELECT nume_test,COUNT(rezultat) AS Teste_pozitive
FROM teste, buletine_teste
WHERE rezultat = 'Detectat'
AND nume_test = 'ARN Viral SARS-CoV-2'
GROUP BY nume_test;

--Ce teste au fost recoltate la data curenta?--
SELECT e.data_recoltare,t.nume_test
FROM teste_efectuate e, teste t
WHERE t.id_test = e.id_test;

--Ce teste au fost prelucrate in data de SYSDATE+2?--
SELECT data_prelucrare,t.nume_test
FROM teste_efectuate e, teste t
WHERE t.id_test = e.id_test
AND trunc(data_prelucrare) = TO_DATE(SYSDATE+2);

--Ce teste au fost validate in data de SYSDATE+3?--
SELECT data_validare,t.nume_test
FROM teste_efectuate e, teste t, buletine_teste b
WHERE t.id_test = e.id_test
AND b.id_test_efectuat = e.id_test_efectuat
AND trunc(data_validare) = TO_DATE(SYSDATE+3);

--Caror buletine apartin testele efectuate?--    
SELECT t.nume_test, b.id_buletin_test
FROM teste t, buletine_teste b, teste_efectuate e
WHERE t.id_test = e.id_test
AND e.id_test_efectuat = b.id_test_efectuat;

--Cate teste sunt intr-un buletin pentru pacientul cu cnp-ul 6150501220018--
SELECT p.nume_pacient,COUNT(e.id_pacient) AS Numar_teste
FROM pacienti p, teste_efectuate e
WHERE p.cnp = 6150501220018
AND p.id_pacient = e.id_pacient
GROUP BY nume_pacient;

--Suma totala de plata a unui pacient--
SELECT p.nume_pacient, SUM(t.pret_test) AS total
FROM pacienti p,teste t, teste_efectuate e
WHERE cnp = 6150501220018
AND p.id_pacient = e.id_pacient
AND t.id_test = e.id_test
GROUP BY nume_pacient;

--Stergeti inregistrarea din tabela pacienti pentru pacientul cu cnp-ul 1891030220035--
DELETE FROM pacienti
WHERE cnp = 1891030220035;

--Stergeti inregistrarea din tabela asistenti pentru asistentul care are codul 106--
DELETE FROM asistenti
WHERE cod_asistent = 106;

--Stergeti inregistrarea din tabela laboranti pentru laborantul care are codul 103--
DELETE FROM laboranti
WHERE cod_laborant = 103;

--Stergeti inregistrarea din tabela teste pentru testul 'Celule lupice'--
DELETE FROM teste
WHERE nume_test = 'Celule lupice';




