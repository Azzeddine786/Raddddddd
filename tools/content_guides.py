# -*- coding: utf-8 -*-
"""Guide pages. Tokens: {link:KEY} -> URL in the page language (falls back to Arabic page),
{{STLIST:filter}} -> auto list of directory stations, {{FREQ}} -> verified frequency table."""

GUIDES = {}

# ---------------------------------------------------------------- listen online
GUIDES['listen-online'] = dict(img='art-online.svg', pill='pill_listener', read=6,
 slug=dict(ar='listen-radio-online-morocco', fr='ecouter-radio-maroc-en-ligne-gratuit', en='listen-moroccan-radio-online-free'),
 ar=dict(title='الاستماع إلى الإذاعات المغربية أونلاين مجاناً: دليل خطوة بخطوة',
  mt='الاستماع للراديو المغربي أونلاين مجاناً | راديو المغرب',
  desc='كيف تستمع إلى الإذاعات المغربية مباشرة عبر الإنترنت مجاناً من الهاتف أو الحاسوب؟ دليل بسيط مع حلول لمشاكل الانقطاع.',
  kw='استمع للراديو المغربي أونلاين, radio maroc en ligne gratuit, الراديو المغربي بدون تطبيق',
  body='''<p>الاستماع إلى إذاعة مغربية عبر الإنترنت أسهل مما يظن كثيرون: لا حساب ولا اشتراك ولا تحميل. يكفي متصفح على الهاتف أو الحاسوب واتصال مستقر. في هذا الدليل نشرح الخطوات، ونقارن بين الطرق، ونعرض كم يستهلك البث من البيانات.</p>
<h2>أسرع طريقة: من دليل المحطات</h2>
<ol><li>افتح <a href="{link:home}#radios">دليل المحطات</a> على موقعنا.</li><li>ابحث عن المحطة بالاسم أو اختر تصنيفاً مثل الأخبار أو الموسيقى أو الرياضة.</li><li>اضغط «استمع» فيظهر المشغّل أسفل الصفحة.</li><li>احفظ محطاتك في المفضلة لتعود إليها بضغطة واحدة؛ تُحفظ المفضلة على جهازك فقط.</li></ol>
<h2>من الهاتف</h2>
<p>افتح الموقع في المتصفح وابدأ البث. إن أردت واجهة مصممة للهاتف فهناك تطبيق «راديو المغرب» المجاني على <a href="https://play.google.com/store/apps/details?id=com.maradioazdhj.radiomoroccoandab" target="_blank" rel="noopener">Google Play</a>. وإن كان البث يتوقف عند قفل الشاشة فاستثنِ المتصفح أو التطبيق من «توفير الطاقة» كما نشرح في <a href="{link:fix}">دليل حلول انقطاع البث</a>.</p>
<h2>من الحاسوب أو التلفاز</h2>
<p>على الحاسوب يعمل البث في أي متصفح حديث، ويمكنك ترك التبويب مفتوحاً أثناء العمل. وللتلفاز أو السماعة الخارجية استعمل البلوتوث أو البث من الهاتف، وهو ما نفصّله في <a href="{link:smart-speaker}">دليل السماعات الذكية</a>.</p>
<h2>كم يستهلك البث من البيانات؟</h2>
<p>يُقدَّر الاستهلاك بين 14 و58 ميغابايت في الساعة بحسب جودة البث. فإن كانت باقتك محدودة فاستمع عبر الواي فاي كلما أمكن، وانظر <a href="{link:car}">كيف تختار الإذاعة المناسبة لسيارتك أو هاتفك</a>.</p>
<h2>من خارج المغرب</h2>
<p>معظم المحطات تبث للعالم كله، وقد تقيّد قلة منها البث جغرافياً لأسباب تتعلق بالحقوق. التفاصيل في <a href="{link:abroad}">دليل الاستماع من الخارج</a>.</p>
<h2>أسئلة شائعة</h2>
<details class="faq"><summary>هل أحتاج إلى تطبيق للاستماع؟</summary><p>لا. الموقع يعمل من المتصفح مباشرة. التطبيق اختياري لمن يريد واجهة مخصصة للهاتف.</p></details>
<details class="faq"><summary>هل الاستماع مجاني فعلاً؟</summary><p>نعم، الدليل مجاني. تدفع فقط ثمن استهلاك الإنترنت لديك.</p></details>
<details class="faq"><summary>لماذا لا يبدأ البث عندي؟</summary><p>جرّب محطة أخرى، ثم أعد تحميل الصفحة، ثم تحقق من الاتصال. وإن استمر الخلل فاتبع الخطوات العشر في دليل الحلول.</p></details>'''),
 fr=dict(title='Écouter la radio marocaine en ligne gratuitement : guide pas à pas',
  mt='Écouter radio Maroc en ligne gratuit | Radio Maroc',
  desc="Comment écouter les radios marocaines en direct sur Internet, gratuitement, depuis un téléphone ou un ordinateur ? Un guide simple, avec des solutions aux coupures.",
  kw='écouter radio maroc gratuit sans application, radio maroc en ligne gratuit, radio marocaine en direct',
  body='''<p>Écouter une radio marocaine sur Internet est plus simple qu'on ne le croit : ni compte, ni abonnement, ni téléchargement. Un navigateur sur téléphone ou ordinateur et une connexion stable suffisent. Ce guide explique les étapes, compare les méthodes et indique la consommation de données.</p>
<h2>La méthode la plus rapide : le guide des stations</h2>
<ol><li>Ouvrez le <a href="{link:home}#radios">guide des stations</a>.</li><li>Cherchez la station par son nom ou choisissez une catégorie : actualité, musique, sport…</li><li>Appuyez sur « Écouter » : le lecteur s'affiche en bas de page.</li><li>Enregistrez vos stations préférées en favoris ; ils sont conservés uniquement sur votre appareil.</li></ol>
<h2>Depuis un téléphone</h2>
<p>Ouvrez le site dans le navigateur et lancez le flux. Si vous préférez une interface pensée pour le mobile, l'application gratuite « Radio Maroc » existe sur <a href="https://play.google.com/store/apps/details?id=com.maradioazdhj.radiomoroccoandab" target="_blank" rel="noopener">Google Play</a>. Si le son s'arrête quand l'écran se verrouille, excluez le navigateur ou l'application des économies d'énergie, comme l'explique notre <a href="{link:fix}">guide des coupures de flux</a> (en arabe).</p>
<h2>Depuis un ordinateur ou un téléviseur</h2>
<p>Sur ordinateur, le flux fonctionne dans tout navigateur récent et vous pouvez laisser l'onglet ouvert pendant que vous travaillez. Pour un téléviseur ou une enceinte, passez par le Bluetooth ou diffusez depuis le téléphone : voir notre <a href="{link:smart-speaker}">guide des enceintes connectées</a>.</p>
<h2>Quelle consommation de données ?</h2>
<p>Comptez environ 14 à 58 Mo par heure selon la qualité du flux. Si votre forfait est limité, écoutez en Wi-Fi quand c'est possible.</p>
<h2>Depuis l'étranger</h2>
<p>La plupart des stations diffusent dans le monde entier ; quelques-unes limitent la diffusion géographiquement pour des raisons de droits. Voir le <a href="{link:abroad}">guide de la diaspora</a> (en arabe).</p>
<h2>Questions fréquentes</h2>
<details class="faq"><summary>Faut-il une application pour écouter ?</summary><p>Non. Le site fonctionne directement dans le navigateur. L'application est facultative.</p></details>
<details class="faq"><summary>L'écoute est-elle vraiment gratuite ?</summary><p>Oui, le guide est gratuit. Vous ne payez que votre consommation Internet.</p></details>
<details class="faq"><summary>Pourquoi le flux ne démarre-t-il pas ?</summary><p>Essayez une autre station, rechargez la page, puis vérifiez votre connexion. Si le problème persiste, suivez les dix étapes du guide de dépannage.</p></details>'''),
 en=dict(title='How to Listen to Moroccan Radio Online for Free: A Step-by-Step Guide',
  mt='Listen to Moroccan Radio Online for Free | Radio Maroc',
  desc='How to stream Moroccan radio live on the internet for free from your phone or computer. A simple guide with fixes for cut-outs.',
  kw='listen to Moroccan radio online, Moroccan radio live free, Moroccan radio no app',
  body='''<p>Listening to a Moroccan radio station online is easier than most people think: no account, no subscription and no download. A browser on your phone or computer and a steady connection are enough. This guide walks through the steps, compares the options and shows how much data streaming uses.</p>
<h2>The fastest way: the station directory</h2>
<ol><li>Open the <a href="{link:home}#radios">station directory</a>.</li><li>Search for a station by name or pick a category such as news, music or sports.</li><li>Press “Listen” and the player appears at the bottom of the page.</li><li>Save your stations to favorites to return with one tap; favorites are stored on your device only.</li></ol>
<h2>On a phone</h2>
<p>Open the site in your browser and start the stream. If you want an interface built for phones, the free Radio Maroc app is on <a href="https://play.google.com/store/apps/details?id=com.maradioazdhj.radiomoroccoandab" target="_blank" rel="noopener">Google Play</a>. If audio stops when the screen locks, exclude the browser or app from battery saving, as explained in our <a href="{link:fix}">guide to stream cut-outs</a> (in Arabic).</p>
<h2>On a computer or TV</h2>
<p>On a computer the stream works in any modern browser, and you can leave the tab open while you work. For a TV or speaker, use Bluetooth or stream from your phone; see our <a href="{link:smart-speaker}">smart speaker guide</a>.</p>
<h2>How much data does it use?</h2>
<p>Roughly 14 to 58 MB per hour depending on stream quality. If your data plan is limited, listen over Wi-Fi when you can.</p>
<h2>From outside Morocco</h2>
<p>Most stations broadcast worldwide, although a few restrict streaming by region for rights reasons. See the <a href="{link:abroad}">guide for listeners abroad</a> (in Arabic).</p>
<h2>Frequently asked questions</h2>
<details class="faq"><summary>Do I need an app to listen?</summary><p>No. The site works directly in your browser. The app is optional.</p></details>
<details class="faq"><summary>Is listening really free?</summary><p>Yes, the directory is free. You only pay for your own internet data.</p></details>
<details class="faq"><summary>Why won’t the stream start?</summary><p>Try another station, reload the page, then check your connection. If it still fails, follow the ten steps in the troubleshooting guide.</p></details>'''))

