# -*- coding: utf-8 -*-
"""French and English versions of the static pages (the Arabic originals stay in the repo).
Tokens {contact}, {privacy}, {cookies}, {terms}, {disclaimer}, {about}, {link:KEY} are resolved by build.py."""

EMAIL = 'contact@radiomaroc.live'
LEGAL = {}

LEGAL['about'] = dict(
 fr=('À propos de Radio Maroc', 'Radio Maroc est un guide indépendant des radios marocaines : notre mission, notre démarche éditoriale et notre politique de correction.', '''
<p>« Radio Maroc » est un guide indépendant qui réunit les radios marocaines au même endroit et écrit à leur sujet ce qui sert l'auditeur : par où commencer, que choisir, comment surmonter les problèmes de flux. Le projet part d'une idée simple : écouter une radio marocaine doit être facile et rapide, et s'accompagner de contenus écrits qui expliquent et orientent au lieu de se limiter à une liste de liens.</p>
<h2>Notre mission</h2>
<p>Rapprocher l'auditeur marocain, au Maroc comme à l'étranger, des voix de son pays et lui offrir une référence claire sur le paysage radiophonique marocain. Nous croyons que la radio reste un média proche et influent, et que la diversité linguistique et culturelle du Maroc, de l'arabe et de la darija à l'amazigh et au français, mérite un guide qui la célèbre.</p>
<h2>Ce que nous proposons</h2>
<ul><li><strong>Un guide des stations :</strong> une liste de radios marocaines et de chaînes spécialisées, avec recherche, catégories, favoris et écoute directe.</li><li><strong>Des articles et des guides :</strong> pour choisir la bonne station, comprendre l'histoire de la radio et écouter sans problème sur Internet.</li><li><strong>Une application mobile :</strong> une version Android dédiée, disponible sur Google Play.</li></ul>
<h2>Notre démarche éditoriale</h2>
<ul><li><strong>Indépendance :</strong> nous ne dépendons d'aucune station et ne sommes pas payés pour en référencer une ou la mettre en avant.</li><li><strong>Originalité :</strong> nous rédigeons nous-mêmes nos contenus, sans les copier ailleurs.</li><li><strong>Exactitude :</strong> nous nous appuyons sur des sources publiques et officielles et sur les informations des stations, et nous signalons les limites de nos connaissances quand une information est approximative. Nous ne publions pas de fréquence FM avant de l'avoir vérifiée.</li><li><strong>Transparence :</strong> nos listes sont éditoriales et ne prétendent pas mesurer l'audience.</li><li><strong>L'utilité d'abord :</strong> nous écrivons pour l'auditeur, pas pour remplir des pages de mots-clés.</li></ul>
<h2>Comment choisissons-nous et vérifions-nous les stations ?</h2>
<p>Nous référençons les stations qui diffusent un contenu marocain ou destiné à l'auditeur marocain, nous testons les liens de flux pour vérifier qu'ils fonctionnent et nous relisons la description de la station sur son site officiel quand c'est possible. Si un lien reste en panne longtemps, nous le corrigeons ou le retirons. Nous n'acceptons aucun contenu illégal ou offensant.</p>
<h2>Politique de correction</h2>
<p>L'erreur est humaine. Si vous trouvez une information inexacte, un lien qui ne fonctionne pas ou un logo à modifier, écrivez-nous via la page Contact. Nous examinons chaque message sérieux, corrigeons rapidement et mettons à jour la date de l'article lorsque la modification est substantielle.</p>
<h2>Publicité et financement</h2>
<p>Le site est gratuit pour les auditeurs. Nous pouvons afficher des publicités pour couvrir les coûts d'exploitation et de développement. Nous veillons à ce qu'elles restent clairement séparées du contenu éditorial et n'influencent pas nos choix. Pour les détails, lisez la <a href="{privacy}">politique de confidentialité</a>.</p>
<h2>Droits des stations et des marques</h2>
<p>Nous respectons les droits des propriétaires de stations. Les noms et logos appartiennent à leurs propriétaires et sont affichés à titre d'identification uniquement. Voir l'<a href="{disclaimer}">avertissement</a>.</p>
<h2>Contribuez</h2>
<p>Vos suggestions améliorent le guide : proposez une station, signalez un lien cassé ou dites-nous de quel sujet vous voulez que nous parlions. Écrivez-nous à {email}.</p>'''),
 en=('About Radio Maroc', 'Radio Maroc is an independent directory of Moroccan radio: our mission, editorial approach and corrections policy.', '''
<p>“Radio Maroc” is an independent guide that brings Moroccan radio together in one place and writes about it in ways that help listeners: where to start, what to pick, and how to get past streaming problems. The project began with a simple idea: listening to a Moroccan station should be easy and quick, and come with written content that explains and guides rather than just a list of links.</p>
<h2>Our mission</h2>
<p>To bring Moroccan listeners, in Morocco and abroad, closer to the voices of their country, and to offer a clear reference on Morocco’s radio landscape. We believe radio is still a close and influential medium, and that Morocco’s linguistic and cultural diversity, from Arabic and Darija to Amazigh and French, deserves a guide that celebrates it.</p>
<h2>What we offer</h2>
<ul><li><strong>A station directory:</strong> a list of Moroccan stations and specialised channels, with search, categories, favorites and live listening.</li><li><strong>Articles and guides:</strong> to help you pick the right station, understand the history of radio, and listen online without trouble.</li><li><strong>A phone app:</strong> a dedicated Android version available on Google Play.</li></ul>
<h2>Our editorial approach</h2>
<ul><li><strong>Independence:</strong> we are not affiliated with any station and are not paid to list one or to put it ahead of another.</li><li><strong>Originality:</strong> we write our content ourselves and do not copy it from other sites.</li><li><strong>Accuracy:</strong> we rely on public and official sources and on information from the stations, and we flag the limits of what we know when something is approximate. We do not publish an FM frequency until we have verified it.</li><li><strong>Transparency:</strong> our lists are editorial and do not claim to measure audiences.</li><li><strong>Usefulness first:</strong> we write to help listeners, not to stuff pages with keywords.</li></ul>
<h2>How do we choose and check stations?</h2>
<p>We list stations that broadcast Moroccan content or content aimed at Moroccan listeners, we test the stream links to make sure they work, and we review the station’s description on its official site where possible. If a link stays down for a long time we fix or remove it. We do not accept illegal or offensive content.</p>
<h2>Corrections policy</h2>
<p>Mistakes happen in any human work. If you find inaccurate information, a link that does not work, or a logo that should change, write to us through the Contact page. We review every serious message, correct errors quickly and update the article date when a change is substantial.</p>
<h2>Advertising and funding</h2>
<p>The site is free for listeners. We may show ads to cover running and development costs. We keep ads clearly separate from editorial content and do not let them affect our choices. For details, read the <a href="{privacy}">privacy policy</a>.</p>
<h2>Station and brand rights</h2>
<p>We respect station owners’ rights. Names and logos belong to their owners and are shown for identification only. See the <a href="{disclaimer}">disclaimer</a>.</p>
<h2>Contribute</h2>
<p>Your suggestions make a better guide: suggest a station, report a broken link, or tell us a topic you would like us to cover. Write to us at {email}.</p>'''))

