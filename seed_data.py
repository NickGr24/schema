"""
Скрипт для заполнения базы данных полными данными УПК РМ.
Источник: Codul de Procedură Penală al Republicii Moldova (Nr. 122 din 14.03.2003)
Запуск: python manage.py shell < seed_data.py
"""

from flowchart.models import (
    ProcedureCategory, LegalArticle, ProcedureStage, StageConnection
)

# Очистка старых данных
StageConnection.objects.all().delete()
ProcedureStage.objects.all().delete()
LegalArticle.objects.all().delete()
ProcedureCategory.objects.all().delete()

print("Создание категорий...")

# ==================== КАТЕГОРИИ ====================

cat_general = ProcedureCategory.objects.create(
    name="Dispoziții generale",
    name_ru="Общие положения",
    slug="dispozitii-generale",
    order=1,
    color="#6366f1"
)

cat_urmarire = ProcedureCategory.objects.create(
    name="Urmărirea penală",
    name_ru="Уголовное преследование",
    slug="urmarirea-penala",
    order=2,
    color="#3b82f6"
)

cat_masuri = ProcedureCategory.objects.create(
    name="Măsuri preventive",
    name_ru="Меры пресечения",
    slug="masuri-preventive",
    order=3,
    color="#f59e0b"
)

cat_judecata = ProcedureCategory.objects.create(
    name="Judecata",
    name_ru="Судебное разбирательство",
    slug="judecata",
    order=4,
    color="#8b5cf6"
)

cat_cai_atac = ProcedureCategory.objects.create(
    name="Căile de atac",
    name_ru="Обжалование",
    slug="caile-de-atac",
    order=5,
    color="#ec4899"
)

cat_executare = ProcedureCategory.objects.create(
    name="Executarea hotărârilor",
    name_ru="Исполнение решений",
    slug="executarea-hotararilor",
    order=6,
    color="#ef4444"
)

print("Создание статей УПК...")

# ==================== СТАТЬИ УПК ====================