# ---------------------------------------------------------------- Medi 1 channels
GUIDES['medi1-channels'] = dict(img='art-music.svg', pill='pill_music', read=4,
 slug=dict(ar='medi1-music-channels-guide', fr='chaines-musicales-medi-1', en='medi-1-music-channels-guide'),
 ar=dict(title='قنوات ميدي 1 الموسيقية: أندلسية ونايضة وصوفي وطرب، ماذا تسمع في كل قناة؟',
  mt='قنوات ميدي 1 الموسيقية: نايضة وأندلسية وصوفي | راديو المغرب',
  desc='تعرّف على قنوات ميدي 1 المتخصصة: الأندلسية والنايضة والصوفي والطرب، وما يميز كل قناة، مع رابط الاستماع المباشر.',
  kw='ميدي 1 نايضة مباشر, ميدي 1 أندلسية مباشر, ميدي 1 صوفي مباشر, Medi 1 Tarab',
  body='''<p>إلى جانب البث الرئيسي لميدي 1 راديو، تتفرع عنه قنوات موسيقية متخصصة عبر الإنترنت، كل قناة لنمط واحد بلا فواصل إخبارية. نجمع هنا روابطها كلها، ونقترح متى تناسبك كل واحدة.</p>
<h2>القنوات المتاحة في دليلنا</h2>
{{STLIST:prefix:Medi 1}}
<h2>التراث والطرب</h2>
<p><strong>أندلسية:</strong> قناة الأندلسي والطرب المغربي، حيث تسمع الآلة والموشحات والأغاني الأندلسية دون انقطاع. مناسبة للمساء الهادئ والمجالس العائلية. <strong>طرب وكلاسيك:</strong> للموسيقى العربية الكلاسيكية. <strong>صوفي:</strong> قناة تصنّفها في دليلنا ضمن الفئة الدينية، مناسبة لقبل النوم.</p>
<h2>الإيقاعات الحديثة</h2>
<p><strong>نايضة:</strong> اسمها مأخوذ من حركة «النايضة» الموسيقية المغربية، وتقدم إيقاعات الشباب العصرية ومزجاً بين الأنماط. وهناك قنوات <strong>هيتس</strong> و<strong>دي جي</strong> و<strong>لاتينو</strong> و<strong>جاز</strong> و<strong>لاونج</strong> و<strong>أكوستيك</strong> لأذواق متنوعة، و<strong>فرانسيز</strong> للأغاني الفرنسية.</p>
<h2>كيف تختار؟</h2>
<ul><li>للتركيز أثناء العمل: أكوستيك أو كلاسيك، حتى لا يشتت الكلام تركيزك.</li><li>للتراث: الأندلسية.</li><li>للمزاج العصري: نايضة أو هيتس.</li><li>للأخبار بدل الموسيقى: <a href="{link:medi-1-radio}">ميدي 1 راديو</a>.</li></ul>
<p>للتعرف على أنماط الموسيقى المغربية أكثر اقرأ <a href="{link:music}">الموسيقى المغربية على الراديو</a>، وانظر أيضاً <a href="{link:chaabi}">الشعبي والنايضة على الراديو</a>.</p>'''),
 fr=dict(title='Les chaînes musicales de Medi 1 : andalou, nayda, soufi, tarab… que trouve-t-on sur chacune ?',
  mt='Chaînes musicales Medi 1 : nayda, andalou, soufi | Radio Maroc',
  desc='Découvrez les chaînes spécialisées de Medi 1 : andalou, nayda, soufi, tarab… ce qui les distingue, avec écoute directe.',
  kw='medi 1 nayda en direct, medi 1 andalouse en direct, medi 1 soufi, medi 1 tarab',
  body='''<p>En plus de l'antenne principale de Medi 1 Radio, la marque propose sur Internet des chaînes musicales spécialisées, chacune consacrée à un seul style, sans bulletins d'information. Nous réunissons ici leurs liens et suggérons quand écouter chacune.</p>
<h2>Les chaînes disponibles dans notre guide</h2>
{{STLIST:prefix:Medi 1}}
<h2>Patrimoine et tarab</h2>
<p><strong>Andalouse :</strong> la chaîne de musique andalouse et de tarab marocain, avec l'orchestre, les muwashshahat et les chants andalous sans interruption ; idéale pour une soirée calme ou un moment en famille. <strong>Tarab et Classique :</strong> pour la musique arabe classique. <strong>Soufi :</strong> classée dans la catégorie Religieuse de notre guide, elle convient avant de dormir.</p>
<h2>Rythmes actuels</h2>
<p><strong>Nayda :</strong> son nom vient du mouvement musical marocain « nayda » ; elle propose des rythmes jeunes et modernes et des mélanges de styles. On trouve aussi <strong>Hits</strong>, <strong>DJ</strong>, <strong>Latino</strong>, <strong>Jazz</strong>, <strong>Lounge</strong> et <strong>Acoustic</strong> pour des goûts variés, et <strong>Française</strong> pour la chanson française.</p>
<h2>Comment choisir ?</h2>
<ul><li>Pour se concentrer au travail : Acoustic ou Classique, pour que les paroles ne vous distraient pas.</li><li>Pour le patrimoine : Andalouse.</li><li>Pour une ambiance actuelle : Nayda ou Hits.</li><li>Pour l'actualité plutôt que la musique : <a href="{link:medi-1-radio}">Medi 1 Radio</a>.</li></ul>
<p>Pour mieux connaître les styles de musique marocaine, lisez <a href="{link:music}">la musique marocaine à la radio</a> (en arabe) et notre guide <a href="{link:chaabi}">chaâbi et nayda à la radio</a>.</p>'''),
 en=dict(title='The Medi 1 Music Channels: Andalusi, Nayda, Sufi, Tarab and More',
  mt='Medi 1 Music Channels: Nayda, Andalusi, Sufi | Radio Maroc',
  desc='Meet the specialised Medi 1 channels: Andalusi, Nayda, Sufi, Tarab and more, what sets each one apart, with live listening links.',
  kw='Medi 1 Nayda live, Medi 1 Andalouse live, Medi 1 Soufi, Medi 1 Tarab',
  body='''<p>Besides the main Medi 1 Radio broadcast, the brand runs specialised music channels online, each devoted to a single style with no news bulletins. We gather their links here and suggest when each one fits.</p>
<h2>The channels in our directory</h2>
{{STLIST:prefix:Medi 1}}
<h2>Heritage and tarab</h2>
<p><strong>Andalouse:</strong> the channel for Andalusi music and Moroccan tarab, with the orchestra, muwashshahat and Andalusi songs and no interruptions; good for a calm evening or family gatherings. <strong>Tarab and Classique:</strong> for classical Arabic music. <strong>Soufi:</strong> filed under Religious in our directory, a fit for before bed.</p>
<h2>Modern rhythms</h2>
<p><strong>Nayda:</strong> named after the Moroccan “nayda” music movement, it plays young, modern rhythms and genre blends. There are also <strong>Hits</strong>, <strong>DJ</strong>, <strong>Latino</strong>, <strong>Jazz</strong>, <strong>Lounge</strong> and <strong>Acoustic</strong> channels for different tastes, and <strong>Française</strong> for French songs.</p>
<h2>How to choose</h2>
<ul><li>To focus at work: Acoustic or Classique, so lyrics do not distract you.</li><li>For heritage: Andalouse.</li><li>For a contemporary mood: Nayda or Hits.</li><li>For news rather than music: <a href="{link:medi-1-radio}">Medi 1 Radio</a>.</li></ul>
<p>To learn more about the styles of Moroccan music, read <a href="{link:music}">Moroccan music on the radio</a> (in Arabic) and our guide to <a href="{link:chaabi}">chaabi and nayda on the radio</a>.</p>'''))