LEGAL['contact'] = dict(
 fr=('Nous contacter', 'Contactez Radio Maroc : proposer une station, signaler un lien cassé, corriger une information ou poser une question.', '''
<p>Nous serons heureux de vous lire. Que vous souhaitiez proposer une nouvelle station, signaler un lien cassé ou corriger une information, nous lisons chaque message sérieux.</p>
<p><strong>E-mail :</strong> <a href="mailto:{email}">{email}</a></p>
<h2>Comment pouvons-nous vous aider ?</h2>
<ul><li><strong>Proposer une station :</strong> envoyez le nom de la station, sa ville et le lien de son site ou de son flux.</li><li><strong>Signaler un lien cassé :</strong> indiquez la station, votre appareil, votre navigateur et ce qui s'affiche.</li><li><strong>Corriger une information :</strong> joignez la source si possible pour que nous vérifiions et corrigions.</li><li><strong>Propriétaires de stations et de marques :</strong> pour demander la modification de données ou le retrait d'un logo ou d'une station.</li><li><strong>Confidentialité et données :</strong> pour exercer vos droits d'accès, de rectification ou de suppression.</li><li><strong>Publicité et partenariats :</strong> nous accueillons les propositions compatibles avec l'indépendance du guide.</li></ul>
<h2>Comment traitons-nous votre message ?</h2>
<p>Nous répondons aux messages sérieux en général sous 48 à 72 heures ouvrées, et il nous faut parfois plus de temps pour les demandes qui exigent une vérification. Votre message reste confidentiel et nous ne le partageons avec personne, sauf obligation légale. Pour les détails, voir la <a href="{privacy}">politique de confidentialité</a>.</p>
<h2>Avant de nous écrire</h2>
<ul><li>Si le son ne marche pas, essayez une autre station et rechargez la page : le problème vient le plus souvent du serveur de la station. Notre guide pour <a href="{link:listen-online}">écouter la radio marocaine en ligne</a> propose des solutions à la plupart des problèmes.</li><li>Nous ne sommes pas responsables des programmes des radios ni de leur grille. Pour les questions de programmation, contactez directement la station via son site.</li></ul>
<h2>Application mobile</h2>
<p>Pour vos commentaires sur l'application, vous pouvez utiliser sa page Google Play ou nous écrire directement.</p>'''),
 en=('Contact Us', 'Contact Radio Maroc: suggest a station, report a broken link, correct a detail or ask a question.', '''
<p>We would love to hear from you. Whether you want to suggest a new station, report a broken link or correct a detail, we read every serious message.</p>
<p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
<h2>How can we help?</h2>
<ul><li><strong>Suggest a station:</strong> send the station name, city and the link to its website or stream.</li><li><strong>Report a broken link:</strong> tell us the station, your device, your browser and what you saw.</li><li><strong>Correct a detail:</strong> attach the source if you can so we can check and fix it.</li><li><strong>Station and brand owners:</strong> to request changes to details, or the removal of a logo or station.</li><li><strong>Privacy and your data:</strong> to exercise your rights of access, correction or deletion.</li><li><strong>Advertising and partnerships:</strong> we welcome proposals that fit the directory’s independence.</li></ul>
<h2>How do we handle your message?</h2>
<p>We usually reply to serious messages within 48 to 72 working hours, and requests that need checking may take longer. Your message stays confidential and we share it with nobody unless the law requires it. For details see the <a href="{privacy}">privacy policy</a>.</p>
<h2>Before you write</h2>
<ul><li>If there is no sound, try another station and reload the page; the problem is most often the station’s server. Our guide to <a href="{link:listen-online}">listening to Moroccan radio online</a> has fixes for most problems.</li><li>We are not responsible for stations’ programs or schedules. For programming questions, contact the station directly through its website.</li></ul>
<h2>Phone app</h2>
<p>For feedback on the app you can use its Google Play page or write to us directly.</p>'''))