# --- SESIZAREA ---
art_262 = LegalArticle.objects.create(
    article_number="262",
    title="Sesizarea organului de urmărire penală",
    content="""(1) Organul de urmărire penală poate fi sesizat despre săvîrșirea sau pregătirea pentru săvîrșirea unei infracțiuni prevăzute de Codul penal prin:
1) plîngere;
2) denunț;
3) autodenunț;
4) depistarea nemijlocit de către organul de urmărire penală sau procuror a bănuielii rezonabile cu privire la săvîrșirea unei infracțiuni.

(2) Dacă, potrivit legii, pornirea urmăririi penale se poate face numai la plângerea prealabilă, urmărirea penală nu poate începe în lipsa acesteia.

(3) În cazul depistării infracțiunii nemijlocit de către ofițerul de urmărire penală sau de către procuror, acesta întocmește un proces-verbal în care expune circumstanțele depistate și dispune înregistrarea sesizării.""",
    content_ru="""(1) Орган уголовного преследования может быть уведомлен о совершении или подготовке преступления, предусмотренного Уголовным кодексом, посредством:
1) жалобы;
2) заявления;
3) явки с повинной;
4) непосредственного обнаружения органом уголовного преследования или прокурором обоснованного подозрения в совершении преступления.""",
    chapter="Capitolul II. Sesizarea organului de urmărire penală",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_263 = LegalArticle.objects.create(
    article_number="263",
    title="Plîngerea și denunțul",
    content="""(1) Plîngerea este înștiințarea făcută de o persoană fizică sau de o persoană juridică căreia i s-a cauzat un prejudiciu prin infracțiune.

(2) Denunțul este înștiințarea făcută de o persoană fizică sau de o persoană juridică despre săvîrșirea unei infracțiuni.

(3) Plîngerea sau, după caz, denunțul trebuie să cuprindă: numele, prenumele, calitatea și domiciliul petițioarului, descrierea faptei care formează obiectul plîngerii sau denunțului, indicarea făptuitorului, dacă acesta este cunoscut, și a mijloacelor de probă.

(7) Persoanei care face denunț sau plîngere i se explică răspunderea pe care o poartă în caz dacă denunțul sau plîngerea este intenționat calomnios/oasă.

(8) Plîngerile și denunțurile anonime nu pot servi temei pentru pornirea urmăririi penale.""",
    chapter="Capitolul II. Sesizarea organului de urmărire penală",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_264 = LegalArticle.objects.create(
    article_number="264",
    title="Autodenunțarea",
    content="""(1) Autodenunțarea este înștiințarea benevolă făcută de o persoană fizică sau de o persoană juridică despre săvîrșirea de către ea a unei infracțiuni în cazul în care organele de urmărire penală nu sînt la curent cu această faptă.

(2) Declarația de autodenunțare se face în scris sau oral. În cazul în care autodenunțarea se face oral, despre aceasta se întocmește un proces-verbal cu înregistrarea audio și video a declarației de autodenunțare.

(3) Persoanei care face declarație de autodenunțare, înainte de a o face, i se explică dreptul de a nu spune nimic și de a nu se autoincrimina.""",
    chapter="Capitolul II. Sesizarea organului de urmărire penală",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_265 = LegalArticle.objects.create(
    article_number="265",
    title="Obligativitatea primirii și examinării plîngerilor sau denunțurilor",
    content="""(1) Organul de urmărire penală este obligat să primească plângerile sau denunțurile referitoare la infracțiunile săvârșite, pregătite sau în curs de pregătire chiar și în cazul în care cauza nu este de competența lui. Plângerea sau denunțul se înregistrează în Registrul de evidență a sesizărilor cu privire la infracțiuni. Persoana care a depus plângerea sau denunțul primește o confirmare a recepționării sesizării.

(2) Refuzul organului de urmărire penală de a primi plângerea sau denunțul poate fi contestat la procuror în termen de 15 zile.""",
    chapter="Capitolul II. Sesizarea organului de urmărire penală",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- PORNIREA URMĂRIRII PENALE ---
art_274 = LegalArticle.objects.create(
    article_number="274",
    title="Începerea urmăririi penale",
    content="""(1) Organul de urmărire penală sau procurorul sesizat dispune în termen de 45 de zile, prin ordonanță, începerea urmăririi penale în cazul în care, din cuprinsul actului de sesizare sau al actelor de constatare, rezultă cel puțin o bănuială rezonabilă că a fost săvîrșită o infracțiune și nu există vreuna din circumstanțele care exclud urmărirea penală.

(2) În cazul în care organul de urmărire penală sau procurorul se autosesizează, el întocmește un proces-verbal în care consemnează cele constatate privitor la infracțiunea depistată, apoi, prin ordonanță, dispune începerea urmăririi penale.

(3) Ordonanța de începere a urmăririi penale, în termen de 24 de ore, se aduce la cunoștință în scris procurorului care efectuează conducerea activității de urmărire penală.

(5) În cazul în care procurorul refuză pornirea urmăririi penale, el confirmă faptul prin ordonanță motivată și anunță despre aceasta persoana care a înaintat sesizarea în termen de 15 zile.

(6) Ordonanța de a refuza începerea urmăririi penale poate fi atacată, prin plîngere, în instanța judecătorească.""",
    content_ru="""(1) Орган уголовного преследования или прокурор в течение 45 дней выносит постановление о начале уголовного преследования, если из содержания сообщения о преступлении следует обоснованное подозрение в совершении преступления.""",
    chapter="Capitolul IV. Pornirea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_275 = LegalArticle.objects.create(
    article_number="275",
    title="Circumstanțele care exclud urmărirea penală",
    content="""Urmărirea penală nu poate fi pornită, iar dacă a fost pornită, nu poate fi efectuată, și va fi încetată în cazurile în care:

1) nu există faptul infracțiunii;
2) fapta nu este prevăzută de legea penală ca infracțiune;
3) fapta nu întrunește elementele infracțiunii;
4) a intervenit termenul de prescripție sau amnistia;
4¹) fapta constituie contravenție;
5) a intervenit decesul făptuitorului;
6) lipsește plîngerea victimei în cazurile în care urmărirea penală începe numai în baza plîngerii acesteia sau plîngerea prealabilă a fost retrasă;
7) în privința unei persoane există o hotărîre judecătorească definitivă în legătură cu aceeași acuzație;
8) în privința unei persoane există o hotărâre neanulată de neîncepere a urmăririi penale;
9) există alte circumstanțe prevăzute de Codul penal care exclud urmărirea penală.""",
    content_ru="""Уголовное преследование не может быть начато, а начатое подлежит прекращению при наличии следующих обстоятельств: отсутствие факта преступления, отсутствие состава преступления, истечение срока давности, амнистия, смерть обвиняемого и др.""",
    chapter="Capitolul IV. Pornirea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_276 = LegalArticle.objects.create(
    article_number="276",
    title="Pornirea urmăririi penale în baza plîngerii victimei",
    content="""(1) Urmărirea penală se pornește numai în baza plîngerii prealabile a victimei în cazul infracțiunilor prevăzute în articolele: 152 alin.(1), 155, 157, 161, 177, 179 alin.(1) și (2), 193, 194, 197 alin.(1), 204 și 246¹ din Codul penal.

(4) Dacă victima nu este în stare să-și apere drepturile, procurorul pornește urmărirea penală chiar dacă victima nu a depus plîngere.

(5) La împăcarea părții vătămate cu bănuitul, învinuitul, inculpatul, urmărirea penală încetează. Împăcarea este personală și produce efect doar dacă intervine pînă la rămînerea definitivă a hotărîrii judecătorești.

(7) Împăcarea părților poate avea loc și prin aplicarea medierii conform Legii cu privire la mediere.""",
    chapter="Capitolul IV. Pornirea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- DESFĂȘURAREA URMĂRIRII ---
art_279 = LegalArticle.objects.create(
    article_number="279",
    title="Efectuarea acțiunilor de urmărire penală",
    content="""(1) Acțiunile procesuale se efectuează în strictă conformitate cu prevederile prezentului cod și numai după înregistrarea sesizării cu privire la infracțiune. Acțiunile de urmărire penală pentru efectuarea cărora este necesară autorizarea judecătorului de instrucție, precum și măsurile procesuale de constrîngere sînt pasibile de realizare doar după pornirea urmăririi penale.

(2) Orice acțiune de urmărire penală în incinta unei unități publice sau private se poate efectua doar cu consimțămîntul conducerii sau cu autorizația procurorului.

(3) Cercetarea, percheziția, ridicarea de obiecte și alte acțiuni procesuale la domiciliu pot fi efectuate doar cu consimțămîntul persoanei domiciliate sau cu autorizația respectivă.

(4) În cazul infracțiunilor flagrante, precum și în cazurile ce nu suferă amînare, consimțămîntul sau autorizația nu sînt necesare.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_280 = LegalArticle.objects.create(
    article_number="280",
    title="Propunerea de punere sub învinuire",
    content="""(1) În cazul în care există suficiente probe că infracțiunea a fost săvîrșită de o anumită persoană, organul de urmărire penală întocmește un raport cu propunerea de a pune persoana respectivă sub învinuire. Raportul cu materialele cauzei se înaintează procurorului.

(2) În cazul în care organul de urmărire penală consideră că sînt întrunite condițiile prevăzute de lege pentru luarea măsurii preventive, el înaintează propuneri și în această privință.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_281 = LegalArticle.objects.create(
    article_number="281",
    title="Punerea sub învinuire",
    content="""(1) Dacă, după examinarea raportului organului de urmărire penală și a materialelor cauzei, procurorul consideră că probele acumulate sînt concludente și suficiente, el emite o ordonanță de punere sub învinuire a persoanei.

(2) Ordonanța de punere sub învinuire trebuie să cuprindă: data și locul întocmirii; numele, prenumele, ziua, luna, anul și locul nașterii persoanei puse sub învinuire; formularea învinuirii cu indicarea datei, locului, mijloacelor și modului de săvîrșire a infracțiunii și consecințele ei, formelor vinovăției, motivelor și semnelor calificative pentru încadrarea juridică a faptei.

(3) În cazul în care învinuitul este tras la răspundere pentru săvîrșirea mai multor infracțiuni, în ordonanță se arată care anume infracțiuni au fost săvîrșite și articolele care prevăd răspunderea.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_282 = LegalArticle.objects.create(
    article_number="282",
    title="Înaintarea acuzării",
    content="""(1) Înaintarea acuzării învinuitului se va face de către procuror în prezența avocatului în decurs de 48 de ore din momentul emiterii ordonanței de punere sub învinuire, dar nu mai tîrziu de ziua în care învinuitul s-a prezentat sau a fost adus în mod silit.

(2) Procurorul, după stabilirea identității învinuitului, îi aduce la cunoștință ordonanța de punere sub învinuire și îi explică conținutul ei.

(3) După înaintarea acuzării, procurorul îi va explica învinuitului drepturile și obligațiile acestuia prevăzute în art. 66. Învinuitului i se înmînează copia de pe ordonanța de punere sub învinuire.

(4) Învinuitul este audiat în aceeași zi în condițiile prevăzute în art. 104.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- SCOATEREA, ÎNCETAREA, CLASAREA ---
art_284 = LegalArticle.objects.create(
    article_number="284",
    title="Scoaterea persoanei de sub urmărirea penală",
    content="""(1) Scoaterea persoanei de sub urmărirea penală este actul de reabilitare și finalizare în privința persoanei a oricăror acțiuni de urmărire penală în legătură cu fapta anterior imputată.

(2) Scoaterea persoanei de sub urmărirea penală are loc cînd aceasta este bănuit sau învinuit și se constată că:
1) fapta nu a fost săvîrșită de bănuit sau învinuit;
2) există vreuna din circumstanțele prevăzute la art. 275 pct. 1)–3);
3) există cel puțin una din cauzele prevăzute la art. 35 din Codul penal.

(3) Procurorul, în cazul în care constată temeiurile prevăzute, dispune, prin ordonanță motivată, scoaterea persoanei de sub urmărirea penală.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_285 = LegalArticle.objects.create(
    article_number="285",
    title="Încetarea urmăririi penale",
    content="""(1) Încetarea urmăririi penale este actul de liberare a persoanei de răspunderea penală și de finalizare a acțiunilor procedurale, în cazul în care pe temei de nereabilitare legea împiedică continuarea acesteia.

(2) Încetarea urmăririi penale are loc în cazurile de nereabilitare a persoanei, prevăzute la art. 275 pct. 4)–9), precum și dacă:
1) plîngerea prealabilă a fost retrasă, a fost încheiată o tranzacție în cadrul procesului de mediere sau părțile s-au împăcat;
2) persoana nu a atins vîrsta la care poate fi trasă la răspundere penală;
3) persoana a săvîrșit o faptă prejudiciabilă fiind în stare de iresponsabilitate.

(4) Încetarea urmăririi penale se dispune de către procuror prin ordonanță.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_286 = LegalArticle.objects.create(
    article_number="286",
    title="Clasarea procesului penal",
    content="""Clasarea procesului penal este actul de finalizare a oricăror acțiuni procesuale într-o cauză penală sau pe marginea unei sesizări cu privire la infracțiune. Clasarea procesului penal se dispune printr-o ordonanță motivată a procurorului, fie concomitent cu încetarea urmăririi penale sau scoaterea integrală de sub urmărirea penală, fie cînd în cauza penală nu este bănuit sau învinuit și există una din circumstanțele prevăzute la art. 275 pct. 1)–3).""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_287 = LegalArticle.objects.create(
    article_number="287",
    title="Reluarea urmăririi penale",
    content="""(1) Reluarea urmăririi penale după încetarea urmăririi penale, după scoaterea persoanei de sub urmărire și/sau după clasarea cauzei se dispune prin ordonanță de către procurorul ierarhic superior dacă se constată că:
1) decizia este afectată de un viciu fundamental;
2) apar fapte noi sau recent descoperite, care existau la data adoptării ordonanței, dar despre care nu avea cunoștință organul de urmărire penală.

(2) Urmărirea penală poate fi reluată și de către judecătorul de instrucție în cazul admiterii plîngerii împotriva ordonanței.

(4) Reluarea urmăririi penale poate avea loc doar în interiorul termenului de prescripție de tragere la răspundere penală.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- TERMINAREA ȘI TRIMITEREA ÎN JUDECATĂ ---
art_291 = LegalArticle.objects.create(
    article_number="291",
    title="Soluțiile dispuse de procuror la terminarea urmăririi penale",
    content="""Dacă procurorul constată că au fost respectate dispozițiile prezentului cod privind urmărirea penală, că urmărirea penală este completă, că există probe suficiente și legal administrate, el dispune una din următoarele soluții:

1) atunci cînd din materialele cauzei rezultă că fapta există, că a fost constatat făptuitorul și că acesta poartă răspundere penală:
a) pune sub învinuire făptuitorul conform prevederilor art.281 și 282, dacă acesta nu a fost pus sub învinuire în cursul urmăririi penale, apoi întocmește rechizitoriul prin care dispune trimiterea cauzei în judecată;
b) dacă făptuitorul a fost pus sub învinuire în cursul urmăririi penale, întocmește rechizitoriul prin care dispune trimiterea cauzei în judecată;

2) prin ordonanță motivată, dispune încetarea urmăririi penale, clasarea cauzei penale sau scoaterea persoanei de sub urmărire.""",
    chapter="Capitolul VI. Terminarea urmăririi penale și trimiterea cauzei în judecată",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_296 = LegalArticle.objects.create(
    article_number="296",
    title="Rechizitoriul",
    content="""(1) După prezentarea materialelor de urmărire penală, procurorul întocmește rechizitoriul imediat sau în limitele termenului rezonabil.

(2) Rechizitoriul se compune din două părți: expunerea și dispozitivul. Expunerea cuprinde informații despre fapta și persoana în privința căreia s-a efectuat urmărirea penală, analiza probelor care confirmă fapta și vinovăția învinuitului, argumentele invocate de învinuit în apărarea sa și rezultatele verificării acestor argumente, circumstanțele care atenuează sau agravează răspunderea învinuitului. Dispozitivul cuprinde date cu privire la persoana învinuitului și formularea învinuirii cu încadrarea juridică și menționarea despre trimiterea dosarului în instanța judecătorească competentă.

(3) Rechizitoriul se semnează de procurorul care l-a întocmit, indicîndu-se locul și data întocmirii lui.

(5) Copia de pe rechizitoriu se înmînează sub recipisă învinuitului și reprezentantului lui legal.""",
    chapter="Capitolul VI. Terminarea urmăririi penale și trimiterea cauzei în judecată",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_297 = LegalArticle.objects.create(
    article_number="297",
    title="Trimiterea cauzei în judecată",
    content="""(1) Cauza se trimite în judecată de către procurorul care a întocmit rechizitoriul.

(2) În cazul în care învinuitul se abține de a se prezenta pentru a lua cunoștință de materialele cauzei și a primi rechizitoriul, procurorul trimite cauza în judecată fără efectuarea acestor acțiuni procesuale, dar cu anexarea la dosar a probelor care confirmă abținerea învinuitului.

(4) Toate cererile, plîngerile și demersurile înaintate după trimiterea cauzei în judecată se soluționează de către instanța care judecă cauza.

(5) În cazul în care inculpatul se află în stare de arest preventiv, procurorul va trimite cauza în judecată cu cel puțin 10 zile pînă la expirarea termenului de arest stabilit.""",
    chapter="Capitolul VI. Terminarea urmăririi penale și trimiterea cauzei în judecată",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- MĂSURI PREVENTIVE ---
art_175 = LegalArticle.objects.create(
    article_number="175",
    title="Noțiunea și categoriile de măsuri preventive",
    content="""(1) Măsurile cu caracter de constrîngere prin care bănuitul, învinuitul, inculpatul este împiedicat să întreprindă anumite acțiuni negative asupra desfășurării procesului penal sau asupra asigurării executării sentinței constituie măsuri preventive.

(3) Măsuri preventive sînt:
1) obligarea de a nu părăsi localitatea;
2) obligarea de a nu părăsi țara;
3) garanția personală;
4) garanția unei organizații;
5) ridicarea provizorie a permisului de conducere;
6) transmiterea sub supraveghere a militarului;
7) transmiterea sub supraveghere a minorului;
8) liberarea provizorie sub control judiciar;
9) liberarea provizorie pe cauțiune;
10) arestarea la domiciliu;
11) arestarea preventivă.

(4) Arestarea la domiciliu și arestarea preventivă pot fi aplicate numai față de învinuit, inculpat.""",
    content_ru="""(1) Меры пресечения - это меры принуждения, которыми подозреваемый, обвиняемый, подсудимый лишается возможности совершать действия, препятствующие уголовному процессу.

(3) Мерами пресечения являются:
1) обязательство не покидать населённый пункт;
2) обязательство не покидать страну;
3) личное поручительство;
4) поручительство организации;
5) временное изъятие водительского удостоверения;
6) передача военнослужащего под наблюдение;
7) передача несовершеннолетнего под наблюдение;
8) временное освобождение под судебный контроль;
9) временное освобождение под залог;
10) домашний арест;
11) предварительное заключение под стражу.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_176 = LegalArticle.objects.create(
    article_number="176",
    title="Temeiurile pentru aplicarea măsurilor preventive",
    content="""(1) Măsurile preventive pot fi aplicate de către procuror sau de către instanța de judecată numai în cazurile în care există suficiente temeiuri rezonabile, susținute prin probe, de a presupune că bănuitul, învinuitul, inculpatul ar putea să se ascundă de organul de urmărire penală sau de instanță, să exercite presiune asupra martorilor, să nimicească sau să deterioreze mijloacele de probă sau să împiedice într-un alt mod stabilirea adevărului în procesul penal, să săvîrșească alte infracțiuni ori că punerea în libertate a acestuia va cauza dezordine publică.

(2) Arestarea preventivă și măsurile alternative de arestare se aplică numai persoanei care este învinuită, inculpată de săvîrșirea unei infracțiuni pentru care legea prevede pedeapsa cu închisoare pe un termen mai mare de 3 ani.

(3) La soluționarea chestiunii privind necesitatea aplicării măsurii preventive respective, procurorul și instanța de judecată vor aprecia: gravitatea și gradul prejudiciabil al faptei incriminate, personalitatea bănuitului, vîrsta și starea sănătății sale, ocupația sa, situația familială și starea materială, dacă are loc permanent de trai.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_178 = LegalArticle.objects.create(
    article_number="178",
    title="Obligarea de a nu părăsi localitatea sau obligarea de a nu părăsi țara",
    content="""(1) Obligarea de a nu părăsi localitatea constă în îndatorirea impusă în scris bănuitului, învinuitului, inculpatului de a se afla la dispoziția organului de urmărire penală sau a instanței, de a nu părăsi localitatea fără încuviințarea procurorului sau a instanței, de a nu se ascunde, de a nu împiedica urmărirea penală și judecarea cauzei, de a se prezenta la citare.

(2) Obligarea de a nu părăsi țara constă în îndatorirea impusă de a nu părăsi țara fără încuviințarea organului care a dispus această măsură.

(3) Durata măsurilor preventive nu poate depăși 60 de zile și poate fi prelungită doar motivat. Fiecare prelungire nu poate depăși 60 de zile.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_185 = LegalArticle.objects.create(
    article_number="185",
    title="Arestarea preventivă",
    content="""(1) Arestarea preventivă constă în deținerea învinuitului, inculpatului în stare de arest în locurile și în condițiile prevăzute de lege. Arestarea preventivă constituie o măsură excepțională și se dispune doar atunci cînd se demonstrează că alte măsuri nu sînt suficiente pentru a înlătura riscurile care justifică aplicarea arestării.

(2) Arestarea preventivă poate fi aplicată în cazurile și în condițiile prevăzute în art.176, luînd în considerare și dacă:
1) învinuitul, inculpatul nu are loc permanent de trai pe teritoriul Republicii Moldova;
3) învinuitul, inculpatul a încălcat condițiile altor măsuri preventive aplicate în privința sa;
4) există probe suficiente asupra faptului că învinuitul, inculpatul, aflîndu-se în libertate, prezintă un risc iminent pentru securitatea și ordinea publică.

(3) La soluționarea chestiunii privind arestarea preventivă, judecătorul are obligația să examineze prioritar oportunitatea aplicării altor măsuri preventive, neprivative de libertate.

(4) Încheierea privind arestarea preventivă poate fi atacată cu recurs în instanța ierarhic superioară.""",
    content_ru="""(1) Предварительное заключение под стражу состоит в содержании обвиняемого, подсудимого под стражей. Является исключительной мерой и применяется только тогда, когда другие меры недостаточны для устранения рисков.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_186 = LegalArticle.objects.create(
    article_number="186",
    title="Termenul ținerii persoanei în stare de arest și prelungirea lui",
    content="""(1) Termenul ținerii persoanei în stare de arest curge de la momentul privării persoanei de libertate la reținerea ei.

(2) Perioada de ținere în arest nu poate depăși un termen rezonabil.

(3) Arestul se dispune pentru un termen de cel mult 30 de zile.

(4) Termenul arestului poate fi prelungit doar atunci cînd alte măsuri preventive neprivative de libertate nu sînt suficiente.

(5) Fiecare perioadă cu care se prelungește arestul preventiv nu poate depăși termenul de 30 de zile.

(6) În privința aceleiași fapte și aceleiași persoane, arestul poate fi aplicat pe un termen de cel mult 12 luni cumulativ, pînă la pronunțarea sentinței de către instanța de fond.

(8) Pentru învinuiții, inculpații minori durata totală de ținere în stare de arest preventiv nu poate depăși termenul de 8 luni.

(12) Urmărirea penală în cauzele penale în care sînt învinuiți arestații preventiv se desfășoară de urgență și în mod preferențial.""",
    content_ru="""(1) Срок содержания под стражей исчисляется с момента лишения свободы.
(3) Арест назначается на срок не более 30 дней.
(6) Максимальный срок ареста - 12 месяцев суммарно (до приговора первой инстанции).
(8) Для несовершеннолетних - не более 8 месяцев.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_188 = LegalArticle.objects.create(
    article_number="188",
    title="Arestarea la domiciliu",
    content="""(1) Arestarea la domiciliu constă în izolarea învinuitului, inculpatului de societate în locuința acestuia, cu stabilirea anumitor restricții.

(2) Arestarea la domiciliu se aplică față de învinuit, inculpat în baza hotărîrii judecătorului de instrucție sau a instanței de judecată în modul prevăzut în art.185 și 186, în condițiile care permit aplicarea măsurii preventive sub formă de arest, însă izolarea lui totală nu este rațională în legătură cu vîrsta, starea sănătății, starea familială sau cu alte împrejurări.

(3) Arestarea la domiciliu este însoțită de una sau mai multe din următoarele restricții:
1) interzicerea de a ieși din locuință;
2) limitarea convorbirilor telefonice, recepționării și expedierii trimiterilor poștale și utilizării altor mijloace de comunicare;
3) interzicerea comunicării cu anumite persoane și primirea pe cineva în locuința sa.

(4) Persoana arestată la domiciliu poate fi supusă obligațiilor:
1) de a menține în stare de funcționare mijloacele electronice de control și de a le purta permanent;
2) de a răspunde la semnalele de control.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- REȚINEREA ---
art_165 = LegalArticle.objects.create(
    article_number="165",
    title="Reținerea",
    content="""(1) Reținerea este o măsură procesuală de constrîngere care constă în privarea de libertate pe termen scurt a persoanei bănuite de săvîrşirea unei infracțiuni.

(2) Reţinerea poate fi aplicată:
1) persoanei în privinţa căreia există o bănuială rezonabilă de săvîrşire a unei infracţiuni pentru care legea prevede pedeapsă cu închisoare pe un termen mai mare de un an, ori
2) persoanei bănuite de săvîrşirea unei infracţiuni pentru care legea prevede pedeapsă cu închisoare pe un termen de pînă la un an, însă care nu are loc permanent de trai pe teritoriul Republicii Moldova sau identitatea căreia nu a fost stabilită sau care a încălcat condiţiile unei măsuri preventive neprivative de libertate ori a comis acţiunile prevăzute la art.176 alin.(1).

(3) Persoana poate fi reținută:
1) cînd este prinsă în flagrant delict;
2) cînd martorul ocular sau partea vătămată indică direct că această persoană a săvîrșit infracțiunea;
3) cînd pe corpul sau pe hainele persoanei, la domiciliul ei ori în unitatea ei de transport sînt descoperite urme evidente ale infracțiunii.

(4) Persoana poate fi reținută și în alte împrejurări dacă sînt probe suficiente pentru a bănui că ea a săvîrșit o infracțiune, însă numai după interogarea ei.""",
    content_ru="""(1) Задержание - это процессуальная мера принуждения, заключающаяся в кратковременном лишении свободы лица, подозреваемого в совершении преступления.

(2) Задержание может применяться к лицу, в отношении которого имеется обоснованное подозрение в совершении преступления, за которое предусмотрено наказание в виде лишения свободы на срок более одного года.

(3) Лицо может быть задержано: при совершении преступления, когда очевидцы указывают на это лицо, когда обнаружены явные следы преступления.""",
    chapter="Capitolul I. Reținerea bănuitului",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_166 = LegalArticle.objects.create(
    article_number="166",
    title="Termenul reținerii",
    content="""(1) Reţinerea nu poate depăşi 72 de ore din momentul privării de libertate a persoanei.

(2) În cazul în care pentru infracțiunea săvîrșită legea prevede pedeapsă cu închisoare pe un termen de pînă la 10 ani sau o pedeapsă mai ușoară, persoana poate fi reținută pe un termen de pînă la 24 de ore. În această perioadă, demersul privind arestarea preventivă trebuie examinat de către judecătorul de instrucție.

(3) Minorul, persoana care nu a atins vîrsta de 18 ani, poate fi reținut pentru un termen care să nu depășească 24 de ore.

(4) În termenul reținerii se include și timpul reținerii administrative dacă aceasta este urmată de reținere.""",
    content_ru="""(1) Задержание не может превышать 72 часов с момента фактического лишения свободы.
(2) За преступления с наказанием до 10 лет - задержание до 24 часов.
(3) Несовершеннолетние могут быть задержаны на срок не более 24 часов.""",
    chapter="Capitolul I. Reținerea bănuitului",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- JUDECATA ---
art_314 = LegalArticle.objects.create(
    article_number="314",
    title="Nemijlocirea, oralitatea și contradictorialitatea judecării cauzei",
    content="""(1) Instanță de judecată este obligată, în cursul judecării cauzei, să cerceteze nemijlocit, sub toate aspectele, probele prezentate de părți sau administrate la cererea acestora, inclusiv să audieze inculpații, părțile vătămate, martorii, să cerceteze corpurile delicte, să dea citire rapoartelor de expertiză judiciară, proceselor-verbale și altor documente, precum și să examineze alte probe.

(2) Instanța de judecată, la judecarea cauzei, creează părții acuzării și părții apărării condiții necesare pentru cercetarea multilaterală și în deplină măsură a circumstanțelor cauzei.""",
    chapter="Capitolul I. Condiţiile generale ale judecării cauzei",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_321 = LegalArticle.objects.create(
    article_number="321",
    title="Participarea inculpatului la judecarea cauzei și efectele neprezentării lui",
    content="""(1) Judecarea cauzei în primă instanță și în instanța de apel are loc cu participarea inculpatului, cu excepția cazurilor prevăzute de prezentul articol.

(2) Judecarea cauzei în lipsa inculpatului poate avea loc în cazul:
1) cînd inculpatul se ascunde de prezentarea în instanță;
2) cînd inculpatul, aflat în detenție, refuză să fie adus în instanță pentru judecarea cauzei;
3) când inculpatul solicită judecarea cauzei în lipsa sa, dacă instanța constată existența circumstanțelor excepționale.

(3) În cazul judecării cauzei în lipsa inculpatului, participarea apărătorului și, după caz, a reprezentantului lui legal este obligatorie.

(5) Instanța, în cazul neprezentării nemotivate a inculpatului la judecarea cauzei, este în drept să dispună aducerea silită a inculpatului și să-i aplice o măsură preventivă.""",
    chapter="Capitolul I. Condiţiile generale ale judecării cauzei",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_325 = LegalArticle.objects.create(
    article_number="325",
    title="Limitele judecării cauzei",
    content="""(1) Judecarea cauzei în primă instanță se efectuează numai în privința persoanei puse sub învinuire și numai în limitele învinuirii formulate în rechizitoriu.

(2) Modificarea învinuirii în instanța de judecată se admite dacă prin aceasta nu se agravează situația inculpatului și nu se lezează dreptul lui la apărare. Modificarea învinuirii în sensul agravării situației inculpatului se admite numai în cazurile și în condițiile prevăzute de prezentul cod.""",
    chapter="Capitolul I. Condiţiile generale ale judecării cauzei",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_384 = LegalArticle.objects.create(
    article_number="384",
    title="Sentința judecătorească",
    content="""(1) Instanța hotărăște asupra învinuirii înaintate inculpatului prin adoptarea sentinței de condamnare, de achitare sau de încetare a procesului penal.

(2) Sentința se adoptă în numele legii.

(3) Sentința instanței de judecată trebuie să fie legală, întemeiată și motivată.

(4) Instanța își întemeiază sentința numai pe probele care au fost cercetate în ședința de judecată.""",
    content_ru="""(1) Суд решает вопрос о предъявленном обвинении путём вынесения обвинительного приговора, оправдательного приговора или приговора о прекращении уголовного процесса.
(2) Приговор выносится именем закона.
(3) Приговор должен быть законным, обоснованным и мотивированным.
(4) Суд основывает приговор только на доказательствах, исследованных в судебном заседании.""",
    chapter="Capitolul III. Deliberarea și adoptarea sentinței",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_385 = LegalArticle.objects.create(
    article_number="385",
    title="Chestiunile pe care trebuie să le soluționeze instanța de judecată la adoptarea sentinței",
    content="""(1) La adoptarea sentinței, instanța de judecată soluționează următoarele chestiuni:
1) dacă a avut loc fapta de săvîrșirea căreia este învinuit inculpatul;
2) dacă această faptă a fost săvîrșită de inculpat;
3) dacă fapta întrunește elementele infracțiunii și de care anume lege penală este prevăzută ea;
4) dacă inculpatul este vinovat de săvîrșirea acestei infracțiuni;
5) dacă inculpatul trebuie să fie pedepsit pentru infracțiunea săvîrșită;
6) dacă există circumstanțe care atenuează sau agravează răspunderea inculpatului și care anume;
7) ce măsură de pedeapsă urmează să fie stabilită inculpatului;
8) dacă măsura de pedeapsă stabilită inculpatului trebuie să fie executată de inculpat sau nu;
9) tipul penitenciarului în care urmează să execute pedeapsa închisorii;
10) dacă trebuie admisă acțiunea civilă;
11-16) alte chestiuni.""",
    chapter="Capitolul III. Deliberarea și adoptarea sentinței",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_389 = LegalArticle.objects.create(
    article_number="389",
    title="Sentința de condamnare",
    content="""(1) Sentința de condamnare se adoptă numai în condiția în care, în urma cercetării judecătorești, vinovăția inculpatului în săvîrșirea infracțiunii a fost confirmată prin ansamblul de probe cercetate de instanța de judecată.

(2) Sentința de condamnare nu poate fi bazată pe presupuneri sau, în mod exclusiv ori în principal, pe declarațiile martorilor depuse în timpul urmăririi penale și citite în instanța de judecată în absența lor.

(4) Sentința de condamnare se adoptă:
1) cu stabilirea pedepsei care urmează să fie executată;
2) cu stabilirea pedepsei și cu liberarea de executarea ei în cazul amnistiei;
3) fără stabilirea pedepsei, cu liberarea de răspundere penală în cazurile prevăzute de Codul penal.""",
    content_ru="""(1) Обвинительный приговор выносится только при условии, что виновность подсудимого в совершении преступления подтверждена совокупностью доказательств, исследованных судом.

(2) Обвинительный приговор не может быть основан на предположениях.

(4) Обвинительный приговор выносится:
1) с назначением наказания;
2) с назначением наказания и освобождением от его отбывания;
3) без назначения наказания, с освобождением от уголовной ответственности.""",
    chapter="Capitolul III. Deliberarea și adoptarea sentinței",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_390 = LegalArticle.objects.create(
    article_number="390",
    title="Sentința de achitare",
    content="""(1) Sentința de achitare se adoptă dacă:
1) nu s-a constatat existența faptei infracțiunii;
2) fapta nu a fost săvîrșită de inculpat;
3) fapta inculpatului nu întrunește elementele infracțiunii;
4) fapta nu este prevăzută de legea penală;
5) există una din cauzele care înlătură caracterul penal al faptei.

(2) În cazul achitării persoanei în temeiul alin.(1) pct.2), organul de urmărire penală este obligat să continue urmărirea penală pentru identificarea făptuitorului.

(3) Sentința de achitare duce la reabilitarea deplină a inculpatului.""",
    content_ru="""(1) Оправдательный приговор выносится, если:
1) не установлено событие преступления;
2) деяние не совершено подсудимым;
3) деяние не содержит состава преступления;
4) деяние не предусмотрено уголовным законом;
5) имеются обстоятельства, устраняющие преступный характер деяния.

(3) Оправдательный приговор влечёт полную реабилитацию подсудимого.""",
    chapter="Capitolul III. Deliberarea și adoptarea sentinței",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_391 = LegalArticle.objects.create(
    article_number="391",
    title="Sentința de încetare a procesului penal",
    content="""(1) Sentința de încetare a procesului penal se adoptă dacă:
1) lipsește plîngerea părții vătămate, plîngerea a fost retrasă sau părțile sau împăcat;
2) a intervenit decesul inculpatului;
3) persoana nu a atins vîrsta pentru tragere la răspundere penală;
4) există o hotărîre judecătorească definitivă asupra aceleiași persoane pentru aceeași faptă;
5) există o hotărîre a organului de urmărire penală asupra aceleiași persoane pentru aceeași faptă;
6) există alte circumstanțe care exclud sau condiționează pornirea urmăririi penale și tragerea la răspundere penală;
7) în cazurile prevăzute în art.54-56 din Codul penal.""",
    chapter="Capitolul III. Deliberarea și adoptarea sentinței",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- CĂILE DE ATAC - APELUL ---
art_400 = LegalArticle.objects.create(
    article_number="400",
    title="Hotărîrile supuse apelului",
    content="""(1) Sentințele pot fi atacate cu apel în vederea unei noi judecări în fapt și în drept a cauzei, cu excepția sentințelor pronunțate de către instanțele judecătorești privind infracțiunile pentru a căror săvîrșire legea prevede exclusiv pedeapsă nonprivativă de libertate.

(2) Încheierile date în primă instanță pot fi atacate cu apel numai o dată cu sentința cu excepția cazurilor în care, potrivit legii, pot fi atacate separat.

(3) Apelul declarat împotriva sentinței se consideră făcut și împotriva încheierilor, chiar dacă acestea au fost date după pronunțarea sentinței.""",
    chapter="Capitolul IV. Căile ordinare de atac - Apelul",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_401 = LegalArticle.objects.create(
    article_number="401",
    title="Persoanele care pot declara apel",
    content="""(1) Pot declara apel:
1) procurorul, în ce privește latura penală și latura civilă;
2) inculpatul, în ce privește latura penală și latura civilă. Sentințele de achitare sau de încetare a procesului penal pot fi atacate și în ce privește temeiurile achitării sau încetării procesului penal;
3) partea vătămată, în ce privește latura penală;
4) partea civilă și partea civilmente responsabilă, în ce privește latura civilă;
5) martorul, expertul, interpretul, traducătorul și apărătorul, în ce privește cheltuielile judiciare cuvenite acestora;
6) orice persoană ale cărei interese legitime au fost prejudiciate printr-o măsură sau printr-un act al instanței.

(2) Apelul poate fi declarat în numele persoanelor menționate la alin.(1) pct.2)-4) și de către apărător sau reprezentantul lor legal ori de către succesorii acestora.""",
    content_ru="""(1) Могут подать апелляцию:
1) прокурор;
2) подсудимый;
3) потерпевший;
4) гражданский истец и гражданский ответчик;
5) свидетель, эксперт, переводчик и защитник - в части судебных расходов;
6) любое лицо, чьи законные интересы нарушены актом суда.

(2) Апелляция может быть подана от имени указанных лиц их защитником или законным представителем.""",
    chapter="Capitolul IV. Căile ordinare de atac - Apelul",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_402 = LegalArticle.objects.create(
    article_number="402",
    title="Termenul de declarare a apelului",
    content="""(1) Termenul de apel este de 15 zile de la data pronunțării sentinței integrale, dacă legea nu dispune altfel.

(3) În cazurile prevăzute în art.401 alin.(1) pct.5) și 6), calea de atac poate fi exercitată de îndată după pronunțarea încheierii, dar nu mai tîrziu de 15 zile de la pronunțarea sentinței prin care s-a soluționat cauza.

(4) Dacă procurorul sau partea vătămată a declarat în termen apel în defavoarea inculpatului, procurorul participant la instanța de apel, în termen de 15 zile de la data primirii copiei apelului declarat, poate declara apel suplimentar.""",
    content_ru="""(1) Срок подачи апелляции составляет 15 дней со дня провозглашения полного текста приговора.

(4) Если прокурор или потерпевший подали апелляцию против подсудимого в срок, прокурор может подать дополнительную апелляцию в течение 15 дней.""",
    chapter="Capitolul IV. Căile ordinare de atac - Apelul",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- RECURSUL ---
art_427 = LegalArticle.objects.create(
    article_number="427",
    title="Hotărîrile supuse recursului",
    content="""(1) Deciziile pronunțate de curțile de apel, ca instanțe de apel, pot fi atacate cu recurs în condițiile prezentului cod.

(2) Deciziile pot fi atacate cu recurs de persoanele indicate la art.401, precum și de alte persoane ale căror interese legitime au fost lezate prin decizie.""",
    chapter="Capitolul IV. Căile ordinare de atac - Recursul",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_432 = LegalArticle.objects.create(
    article_number="432",
    title="Termenul de declarare a recursului",
    content="""(1) Recursul poate fi declarat în termen de 30 de zile de la data pronunțării deciziei instanței de apel.

(2) Procurorul General și adjuncții lui pot declara recurs în termen de 6 luni de la data pronunțării deciziei instanței de apel.""",
    chapter="Capitolul IV. Căile ordinare de atac - Recursul",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- CONTROLUL JUDICIAR ---
art_298 = LegalArticle.objects.create(
    article_number="298",
    title="Plîngerea împotriva acțiunilor, inacțiunilor și actelor organului de urmărire penală",
    content="""(1) Împotriva acțiunilor, inacțiunilor și actelor organului de urmărire penală și ale organului care exercită activitate specială de investigații pot înainta plîngere bănuitul, învinuitul, reprezentantul lor legal, apărătorul, partea vătămată, partea civilă, partea civilmente responsabilă și reprezentanții acestora, precum și alte persoane ale căror drepturi și interese legitime au fost lezate de aceste organe.

(2) Plângerea se adresează, în termen de 15 zile, procurorului care conduce urmărirea penală. Termenul de adresare a plângerii se calculează din momentul când au luat cunoștință de act ori au aflat despre inacțiunea organului.

(3) Plîngerea depusă în condițiile prezentului articol nu suspendă executarea acțiunii sau actelor atacate dacă procurorul nu consideră aceasta necesar.""",
    chapter="Capitolul VII. Controlul de către procuror al legalității acțiunilor, inacțiunilor și actelor",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_313 = LegalArticle.objects.create(
    article_number="313",
    title="Plîngerea împotriva actelor ilegale ale organului de urmărire penală și ale procurorului",
    content="""(1) Plîngerile împotriva acțiunilor ilegale ale organului de urmărire penală și ale procurorului depuse conform art.298-2992 din prezentul cod se judecă de judecătorul de instrucție.

(2) Judecătorul de instrucție examinează plîngerea în termen de 10 zile de la data depunerii ei în ședință cu participarea procurorului, a apărătorului și a persoanei ale cărei interese au fost lezate. Neprezentarea acestor persoane nu împiedică judecarea plîngerii.

(3) După examinarea plîngerii, judecătorul de instrucție, prin încheiere motivată:
1) admite plîngerea și anulează actul atacat sau obligă funcționarul respectiv să execute acțiunile cerute;
2) respinge plîngerea ca neîntemeiată.

(4) Încheierea judecătorului de instrucție poate fi atacată cu recurs în termen de 15 zile.""",
    chapter="Capitolul VIII. Controlul judiciar al procedurii prejudiciare",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- ACORDUL DE RECUNOAȘTERE A VINOVĂȚIEI ---
art_504 = LegalArticle.objects.create(
    article_number="504",
    title="Dispoziții generale privind acordul de recunoaștere a vinovăției",
    content="""(1) Procedura de încheiere a acordului de recunoaștere a vinovăției și judecarea cauzelor penale în cazul încheierii acordului de recunoaștere a vinovăției se desfășoară în ordinea generală stabilită în prezentul cod, cu completările și derogările prevăzute în prezentul capitol.

(2) Acordul de recunoaștere a vinovăției este o tranzacție încheiată între procuror și învinuitul persoană fizică sau juridică care și-a exprimat acordul de a-și recunoaște vina și acceptă încadrarea juridică a faptei, precum și forma de executare a pedepsei, în schimbul unei pedepse reduse.

(3) Procedura se aplică în cazul infracțiunilor pentru care se aplică pedeapsa cu închisoare pe un termen până la 15 ani inclusiv.

(5) Acordul poate fi inițiat de către procuror, de către învinuit și apărătorul său și poate fi încheiat în orice moment după punerea sub învinuire și până la trimiterea cauzei în judecată.""",
    content_ru="""Соглашение о признании вины - это сделка между прокурором и обвиняемым, который согласился признать свою вину и принять юридическую квалификацию деяния в обмен на смягчение наказания.""",
    chapter="Capitolul III. Procedura acordului de recunoaștere a vinovăției",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_505 = LegalArticle.objects.create(
    article_number="505",
    title="Condițiile de inițiere și încheiere a acordului",
    content="""(1) Acordul de recunoaștere a vinovăției se întocmește în scris, după aprobarea, în scris, a limitelor pedepsei de către procurorul ierarhic superior, cu participarea obligatorie a învinuitului și a apărătorului acestuia.

(2) Acordul poate fi încheiat atunci când, în baza probelor administrate, reiese că faptele au fost săvârșite de învinuit și rezultă stabilirea vinovăției acestuia.

(3) Procurorul negociază cu învinuitul și apărătorul acestuia categoria, cuantumul și modul de executare a pedepsei.""",
    chapter="Capitolul III. Procedura acordului de recunoaștere a vinovăției",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_506 = LegalArticle.objects.create(
    article_number="506",
    title="Conținutul acordului de recunoaștere a vinovăției",
    content="""(1) Acordul de recunoaștere a vinovăției trebuie să cuprindă:
1) data și locul încheierii;
2) numele, prenumele și calitatea persoanelor care au participat la încheierea acordului;
3) datele pentru identificarea învinuitului;
4) descrierea faptei ce formează obiectul acordului;
5) încadrarea juridică a faptei și pedeapsa prevăzută de lege;
6) mijloacele de probă;
7) declarația expresă a învinuitului prin care recunoaște comiterea faptei;
8) categoria, mărimea și modul de executare a pedepsei negociate.""",
    chapter="Capitolul III. Procedura acordului de recunoaștere a vinovăției",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_509 = LegalArticle.objects.create(
    article_number="509",
    title="Examinarea de către instanță a acordului",
    content="""(1) Instanța de judecată examinează cauza în procedura acordului în ședință publică. Se citește acordul, se audiază inculpatul și se ascultă poziția apărătorului.

(2) Instanța trebuie să constate dacă inculpatul:
1) înțelege pentru ce infracțiune este învinuit;
2) recunoaște vinovăția;
3) a încheiat acordul în mod benevol și cu bună știință, în prezența apărătorului;
4) înțelege consecințele acordului și pedeapsa.""",
    chapter="Capitolul III. Procedura acordului de recunoaștere a vinovăției",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_510_acord = LegalArticle.objects.create(
    article_number="510¹",
    title="Sentința în procedura acordului de recunoaștere a vinovăției",
    content="""(1) În cazul acceptării acordului, sentința se adoptă în condițiile prezentului cod.
(2) Partea introductivă conține mențiunea despre judecarea cauzei în procedura acordului.
(3) Instanța nu poate modifica încadrarea juridică a faptei sau pedeapsa negociată în acord.""",
    chapter="Capitolul III. Procedura acordului de recunoaștere a vinovăției",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- REVIZUIREA ---
art_458 = LegalArticle.objects.create(
    article_number="458",
    title="Temeiurile de revizuire a procesului penal",
    content="""(1) Hotărârile judecătorești irevocabile pot fi supuse revizuirii atât cu privire la latura penală, cât și cu privire la latura civilă.

(3) Revizuirea poate fi cerută în cazurile în care:
1) s-a constatat, prin sentință penală irevocabilă, comiterea unei infracțiuni în timpul urmăririi penale;
2) s-au stabilit circumstanțe noi sau recent descoperite;
3) două sau mai multe hotărâri judecătorești irevocabile nu se pot concilia;
4) Curtea Constituțională a recunoscut drept neconstituțională prevederea legii aplicată;
5) Curtea Europeană a Drepturilor Omului a informat Guvernul despre existența unui viciu fundamental;
6) CEDO a constatat o încălcare a drepturilor fundamentale.""",
    content_ru="""Вступившие в силу судебные решения могут быть пересмотрены как в уголовной, так и в гражданской части при наличии оснований: вновь открывшиеся обстоятельства, решения КС, решения ЕСПЧ.""",
    chapter="Capitolul V. Căile extraordinare de atac - Revizuirea",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_459 = LegalArticle.objects.create(
    article_number="459",
    title="Termenul de revizuire",
    content="""(1) Revizuirea unei hotărâri de achitare sau condamnare poate fi cerută în termen de un an de la data când au devenit cunoscute motivele.

(2) Revizuirea în favoarea condamnatului nu este limitată în timp.

(4) Revizuirea în temeiul hotărârii CEDO poate fi cerută în termen de 6 luni de la data rămânerii definitive a hotărârii CEDO.""",
    chapter="Capitolul V. Căile extraordinare de atac - Revizuirea",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_460 = LegalArticle.objects.create(
    article_number="460",
    title="Depunerea cererii de revizuire",
    content="""(1) Pot cere revizuirea:
1) oricare parte din proces, în limitele calității sale procesuale;
2) rudele apropiate, soțul sau soția condamnatului, chiar și după decesul acestuia;
3) Agentul guvernamental, în cazurile prevăzute la art. 458 alin. (3) pct. 5) și 6).

(2) Cererea de revizuire este formulată în scris și trebuie să conțină temeiul de revizuire și probele ce confirmă temeinicia ei.

(4) Cererile de revizuire în temeiul hotărârii CEDO sunt de competența Curții Supreme de Justiție.""",
    chapter="Capitolul V. Căile extraordinare de atac - Revizuirea",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_462_rev = LegalArticle.objects.create(
    article_number="462",
    title="Hotărârea instanței de revizuire",
    content="""(1) După ce examinează cererea de revizuire considerată admisibilă, instanța emite o încheiere privind:
a) respingerea cererii de revizuire;
b) admiterea cererii de revizuire, casarea hotărârii supuse revizuirii și reluarea examinării cauzei de către instanța competentă.

(2) Odată cu admiterea cererii și reluarea examinării, instanța poate suspenda motivat executarea pedepsei și aplica măsuri preventive.""",
    chapter="Capitolul V. Căile extraordinare de atac - Revizuirea",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- MĂSURI SPECIALE DE INVESTIGAȚII ---
art_134 = LegalArticle.objects.create(
    article_number="134",
    title="Măsurile speciale de investigații",
    content="""(1) În cadrul urmăririi penale pot fi efectuate următoarele măsuri speciale de investigații:

1) cu autorizarea judecătorului de instrucție:
a) cercetarea domiciliului, utilizarea și/sau instalarea aparatelor de supraveghere;
b) supravegherea tehnică;
c) interceptarea și înregistrarea comunicărilor și/sau a imaginilor;
d) reținerea, cercetarea trimiterilor poștale;
e) monitorizarea tranzacțiilor financiare;
f) accesarea, interceptarea datelor informatice;
g) folosirea investigatorului sub acoperire;

2) cu autorizarea procurorului:
a) identificarea abonatului, posesorului de telefon;
b) livrarea supravegheată;
c) colectarea informațiilor despre tranzacții.""",
    content_ru="""Специальные следственные меры включают: прослушивание, слежку, перехват корреспонденции, работу под прикрытием, контролируемую поставку и др.""",
    chapter="Secțiunea a 2-a. Măsurile speciale de investigații",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_138_3 = LegalArticle.objects.create(
    article_number="138³",
    title="Interceptarea și înregistrarea comunicărilor",
    content="""(1) Interceptarea și înregistrarea comunicărilor constă în ascultarea, înregistrarea și fixarea pe suport tehnic a comunicărilor efectuate prin mijloace de comunicare.

(2) Interceptarea se autorizează de judecătorul de instrucție pe un termen de cel mult 30 de zile.

(3) Fiecare prelungire nu poate depăși 30 de zile, iar durata totală nu poate depăși 6 luni.""",
    chapter="Secțiunea a 2-a. Măsurile speciale de investigații",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- LIBERARE PROVIZORIE ---
art_191 = LegalArticle.objects.create(
    article_number="191",
    title="Liberarea provizorie sub control judiciar",
    content="""(1) Liberarea provizorie sub control judiciar se poate aplica de către judecătorul de instrucție sau de către instanță pe un termen de cel mult 60 de zile.

(3) Liberarea provizorie este însoțită de una sau mai multe din următoarele obligații:
1) să nu părăsească localitatea;
2) să comunice orice schimbare de domiciliu;
3) să nu meargă în locuri anume stabilite;
4) să se prezinte la citare;
5) să nu comunice cu anumite persoane;
6) să nu conducă autovehicule;
7) să predea pașaportul.

(32) Măsura poate fi dispusă pe un termen de cel mult 12 luni cumulative sau 24 luni pentru infracțiuni grave.""",
    content_ru="""Условное освобождение под судебный контроль назначается на срок до 60 дней с возможностью продления до 12-24 месяцев.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_192 = LegalArticle.objects.create(
    article_number="192",
    title="Liberarea provizorie pe cauțiune",
    content="""(1) Liberarea provizorie pe cauțiune poate fi acordată în cazul în care este aplicată măsura asiguratorie pentru repararea prejudiciului și s-a depus cauțiunea stabilită.

(21) Judecătorul de instrucție sau instanța dispune, prin încheiere, aplicarea măsurii de liberare provizorie pe cauțiune, stabilește valoarea cauțiunii și termenul de depunere.

(23) Măsura poate fi dispusă pe un termen de cel mult 12 luni cumulative sau 24 luni pentru infracțiuni grave.

(4) Dacă învinuitul nu depune cauțiunea în termenul stabilit, se dispune înlocuirea cu arestarea preventivă.""",
    content_ru="""Условное освобождение под залог применяется при внесении установленной суммы залога на срок до 12-24 месяцев.""",
    chapter="Capitolul II. Măsurile preventive",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- PREGĂTIREA ȘEDINȚEI ---
art_344 = LegalArticle.objects.create(
    article_number="344",
    title="Repartizarea cauzei parvenite pentru judecare",
    content="""(1) Cauza penală parvenită în instanță se repartizează, în termen de o zi, judecătorului sau completului de judecată în mod aleatoriu, prin intermediul Programului integrat de gestionare a dosarelor.

(2) Extrasul din Program sau încheierea președintelui instanței cu privire la repartizarea aleatorie a cauzei se anexează la dosar.""",
    chapter="Capitolul II. Punerea pe rol a cauzei penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_345 = LegalArticle.objects.create(
    article_number="345",
    title="Ședința preliminară",
    content="""(1) După repartizarea cauzei, judecătorul sau completul de judecată fixează data ședinței preliminare în cel mult 30 de zile.

(2) În cazul posibilității judecării cauzei în procedură de urgență, judecătorul pune cauza pe rol fără a ține ședința preliminară.

(3) Ședința preliminară constă în soluționarea, cu participarea părților, a chestiunilor legate de punerea pe rol a cauzei.

(4) În ședința preliminară se soluționează chestiunile privind:
1) cererile și demersurile înaintate, precum și recuzările declarate;
2) lista probelor care vor fi prezentate de către părți la judecarea cauzei.""",
    chapter="Capitolul II. Punerea pe rol a cauzei penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- EXECUTARE ---
art_469 = LegalArticle.objects.create(
    article_number="469",
    title="Amânarea executării pedepsei",
    content="""(1) Executarea pedepsei poate fi amânată în cazurile prevăzute de art. 96 din Codul penal.

(2) Cererea de amânare a executării pedepsei se soluționează de instanța care a pronunțat sentința sau de instanța în raza teritorială a căreia se află condamnatul.""",
    chapter="Titlul IV. Executarea hotărârilor judecătorești",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_470 = LegalArticle.objects.create(
    article_number="470",
    title="Liberarea condiționată înainte de termen",
    content="""(1) Liberarea condiționată de pedeapsă înainte de termen se dispune în condițiile art. 91 din Codul penal.

(2) Cererea de liberare condiționată se examinează de instanța în raza teritorială a căreia se află instituția penitenciară.

(3) La examinarea cererii se citează condamnatul, procurorul și reprezentantul administrației penitenciare.""",
    chapter="Titlul IV. Executarea hotărârilor judecătorești",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_287_reluare = LegalArticle.objects.create(
    article_number="287",
    title="Reluarea urmăririi penale",
    content="""(1) Reluarea urmăririi penale după încetarea urmăririi penale, după scoaterea persoanei de sub urmărire și/sau după clasarea cauzei se dispune prin ordonanță de către procurorul ierarhic superior dacă se constată că:
1) decizia este afectată de un viciu fundamental;
2) apar fapte noi sau recent descoperite, care existau la data adoptării ordonanței, dar despre care nu avea cunoștință organul de urmărire penală.

(2) Urmărirea penală poate fi reluată și de către judecătorul de instrucție în cazul admiterii plângerii împotriva ordonanței.

(4) Reluarea urmăririi penale poate avea loc doar în interiorul termenului de prescripție.""",
    chapter="Capitolul V. Desfășurarea urmăririi penale",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

# --- ETAPELE JUDECĂȚII (DETALIERE) ---
art_366 = LegalArticle.objects.create(
    article_number="366",
    title="Începerea cercetării judecătorești",
    content="""(1) Președintele ședinței de judecată anunță începerea cercetării judecătorești. Cercetarea judecătorească începe cu expunerea de către procuror a învinuirii formulate. Dacă în procesul penal a fost pornită o acțiune civilă, se expune și aceasta.

(3) Președintele ședinței întreabă inculpatul dacă îi este clară învinuirea adusă, dacă acceptă să facă declarații și să răspundă la întrebări.

(4) După executarea acțiunilor menționate, procurorul prezintă spre examinare probele acuzării.""",
    chapter="Secțiunea a 2-a. Cercetarea judecătorească",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_367 = LegalArticle.objects.create(
    article_number="367",
    title="Audierea inculpatului",
    content="""(1) Inculpatul poate fi audiat în orice moment al cercetării judecătorești, la cererea sa sau la solicitarea părților.

(2) Primii pun întrebări reprezentanții părții care a cerut audierea. Judecătorul poate pune întrebări inculpatului în orice moment.

(3) Inculpatul poate refuza să facă declarații sau să răspundă la întrebări și își poate da acordul să fie audiat în lipsa unor participanți la proces.

(4) Inculpatul poate citi documentele care se referă la declarațiile lui.""",
    chapter="Secțiunea a 2-a. Cercetarea judecătorească",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_370 = LegalArticle.objects.create(
    article_number="370",
    title="Audierea martorilor",
    content="""(1) Martorii se audiază fiecare separat și în lipsa martorilor care încă nu au fost audiați. Primii sunt audiați martorii din partea acuzării.

(2) Audierea martorului se efectuează în condițiile prevăzute în art.105-110.

(3) Părțile la proces sunt în drept să pună întrebări martorului. Primii pun întrebări participanții la proces ai acelei părți care a solicitat audierea martorului.

(4) Fiecare din părți poate pune întrebări suplimentare pentru a elucida și a completa răspunsurile.""",
    chapter="Secțiunea a 2-a. Cercetarea judecătorească",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_372 = LegalArticle.objects.create(
    article_number="372",
    title="Examinarea corpurilor delicte",
    content="""(1) Corpurile delicte se examinează de către instanță și se prezintă spre examinare părților.

(2) Corpurile delicte care nu pot fi aduse în sala de ședință pot fi examinate, dacă este necesar, la locul aflării lor.

(3) Examinarea corpurilor delicte restituite conform art. 161 alin. (5) nu poate fi solicitată nici de părți, nici la inițiativa instanței.""",
    chapter="Secțiunea a 2-a. Cercetarea judecătorească",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_377 = LegalArticle.objects.create(
    article_number="377",
    title="Anunțarea și ordinea dezbaterilor judiciare",
    content="""(1) După terminarea cercetării judecătorești, președintele ședinței de judecată anunță dezbaterile judiciare.

(2) Dezbaterile judiciare constau din cuvântările procurorului, părții vătămate, părții civile, părții civilmente responsabile, apărătorului și inculpatului când apărătorul nu participă la cauza dată sau dacă inculpatul cere cuvântul.

(3) În cazul în care cel puțin una din persoanele care participă la dezbateri cere termen pentru pregătirea către dezbateri, președintele anunță întrerupere.""",
    chapter="Secțiunea a 3-a. Dezbaterile judiciare",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

art_380 = LegalArticle.objects.create(
    article_number="380",
    title="Ultimul cuvânt al inculpatului",
    content="""(1) După terminarea dezbaterilor judiciare, președintele ședinței acordă ultimul cuvânt inculpatului.

(2) În timpul în care inculpatul are ultimul cuvânt, nu i se pot pune întrebări și el nu poate fi întrerupt decât în cazul în care el se referă la alte împrejurări decât cele care se referă la cauză.

(3) Dacă inculpatul, în ultimul cuvânt, relevă fapte sau împrejurări noi, esențiale pentru soluționarea cauzei, instanța poate dispune reluarea cercetării judecătorești pentru verificarea acestora.""",
    chapter="Secțiunea a 3-a. Dezbaterile judiciare",
    external_url="https://www.legis.md/cautare/getResults?doc_id=140131&lang=ro#"
)

print("Создание этапов процедуры...")

# ==================== ЭТАПЫ ПРОЦЕДУРЫ ====================

# ===== БЛОК 1: SESIZAREA (НАЧАЛО) =====

stage_sesizare = ProcedureStage.objects.create(
    title="Sesizarea organului de urmărire penală",
    title_ru="Уведомление органа уголовного преследования",
    short_title="Sesizare",
    description="Depunerea plîngerii, denunțului, autodenunțului sau depistarea infracțiunii",
    description_ru="Подача жалобы, заявления, явки с повинной или обнаружение преступления",
    category=cat_urmarire,
    node_type='start',
    position_x=400,
    position_y=50,
    order=1,
    search_keywords="plîngere, denunț, autodenunț, sesizare, infracțiune"
)
stage_sesizare.articles.add(art_262, art_263, art_264)

stage_plangere = ProcedureStage.objects.create(
    title="Plîngere",
    title_ru="Жалоба",
    short_title="Plîngere",
    description="Înștiințarea făcută de o persoană căreia i s-a cauzat un prejudiciu prin infracțiune",
    category=cat_urmarire,
    node_type='process',
    position_x=150,
    position_y=200,
    order=2
)
stage_plangere.articles.add(art_263)

stage_denunt = ProcedureStage.objects.create(
    title="Denunț",
    title_ru="Заявление",
    short_title="Denunț",
    description="Înștiințarea făcută de o persoană despre săvîrșirea unei infracțiuni",
    category=cat_urmarire,
    node_type='process',
    position_x=400,
    position_y=200,
    order=3
)
stage_denunt.articles.add(art_263)

stage_autodenunt = ProcedureStage.objects.create(
    title="Autodenunț",
    title_ru="Явка с повинной",
    short_title="Autodenunț",
    description="Înștiințarea benevolă despre săvîrșirea de către persoană a unei infracțiuni",
    category=cat_urmarire,
    node_type='process',
    position_x=650,
    position_y=200,
    order=4
)
stage_autodenunt.articles.add(art_264)

# ===== БЛОК 2: EXAMINAREA SESIZĂRII =====

stage_inregistrare = ProcedureStage.objects.create(
    title="Înregistrarea sesizării",
    title_ru="Регистрация уведомления",
    short_title="Înregistrare",
    description="Înregistrarea în Registrul de evidență a sesizărilor cu privire la infracțiuni. Eliberarea confirmării de recepționare.",
    category=cat_urmarire,
    node_type='process',
    position_x=400,
    position_y=350,
    order=5
)
stage_inregistrare.articles.add(art_265)

stage_examinare = ProcedureStage.objects.create(
    title="Examinarea sesizării",
    title_ru="Рассмотрение уведомления",
    short_title="Examinare",
    description="Verificarea îndeplinirii condițiilor pentru pornirea urmăririi penale în termen de 45 de zile",
    category=cat_urmarire,
    node_type='process',
    position_x=400,
    position_y=500,
    order=6,
    deadline_days=45,
    deadline_note="Termen maxim de examinare"
)

# ===== БЛОК 3: DECIZIA PRIVIND PORNIREA =====

stage_decizie_pornire = ProcedureStage.objects.create(
    title="Decizia privind pornirea urmăririi penale",
    title_ru="Решение о начале уголовного преследования",
    short_title="Decizie pornire",
    description="Există bănuială rezonabilă că a fost săvîrșită o infracțiune?",
    category=cat_urmarire,
    node_type='decision',
    position_x=400,
    position_y=650,
    order=7
)
stage_decizie_pornire.articles.add(art_274, art_275)

stage_pornire = ProcedureStage.objects.create(
    title="Pornirea urmăririi penale",
    title_ru="Начало уголовного преследования",
    short_title="Pornire UP",
    description="Emiterea ordonanței de începere a urmăririi penale. Informarea procurorului în 24 ore.",
    category=cat_urmarire,
    node_type='document',
    position_x=200,
    position_y=800,
    order=8,
    deadline_days=1,
    deadline_note="24 ore pentru informarea procurorului"
)
stage_pornire.articles.add(art_274)

stage_refuz = ProcedureStage.objects.create(
    title="Refuzul de a porni urmărirea penală",
    title_ru="Отказ в начале уголовного преследования",
    short_title="Refuz",
    description="Ordonanța de refuz în pornirea urmăririi penale. Poate fi atacată în instanța judecătorească.",
    category=cat_urmarire,
    node_type='end',
    position_x=600,
    position_y=800,
    order=9,
    deadline_days=15,
    deadline_note="15 zile pentru anunțarea petentului"
)
stage_refuz.articles.add(art_274, art_275)

# ===== БЛОК 4: DESFĂȘURAREA URMĂRIRII PENALE =====

stage_desfasurare = ProcedureStage.objects.create(
    title="Desfășurarea urmăririi penale",
    title_ru="Проведение уголовного преследования",
    short_title="Desfășurare UP",
    description="Efectuarea acțiunilor de urmărire penală pentru colectarea probelor",
    category=cat_urmarire,
    node_type='subprocess',
    position_x=200,
    position_y=950,
    order=10
)
stage_desfasurare.articles.add(art_279)

# Дочерние этапы desfășurare
stage_audiere = ProcedureStage.objects.create(
    title="Audierea persoanelor",
    title_ru="Допрос лиц",
    short_title="Audiere",
    description="Audierea martorilor, bănuitului, învinuitului, părții vătămate",
    category=cat_urmarire,
    node_type='process',
    parent=stage_desfasurare,
    position_x=50,
    position_y=1100,
    order=1
)

stage_perchezitie = ProcedureStage.objects.create(
    title="Percheziția",
    title_ru="Обыск",
    short_title="Percheziție",
    description="Percheziție domiciliară sau corporală cu autorizarea judecătorului de instrucție",
    category=cat_urmarire,
    node_type='process',
    parent=stage_desfasurare,
    position_x=200,
    position_y=1100,
    order=2
)

stage_expertiza = ProcedureStage.objects.create(
    title="Expertiza judiciară",
    title_ru="Судебная экспертиза",
    short_title="Expertiza",
    description="Efectuarea expertizelor judiciare necesare",
    category=cat_urmarire,
    node_type='process',
    parent=stage_desfasurare,
    position_x=350,
    position_y=1100,
    order=3
)

# ===== БЛОК 5: MĂSURI PREVENTIVE =====

stage_masuri_preventive = ProcedureStage.objects.create(
    title="Aplicarea măsurilor preventive",
    title_ru="Применение мер пресечения",
    short_title="Măsuri prev.",
    description="Alegerea și aplicarea măsurilor preventive adecvate",
    category=cat_masuri,
    node_type='subprocess',
    position_x=500,
    position_y=950,
    order=11
)
stage_masuri_preventive.articles.add(art_175, art_176)

stage_retinere = ProcedureStage.objects.create(
    title="Reținerea",
    title_ru="Задержание",
    short_title="Reținere",
    description="Măsură procesuală de privare de libertate pe termen scurt (max. 72 ore, minori - 24 ore)",
    category=cat_masuri,
    node_type='process',
    parent=stage_masuri_preventive,
    position_x=400,
    position_y=1100,
    order=1,
    deadline_days=3,
    deadline_note="Maxim 72 ore (24 ore pentru minori)"
)
stage_retinere.articles.add(art_165, art_166)

stage_arest = ProcedureStage.objects.create(
    title="Arestarea preventivă",
    title_ru="Предварительное заключение под стражу",
    short_title="Arest preventiv",
    description="Deținerea învinuitului în stare de arest. Măsură excepțională aplicată de instanță.",
    category=cat_masuri,
    node_type='process',
    parent=stage_masuri_preventive,
    position_x=550,
    position_y=1100,
    order=2,
    deadline_days=30,
    deadline_note="Max. 30 zile (total max. 12 luni, minori - 8 luni)"
)
stage_arest.articles.add(art_185, art_186)

stage_arest_domiciliu = ProcedureStage.objects.create(
    title="Arestarea la domiciliu",
    title_ru="Домашний арест",
    short_title="Arest domiciliu",
    description="Izolarea în locuință cu restricții, alternativă la arestul preventiv",
    category=cat_masuri,
    node_type='process',
    parent=stage_masuri_preventive,
    position_x=700,
    position_y=1100,
    order=3
)
stage_arest_domiciliu.articles.add(art_188)

stage_neprivativi = ProcedureStage.objects.create(
    title="Măsuri neprivative de libertate",
    title_ru="Меры, не связанные с лишением свободы",
    short_title="Neprivative",
    description="Obligarea de a nu părăsi localitatea/țara, garanție personală, cauțiune",
    category=cat_masuri,
    node_type='process',
    parent=stage_masuri_preventive,
    position_x=850,
    position_y=1100,
    order=4,
    deadline_days=60,
    deadline_note="Max. 60 zile (prelungire posibilă, total max. 24 luni)"
)
stage_neprivativi.articles.add(art_178)

# ===== БЛОК 6: PUNEREA SUB ÎNVINUIRE =====

stage_propunere_invinuire = ProcedureStage.objects.create(
    title="Propunerea de punere sub învinuire",
    title_ru="Предложение о предъявлении обвинения",
    short_title="Propunere înv.",
    description="Raportul organului de urmărire penală cu propunerea de punere sub învinuire",
    category=cat_urmarire,
    node_type='document',
    position_x=200,
    position_y=1250,
    order=12
)
stage_propunere_invinuire.articles.add(art_280)

stage_punere_invinuire = ProcedureStage.objects.create(
    title="Punerea sub învinuire",
    title_ru="Предъявление обвинения",
    short_title="Sub învinuire",
    description="Emiterea ordonanței de punere sub învinuire de către procuror",
    category=cat_urmarire,
    node_type='document',
    position_x=200,
    position_y=1400,
    order=13
)
stage_punere_invinuire.articles.add(art_281)

stage_inaintare_acuzare = ProcedureStage.objects.create(
    title="Înaintarea acuzării",
    title_ru="Предъявление обвинения лицу",
    short_title="Înaintare acuz.",
    description="Aducerea la cunoștința învinuitului a ordonanței de punere sub învinuire în prezența avocatului",
    category=cat_urmarire,
    node_type='process',
    position_x=200,
    position_y=1550,
    order=14,
    deadline_days=2,
    deadline_note="În decurs de 48 de ore"
)
stage_inaintare_acuzare.articles.add(art_282)

# ===== БЛОК 7: FINALIZAREA URMĂRIRII =====

stage_finalizare = ProcedureStage.objects.create(
    title="Finalizarea urmăririi penale",
    title_ru="Завершение уголовного преследования",
    short_title="Finalizare UP",
    description="Decizia procurorului privind rezultatul urmăririi penale",
    category=cat_urmarire,
    node_type='decision',
    position_x=200,
    position_y=1700,
    order=15
)
stage_finalizare.articles.add(art_291)

stage_trimitere = ProcedureStage.objects.create(
    title="Trimiterea în judecată",
    title_ru="Направление дела в суд",
    short_title="Rechizitoriu",
    description="Întocmirea rechizitoriului și trimiterea cauzei în judecată",
    category=cat_urmarire,
    node_type='document',
    position_x=50,
    position_y=1850,
    order=16
)
stage_trimitere.articles.add(art_296, art_297)

stage_scoatere = ProcedureStage.objects.create(
    title="Scoaterea de sub urmărirea penală",
    title_ru="Прекращение уголовного преследования (реабилитация)",
    short_title="Scoatere",
    description="Actul de reabilitare cînd fapta nu a fost săvîrșită de bănuit sau nu există infracțiune",
    category=cat_urmarire,
    node_type='end',
    position_x=200,
    position_y=1850,
    order=17
)
stage_scoatere.articles.add(art_284)

stage_incetare = ProcedureStage.objects.create(
    title="Încetarea urmăririi penale",
    title_ru="Прекращение уголовного преследования (без реабилитации)",
    short_title="Încetare",
    description="Liberarea de răspundere penală pe temei de nereabilitare (prescripție, amnistie, împăcare etc.)",
    category=cat_urmarire,
    node_type='end',
    position_x=350,
    position_y=1850,
    order=18
)
stage_incetare.articles.add(art_285)

stage_clasare = ProcedureStage.objects.create(
    title="Clasarea cauzei penale",
    title_ru="Прекращение уголовного дела",
    short_title="Clasare",
    description="Finalizarea acțiunilor procesuale într-o cauză penală",
    category=cat_urmarire,
    node_type='end',
    position_x=500,
    position_y=1850,
    order=19
)
stage_clasare.articles.add(art_286)

# ===== БЛОК 8: CONTROLUL JUDICIAR =====

stage_contestare_procuror = ProcedureStage.objects.create(
    title="Plîngerea la procuror",
    title_ru="Жалоба прокурору",
    short_title="Plîngere proc.",
    description="Contestarea acțiunilor organului de urmărire penală la procuror în 15 zile",
    category=cat_urmarire,
    node_type='process',
    position_x=650,
    position_y=1700,
    order=20,
    deadline_days=15,
    deadline_note="15 zile de la luarea la cunoștință"
)
stage_contestare_procuror.articles.add(art_298)

stage_contestare_judecator = ProcedureStage.objects.create(
    title="Plîngerea la judecătorul de instrucție",
    title_ru="Жалоба следственному судье",
    short_title="Plîngere jud.",
    description="Contestarea actelor organului de urmărire sau procurorului la judecătorul de instrucție",
    category=cat_urmarire,
    node_type='process',
    position_x=650,
    position_y=1850,
    order=21,
    deadline_days=10,
    deadline_note="10 zile - examinarea plîngerii"
)
stage_contestare_judecator.articles.add(art_313)

# ===== БЛОК 9: JUDECATA =====

stage_judecata = ProcedureStage.objects.create(
    title="Judecata în primă instanță",
    title_ru="Рассмотрение дела в первой инстанции",
    short_title="Prima instanță",
    description="Cercetarea judecătorească și deliberarea",
    category=cat_judecata,
    node_type='subprocess',
    position_x=50,
    position_y=2000,
    order=22
)
stage_judecata.articles.add(art_314, art_321, art_325)

stage_cercetare = ProcedureStage.objects.create(
    title="Cercetarea judecătorească",
    title_ru="Судебное следствие",
    short_title="Cercetare",
    description="Audierea inculpaților, martorilor, cercetarea probelor",
    category=cat_judecata,
    node_type='subprocess',
    parent=stage_judecata,
    position_x=50,
    position_y=2150,
    order=1
)

# Дочерние этапы cercetare judecătorească
stage_expunere_invinuire = ProcedureStage.objects.create(
    title="Expunerea învinuirii",
    title_ru="Оглашение обвинения",
    short_title="Expunere învinuire",
    description="Președintele ședinței anunță începerea cercetării, procurorul expune învinuirea",
    category=cat_judecata,
    node_type='process',
    parent=stage_cercetare,
    position_x=50,
    position_y=2200,
    order=1
)
stage_expunere_invinuire.articles.add(art_366)

stage_audiere_inculpat = ProcedureStage.objects.create(
    title="Audierea inculpatului",
    title_ru="Допрос подсудимого",
    short_title="Audiere inculpat",
    description="Audierea inculpatului în ședință de judecată cu participarea părților",
    category=cat_judecata,
    node_type='process',
    parent=stage_cercetare,
    position_x=150,
    position_y=2200,
    order=2
)
stage_audiere_inculpat.articles.add(art_367)

stage_audiere_martori = ProcedureStage.objects.create(
    title="Audierea martorilor",
    title_ru="Допрос свидетелей",
    short_title="Audiere martori",
    description="Audierea martorilor acuzării și apărării, confruntări dacă e necesar",
    category=cat_judecata,
    node_type='process',
    parent=stage_cercetare,
    position_x=250,
    position_y=2200,
    order=3
)
stage_audiere_martori.articles.add(art_370)

stage_examinare_probe = ProcedureStage.objects.create(
    title="Examinarea probelor materiale",
    title_ru="Исследование вещественных доказательств",
    short_title="Examinare probe",
    description="Cercetarea corpurilor delicte, actelor, înscrisurilor și altor probe",
    category=cat_judecata,
    node_type='process',
    parent=stage_cercetare,
    position_x=350,
    position_y=2200,
    order=4
)
stage_examinare_probe.articles.add(art_372)

stage_dezbateri = ProcedureStage.objects.create(
    title="Dezbaterile judiciare",
    title_ru="Судебные прения",
    short_title="Dezbateri",
    description="Pledoariile procurorului și apărării",
    category=cat_judecata,
    node_type='subprocess',
    parent=stage_judecata,
    position_x=200,
    position_y=2150,
    order=2
)

# Дочерние этапы dezbateri judiciare
stage_cuvantari = ProcedureStage.objects.create(
    title="Cuvântările părților",
    title_ru="Выступления сторон",
    short_title="Cuvântări",
    description="Cuvântările procurorului, părții vătămate, părții civile și inculpatului",
    category=cat_judecata,
    node_type='process',
    parent=stage_dezbateri,
    position_x=200,
    position_y=2200,
    order=1
)
stage_cuvantari.articles.add(art_377)

stage_replica = ProcedureStage.objects.create(
    title="Replica",
    title_ru="Реплика",
    short_title="Replica",
    description="Dreptul părților la replică pentru a răspunde argumentelor oponenților",
    category=cat_judecata,
    node_type='process',
    parent=stage_dezbateri,
    position_x=280,
    position_y=2200,
    order=2
)

stage_ultim_cuvant = ProcedureStage.objects.create(
    title="Ultimul cuvânt al inculpatului",
    title_ru="Последнее слово подсудимого",
    short_title="Ultim cuvânt",
    description="Dreptul inculpatului de a lua ultimul cuvânt înainte de retragerea completului",
    category=cat_judecata,
    node_type='process',
    parent=stage_dezbateri,
    position_x=360,
    position_y=2200,
    order=3
)
stage_ultim_cuvant.articles.add(art_380)

stage_deliberare = ProcedureStage.objects.create(
    title="Deliberarea",
    title_ru="Совещание судей",
    short_title="Deliberare",
    description="Deliberarea și adoptarea sentinței de către instanță",
    category=cat_judecata,
    node_type='process',
    parent=stage_judecata,
    position_x=350,
    position_y=2150,
    order=3
)
stage_deliberare.articles.add(art_385)

# ===== БЛОК 10: SENTINȚA =====

stage_sentinta = ProcedureStage.objects.create(
    title="Pronunțarea sentinței",
    title_ru="Провозглашение приговора",
    short_title="Sentința",
    description="Sentință de condamnare, achitare sau încetare",
    category=cat_judecata,
    node_type='decision',
    position_x=200,
    position_y=2300,
    order=23
)
stage_sentinta.articles.add(art_384)

stage_condamnare = ProcedureStage.objects.create(
    title="Sentința de condamnare",
    title_ru="Обвинительный приговор",
    short_title="Condamnare",
    description="Persoana este declarată vinovată și se stabilește pedeapsa",
    category=cat_judecata,
    node_type='end',
    position_x=50,
    position_y=2450,
    order=24
)
stage_condamnare.articles.add(art_389)

stage_achitare = ProcedureStage.objects.create(
    title="Sentința de achitare",
    title_ru="Оправдательный приговор",
    short_title="Achitare",
    description="Persoana este declarată nevinovată - reabilitare deplină",
    category=cat_judecata,
    node_type='end',
    position_x=200,
    position_y=2450,
    order=25
)
stage_achitare.articles.add(art_390)

stage_incetare_judecata = ProcedureStage.objects.create(
    title="Sentința de încetare a procesului penal",
    title_ru="Приговор о прекращении уголовного процесса",
    short_title="Încetare proc.",
    description="Încetarea procesului penal în cazurile prevăzute de lege (împăcare, deces etc.)",
    category=cat_judecata,
    node_type='end',
    position_x=350,
    position_y=2450,
    order=26
)
stage_incetare_judecata.articles.add(art_391)

# ===== БЛОК 11: CĂILE DE ATAC =====

stage_apel = ProcedureStage.objects.create(
    title="Apelul",
    title_ru="Апелляция",
    short_title="Apel",
    description="Calea ordinară de atac împotriva sentinței pentru o nouă judecată în fapt și în drept",
    category=cat_cai_atac,
    node_type='process',
    position_x=200,
    position_y=2600,
    order=27,
    deadline_days=15,
    deadline_note="15 zile de la pronunțarea sentinței integrale"
)
stage_apel.articles.add(art_400, art_401, art_402)

stage_decizie_apel = ProcedureStage.objects.create(
    title="Decizia instanței de apel",
    title_ru="Решение апелляционной инстанции",
    short_title="Decizie apel",
    description="Respingerea apelului, admiterea cu casare/modificare, trimitere la rejudecare",
    category=cat_cai_atac,
    node_type='decision',
    position_x=200,
    position_y=2750,
    order=28
)

stage_recurs = ProcedureStage.objects.create(
    title="Recursul",
    title_ru="Кассация",
    short_title="Recurs",
    description="Calea de atac în puncte de drept la Curtea Supremă de Justiție",
    category=cat_cai_atac,
    node_type='process',
    position_x=200,
    position_y=2900,
    order=29,
    deadline_days=30,
    deadline_note="30 de zile de la pronunțarea deciziei de apel"
)
stage_recurs.articles.add(art_427, art_432)

stage_hotarare_definitiva = ProcedureStage.objects.create(
    title="Hotărîrea definitivă",
    title_ru="Окончательное решение",
    short_title="Definitivă",
    description="Hotărîrea judecătorească rămasă definitivă și executorie",
    category=cat_cai_atac,
    node_type='end',
    position_x=200,
    position_y=3050,
    order=30
)

# ===== БЛОК 12: EXECUTAREA =====

stage_executare = ProcedureStage.objects.create(
    title="Executarea hotărîrii",
    title_ru="Исполнение приговора",
    short_title="Executare",
    description="Punerea în executare a sentinței de condamnare",
    category=cat_executare,
    node_type='subprocess',
    position_x=50,
    position_y=3050,
    order=31
)

# Дочерние этапы executare
stage_punere_executare = ProcedureStage.objects.create(
    title="Punerea în executare",
    title_ru="Обращение к исполнению",
    short_title="Punere execut.",
    description="Trimiterea mandatului de executare către organele competente",
    category=cat_executare,
    node_type='process',
    parent=stage_executare,
    position_x=50,
    position_y=3100,
    order=1
)

stage_amanare_executare = ProcedureStage.objects.create(
    title="Amânarea executării pedepsei",
    title_ru="Отсрочка исполнения наказания",
    short_title="Amânare",
    description="Amânarea executării pentru gravide, mame cu copii mici sau boală gravă",
    category=cat_executare,
    node_type='process',
    parent=stage_executare,
    position_x=150,
    position_y=3100,
    order=2
)
stage_amanare_executare.articles.add(art_469)

stage_liberare_conditionata = ProcedureStage.objects.create(
    title="Liberarea condiționată",
    title_ru="Условно-досрочное освобождение",
    short_title="Liber. cond.",
    description="Eliberarea condiționată înainte de termen pentru bună purtare",
    category=cat_executare,
    node_type='process',
    parent=stage_executare,
    position_x=250,
    position_y=3100,
    order=3
)
stage_liberare_conditionata.articles.add(art_470)

# ===== БЛОК 13: PREGĂTIREA ȘEDINȚEI =====

stage_pregatire_sedinta = ProcedureStage.objects.create(
    title="Pregătirea ședinței de judecată",
    title_ru="Подготовка судебного заседания",
    short_title="Pregătire ședință",
    description="Examinarea rechizitoriului, citarea părților, fixarea termenului de judecată",
    category=cat_judecata,
    node_type='process',
    position_x=200,
    position_y=1950,
    order=21
)
stage_pregatire_sedinta.articles.add(art_344, art_345)

stage_restituire_procuror = ProcedureStage.objects.create(
    title="Restituirea dosarului procurorului",
    title_ru="Возвращение дела прокурору",
    short_title="Restituire",
    description="Restituirea dosarului procurorului pentru completarea urmăririi penale",
    category=cat_judecata,
    node_type='process',
    position_x=400,
    position_y=1950,
    order=22
)

# ===== БЛОК 14: ACORDUL DE RECUNOAȘTERE A VINOVĂȚIEI =====

stage_acord_vinovatie = ProcedureStage.objects.create(
    title="Acordul de recunoaștere a vinovăției",
    title_ru="Соглашение о признании вины",
    short_title="Acord vinovăție",
    description="Procedura simplificată prin acordul dintre procuror și învinuit",
    category=cat_urmarire,
    node_type='subprocess',
    position_x=450,
    position_y=1400,
    order=100
)
stage_acord_vinovatie.articles.add(art_504)

stage_negociere_acord = ProcedureStage.objects.create(
    title="Negocierea și întocmirea acordului",
    title_ru="Переговоры и составление соглашения",
    short_title="Negociere",
    description="Negocierea condițiilor acordului și întocmirea lui în scris",
    category=cat_urmarire,
    node_type='process',
    parent=stage_acord_vinovatie,
    position_x=450,
    position_y=1450,
    order=1
)
stage_negociere_acord.articles.add(art_505, art_506)

stage_judecata_acord = ProcedureStage.objects.create(
    title="Examinarea acordului de instanță",
    title_ru="Рассмотрение соглашения судом",
    short_title="Judecată acord",
    description="Verificarea legalității acordului și audierea părților",
    category=cat_judecata,
    node_type='process',
    parent=stage_acord_vinovatie,
    position_x=550,
    position_y=1450,
    order=2
)
stage_judecata_acord.articles.add(art_509)

stage_sentinta_acord = ProcedureStage.objects.create(
    title="Sentința în baza acordului",
    title_ru="Приговор по соглашению",
    short_title="Sentință acord",
    description="Pronunțarea sentinței de condamnare cu pedeapsă redusă",
    category=cat_judecata,
    node_type='end',
    parent=stage_acord_vinovatie,
    position_x=650,
    position_y=1450,
    order=3
)
stage_sentinta_acord.articles.add(art_510_acord)

# ===== БЛОК 15: REVIZUIREA =====

stage_revizuire = ProcedureStage.objects.create(
    title="Revizuirea procesului penal",
    title_ru="Пересмотр уголовного дела",
    short_title="Revizuire",
    description="Cale extraordinară de atac împotriva hotărârilor definitive",
    category=cat_cai_atac,
    node_type='subprocess',
    position_x=450,
    position_y=3050,
    order=32
)
stage_revizuire.articles.add(art_458)

stage_cerere_revizuire = ProcedureStage.objects.create(
    title="Depunerea cererii de revizuire",
    title_ru="Подача заявления о пересмотре",
    short_title="Cerere revizuire",
    description="Depunerea cererii de revizuire în temeiurile prevăzute de lege",
    category=cat_cai_atac,
    node_type='process',
    parent=stage_revizuire,
    position_x=450,
    position_y=3100,
    order=1
)
stage_cerere_revizuire.articles.add(art_460)

stage_examinare_revizuire = ProcedureStage.objects.create(
    title="Examinarea cererii de revizuire",
    title_ru="Рассмотрение заявления о пересмотре",
    short_title="Examinare reviz.",
    description="Procedura de examinare a cererii de către Curtea Supremă",
    category=cat_cai_atac,
    node_type='process',
    parent=stage_revizuire,
    position_x=550,
    position_y=3100,
    order=2
)

stage_hotarare_revizuire = ProcedureStage.objects.create(
    title="Hotărârea instanței de revizuire",
    title_ru="Решение суда по пересмотру",
    short_title="Hotărâre reviz.",
    description="Admiterea sau respingerea cererii, trimiterea la rejudecare",
    category=cat_cai_atac,
    node_type='decision',
    parent=stage_revizuire,
    position_x=650,
    position_y=3100,
    order=3
)
stage_hotarare_revizuire.articles.add(art_462_rev)

# ===== БЛОК 16: LIBERARE PROVIZORIE =====

stage_liberare_control = ProcedureStage.objects.create(
    title="Liberarea provizorie sub control judiciar",
    title_ru="Освобождение под судебный контроль",
    short_title="Control judiciar",
    description="Eliberarea cu impunerea obligațiilor și restricțiilor",
    category=cat_masuri,
    node_type='process',
    parent=stage_masuri_preventive,
    position_x=500,
    position_y=1100,
    order=10,
    deadline_days=60,
    deadline_note="Max. 60 zile, poate fi prelungit până la 12 luni"
)
stage_liberare_control.articles.add(art_191)

stage_liberare_cautiune = ProcedureStage.objects.create(
    title="Liberarea provizorie pe cauțiune",
    title_ru="Освобождение под залог",
    short_title="Cauțiune",
    description="Eliberarea în schimbul depunerii unei garanții financiare",
    category=cat_masuri,
    node_type='process',
    parent=stage_masuri_preventive,
    position_x=600,
    position_y=1100,
    order=11
)
stage_liberare_cautiune.articles.add(art_192)

# ===== БЛОК 17: RELUAREA URMĂRIRII =====

stage_reluare_urmarire = ProcedureStage.objects.create(
    title="Reluarea urmăririi penale",
    title_ru="Возобновление уголовного преследования",
    short_title="Reluare UP",
    description="Reluarea urmăririi penale după încetare, clasare sau scoatere",
    category=cat_urmarire,
    node_type='process',
    position_x=450,
    position_y=1750,
    order=101
)
stage_reluare_urmarire.articles.add(art_287_reluare)

print("Создание связей между этапами...")

# ==================== CONEXIUNI ====================

# Sesizare -> Типы сесизării
connections = [
    # Начало
    (stage_sesizare, stage_plangere, 'default', '', 1),
    (stage_sesizare, stage_denunt, 'default', '', 2),
    (stage_sesizare, stage_autodenunt, 'default', '', 3),

    # Типы -> Регистрация
    (stage_plangere, stage_inregistrare, 'default', '', 4),
    (stage_denunt, stage_inregistrare, 'default', '', 5),
    (stage_autodenunt, stage_inregistrare, 'default', '', 6),

    # Регистрация -> Рассмотрение -> Решение
    (stage_inregistrare, stage_examinare, 'default', '', 7),
    (stage_examinare, stage_decizie_pornire, 'default', '', 8),

    # Решение о начале
    (stage_decizie_pornire, stage_pornire, 'success', 'Da - bănuială rezonabilă', 9),
    (stage_decizie_pornire, stage_refuz, 'failure', 'Nu - lipsesc temeiuri', 10),

    # Refuz -> contestare
    (stage_refuz, stage_contestare_judecator, 'optional', 'Poate fi atacat', 11),

    # Pornire -> Desfășurare
    (stage_pornire, stage_desfasurare, 'default', '', 12),
    (stage_pornire, stage_masuri_preventive, 'conditional', 'Dacă e necesar', 13),

    # Desfășurare -> Дочерние
    (stage_desfasurare, stage_audiere, 'default', '', 14),
    (stage_desfasurare, stage_perchezitie, 'default', '', 15),
    (stage_desfasurare, stage_expertiza, 'default', '', 16),

    # Măsuri preventive -> Дочерние
    (stage_masuri_preventive, stage_retinere, 'default', '', 17),
    (stage_masuri_preventive, stage_arest, 'conditional', 'Excepțional', 18),
    (stage_masuri_preventive, stage_arest_domiciliu, 'conditional', 'Alternativă', 19),
    (stage_masuri_preventive, stage_neprivativi, 'default', 'Prioritar', 20),

    # Retinere -> Arest
    (stage_retinere, stage_arest, 'conditional', 'Demers de arestare', 21),

    # Desfășurare -> Propunere învinuire
    (stage_desfasurare, stage_propunere_invinuire, 'default', '', 22),
    (stage_propunere_invinuire, stage_punere_invinuire, 'success', 'Probe suficiente', 23),
    (stage_punere_invinuire, stage_inaintare_acuzare, 'default', '', 24),
    (stage_inaintare_acuzare, stage_finalizare, 'default', '', 25),

    # Finalizare -> Исходы
    (stage_finalizare, stage_trimitere, 'success', 'Trimitere în judecată', 26),
    (stage_finalizare, stage_scoatere, 'failure', 'Reabilitare', 27),
    (stage_finalizare, stage_incetare, 'failure', 'Nereabilitare', 28),
    (stage_finalizare, stage_clasare, 'failure', 'Clasare', 29),

    # Контроль
    (stage_desfasurare, stage_contestare_procuror, 'optional', 'Poate fi contestat', 30),
    (stage_contestare_procuror, stage_contestare_judecator, 'optional', 'Dacă nu e de acord', 31),

    # Trimitere -> Pregătire (direct connection removed, now via pregatire_sedinta)

    # Judecată -> Дочерние
    (stage_judecata, stage_cercetare, 'default', '', 33),
    (stage_cercetare, stage_dezbateri, 'default', '', 34),
    (stage_dezbateri, stage_deliberare, 'default', '', 35),

    # Judecată -> Sentință
    (stage_judecata, stage_sentinta, 'default', '', 36),

    # Sentință -> Типы
    (stage_sentinta, stage_condamnare, 'failure', 'Vinovat', 37),
    (stage_sentinta, stage_achitare, 'success', 'Nevinovat', 38),
    (stage_sentinta, stage_incetare_judecata, 'conditional', 'Încetare', 39),

    # Căile de atac
    (stage_condamnare, stage_apel, 'optional', 'Poate fi atacată (15 zile)', 40),
    (stage_achitare, stage_apel, 'optional', 'Poate fi atacată (15 zile)', 41),
    (stage_incetare_judecata, stage_apel, 'optional', 'Poate fi atacată (15 zile)', 42),

    # Apel -> Decizie
    (stage_apel, stage_decizie_apel, 'default', '', 43),

    # Decizie apel -> Recurs sau Definitivă
    (stage_decizie_apel, stage_recurs, 'optional', 'Poate fi atacată (30 zile)', 44),
    (stage_decizie_apel, stage_hotarare_definitiva, 'success', 'Definitivă', 45),

    # Recurs -> Definitivă
    (stage_recurs, stage_hotarare_definitiva, 'default', '', 46),

    # Executare
    (stage_condamnare, stage_executare, 'conditional', 'După definitivare', 47),
    (stage_hotarare_definitiva, stage_executare, 'conditional', 'Condamnare', 48),

    # --- НОВЫЕ СВЯЗИ ---

    # Pregătirea ședinței (между trimitere și judecată)
    (stage_trimitere, stage_pregatire_sedinta, 'default', '', 49),
    (stage_pregatire_sedinta, stage_judecata, 'success', '', 50),
    (stage_pregatire_sedinta, stage_restituire_procuror, 'failure', 'Dosar incomplet', 51),
    (stage_restituire_procuror, stage_finalizare, 'default', 'Completare UP', 52),

    # Acordul de recunoaștere a vinovăției
    (stage_punere_invinuire, stage_acord_vinovatie, 'conditional', 'Acordul de vinovăție', 53),
    (stage_acord_vinovatie, stage_negociere_acord, 'default', '', 54),
    (stage_negociere_acord, stage_judecata_acord, 'default', '', 55),
    (stage_judecata_acord, stage_sentinta_acord, 'success', 'Acord valid', 56),
    (stage_judecata_acord, stage_judecata, 'failure', 'Acord refuzat', 57),
    (stage_sentinta_acord, stage_apel, 'optional', 'Poate fi atacată', 58),

    # Revizuirea (cale extraordinară)
    (stage_hotarare_definitiva, stage_revizuire, 'optional', 'Cale extraordinară', 59),
    (stage_revizuire, stage_cerere_revizuire, 'default', '', 60),
    (stage_cerere_revizuire, stage_examinare_revizuire, 'default', '', 61),
    (stage_examinare_revizuire, stage_hotarare_revizuire, 'default', '', 62),
    (stage_hotarare_revizuire, stage_judecata, 'conditional', 'Rejudecare', 63),
    (stage_hotarare_revizuire, stage_hotarare_definitiva, 'failure', 'Respingere', 64),

    # Liberare provizorie
    (stage_arest, stage_liberare_control, 'optional', 'Substituire arest', 65),
    (stage_arest, stage_liberare_cautiune, 'optional', 'Substituire arest', 66),
    (stage_masuri_preventive, stage_liberare_control, 'conditional', 'Control judiciar', 67),
    (stage_masuri_preventive, stage_liberare_cautiune, 'conditional', 'Pe cauțiune', 68),

    # Reluarea urmăririi
    (stage_incetare, stage_reluare_urmarire, 'conditional', 'Fapte noi', 69),
    (stage_clasare, stage_reluare_urmarire, 'conditional', 'Fapte noi', 70),
    (stage_scoatere, stage_reluare_urmarire, 'conditional', 'Fapte noi', 71),
    (stage_reluare_urmarire, stage_desfasurare, 'default', 'Continuare UP', 72),

    # Executare detalii
    (stage_executare, stage_punere_executare, 'default', '', 73),
    (stage_executare, stage_amanare_executare, 'conditional', 'Amânare', 74),
    (stage_punere_executare, stage_liberare_conditionata, 'conditional', 'După fracție', 75),

    # Cercetare judecătorească - sub-etape
    (stage_cercetare, stage_expunere_invinuire, 'default', '', 76),
    (stage_expunere_invinuire, stage_audiere_inculpat, 'default', '', 77),
    (stage_audiere_inculpat, stage_audiere_martori, 'default', '', 78),
    (stage_audiere_martori, stage_examinare_probe, 'default', '', 79),

    # Dezbateri - sub-etape
    (stage_dezbateri, stage_cuvantari, 'default', '', 80),
    (stage_cuvantari, stage_replica, 'default', '', 81),
    (stage_replica, stage_ultim_cuvant, 'default', '', 82),

    # Deliberare -> Sentința (direct)
    (stage_deliberare, stage_sentinta, 'default', '', 83),

    # Rejudecare din apel
    (stage_decizie_apel, stage_judecata, 'conditional', 'Rejudecare', 84),
]

for source, target, edge_type, label, order in connections:
    StageConnection.objects.create(
        source=source,
        target=target,
        edge_type=edge_type,
        label=label,
        order=order
    )

print(f"""
✅ Данные успешно созданы!

Категории: {ProcedureCategory.objects.count()}
Статьи УПК: {LegalArticle.objects.count()}
Этапы процедуры: {ProcedureStage.objects.count()}
Связи: {StageConnection.objects.count()}

Основные разделы схемы:
  • Sesizarea (ст. 262-265)
  • Pornirea urmăririi penale (ст. 274-276)
  • Desfășurarea urmăririi (ст. 279-282)
  • Măsuri preventive (ст. 165-166, 175-188)
  • Finalizarea urmăririi (ст. 284-291)
  • Rechizitoriul și trimiterea în judecată (ст. 296-297)
  • Judecata (ст. 314, 321, 325)
  • Sentința (ст. 384-391)
  • Căile de atac - Apelul (ст. 400-402)
  • Căile de atac - Recursul (ст. 427, 432)

Теперь запустите сервер:
  source venv/bin/activate
  python manage.py runserver

И откройте:
  http://127.0.0.1:8000/ - схема
  http://127.0.0.1:8000/admin/ - админка (admin/admin)
""")