# ---------------------------------------------------------------- FM frequencies hub
GUIDES['fm-frequencies'] = dict(img='art-regional.svg', pill='pill_guide', read=5,
 slug=dict(ar='moroccan-radio-fm-frequencies-by-city', fr='frequences-radios-maroc-fm-par-ville', en='moroccan-radio-fm-frequencies-by-city'),
 ar=dict(title='ترددات الإذاعات المغربية FM حسب المدينة: الدار البيضاء والرباط ومراكش وطنجة',
  mt='ترددات الإذاعات المغربية FM حسب المدينة | راديو المغرب',
  desc='محطات الإذاعات المغربية حسب المدينة، وكيف تعرف تردد FM لكل محطة في مدينتك، مع رابط البث المباشر لكل محطة.',
  kw='ترددات الإذاعات المغربية FM, fréquences radios Maroc FM, تردد راديو مارس, تردد هيت راديو',
  body='''<p>تختلف ترددات FM من مدينة إلى أخرى، وقد تتغير مع الوقت، ولذلك لا ننشر رقماً قبل التحقق منه من مصدر رسمي. تجد في هذه الصفحة المحطات مرتبة حسب المدينة، وجدولاً للترددات يُملأ بالأرقام التي تأكدنا منها، وطرقاً موثوقة لمعرفة التردد في مدينتك.</p>
<h2>الترددات المؤكدة</h2>
{{FREQ}}
<h2>كيف تعرف تردد المحطة في مدينتك؟</h2>
<ol><li><strong>الموقع الرسمي للمحطة</strong> أو حساباتها الرسمية، فغالباً تنشر الترددات حسب المدن.</li><li><strong>مستقبل السيارة:</strong> فعّل البحث التلقائي عن المحطات، فيعرض كثير منها أسماءها بدل الأرقام.</li><li><strong>خطط الترددات</strong> التي تنشرها الهيئة العليا للاتصال السمعي البصري (HACA).</li><li><strong>الاستماع عبر الإنترنت</strong> من دليلنا، فلا يحتاج إلى تردد أصلاً.</li></ol>
<h2>المحطات حسب المدينة</h2>
<h3>الدار البيضاء</h3>
{{STLIST:city:الدار البيضاء}}
<h3>الرباط</h3>
{{STLIST:city:الرباط}}
<h3>طنجة</h3>
{{STLIST:city:طنجة}}
<h3>مراكش</h3>
{{STLIST:city:مراكش}}
<p>لمزيد من التفاصيل عن الإذاعات في مناطق أخرى انظر <a href="{link:regional}">دليل الإذاعات الجهوية المغربية</a>.</p>'''),
 fr=dict(title='Fréquences FM des radios marocaines par ville : Casablanca, Rabat, Marrakech, Tanger',
  mt='Fréquences radios Maroc FM par ville | Radio Maroc',
  desc='Les radios marocaines par ville et comment trouver la fréquence FM de chaque station chez vous, avec écoute directe.',
  kw='fréquences radios Maroc FM, fréquence radio mars casablanca, fréquence hit radio, fréquence medi 1',
  body='''<p>Les fréquences FM varient d'une ville à l'autre et peuvent changer avec le temps ; c'est pourquoi nous ne publions un chiffre qu'après l'avoir vérifié auprès d'une source officielle. Cette page présente les stations par ville, un tableau des fréquences confirmées et des moyens fiables de trouver la fréquence dans votre ville.</p>
<h2>Fréquences confirmées</h2>
{{FREQ}}
<h2>Comment trouver la fréquence d'une station chez vous ?</h2>
<ol><li><strong>Le site officiel de la station</strong> ou ses comptes officiels, qui publient souvent les fréquences par ville.</li><li><strong>L'autoradio :</strong> activez la recherche automatique ; beaucoup affichent le nom des stations au lieu des chiffres.</li><li><strong>Les plans de fréquences</strong> publiés par la HACA, le régulateur de l'audiovisuel.</li><li><strong>L'écoute en ligne</strong> depuis notre guide, qui ne demande aucune fréquence.</li></ol>
<h2>Stations par ville</h2>
<h3>Casablanca</h3>
{{STLIST:city:الدار البيضاء}}
<h3>Rabat</h3>
{{STLIST:city:الرباط}}
<h3>Tanger</h3>
{{STLIST:city:طنجة}}
<h3>Marrakech</h3>
{{STLIST:city:مراكش}}
<p>Pour les radios des autres régions, voyez le <a href="{link:regional}">guide des radios régionales marocaines</a> (en arabe).</p>'''),
 en=dict(title='FM Frequencies of Moroccan Radio Stations by City: Casablanca, Rabat, Marrakech, Tangier',
  mt='Moroccan Radio FM Frequencies by City | Radio Maroc',
  desc='Moroccan radio stations by city and how to find each station’s FM frequency where you live, with live listening links.',
  kw='Moroccan radio FM frequencies, Radio Mars frequency, Hit Radio frequency, Medi 1 frequency',
  body='''<p>FM frequencies differ from city to city and can change over time, which is why we only publish a number after verifying it with an official source. This page lists the stations by city, a table of confirmed frequencies, and reliable ways to find the frequency in your own city.</p>
<h2>Confirmed frequencies</h2>
{{FREQ}}
<h2>How to find a station’s frequency where you live</h2>
<ol><li><strong>The station’s official website</strong> or official social accounts, which often list frequencies by city.</li><li><strong>Your car radio:</strong> turn on automatic scanning; many sets show station names instead of numbers.</li><li><strong>Frequency plans</strong> published by the HACA, Morocco’s audiovisual regulator.</li><li><strong>Listening online</strong> from our directory, which needs no frequency at all.</li></ol>
<h2>Stations by city</h2>
<h3>Casablanca</h3>
{{STLIST:city:الدار البيضاء}}
<h3>Rabat</h3>
{{STLIST:city:الرباط}}
<h3>Tangier</h3>
{{STLIST:city:طنجة}}
<h3>Marrakech</h3>
{{STLIST:city:مراكش}}
<p>For stations in other regions, see our <a href="{link:regional}">guide to Morocco’s regional radio stations</a> (in Arabic).</p>'''))