LEGAL['privacy'] = dict(
 fr=('Politique de confidentialité', 'Quelles données Radio Maroc peut traiter, pourquoi, avec qui elles sont partagées et comment les contrôler (RGPD et loi marocaine 09-08).', '''
<p>Dernière mise à jour : 18 novembre 2026</p>
<p>Votre vie privée compte. Cette politique explique quelles données le site « Radio Maroc » (https://radiomaroc.live) peut traiter, pourquoi, avec qui elles sont partagées et comment vous pouvez les contrôler. Elle est rédigée en cohérence avec le Règlement général européen sur la protection des données (RGPD) et avec la loi marocaine n° 09-08 relative à la protection des personnes physiques à l'égard du traitement des données à caractère personnel.</p>
<h2>1. Qui est responsable du traitement ?</h2>
<p>Le responsable du site est la rédaction indépendante de « Radio Maroc ». Pour toute question de confidentialité : {email}.</p>
<h2>2. Quelles données pouvons-nous traiter ?</h2>
<h3>a. Données que nous ne collectons pas</h3>
<p>Le site ne demande pas de créer un compte et nous ne collectons ni votre nom, ni votre adresse, ni votre numéro de téléphone du seul fait que vous écoutez ou naviguez.</p>
<h3>b. Données techniques générales</h3>
<p>Quand vous visitez un site, le serveur reçoit des informations techniques du fait du fonctionnement d'Internet, comme l'adresse IP, le type de navigateur, la page demandée et la date de la requête. Ces informations sont traitées par l'hébergeur à des fins de sécurité et techniques.</p>
<h3>c. Vos messages</h3>
<p>Si vous nous écrivez par e-mail, nous conservons votre adresse et le contenu de votre message le temps nécessaire pour vous répondre et traiter votre demande, puis nous les supprimons.</p>
<h3>d. Stockage local sur votre appareil</h3>
<p>Nous utilisons le stockage local du navigateur (localStorage) pour enregistrer vos stations favorites et votre choix concernant l'avis sur les cookies. Ces informations restent sur votre appareil, ne nous sont pas envoyées et peuvent être supprimées à tout moment depuis les réglages du navigateur.</p>
<h2>3. Base juridique et finalités</h2>
<ul><li>Fonctionnement et sécurité du site : intérêt légitime à assurer son bon fonctionnement et à le protéger.</li><li>Réponse à vos messages : exécution de votre demande ou intérêt légitime à communiquer avec vous.</li><li>Préférences locales : enregistrer les favoris pour faciliter votre usage.</li><li>Publicité (lorsqu'elle est activée) : votre consentement lorsque la loi l'exige, notamment pour les utilisateurs de l'Espace économique européen et du Royaume-Uni.</li></ul>
<h2>4. Cookies et publicité</h2>
<p>Le site peut afficher des publicités fournies par Google AdSense. Dans ce cas :</p>
<ul><li>Google et ses partenaires utilisent des cookies et des identifiants similaires pour diffuser les annonces, mesurer leurs performances et prévenir la fraude.</li><li>Google peut utiliser un cookie publicitaire pour afficher des annonces personnalisées selon vos visites sur ce site et sur d'autres.</li><li>Vous pouvez désactiver les annonces personnalisées dans les paramètres des annonces Google, ou consulter la façon dont Google utilise les données.</li><li>Vous pouvez aussi visiter aboutads.info pour contrôler les cookies publicitaires d'autres sociétés.</li></ul>
<p>Pour le détail des types utilisés et leur gestion, voir la <a href="{cookies}">politique de cookies</a>.</p>
<h2>5. Services externes</h2>
<p>Le site s'appuie sur des tiers qui peuvent recevoir certaines données techniques (comme l'adresse IP) lorsque des ressources leur sont demandées :</p>
<ul><li>L'hébergeur : pour servir les pages du site.</li><li>Google Fonts : pour charger les polices.</li><li>jsDelivr : pour charger la bibliothèque de lecture des flux (hls.js) si nécessaire.</li><li>Les serveurs de flux des stations : lorsque vous appuyez sur « Écouter », votre navigateur se connecte directement au serveur de la station, qui a sa propre politique de confidentialité que nous ne contrôlons pas.</li><li>Les sites des logos : les logos des stations peuvent être chargés depuis leurs sites ou des sources publiques.</li><li>Google Play : si vous choisissez de télécharger notre application, la politique de la boutique Google s'applique.</li></ul>
<h2>6. Durée de conservation</h2>
<p>Nous conservons les messages reçus aussi longtemps que nécessaire pour répondre et garder une trace raisonnable. Les données du stockage local restent sur votre appareil jusqu'à ce que vous les supprimiez.</p>
<h2>7. Transferts de données hors de votre pays</h2>
<p>Certaines données techniques peuvent être traitées chez des prestataires situés hors du Maroc ou de l'Union européenne. Nous cherchons à travailler avec des prestataires offrant des garanties appropriées de protection des données.</p>
<h2>8. Vos droits</h2>
<p>Selon le droit qui vous est applicable, vous pouvez :</p>
<ul><li>accéder aux données personnelles que nous détenons ;</li><li>les faire rectifier si elles sont inexactes, ou les faire supprimer ;</li><li>limiter le traitement ou vous y opposer ;</li><li>retirer votre consentement à tout moment, sans affecter la licéité du traitement antérieur ;</li><li>demander une copie de vos données dans un format portable lorsque cela s'applique ;</li><li>déposer une plainte auprès de l'autorité de contrôle : la Commission nationale de contrôle de la protection des données à caractère personnel (CNDP) au Maroc, ou l'autorité de protection des données de votre pays de résidence.</li></ul>
<p>Pour exercer ces droits, écrivez-nous à {email} ; nous répondrons dans un délai raisonnable ne dépassant pas 30 jours.</p>
<h2>9. Enfants</h2>
<p>Le site s'adresse au grand public et nous ne collectons pas sciemment de données personnelles d'enfants de moins de 13 ans. Si vous apprenez qu'un enfant nous a envoyé des données, écrivez-nous pour que nous les supprimions.</p>
<h2>10. Sécurité</h2>
<p>Nous utilisons une connexion chiffrée (HTTPS) et limitons les données traitées. Une sécurité totale ne peut toutefois être garantie sur Internet ; nous vous conseillons de protéger et de mettre à jour votre appareil.</p>
<h2>11. Modifications de cette politique</h2>
<p>Nous pouvons mettre à jour cette politique de temps à autre et modifierons alors la date de « dernière mise à jour » en haut de la page. Nous vous conseillons de la relire régulièrement.</p>
<h2>12. Contact</h2>
<p>Pour toute question de confidentialité : {email}, ou via la page <a href="{contact}">Contact</a>.</p>'''),
 en=('Privacy Policy', 'What data Radio Maroc may process, why, who it is shared with and how you can control it (GDPR and Moroccan Law 09-08).', '''
<p>Last updated: November 18, 2026</p>
<p>Your privacy matters. This policy explains what data the “Radio Maroc” website (https://radiomaroc.live) may process, why, who it is shared with and how you can control it. It is written to be consistent with the European General Data Protection Regulation (GDPR) and Moroccan Law No. 09-08 on the protection of individuals with regard to the processing of personal data.</p>
<h2>1. Who is responsible for data processing?</h2>
<p>The site is run by the independent “Radio Maroc” editorial team. For any privacy question write to {email}.</p>
<h2>2. What data may we process?</h2>
<h3>a. Data we do not collect</h3>
<p>The site does not ask you to create an account, and we do not collect your name, address or phone number simply because you listen or browse.</p>
<h3>b. General technical data</h3>
<p>When you visit any website, the server receives technical information as a matter of how the internet works, such as IP address, browser type, the page requested and the date of the request. This information is processed by the hosting provider for security and technical purposes.</p>
<h3>c. Your messages to us</h3>
<p>If you email us, we keep your address and the content of your message for as long as needed to reply and handle your request, then delete them when no longer needed.</p>
<h3>d. Local storage on your device</h3>
<p>We use the browser’s local storage (localStorage) to save your favorite stations and your choice about the cookie notice. This information stays on your device, is not sent to us, and can be deleted at any time from your browser settings.</p>
<h2>3. Legal basis and purposes</h2>
<ul><li>Running and securing the site: our legitimate interest in keeping it working and protected.</li><li>Replying to your messages: carrying out your request or our legitimate interest in communicating with you.</li><li>Local preferences: saving favorites to make the site easier to use.</li><li>Advertising (when enabled): your consent where the law requires it, notably for users in the European Economic Area and the United Kingdom.</li></ul>
<h2>4. Cookies and advertising</h2>
<p>The site may show ads served by Google AdSense. In that case:</p>
<ul><li>Google and its partners use cookies and similar identifiers to serve ads, measure their performance and prevent fraud.</li><li>Google may use an advertising cookie to show personalised ads based on your visits to this and other sites.</li><li>You can opt out of personalised ads in Google’s ad settings, or read how Google uses data.</li><li>You can also visit aboutads.info to control advertising cookies from other companies.</li></ul>
<p>For full details of the types we use and how to manage them, see the <a href="{cookies}">cookie policy</a>.</p>
<h2>5. External services</h2>
<p>The site relies on third parties that may receive some technical data (such as your IP address) when resources are requested from them:</p>
<ul><li>The hosting provider: to serve the site’s pages.</li><li>Google Fonts: to load fonts.</li><li>jsDelivr: to load the stream-playback library (hls.js) when needed.</li><li>Stations’ streaming servers: when you press “Listen”, your browser connects directly to the station’s server, which has its own privacy policy that we do not control.</li><li>Logo sources: station logos may be loaded from their own sites or public sources.</li><li>Google Play: if you choose to download our app, Google’s store policy applies.</li></ul>
<h2>6. Retention</h2>
<p>We keep incoming messages no longer than needed to reply and keep a reasonable record. Local-storage data stays on your device until you delete it.</p>
<h2>7. Transfers outside your country</h2>
<p>Some technical data may be processed by providers outside Morocco or outside the European Union. We aim to work with providers that offer appropriate data-protection safeguards.</p>
<h2>8. Your rights</h2>
<p>Depending on the law that applies to you, you may:</p>
<ul><li>access the personal data we hold about you;</li><li>have it corrected if wrong, or deleted;</li><li>restrict or object to processing;</li><li>withdraw your consent at any time without affecting the lawfulness of earlier processing;</li><li>ask for a copy of your data in a portable format where applicable;</li><li>lodge a complaint with the supervisory authority: Morocco’s National Commission for the Control of Personal Data Protection (CNDP), or the data protection authority in your country of residence.</li></ul>
<p>To exercise these rights write to {email}; we will reply within a reasonable time not exceeding 30 days.</p>
<h2>9. Children</h2>
<p>The site is aimed at a general audience and we do not knowingly collect personal data from children under 13. If you learn that a child has sent us data, write to us so we can delete it.</p>
<h2>10. Security</h2>
<p>We use an encrypted connection (HTTPS) and keep the data we process to a minimum. Total security cannot be guaranteed on the internet, so we recommend protecting and updating your device.</p>
<h2>11. Changes to this policy</h2>
<p>We may update this policy from time to time and will change the “last updated” date at the top of the page. We suggest you review it regularly.</p>
<h2>12. Contact</h2>
<p>For any privacy question: {email}, or through the <a href="{contact}">Contact</a> page.</p>'''))