# ---------------------------------------------------------------- French-language radio
GUIDES['french-radio'] = dict(img='art-stations.svg', pill='pill_guide', read=4,
 slug=dict(ar='moroccan-french-language-radio', fr='radios-marocaines-en-francais', en='french-language-radio-morocco'),
 ar=dict(title='الإذاعات المغربية الناطقة بالفرنسية: دليل الاستماع',
  mt='الإذاعات المغربية بالفرنسية: القائمة الكاملة | راديو المغرب',
  desc='قائمة الإذاعات المغربية التي تبث كلياً أو جزئياً بالفرنسية: الأخبار والموسيقى والحوار، مع الاستماع المباشر المجاني.',
  kw='radios marocaines en français, إذاعات مغربية بالفرنسية, radio marocaine francophone',
  body='''<p>الفرنسية حاضرة بقوة في المشهد الإذاعي المغربي، سواء كلغة كاملة للبث أو مزجاً مع العربية والدارجة. هذا الدليل يجمع المحطات التي تبث بالفرنسية في دليلنا، مرتبة بحسب ما تجده عند كل واحدة.</p>
<h2>المحطات التي تبث بالفرنسية</h2>
{{STLIST:lang:فرنسية}}
<h2>كيف تختار؟</h2>
<ul><li><strong>الأخبار بلغتين:</strong> <a href="{link:medi-1-radio}">ميدي 1 راديو</a> بالعربية والفرنسية، و<a href="{link:atlantic-radio}">أطلنتيك راديو</a> بالفرنسية والدارجة.</li><li><strong>الموسيقى:</strong> <a href="{link:hit-radio-maroc}">هيت راديو</a> وقناة ميدي 1 فرانسيز لمحبي الأغنية الفرنسية.</li><li><strong>الحوار والمجتمع:</strong> <a href="{link:med-radio}">ميد راديو</a>.</li></ul>
<h2>نصيحة لمن يتعلم الفرنسية</h2>
<p>ابدأ بمحطة تتحدث بالدارجة والفرنسية معاً ثم انتقل تدريجياً إلى محطة فرنسية كاملة. الإذاعة وسيلة ممتازة لتدريب الأذن على الإيقاع الطبيعي للغة.</p>'''),
 fr=dict(title='Radios marocaines en français : les meilleures stations à écouter en direct',
  mt='Radios marocaines en français : les stations | Radio Maroc',
  desc='Les radios marocaines qui émettent en français, en tout ou en partie : actualité, musique et débats, avec écoute en direct et gratuite.',
  kw='radios marocaines en français, radio marocaine francophone, écouter radio maroc en français',
  body='''<p>Le français est très présent dans le paysage radiophonique marocain, soit comme langue complète d'antenne, soit mêlé à l'arabe et à la darija. Ce guide réunit les stations de notre annuaire qui émettent en français, avec ce que l'on peut attendre de chacune.</p>
<h2>Les stations qui émettent en français</h2>
{{STLIST:lang:فرنسية}}
<h2>Comment choisir ?</h2>
<ul><li><strong>L'actualité en deux langues :</strong> <a href="{link:medi-1-radio}">Medi 1 Radio</a> en arabe et en français, et <a href="{link:atlantic-radio}">Atlantic Radio</a> en français et en darija.</li><li><strong>La musique :</strong> <a href="{link:hit-radio-maroc}">Hit Radio</a>, et la chaîne Medi 1 Française pour la chanson française.</li><li><strong>Le débat et la société :</strong> <a href="{link:med-radio}">Med Radio</a>.</li></ul>
<h2>Un conseil si vous apprenez le français</h2>
<p>Commencez par une station qui mélange darija et français, puis passez progressivement à une station entièrement française. La radio est un excellent moyen d'habituer l'oreille au rythme naturel de la langue.</p>
<h2>Écouter depuis la France ou l'Europe</h2>
<p>Les stations marocaines diffusent pour la plupart dans le monde entier. Notre guide <a href="{link:listen-online}">pour écouter la radio marocaine en ligne</a> explique comment faire, et le <a href="{link:abroad}">guide de la diaspora</a> (en arabe) détaille les décalages horaires et les restrictions géographiques.</p>'''),
 en=dict(title='French-Language Radio in Morocco: The Best Stations to Listen to Live',
  mt='French-Language Radio in Morocco | Radio Maroc',
  desc='Moroccan radio stations that broadcast in French, fully or partly: news, music and talk, with free live listening.',
  kw='French radio Morocco, Moroccan radio in French, listen to Moroccan radio in French',
  body='''<p>French has a strong presence in Moroccan radio, either as the full language of the broadcast or mixed with Arabic and Darija. This guide gathers the stations in our directory that broadcast in French and what to expect from each.</p>
<h2>Stations that broadcast in French</h2>
{{STLIST:lang:فرنسية}}
<h2>How to choose</h2>
<ul><li><strong>News in two languages:</strong> <a href="{link:medi-1-radio}">Medi 1 Radio</a> in Arabic and French, and <a href="{link:atlantic-radio}">Atlantic Radio</a> in French and Darija.</li><li><strong>Music:</strong> <a href="{link:hit-radio-maroc}">Hit Radio</a>, and the Medi 1 Française channel for French songs.</li><li><strong>Talk and society:</strong> <a href="{link:med-radio}">Med Radio</a>.</li></ul>
<h2>A tip if you are learning French</h2>
<p>Start with a station that mixes Darija and French, then move gradually to a fully French one. Radio is an excellent way to train your ear to the natural rhythm of a language.</p>
<h2>Listening from France or Europe</h2>
<p>Most Moroccan stations broadcast worldwide. Our guide to <a href="{link:listen-online}">listening to Moroccan radio online</a> explains how, and the <a href="{link:abroad}">guide for listeners abroad</a> (in Arabic) covers time differences and regional restrictions.</p>'''))

# ---------------------------------------------------------------- Casablanca
GUIDES['casablanca'] = dict(img='art-regional.svg', pill='pill_guide', read=4,
 slug=dict(ar='casablanca-radio-stations', fr='radios-casablanca-en-direct', en='casablanca-radio-stations'),
 ar=dict(title='إذاعات الدار البيضاء: أبرز المحطات وكيف تستمع إليها مباشرة',
  mt='إذاعات الدار البيضاء FM: القائمة الكاملة | راديو المغرب',
  desc='تعرّف على أبرز إذاعات الدار البيضاء وما تقدمه كل محطة، مع رابط الاستماع المباشر.',
  kw='إذاعات الدار البيضاء FM, radio Casablanca en direct, Radio Mars Casablanca',
  body='''<p>تحتضن الدار البيضاء عدداً كبيراً من الإذاعات الخاصة، من الموسيقى إلى الرياضة والحوار والأخبار. وفي ما يلي المحطات المرتبطة بالمدينة في دليلنا مع ما يميز كل واحدة.</p>
<h2>محطات الدار البيضاء في الدليل</h2>
{{STLIST:city:الدار البيضاء}}
<h2>اختر حسب ما تريد</h2>
<ul><li><strong>الرياضة:</strong> <a href="{link:radio-mars}">راديو مارس</a>.</li><li><strong>الموسيقى الحديثة:</strong> <a href="{link:hit-radio-maroc}">هيت راديو</a> و<a href="{link:uradio-maroc}">يو راديو</a>.</li><li><strong>الأغنية بالدارجة:</strong> <a href="{link:chada-fm}">شذى إف إم</a>.</li><li><strong>الحوار والمجتمع:</strong> <a href="{link:med-radio}">ميد راديو</a> و<a href="{link:radio-aswat}">أصوات راديو</a>.</li><li><strong>الفرنسية:</strong> <a href="{link:atlantic-radio}">أطلنتيك راديو</a>.</li></ul>
<h2>والتردد؟</h2>
<p>إن كنت في الدار البيضاء وتريد التردد على موجة FM فانظر <a href="{link:fm-frequencies}">دليل ترددات الإذاعات حسب المدينة</a>. أما الاستماع من هاتفك فيكفيه زر «استمع».</p>'''),
 fr=dict(title='Les radios de Casablanca : stations principales et écoute en direct',
  mt='Radios de Casablanca en direct | Radio Maroc',
  desc='Les principales radios de Casablanca et ce que propose chaque station, avec écoute directe.',
  kw='radio Casablanca en direct, radios Casablanca FM, radio mars casablanca',
  body='''<p>Casablanca abrite un grand nombre de radios privées, de la musique au sport, du débat à l'actualité. Voici les stations liées à la ville dans notre guide, avec ce qui distingue chacune.</p>
<h2>Les stations de Casablanca dans le guide</h2>
{{STLIST:city:الدار البيضاء}}
<h2>Choisir selon l'envie</h2>
<ul><li><strong>Le sport :</strong> <a href="{link:radio-mars}">Radio Mars</a>.</li><li><strong>La musique actuelle :</strong> <a href="{link:hit-radio-maroc}">Hit Radio</a> et <a href="{link:uradio-maroc}">URADIO</a>.</li><li><strong>La chanson en darija :</strong> <a href="{link:chada-fm}">Chada FM</a>.</li><li><strong>Le débat et la société :</strong> <a href="{link:med-radio}">Med Radio</a> et <a href="{link:radio-aswat}">Radio Aswat</a>.</li><li><strong>Le français :</strong> <a href="{link:atlantic-radio}">Atlantic Radio</a>.</li></ul>
<h2>Et la fréquence ?</h2>
<p>Si vous êtes à Casablanca et cherchez la fréquence FM, consultez notre <a href="{link:fm-frequencies}">guide des fréquences par ville</a>. Pour écouter depuis votre téléphone, le bouton « Écouter » suffit.</p>'''),
 en=dict(title='Casablanca Radio Stations: The Main Stations and How to Listen Live',
  mt='Casablanca Radio Stations Live | Radio Maroc',
  desc='The main radio stations of Casablanca and what each one offers, with live listening links.',
  kw='Casablanca radio stations, Casablanca radio live, Radio Mars Casablanca',
  body='''<p>Casablanca is home to many private radio stations, from music to sports, talk and news. Here are the stations tied to the city in our directory and what sets each one apart.</p>
<h2>Casablanca stations in the directory</h2>
{{STLIST:city:الدار البيضاء}}
<h2>Choose by what you want</h2>
<ul><li><strong>Sports:</strong> <a href="{link:radio-mars}">Radio Mars</a>.</li><li><strong>Modern music:</strong> <a href="{link:hit-radio-maroc}">Hit Radio</a> and <a href="{link:uradio-maroc}">URADIO</a>.</li><li><strong>Songs in Darija:</strong> <a href="{link:chada-fm}">Chada FM</a>.</li><li><strong>Talk and society:</strong> <a href="{link:med-radio}">Med Radio</a> and <a href="{link:radio-aswat}">Radio Aswat</a>.</li><li><strong>French:</strong> <a href="{link:atlantic-radio}">Atlantic Radio</a>.</li></ul>
<h2>What about the frequency?</h2>
<p>If you are in Casablanca and want the FM frequency, see our <a href="{link:fm-frequencies}">guide to frequencies by city</a>. To listen from your phone, the “Listen” button is all you need.</p>'''))