LEGAL['terms'] = dict(
 fr=("Conditions d'utilisation", "Conditions d'utilisation du site Radio Maroc : nature du service, usage acceptable, propriété intellectuelle et responsabilité.", '''
<p>Dernière mise à jour : 18 novembre 2026</p>
<p>Bienvenue sur « Radio Maroc ». En utilisant le site (https://radiomaroc.live) ou nos applications, vous reconnaissez avoir lu ces conditions et les accepter. Si vous ne les acceptez pas, nous vous prions de ne pas utiliser le site.</p>
<h2>1. Nature du service</h2>
<p>« Radio Maroc » est un guide éditorial indépendant qui réunit les liens des radios marocaines et ce qui s'y rapporte, fournit un lecteur pour écouter leur flux en direct, ainsi que des articles et des guides utiles à l'auditeur. Le service est gratuit et fourni « en l'état ».</p>
<h2>2. Nous ne diffusons pas le contenu</h2>
<p>Le flux que vous entendez provient des serveurs des stations ou de leurs prestataires de diffusion. Nous ne possédons pas ces stations, ne contrôlons ni leurs programmes ni leur disponibilité ni leur qualité, et ne sommes pas responsables de ce qu'elles diffusent. Un lien de flux peut s'arrêter ou changer à tout moment sans préavis.</p>
<h2>3. Usage acceptable</h2>
<p>En utilisant le site, vous vous engagez à :</p>
<ul><li>l'utiliser à des fins légitimes, personnelles et conformes à la loi ;</li><li>ne pas tenter de pirater le site, de le perturber ou d'accéder sans autorisation à ses systèmes ;</li><li>ne pas utiliser de programmes automatisés pour en extraire massivement le contenu ou le republier sans autorisation ;</li><li>ne pas retransmettre le contenu radiophonique ni l'exploiter commercialement en violation des droits de ses titulaires ;</li><li>ne pas nous envoyer de contenu offensant ou trompeur.</li></ul>
<h2>4. Propriété intellectuelle</h2>
<p>Les textes originaux, les articles, la conception du site et ses éléments sont produits par l'équipe de « Radio Maroc » et protégés par le droit d'auteur. Vous pouvez en citer des extraits de façon raisonnable en indiquant la source et le lien de la page ; il est interdit de les copier intégralement ou de les republier sans autorisation écrite.</p>
<p>Les noms, logos et marques des stations appartiennent à leurs propriétaires et sont affichés dans le guide à titre d'identification et d'orientation uniquement ; ils n'impliquent aucun lien officiel, parrainage ou partenariat avec nous. Si vous êtes titulaire de droits et estimez que quelque chose doit être modifié ou retiré, écrivez-nous à {email} et nous traiterons rapidement votre demande.</p>
<h2>5. Liens externes</h2>
<p>Le site contient des liens vers des sites externes (sites de stations, boutiques d'applications, etc.). Ces sites échappent à notre contrôle et nous ne sommes pas responsables de leur contenu ni de leurs politiques. La présence d'un lien ne vaut pas approbation.</p>
<h2>6. Publicité</h2>
<p>Nous pouvons afficher des publicités de tiers comme Google AdSense pour financer le site. Nous ne contrôlons pas chaque annonce ; merci de nous signaler toute annonce inappropriée. Les politiques de ces tiers s'appliquent à vos données, comme dans la politique de confidentialité.</p>
<h2>7. Avertissement et limites de responsabilité</h2>
<p>Nous faisons de notre mieux pour fournir des informations exactes et des liens fonctionnels, mais nous ne garantissons pas l'absence d'erreurs ni un fonctionnement ininterrompu. Dans la mesure permise par la loi, nous déclinons toute responsabilité pour tout dommage direct ou indirect résultant de l'usage du site, de la confiance accordée à son contenu ou de l'interruption des flux des stations. Cela ne limite pas vos droits légaux impératifs. Pour en savoir plus, voir l'<a href="{disclaimer}">avertissement</a>.</p>
<h2>8. Modification et arrêt</h2>
<p>Nous pouvons modifier le site ou une partie du site, l'arrêter ou mettre à jour ces conditions à tout moment. Continuer à l'utiliser après une modification vaut acceptation des nouvelles conditions.</p>
<h2>9. Droit applicable</h2>
<p>Ces conditions sont régies par le droit marocain, sous réserve des dispositions impératives protégeant les consommateurs dans votre pays de résidence. En cas de litige, nous cherchons d'abord une solution amiable.</p>
<h2>10. Contact</h2>
<p>Pour toute question sur ces conditions : {email}.</p>'''),
 en=('Terms of Use', 'Terms of use of the Radio Maroc website: nature of the service, acceptable use, intellectual property and liability.', '''
<p>Last updated: November 18, 2026</p>
<p>Welcome to “Radio Maroc”. By using the site (https://radiomaroc.live) or our apps, you acknowledge that you have read and agree to these terms. If you do not agree, please do not use the site.</p>
<h2>1. Nature of the service</h2>
<p>“Radio Maroc” is an independent editorial directory that gathers links to Moroccan radio stations and related material, provides a player so you can listen to their live streams, and publishes articles and guides useful to listeners. The service is free and provided “as is”.</p>
<h2>2. We do not broadcast the content</h2>
<p>The stream you hear comes from the stations’ servers or their streaming providers. We do not own these stations and do not control their programs, availability or quality, and we are not responsible for what they broadcast. Any stream link may stop or change at any time without notice.</p>
<h2>3. Acceptable use</h2>
<p>When using the site you agree to:</p>
<ul><li>use it for lawful, personal purposes that do not break the law;</li><li>not try to hack or disrupt the site or gain unauthorised access to its systems;</li><li>not use automated programs to scrape its content in bulk or republish it without permission;</li><li>not rebroadcast radio content or exploit it commercially in breach of its owners’ rights;</li><li>not send us offensive or misleading content.</li></ul>
<h2>4. Intellectual property</h2>
<p>The original texts, articles, site design and elements are produced by the “Radio Maroc” team and protected by copyright. You may quote from them reasonably with credit and a link to the page; you may not copy them in full or republish them without written permission.</p>
<p>Station names, logos and trademarks belong to their owners and are shown in the directory for identification and guidance only; they do not imply any official relationship, sponsorship or partnership with us. If you are a rights holder and think something should be changed or removed, write to us at {email} and we will handle your request quickly.</p>
<h2>5. External links</h2>
<p>The site contains links to external sites (station sites, app stores and others). These sites are outside our control and we are not responsible for their content or policies. A link does not mean endorsement.</p>
<h2>6. Advertising</h2>
<p>We may show third-party ads such as Google AdSense to fund the site. We do not control every ad that appears; please tell us if you see an inappropriate one. These third parties’ policies apply to your data, as set out in the privacy policy.</p>
<h2>7. Disclaimer and limits of liability</h2>
<p>We do our best to provide accurate information and working links, but we do not guarantee that the site is free of errors or runs without interruption. To the extent the law allows, we accept no liability for any direct or indirect damage resulting from use of the site, reliance on its content or interruption of stations’ streams. This does not limit your mandatory legal rights. For more, see the <a href="{disclaimer}">disclaimer</a>.</p>
<h2>8. Changes and discontinuation</h2>
<p>We may change the site or any part of it, discontinue it, or update these terms at any time. Continuing to use the site after a change means you accept the new terms.</p>
<h2>9. Governing law</h2>
<p>These terms are governed by Moroccan law, subject to any mandatory provisions protecting consumers in your country of residence. In a dispute we first seek to resolve it through friendly contact.</p>
<h2>10. Contact</h2>
<p>For any question about these terms: {email}.</p>'''))