# ---------------------------------------------------------------- smart speakers
GUIDES['smart-speaker'] = dict(img='art-car.svg', pill='pill_listener', read=4,
 slug=dict(ar='moroccan-radio-alexa-google-home', fr='radio-marocaine-alexa-google-home', en='moroccan-radio-alexa-google-home'),
 ar=dict(title='كيف تستمع إلى الإذاعات المغربية عبر أليكسا وجوجل هوم والمكبرات الذكية؟',
  mt='الراديو المغربي على أليكسا وجوجل هوم | راديو المغرب',
  desc='طرق الاستماع إلى الإذاعات المغربية على المكبرات الذكية والسماعات، مع خطوات بسيطة وحلول للمشاكل الشائعة.',
  kw='الراديو المغربي أليكسا, radio marocaine Alexa Google Home, مكبر صوت ذكي راديو مغربي',
  body='''<p>هل يمكن أن تطلب من مكبر الصوت الذكي تشغيل إذاعة مغربية؟ أحياناً نعم، لكن ذلك يعتمد على خدمة الراديو التي يستعملها مكبرك، وتغطية المحطات المغربية فيها تختلف وتتغير، لذلك لا نعدك بأمر صوتي بعينه. الطريقة التي تنجح دائماً هي الاستماع من هاتفك وتمرير الصوت إلى المكبر.</p>
<h2>الطريقة 1: البلوتوث</h2>
<p>اقرن هاتفك بالمكبر ثم شغّل أي محطة من <a href="{link:home}#radios">دليلنا</a>. لإقران أليكسا قل «Alexa, pair»، ولجوجل هوم قل «Hey Google, Bluetooth pairing»، ثم اختر المكبر من إعدادات البلوتوث في هاتفك. يستهلك الهاتف البيانات، ويعمل المكبر كسماعة فقط.</p>
<h2>الطريقة 2: البث من المتصفح أو الهاتف</h2>
<p>إن كان عندك مكبر أو تلفاز يدعم Chromecast أو AirPlay فيمكنك بث الصوت إليه من المتصفح أو من إعدادات الصوت في هاتفك. تختلف الخطوات بحسب الجهاز، فجرّبها مرة قبل الاعتماد عليها.</p>
<h2>الطريقة 3: سماعة بسلك أو مدخل AUX</h2>
<p>الأبسط والأكثر ثباتاً: كابل من الهاتف إلى المكبر. لا يحتاج إلى إعدادات ولا ينقطع بسبب الاقتران.</p>
<h2>إن لم يعمل الصوت</h2>
<ul><li>تأكد أن الصوت موجّه إلى المكبر لا إلى سماعة أخرى متصلة بالبلوتوث.</li><li>أعد الإقران، وقرّب الهاتف من المكبر.</li><li>جرّب محطة أخرى للتأكد أن المشكلة ليست في الجهاز؛ وراجع <a href="{link:fix}">دليل حلول انقطاع البث</a>.</li></ul>
<p>وللاستماع في السيارة والهاتف اقرأ <a href="{link:car}">كيف تختار الإذاعة المناسبة لسيارتك أو هاتفك</a>.</p>'''),
 fr=dict(title='Écouter les radios marocaines avec Alexa, Google Home et les enceintes connectées',
  mt='Radio marocaine sur Alexa et Google Home | Radio Maroc',
  desc="Comment écouter les radios marocaines sur une enceinte connectée : étapes simples et solutions aux problèmes courants.",
  kw='radio marocaine Alexa, radio marocaine Google Home, enceinte connectée radio maroc',
  body='''<p>Peut-on demander à une enceinte connectée de lancer une radio marocaine ? Parfois oui, mais cela dépend du service radio qu'utilise votre enceinte, et la présence des stations marocaines y varie et change ; nous ne promettons donc aucune commande vocale précise. La méthode qui fonctionne toujours consiste à écouter depuis votre téléphone et à envoyer le son vers l'enceinte.</p>
<h2>Méthode 1 : le Bluetooth</h2>
<p>Associez votre téléphone à l'enceinte, puis lancez une station depuis <a href="{link:home}#radios">notre guide</a>. Pour associer une enceinte Alexa, dites « Alexa, pair » ; pour Google Home, « Hey Google, Bluetooth pairing », puis choisissez l'enceinte dans les réglages Bluetooth du téléphone. Le téléphone consomme les données et l'enceinte sert simplement de haut-parleur.</p>
<h2>Méthode 2 : la diffusion depuis le navigateur ou le téléphone</h2>
<p>Si votre enceinte ou votre téléviseur prend en charge Chromecast ou AirPlay, vous pouvez y envoyer le son depuis le navigateur ou les réglages audio du téléphone. Les étapes varient selon l'appareil ; essayez-les une fois avant de compter dessus.</p>
<h2>Méthode 3 : le câble ou l'entrée AUX</h2>
<p>La plus simple et la plus stable : un câble du téléphone à l'enceinte. Aucun réglage, aucune coupure liée à l'association.</p>
<h2>Si le son ne marche pas</h2>
<ul><li>Vérifiez que le son est dirigé vers l'enceinte et non vers un autre appareil Bluetooth.</li><li>Refaites l'association et rapprochez le téléphone de l'enceinte.</li><li>Essayez une autre station pour écarter un problème d'appareil ; voyez le <a href="{link:fix}">guide des coupures de flux</a> (en arabe).</li></ul>
<p>Pour la voiture et le téléphone, lisez <a href="{link:car}">comment choisir sa radio</a> (en arabe).</p>'''),
 en=dict(title='How to Listen to Moroccan Radio on Alexa, Google Home and Smart Speakers',
  mt='Moroccan Radio on Alexa and Google Home | Radio Maroc',
  desc='Ways to listen to Moroccan radio on smart speakers, with simple steps and fixes for common problems.',
  kw='Moroccan radio Alexa, Moroccan radio Google Home, smart speaker Moroccan radio',
  body='''<p>Can you ask a smart speaker to play a Moroccan station? Sometimes, but it depends on the radio service your speaker uses, and coverage of Moroccan stations there varies and changes, so we do not promise any specific voice command. The method that always works is to listen on your phone and send the sound to the speaker.</p>
<h2>Method 1: Bluetooth</h2>
<p>Pair your phone with the speaker, then play any station from <a href="{link:home}#radios">our directory</a>. To pair an Alexa speaker say “Alexa, pair”; for Google Home say “Hey Google, Bluetooth pairing”, then pick the speaker in your phone’s Bluetooth settings. The phone uses the data and the speaker simply acts as a loudspeaker.</p>
<h2>Method 2: casting from the browser or phone</h2>
<p>If your speaker or TV supports Chromecast or AirPlay, you can send audio to it from the browser or from your phone’s audio settings. The steps vary by device, so try them once before relying on them.</p>
<h2>Method 3: cable or AUX input</h2>
<p>The simplest and steadiest: a cable from the phone to the speaker. No setup and no pairing dropouts.</p>
<h2>If there is no sound</h2>
<ul><li>Check that audio is routed to the speaker and not to another Bluetooth device.</li><li>Pair again and move the phone closer to the speaker.</li><li>Try another station to rule out a device problem; see the <a href="{link:fix}">guide to stream cut-outs</a> (in Arabic).</li></ul>
<p>For the car and phone, read <a href="{link:car}">how to choose a radio</a> (in Arabic).</p>'''))