LEGAL['disclaimer'] = dict(
 fr=('Avertissement', 'Avertissement de Radio Maroc : site indépendant et non officiel, droits des stations, disponibilité des flux et exactitude des informations.', '''
<p>Dernière mise à jour : 18 novembre 2026</p>
<p>Chez « Radio Maroc », nous voulons être clairs avec nos visiteurs. Cette page précise les limites de ce que nous proposons et de ce que nous ne proposons pas, afin que vous connaissiez exactement la nature du service.</p>
<h2>Un site indépendant et non officiel</h2>
<p>« Radio Maroc » est un projet éditorial indépendant. Nous ne dépendons d'aucune radio, autorité officielle ou société, ne représentons aucune d'elles et ne parlons pas en leur nom. La présence d'une station dans notre guide ne signifie pas qu'elle nous parraine ni que nous l'avons homologuée.</p>
<h2>Propriété des stations et des marques</h2>
<p>Tous les noms, logos, marques et programmes des stations appartiennent à leurs propriétaires légitimes. Ils sont affichés dans le guide à titre informatif et d'orientation uniquement, et tout contenu diffusé reste sous la responsabilité de la station qui le diffuse. Si vous êtes propriétaire d'une station ou d'une marque et souhaitez modifier ses données ou les retirer, écrivez-nous à {email}.</p>
<h2>Disponibilité et qualité du flux</h2>
<p>Nous fournissons des liens vers le flux direct émis par les stations. Le flux peut s'arrêter, se couper ou changer de lien selon les serveurs de la station, la qualité de votre connexion ou des restrictions géographiques imposées par la station. Nous ne garantissons donc la disponibilité d'aucun flux à aucun moment ; en cas de coupure, nous vous conseillons de consulter le site officiel de la station.</p>
<h2>Exactitude des informations</h2>
<p>Nous rédigeons nos articles et guides avec soin et nous appuyons sur des sources publiques et sur les informations des stations elles-mêmes. Malgré cela, programmes, dates et descriptions peuvent changer, et une erreur involontaire peut se glisser. Les informations fournies sont générales et indicatives et ne remplacent pas les sources officielles. Les fréquences FM varient selon la ville : vérifiez-les auprès de la station. Si vous constatez une erreur, dites-le-nous et nous la corrigerons rapidement.</p>
<h2>Pas de conseil professionnel</h2>
<p>Les indications que nous publions sur l'écoute, la technique et la connexion sont des informations générales et non un conseil professionnel, juridique ou technique spécialisé. En voiture, nous rappelons la nécessité de respecter les règles de sécurité routière et de ne pas utiliser le téléphone en conduisant.</p>
<h2>Liens externes</h2>
<p>Nous pouvons renvoyer à des sites et applications externes. Nous ne contrôlons ni leur contenu, ni leurs politiques, ni leur sécurité et déclinons toute responsabilité pour tout dommage résultant de leur usage. Vérifiez toujours la source d'une application avant de l'installer.</p>
<h2>Publicité</h2>
<p>Le site peut afficher des publicités de tiers. L'apparition d'une annonce ne signifie pas que nous approuvons le produit ou le service, et nous ne sommes pas responsables de l'exactitude de ce que les annonces présentent.</p>
<h2>Limites de responsabilité</h2>
<p>Dans toute la mesure permise par la loi, « Radio Maroc » n'est pas responsable de toute perte ou de tout dommage résultant de l'usage du site ou de la confiance accordée à son contenu. Cela n'affecte aucun droit auquel il est impossible de renoncer légalement. Pour les détails, voir les <a href="{terms}">conditions d'utilisation</a>.</p>
<h2>Contactez-nous</h2>
<p>Pour toute remarque, demande de correction ou de retrait : {email}.</p>'''),
 en=('Disclaimer', 'Radio Maroc disclaimer: an independent, unofficial site, station rights, stream availability and accuracy of information.', '''
<p>Last updated: November 18, 2026</p>
<p>At “Radio Maroc” we want to be clear with our visitors. This page sets out the limits of what we do and do not provide, so you know exactly what kind of service this is.</p>
<h2>An independent, unofficial site</h2>
<p>“Radio Maroc” is an independent editorial project. We are not affiliated with any radio station, official body or company, and we do not represent or speak for any of them. A station’s presence in our directory does not mean it sponsors us or that we have endorsed it.</p>
<h2>Ownership of stations and brands</h2>
<p>All station names, logos, trademarks and programs belong to their rightful owners. They are shown in the directory for information and guidance only, and any content broadcast remains the responsibility of the station that broadcasts it. If you own a station or brand and want its details changed or removed, write to us at {email}.</p>
<h2>Stream availability and quality</h2>
<p>We provide links to the live streams the stations put out. A stream may stop, cut out or change its link depending on the station’s servers, the quality of your connection or regional restrictions the station applies. We therefore do not guarantee that any stream is available at any time; if one drops, we suggest checking the station’s official website.</p>
<h2>Accuracy of information</h2>
<p>We write our articles and guides with care, relying on public sources and on information from the stations themselves. Even so, programs, dates and descriptions may change, and an unintentional error may slip in. The information provided is general and indicative and does not replace official sources. FM frequencies vary by city: check them with the station. If you notice a mistake, tell us and we will correct it quickly.</p>
<h2>No professional advice</h2>
<p>What we publish about listening, technology and connection is general information, not professional, legal or specialised technical advice. In the car we remind you to follow road safety rules and not to use your phone while driving.</p>
<h2>External links</h2>
<p>We may point to external sites and apps. We do not control their content, policies or security, and we accept no liability for any damage resulting from using them. Always check the source of an app before installing it.</p>
<h2>Advertising</h2>
<p>The site may show third-party ads. An ad appearing does not mean we endorse the product or service, and we are not responsible for the accuracy of what ads present.</p>
<h2>Limits of liability</h2>
<p>To the fullest extent the law allows, “Radio Maroc” is not liable for any loss or damage arising from use of the site or reliance on its content. This does not affect any right that cannot legally be waived. For details, see the <a href="{terms}">terms of use</a>.</p>
<h2>Contact us</h2>
<p>For any comment, correction or removal request: {email}.</p>'''))