# ---------------------------------------------------------------- chaabi / nayda
GUIDES['chaabi'] = dict(img='art-music.svg', pill='pill_music', read=4,
 slug=dict(ar='chaabi-radio-morocco', fr='radio-chaabi-nayda-maroc', en='chaabi-nayda-radio-morocco'),
 ar=dict(title='الشعبي والنايضة على الراديو المغربي: أين تسمعهما مباشرة؟',
  mt='الراديو الشعبي المغربي والنايضة مباشر | راديو المغرب',
  desc='أين تسمع الأغاني الشعبية المغربية والنايضة مباشرة على الراديو؟ دليل عملي للمحطات والقنوات مع رابط الاستماع.',
  kw='إذاعة الأغاني الشعبية المغربية, radio chaabi maroc, النايضة راديو',
  body='''<p>الشعبي من أكثر الأنماط حضوراً في الأذن المغربية، والنايضة حركة موسيقية حديثة تمزج الأنماط. لكن لا توجد قناة واحدة مخصصة للشعبي في دليلنا، لذلك نقترح طريقة عملية لتجد ما تريد.</p>
<h2>قناة مخصصة للنايضة</h2>
<p>تجد في الدليل قناة <a href="{link:medi1-channels}">ميدي 1 نايضة</a> المتخصصة في إيقاعات الجيل الجديد، دون فواصل إخبارية. وتجد قناة الأندلسي لمن يبحث عن التراث.</p>
<h2>المحطات الموسيقية الناطقة بالدارجة</h2>
<p>المحطات التي تبث الأغاني بالدارجة هي الأقرب لمحبي الأغنية الشعبية، ومنها في دليلنا:</p>
{{STLIST:ids:17,21}}
<p>تتغير الشبكات البرامجية بين فترة وأخرى، فتحقق من جدول البرامج على موقع المحطة قبل أن تعتمد على فقرة بعينها، ولا تتوقع الشعبي في كل ساعة من اليوم.</p>
<h2>نصيحة</h2>
<p>جرّب المحطة في أوقات مختلفة: المساء وعطلة نهاية الأسبوع أنسب لسهرات الأغنية الشعبية في العادة. ولفهم الأنماط الأخرى اقرأ <a href="{link:music}">الموسيقى المغربية على الراديو</a>.</p>'''),
 fr=dict(title='Chaâbi et nayda à la radio marocaine : où les écouter en direct ?',
  mt='Radio chaâbi et nayda au Maroc en direct | Radio Maroc',
  desc='Où écouter le chaâbi et la nayda en direct à la radio ? Un guide pratique des stations et chaînes, avec écoute directe.',
  kw='radio chaabi maroc, radio nayda en direct, chaabi marocain radio',
  body='''<p>Le chaâbi est l'un des styles les plus présents dans l'oreille marocaine, et la nayda un mouvement musical récent qui mélange les genres. Notre guide ne compte pourtant pas de chaîne unique consacrée au chaâbi ; voici donc une méthode pratique pour trouver ce que vous cherchez.</p>
<h2>Une chaîne dédiée à la nayda</h2>
<p>Le guide propose <a href="{link:medi1-channels}">Medi 1 Nayda</a>, consacrée aux rythmes de la nouvelle génération, sans bulletins d'information. Vous y trouverez aussi la chaîne andalouse pour le patrimoine.</p>
<h2>Les stations musicales en darija</h2>
<p>Les stations qui diffusent des chansons en darija sont les plus proches des amateurs de chanson populaire. Dans notre guide :</p>
{{STLIST:ids:17,21}}
<p>Les grilles changent de temps en temps : vérifiez le programme sur le site de la station avant de compter sur une émission précise, et n'attendez pas du chaâbi à toute heure.</p>
<h2>Un conseil</h2>
<p>Essayez la station à différents moments : le soir et le week-end conviennent en général mieux aux soirées de chanson populaire. Pour les autres styles, lisez <a href="{link:music}">la musique marocaine à la radio</a> (en arabe).</p>'''),
 en=dict(title='Chaabi and Nayda on Moroccan Radio: Where to Listen Live',
  mt='Chaabi and Nayda Radio in Morocco Live | Radio Maroc',
  desc='Where to hear chaabi and nayda live on the radio? A practical guide to stations and channels, with live listening links.',
  kw='chaabi radio Morocco, nayda radio live, Moroccan chaabi music radio',
  body='''<p>Chaabi is one of the most familiar styles to Moroccan ears, and nayda is a recent music movement that blends genres. Our directory has no single channel dedicated to chaabi, so here is a practical way to find what you want.</p>
<h2>A channel dedicated to nayda</h2>
<p>The directory includes <a href="{link:medi1-channels}">Medi 1 Nayda</a>, devoted to the rhythms of the new generation with no news bulletins, and an Andalusi channel for heritage music.</p>
<h2>Music stations in Darija</h2>
<p>Stations that play songs in Darija are the closest fit for fans of popular song. In our directory:</p>
{{STLIST:ids:17,21}}
<p>Schedules change from time to time, so check the program on the station’s website before counting on a specific show, and do not expect chaabi at every hour.</p>
<h2>A tip</h2>
<p>Try the station at different times: evenings and weekends usually suit popular-song nights better. To learn about the other styles, read <a href="{link:music}">Moroccan music on the radio</a> (in Arabic).</p>'''))

# ---------------------------------------------------------------- Marrakech & Tangier
GUIDES['marrakech-tangier'] = dict(img='art-regional.svg', pill='pill_guide', read=4,
 slug=dict(ar='radio-marrakech-tangier', fr='radios-marrakech-tanger', en='marrakech-tangier-radio-stations'),
 ar=dict(title='إذاعات مراكش وطنجة: ميدي 1 ومدينة إف إم وكاب راديو وطنجرميد',
  mt='إذاعات مراكش وطنجة مباشر | راديو المغرب',
  desc='تعرّف على إذاعات مراكش وطنجة في دليلنا، مثل مدينة إف إم وميدي 1 وكاب راديو وطنجرميد، وكيف تستمع إليها مباشرة.',
  kw='radio Marrakech en direct, إذاعات طنجة, Radio Tangermed, مدينة إف إم',
  body='''<p>لكل مدينة نبرتها وإذاعاتها. نجمع هنا المحطات المرتبطة بمراكش وطنجة في دليلنا، سواء كنت تقيم هناك أو تزورهما أو تفتقدهما من الخارج.</p>
<h2>مراكش</h2>
{{STLIST:city:مراكش}}
<p>مراكش حاضرة في الدليل عبر <a href="{link:medina-fm}">مدينة إف إم</a>، وهي محطة موسيقية بالعربية والدارجة.</p>
<h2>طنجة</h2>
{{STLIST:city:طنجة}}
<p>ترتبط طنجة بـ<a href="{link:medi-1-radio}">ميدي 1 راديو</a> وقنواتها الموسيقية، وبمحطات جهوية مثل <a href="{link:cap-radio}">كاب راديو</a> وطنجرميد. ولفهم دور الإذاعات الجهوية اقرأ <a href="{link:regional}">دليل الإذاعات الجهوية المغربية</a>.</p>
<h2>كيف تستمع؟</h2>
<p>اضغط «استمع» في أي بطاقة أعلاه فيبدأ البث مباشرة من هاتفك أو حاسوبك، أياً كان مكانك. وإن كنت تبحث عن التردد في المدينة فانظر <a href="{link:fm-frequencies}">دليل الترددات حسب المدينة</a>.</p>'''),
 fr=dict(title='Radios de Marrakech et de Tanger : Medi 1, Medina FM, Cap Radio, Tangermed',
  mt='Radios de Marrakech et Tanger en direct | Radio Maroc',
  desc='Les radios de Marrakech et de Tanger de notre guide : Medina FM, Medi 1, Cap Radio, Tangermed… et comment les écouter en direct.',
  kw='radio Marrakech en direct, radios Tanger, Radio Tangermed, Medina FM',
  body='''<p>Chaque ville a son ton et ses radios. Nous réunissons ici les stations liées à Marrakech et à Tanger dans notre guide, que vous y viviez, que vous les visitiez ou qu'elles vous manquent depuis l'étranger.</p>
<h2>Marrakech</h2>
{{STLIST:city:مراكش}}
<p>Marrakech est présente dans le guide par <a href="{link:medina-fm}">Medina FM</a>, une station musicale en arabe et en darija.</p>
<h2>Tanger</h2>
{{STLIST:city:طنجة}}
<p>Tanger est liée à <a href="{link:medi-1-radio}">Medi 1 Radio</a> et à ses chaînes musicales, ainsi qu'à des stations régionales comme <a href="{link:cap-radio}">Cap Radio</a> et Tangermed. Pour comprendre le rôle des radios régionales, lisez le <a href="{link:regional}">guide des radios régionales marocaines</a> (en arabe).</p>
<h2>Comment écouter ?</h2>
<p>Appuyez sur « Écouter » sur n'importe quelle carte ci-dessus : le flux démarre depuis votre téléphone ou votre ordinateur, où que vous soyez. Pour la fréquence dans la ville, voyez le <a href="{link:fm-frequencies}">guide des fréquences par ville</a>.</p>'''),
 en=dict(title='Marrakech and Tangier Radio Stations: Medi 1, Medina FM, Cap Radio, Tangermed',
  mt='Marrakech and Tangier Radio Stations Live | Radio Maroc',
  desc='The Marrakech and Tangier radio stations in our directory, such as Medina FM, Medi 1, Cap Radio and Tangermed, and how to listen live.',
  kw='Marrakech radio live, Tangier radio stations, Radio Tangermed, Medina FM',
  body='''<p>Every city has its own tone and its own stations. Here we gather the stations tied to Marrakech and Tangier in our directory, whether you live there, visit, or miss them from abroad.</p>
<h2>Marrakech</h2>
{{STLIST:city:مراكش}}
<p>Marrakech is represented in the directory by <a href="{link:medina-fm}">Medina FM</a>, a music station in Arabic and Darija.</p>
<h2>Tangier</h2>
{{STLIST:city:طنجة}}
<p>Tangier is tied to <a href="{link:medi-1-radio}">Medi 1 Radio</a> and its music channels, and to regional stations such as <a href="{link:cap-radio}">Cap Radio</a> and Tangermed. To understand what regional radio does, read the <a href="{link:regional}">guide to Morocco’s regional radio stations</a> (in Arabic).</p>
<h2>How to listen</h2>
<p>Press “Listen” on any card above and the stream starts from your phone or computer, wherever you are. For the frequency in the city, see the <a href="{link:fm-frequencies}">guide to frequencies by city</a>.</p>'''))