LEGAL['cookies'] = dict(
 fr=('Politique de cookies', "Ce que sont les cookies, comment Radio Maroc les utilise et comment les contrôler.", '''
<p>Dernière mise à jour : 18 novembre 2026</p>
<p>Cette page explique ce que sont les cookies et les technologies similaires, comment « Radio Maroc » les utilise et comment vous pouvez les contrôler. Elle complète la <a href="{privacy}">politique de confidentialité</a>.</p>
<h2>Que sont les cookies ?</h2>
<p>Ce sont de petits fichiers texte que le navigateur enregistre sur votre appareil lorsque vous visitez un site et qui aident celui-ci à mémoriser vos préférences, à mesurer l'usage ou à afficher des publicités. Il existe aussi des technologies similaires comme le stockage local (localStorage) et les identifiants d'appareil.</p>
<h2>Qu'utilisons-nous ?</h2>
<h3>1. Essentiels et préférences (depuis le site lui-même)</h3>
<ul><li>rm_favs (stockage local) : enregistre la liste de vos stations favorites sur votre appareil uniquement.</li><li>rm_cookie (stockage local) : mémorise votre choix concernant l'avis sur les cookies pour ne pas vous le répéter.</li><li>rm_promo (stockage local) : se souvient que vous avez fermé l'avis sur l'application mobile.</li></ul>
<p>Ces éléments ne sont pas envoyés à nos serveurs et ne servent pas à vous suivre.</p>
<h3>2. Fichiers de tiers</h3>
<ul><li>Publicités Google AdSense (lorsqu'elles sont activées) : Google et ses partenaires utilisent des cookies et des identifiants pour diffuser et mesurer les annonces et prévenir la fraude, et peuvent personnaliser les annonces selon vos centres d'intérêt.</li><li>Polices et bibliothèques : votre navigateur peut se connecter à des services comme Google Fonts et jsDelivr pour charger des ressources, et ces services peuvent recevoir des données techniques comme l'adresse IP.</li><li>Serveurs de flux : lorsque vous lancez une station, votre appareil se connecte au serveur de la station, qui peut appliquer ses propres politiques.</li></ul>
<h2>Consentement</h2>
<p>Lors de votre première visite, un avis vous informe de l'utilisation de ces technologies. Pour les visiteurs de l'Espace économique européen et du Royaume-Uni, nous nous appuyons, lorsque la publicité est activée, sur un outil de consentement agréé qui vous permet d'accepter, de refuser ou de personnaliser les cookies publicitaires, et vous pouvez modifier votre choix à tout moment.</p>
<h2>Comment contrôler les cookies ?</h2>
<ul><li>Depuis le navigateur : tous les principaux navigateurs permettent de bloquer ou de supprimer les cookies (dans les réglages de confidentialité et de sécurité).</li><li>Supprimer le stockage local : effacez les données du site dans les réglages du navigateur pour retirer vos favoris et préférences.</li><li>Annonces personnalisées : désactivez-les dans les paramètres des annonces Google ou sur aboutads.info.</li></ul>
<p>Notez que bloquer certains fichiers peut désactiver des fonctions comme l'enregistrement des favoris.</p>
<h2>Modifications de la politique</h2>
<p>Nous pouvons mettre à jour cette page lorsque les outils que nous utilisons changent, et nous modifierons alors la date de dernière mise à jour en haut de la page.</p>
<h2>Contact</h2>
<p>Pour toute question : {email}.</p>'''),
 en=('Cookie Policy', 'What cookies are, how Radio Maroc uses them and how you can control them.', '''
<p>Last updated: November 18, 2026</p>
<p>This page explains what cookies and similar technologies are, how “Radio Maroc” uses them and how you can control them. It supplements the <a href="{privacy}">privacy policy</a>.</p>
<h2>What are cookies?</h2>
<p>They are small text files that the browser stores on your device when you visit a site, helping the site remember your preferences, measure usage or show ads. There are also similar technologies such as local storage (localStorage) and device identifiers.</p>
<h2>What do we use?</h2>
<h3>1. Essential and preferences (from the site itself)</h3>
<ul><li>rm_favs (local storage): saves your list of favorite stations on your device only.</li><li>rm_cookie (local storage): remembers your choice about the cookie notice so we do not repeat it.</li><li>rm_promo (local storage): remembers that you closed the phone-app notice.</li></ul>
<p>These items are not sent to our servers and are not used to track you.</p>
<h3>2. Third-party files</h3>
<ul><li>Google AdSense ads (when enabled): Google and its partners use cookies and identifiers to serve and measure ads and to prevent fraud, and may personalise ads to your interests.</li><li>Fonts and libraries: your browser may connect to services such as Google Fonts and jsDelivr to load resources, and these services may receive technical data such as your IP address.</li><li>Streaming servers: when you play a station, your device connects to the station’s server, which may apply its own policies.</li></ul>
<h2>Consent</h2>
<p>On your first visit a notice tells you about the use of these technologies. For visitors in the European Economic Area and the United Kingdom, when advertising is enabled we rely on an approved consent tool that lets you accept, reject or customise advertising cookies, and you can change your choice at any time.</p>
<h2>How do you control cookies?</h2>
<ul><li>From your browser: all major browsers let you block or delete cookies (in privacy and security settings).</li><li>Delete local storage: clear the site’s data in your browser settings to remove your favorites and preferences.</li><li>Personalised ads: switch them off in Google’s ad settings or at aboutads.info.</li></ul>
<p>Note that blocking some files may disable features such as saving favorites.</p>
<h2>Changes to the policy</h2>
<p>We may update this page when the tools we use change, and will change the last-updated date at the top of the page.</p>
<h2>Contact</h2>
<p>For any question: {email}.</p>'''))
