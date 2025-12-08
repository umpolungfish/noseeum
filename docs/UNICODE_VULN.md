

Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents
(Top)
History

Homographs in ASCII

Homographs in internationalized domain names

    Cyrillic
    Greek
    Armenian
    Hebrew
    Thai
    Chinese
    Other scripts
    Accented characters
    Non-displayable characters
    Known homograph attacks

Defending against the attack

        Client-side mitigation
        Server-side/registry operator mitigation
        Research based mitigations
    See also
    Notes
    References

IDN homograph attack

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
December 7: We owe you an explanation.
We're sorry we've made several attempts to reach you lately, but it's Sunday, December 7, and we still need some help. We're happy you consult Wikipedia often. If everyone reading this gave $2.75 today, we'd hit our goal in a few hours. Most readers don't donate; only 2% do. So if Wikipedia has given you $2.75 worth of knowledge, please give. Any contribution helps, whether it's $2.75 or $25.

An internationalized domain name (IDN) homograph attack (also homoglyph attack) is a method used by malicious parties to deceive computer users about what remote system they are communicating with, by exploiting the fact that many different characters look alike (i.e., they rely on homoglyphs to deceive visitors). For example, the Cyrillic, Greek and Latin alphabets each have a letter ⟨o⟩ that has the same shape but represents different sounds or phonemes in their respective writing systems.[a]

This kind of spoofing attack is also known as script spoofing. Unicode incorporates numerous scripts (writing systems), and, for a number of reasons, similar-looking characters such as Greek Ο, Latin O, and Cyrillic О were not assigned the same code. Their incorrect or malicious usage is a possibility for security attacks. Thus, for example, a regular user of exаmple.com may be lured to click on it unquestioningly as an apparently familiar link, unaware that the third letter is not the Latin character "a" but rather the Cyrillic character "а" and is thus an entirely different domain from the intended one.

The registration of homographic domain names is akin to typosquatting, in that both forms of attacks use a similar-looking name to a more established domain to fool a user.[b] The major difference is that in typosquatting the perpetrator attracts victims by relying on natural typographical errors commonly made when manually entering a URL, while in homograph spoofing the perpetrator deceives the victims by presenting visually indistinguishable hyperlinks. Indeed, it would be a rare accident for a web user to type, for example, a Cyrillic letter within an otherwise English word, turning "bank" into "bаnk". There are cases in which a registration can be both typosquatting and homograph spoofing; the pairs of l/I, i/j, and 0/O are all both close together on keyboards and, depending on the typeface, may be difficult or impossible to distinguish visually.
History
Homoglyphs are common in the three major European alphabets: Latin, Greek and Cyrillic. Unicode does not attempt to unify these glyphs and instead separates most scripts.

An early nuisance of this kind, pre-dating the Internet and even text terminals, was the confusion between "l" (lowercase letter "L") / "1" (the number "one") and "O" (capital letter for vowel "o") / "0" (the number "zero"). Some typewriters in the pre-computer era even combined the L and the one; users had to type a lowercase L when the number one was needed. The zero/o confusion gave rise to the tradition of crossing zeros, so that a computer operator would type them correctly.[1] Unicode may contribute to this greatly with its combining characters, accents, several types of hyphen, etc., often due to inadequate rendering support, especially with smaller font sizes and the wide variety of fonts.[2]

Even earlier, handwriting provided rich opportunities for confusion. A notable example is the etymology of the word "zenith". The translation from the Arabic "samt" included the scribe's confusing of "m" into "ni". This was common in medieval blackletter, which did not connect the vertical columns on the letters i, m, n, or u, making them difficult to distinguish when several were in a row. The latter, as well as "rn"/"m"/"rri" ("RN"/"M"/"RRI") confusion, is still possible for a human eye even with modern advanced computer technology.

Intentional look-alike character substitution with different alphabets has also been known in various contexts. For example, Faux Cyrillic has been used as an amusement or attention-grabber and "Volapuk encoding", in which Cyrillic script is represented by similar Latin characters, was used in early days of the Internet as a way to overcome the lack of support for the Cyrillic alphabet. Another example is that vehicle registration plates can have both Cyrillic (for domestic usage in Cyrillic script countries) and Latin (for international driving) with the same letters. Registration plates that are issued in Greece are limited to using letters of the Greek alphabet that have homoglyphs in the Latin alphabet, as European Union regulations require the use of Latin letters.
Homographs in ASCII

ASCII has several characters or pairs of characters that look alike and are known as homographs (or homoglyphs). Spoofing attacks based on these similarities are known as homograph spoofing attacks. For example, 0 (the number) and O (the letter), "l" lowercase "L", and "I" uppercase "i".

In a typical example of a hypothetical attack, someone could register a domain name that appears almost identical to an existing domain but goes somewhere else. For example, the domain "rnicrosoft.com" begins with "r" and "n", not "m". Other examples are G00GLE.COM which looks much like GOOGLE.COM in some fonts. Using a mix of uppercase and lowercase characters, googIe.com (capital i, not small L) looks much like google.com in some fonts. PayPal was a target of a phishing scam exploiting this, using the domain PayPaI.com. In certain narrow-spaced fonts such as Tahoma (the default in the address bar in Windows XP), placing a c in front of a j, l or i will produce homoglyphs such as cl cj ci (d g a).
Homographs in internationalized domain names

In multilingual computer systems, different logical characters may have identical appearances. For example, Unicode character U+0430, Cyrillic small letter a ("а"), can look identical to Unicode character U+0061, Latin small letter a, ("a") which is the lowercase "a" used in English. Hence wikipediа.org (xn--wikipedi-86g.org; the Cyrillic version) instead of wikipedia.org (the Latin version).

The problem arises from the different treatment of the characters in the user's mind and the computer's programming. From the viewpoint of the user, a Cyrillic "а" within a Latin string is a Latin "a"; there is no difference in the glyphs for these characters in most fonts. However, the computer treats them differently when processing the character string as an identifier. Thus, the user's assumption of a one-to-one correspondence between the visual appearance of a name and the named entity breaks down.

Internationalized domain names provide a backward-compatible way for domain names to use the full Unicode character set, and this standard is already widely supported. However this system expanded the character repertoire from a few dozen characters in a single alphabet to many thousands of characters in many scripts; this greatly increased the scope for homograph attacks.

This opens a rich vein of opportunities for phishing and other varieties of fraud. An attacker could register a domain name that looks just like that of a legitimate website, but in which some of the letters have been replaced by homographs in another alphabet. The attacker could then send e-mail messages purporting to come from the original site, but directing people to the bogus site. The spoof site could then record information such as passwords or account details, while passing traffic through to the real site. The victims may never notice the difference, until suspicious or criminal activity occurs with their accounts.

In December 2001 Evgeniy Gabrilovich and Alex Gontmakher, both from Technion, Israel, published a paper titled "The Homograph Attack",[1] which described an attack that used Unicode URLs to spoof a website URL. To prove the feasibility of this kind of attack, the researchers successfully registered a variant of the domain name microsoft.com which incorporated Cyrillic characters.

Problems of this kind were anticipated before IDN was introduced, and guidelines were issued to registries to try to avoid or reduce the problem. For example, it was advised that registries only accept characters from the Latin alphabet and that of their own country, not all of Unicode characters, but this advice was neglected by major TLDs.[citation needed]

On February 6, 2005, Cory Doctorow reported that this exploit was disclosed by 3ric Johanson at the hacker conference Shmoocon.[3][4] Web browsers supporting IDNA appeared to direct the URL http://www.pаypal.com/, in which the first a character is replaced by a Cyrillic а, to the site of the well known payment site PayPal, but actually led to a spoofed web site with different content. Popular browsers continued to have problems properly displaying international domain names through April 2017.[5]

The following alphabets have characters that can be used for spoofing attacks (please note, these are only the most obvious and common, given artistic license and how much risk the spoofer will take of getting caught; the possibilities are far more numerous than can be listed here):
Cyrillic

Cyrillic is, by far, the most commonly used alphabet for homoglyphs, largely because it contains 11 lowercase glyphs that are identical or nearly identical to Latin counterparts.

The Cyrillic letters а, с, е, о, р, х and у have optical counterparts in the basic Latin alphabet and look close or identical to a, c, e, o, p, x and y. Cyrillic З, Ч and б resemble the numerals 3, 4 and 6. Italic type generates more homoglyphs: дтпи or дтпи (дтпи in standard type), resembling dmnu (in some fonts д can be used, since its italic form resembles a lowercase g; however, in most mainstream fonts, д instead resembles a partial differential sign, ∂).

If capital letters are counted, АВСЕНІЈКМОРЅТХ can substitute ABCEHIJKMOPSTX, in addition to the capitals for the lowercase Cyrillic homoglyphs.

Cyrillic non-Russian problematic letters are і and i, ј and j, ԛ and q, ѕ and s, ԝ and w, Ү and Y, while Ғ and F, Ԍ and G bear some resemblance to each other. Cyrillic ӓёїӧ can also be used if an IDN itself is being spoofed, to fake äëïö.

While Komi De (ԁ), shha (һ), palochka (Ӏ) and izhitsa (ѵ) bear strong resemblance to Latin d, h, l and v, these letters are either rare or archaic and are not widely supported in most standard fonts (they are not included in the WGL-4). Attempting to use them could cause a ransom note effect.
Greek

From the Greek alphabet, only omicron (ο) and sometimes nu (ν) appear identical to a Latin alphabet letter in the lowercase used for URLs. Fonts that are in italic type will feature Greek alpha (α) looking like a Latin a.

This list increases if close matches are also allowed (such as Greek εικηρτυωχγ for eiknptuwxy). Using capital letters, the list expands greatly. Greek ΑΒΕΗΙΚΜΝΟΡΤΧΥΖ looks identical to Latin ABEHIKMNOPTXYZ. Greek ΑΓΒΕΗΚΜΟΠΡΤΦΧ looks similar to Cyrillic АГВЕНКМОПРТФХ (as do Cyrillic Лл (Лл) and Greek Λ in certain geometric sans-serif fonts), Greek letters κ and ο look similar to Cyrillic к and о. Besides this Greek τ, φ can be similar to Cyrillic т, ф in some fonts, Greek δ looks like Cyrillic б, and the Cyrillic а also italicizes the same as its Latin counterpart, making it possible to substitute it for alpha or vice versa. The lunate form of sigma, Ϲϲ, resembles both Latin Cc and Cyrillic Сс. Especially in contemporary typefaces, Cyrillic л is rendered with a glyph indistinguishable from Greek π.

If an IDN itself is being spoofed, Greek beta β can be a substitute for German eszett ß in some fonts (and in fact, code page 437 treats them as equivalent), as can Greek end-of-word-variant sigma ς for ç; accented Greek substitutes όίά can usually be used for óíá in many fonts, with the last of these (alpha) again only resembling a in italic type.
Armenian

The Armenian alphabet can also contribute critical characters: several Armenian characters like օ, ո, ս, as well as capital Տ and Լ are often completely identical to Latin characters in modern fonts, and symbols which similar enough to pass off, such as ցհոօզս which look like ghnoqu, յ which resembles j (albeit dotless), and ք, which can either resemble p or f depending on the font; ա can resemble Cyrillic ш. However, the use of Armenian is, luckily, a bit less reliable: Not all standard fonts feature Armenian glyphs (whereas the Greek and Cyrillic scripts are); Windows prior to Windows 7 rendered Armenian in a distinct font, Sylfaen, of which the mixing of Armenian with Latin would appear obviously different if using a font other than Sylfaen or a Unicode typeface. (This is known as a ransom note effect.) The current version of Tahoma, used in Windows 7, supports Armenian (previous versions did not). Furthermore, this font differentiates Latin g from Armenian ց.

Two letters in Armenian (Ձշ) also can resemble the number 2, Յ resembles 3, while another (վ) sometimes resembles the number 4.
Hebrew

Hebrew spoofing is generally rare. Only three letters from that alphabet can reliably be used: samekh (ס), which sometimes resembles o, vav with diacritic (וֹ), which resembles an i, and heth (ח), which resembles the letter n. Less accurate approximants for some other alphanumerics can also be found, but these are usually only accurate enough to use for the purposes of foreign branding and not for substitution. Furthermore, the Hebrew alphabet is written from right to left and trying to mix it with left-to-right glyphs may cause problems.
Thai
Top: Thai glyphs rendered in a modern font (IBM Plex) in which they resemble Latin glyphs.
Bottom: The same glyphs rendered with traditional loops.

Though the Thai script has historically had a distinct look with numerous loops and small flourishes, modern Thai typography, beginning with Manoptica in 1973 and continuing through IBM Plex in the modern era, has increasingly adopted a simplified style in which Thai characters are represented with glyphs strongly resembling Latin letters. ค (A), ท (n), น (u), บ (U), ป (J), พ (W), ร (S), and ล (a) are among the Thai glyphs that can closely resemble Latin.
Chinese
See also: Martian language

The Chinese language can be problematic for homographs as many characters exist as both traditional (regular script) and simplified Chinese characters. In the .org domain, registering one variant renders the other unavailable to anyone; in .biz a single Chinese-language IDN registration delivers both variants as active domains (which must have the same domain name server and the same registrant). .hk (.香港) also adopts this policy.
Other scripts

Other Unicode scripts in which homographs can be found include Number Forms (Roman numerals), CJK Compatibility and Enclosed CJK Letters and Months (certain abbreviations), Latin (certain digraphs), Currency Symbols, Mathematical Alphanumeric Symbols, and Alphabetic Presentation Forms (typographic ligatures).
Accented characters

Two names which differ only in an accent on one character may look very similar, particularly when the substitution involves the dotted letter i; the tittle (dot) on the i can be replaced with a diacritic (such as a grave accent or acute accent; both ì and í are included in most standard character sets and fonts) that can only be detected with close inspection. In most top-level domain registries, wíkipedia.tld (xn--wkipedia-c2a.tld) and wikipedia.tld are two different names which may be held by different registrants.[6] One exception is .ca, where reserving the plain-ASCII version of the domain prevents another registrant from claiming an accented version of the same name.[7]
Non-displayable characters

Unicode includes many characters which are not displayed by default, such as the zero-width space. In general, ICANN prohibits any domain with these characters from being registered, regardless of TLD.
Known homograph attacks

In 2011, an unknown source (registering under the name "Completely Anonymous") registered a domain name homographic to television station KBOI-TV's to create a fake news website. The sole purpose of the site was to spread an April Fool's Day joke regarding the Governor of Idaho issuing a supposed ban on the sale of music by Justin Bieber.[8][9]

In September 2017, security researcher Ankit Anubhav discovered an IDN homograph attack where the attackers registered adoḅe.com to deliver the Betabot trojan.[10]
Defending against the attack
Client-side mitigation

The simplest defense is for web browsers not to support IDNA or other similar mechanisms, or for users to turn off whatever support their browsers have. That could mean blocking access to IDNA sites, but generally browsers permit access and just display IDNs in Punycode. Either way, this amounts to abandoning non-ASCII domain names.

    Mozilla Firefox versions 22 and later display IDNs if either the TLD prevents homograph attacks by restricting which characters can be used in domain names or labels do not mix scripts for different languages. Otherwise, IDNs are displayed in Punycode.[11][12]
    Google Chrome versions 51 and later use an algorithm similar to the one used by Firefox. Previous versions display an IDN only if all of its characters belong to one (and only one) of the user's preferred languages. Chromium and Chromium-based browsers such as Microsoft Edge (since 2020) and Opera also use the same algorithm.[13][14]
    Safari's approach is to render problematic character sets as Punycode. This can be changed by altering the settings in Mac OS X's system files.[15]
    Internet Explorer versions 7 and later allow IDNs except for labels that mix scripts for different languages. Labels that mix scripts are displayed in Punycode. There are exceptions to locales where ASCII characters are commonly mixed with localized scripts.[16] Internet Explorer 7 was capable of using IDNs, but it imposes restrictions on displaying non-ASCII domain names based on a user-defined list of allowed languages and provides an anti-phishing filter that checks suspicious websites against a remote database of known phishing sites.[citation needed]
    Microsoft Edge Legacy converts all Unicode into Punycode.[citation needed]

As an additional defense, Internet Explorer 7, Firefox 2.0 and above, and Opera 9.10 include phishing filters that attempt to alert users when they visit malicious websites.[17][18][19] As of April 2017, several browsers (including Chrome, Firefox, and Opera) were displaying IDNs consisting purely of Cyrillic characters normally (not as punycode), allowing spoofing attacks. Chrome tightened IDN restrictions in version 59 to prevent this attack.[20][21]

These methods of defense only extend to within a browser. Homographic URLs that house malicious software can still be distributed, without being displayed as Punycode, through e-mail, social networking or other websites without being detected until the user actually clicks the link. While the fake link will show in Punycode when it is clicked, by this point the page has already begun loading into the browser.[citation needed]
Server-side/registry operator mitigation

The IDN homographs database is a Python library that allows developers to defend against this using machine learning-based character recognition.[22]

ICANN has implemented a policy prohibiting any potential internationalized TLD from choosing letters that could resemble an existing Latin TLD and thus be used for homograph attacks. Proposed IDN TLDs .бг (Bulgaria), .укр (Ukraine) and .ελ (Greece) have been rejected or stalled because of their perceived resemblance to Latin letters. All three (and Serbian .срб and Mongolian .мон) have later been accepted.[23] Three-letter TLD are considered safer than two-letter TLD, since they are harder to match to normal Latin ISO-3166 country domains; although the potential to match new generic domains remains, such generic domains are far more expensive than registering a second- or third-level domain address, making it cost-prohibitive to try to register a homoglyphic TLD for the sole purpose of making fraudulent domains (which itself would draw ICANN scrutiny).

The Russian registry operator Coordination Center for TLD RU only accepts Cyrillic names for the top-level domain .рф, forbidding a mix with Latin or Greek characters. However, the problem in .com and other gTLDs remains open.[24]
Research based mitigations

In their 2019 study, Suzuki et al. introduced ShamFinder,[25] a program for recognizing IDNs, shedding light on their prevalence in real-world scenarios. Similarly, Chiba et al. (2019) designed DomainScouter,[26] a system adept at detecting diverse homograph IDNs in domains through analyzing an estimated 4.4 million registered IDNs across 570 Top-Level Domains (TLDs) it was able to successfully identify 8,284 IDN homographs, including many previously unidentified cases targeting brands in languages other than English.[27]
See also

    Security issues in Unicode
    Internationalized domain name
    Homoglyph
    Faux Cyrillic
    Metal umlaut
    Duplicate characters in Unicode
    Unicode equivalence
    Typosquatting
    Leet
    Gyaru-moji
    Yaminjeongeum
    Martian language

Notes

U+043E о CYRILLIC SMALL LETTER O, U+03BF ο GREEK SMALL LETTER OMICRON, U+006F o LATIN SMALL LETTER O

    For example, Microsfot.com

References

Evgeniy Gabrilovich and Alex Gontmakher, "Archived copy" (PDF). Archived from the original (PDF) on 2020-01-02. Retrieved 2005-12-10., Communications of the ACM, 45(2):128, February 2002
"Unicode Security Considerations", Technical Report #36, 2010-04-28
Cory, Doctorow (2005-02-06). "Shmoo Group exploit: 0wn any domain, no defense exists". Boing Boing. Archived from the original on 2015-09-27. Retrieved 2024-10-28.
IDN hacking disclosure by shmoo.com Archived 2005-03-20 at the Wayback Machine
"Chrome and Firefox Phishing Attack Uses Domains Identical to Known Safe Sites". Wordfence. 2017-04-14. Retrieved 2017-04-18.
There are various Punycode converters online, such as https://www.hkdnr.hk/idn_conv.jsp
".CA takes on a French accent | Canadian Internet Registration Authority (CIRA)". Archived from the original on 2015-09-07. Retrieved 2015-09-22.
Fake website URL not from KBOI-TV Archived 2011-04-05 at the Wayback Machine. KBOI-TV. Retrieved 2011-04-01.
Boise TV news website targeted with Justin Bieber prank Archived 2012-03-15 at the Wayback Machine. KTVB. Retrieved 2011-04-01.
Mimoso, Michael (2017-09-06). "IDN Homograph Attack Spreading Betabot Backdoor". Threatpost. Archived from the original on 2023-10-17. Retrieved 2020-09-20.
"IDN Display Algorithm". Mozilla. Retrieved 2016-01-31.
"Bug 722299". Bugzilla.mozilla.org. Retrieved 2016-01-31.
"Internationalized Domain Names (IDN) in Google Chrome". chromium.googlesource.com. Retrieved 2020-08-26.
"Upcoming update with IDN homograph phishing fix - Blog". Opera Security. 2017-04-21. Retrieved 2020-08-26.
"About Safari International Domain Name support". Retrieved 2017-04-29.
Sharif, Tariq (2006-07-31). "Changes to IDN in IE7 to now allow mixing of scripts". IEBlog. Microsoft. Retrieved 2006-11-30.
Sharif, Tariq (2005-09-09). "Phishing Filter in IE7". IEBlog. Microsoft. Retrieved 2006-11-30.
"Firefox 2 Phishing Protection". Mozilla. 2006. Retrieved 2006-11-30.
"Opera Fraud Protection". Opera Software. 2006-12-18. Retrieved 2007-02-24.
Chrome and Firefox Phishing Attack Uses Domains Identical to Known Safe Sites
Phishing with Unicode Domains
"IDN Homographs Database". GitHub. 25 September 2021.
IDN ccTLD Fast Track String Evaluation Completion Archived 2014-10-17 at the Wayback Machine
Emoji to Zero-Day: Latin Homoglyphs in Domains and Subdomains Archived 2020-12-09 at the Wayback Machine
Suzuki, Hiroaki; Chiba, Daiki; Yoneya, Yoshiro; Mori, Tatsuya; Goto, Shigeki (2019-10-21). "ShamFinder: An Automated Framework for Detecting IDN Homographs". Proceedings of the Internet Measurement Conference. New York, NY, USA: ACM. pp. 449–462. doi:10.1145/3355369.3355587. ISBN 978-1-4503-6948-0.
CHIBA, Daiki; AKIYAMA HASEGAWA, Ayako; KOIDE, Takashi; SAWABE, Yuta; GOTO, Shigeki; AKIYAMA, Mitsuaki (2020-07-01). "DomainScouter: Analyzing the Risks of Deceptive Internationalized Domain Names". IEICE Transactions on Information and Systems. E103.D (7): 1493–1511. Bibcode:2020IEITI.103.1493C. doi:10.1587/transinf.2019icp0002. ISSN 0916-8532.

    Safaei Pour, Morteza; Nader, Christelle; Friday, Kurt; Bou-Harb, Elias (May 2023). "A Comprehensive Survey of Recent Internet Measurement Techniques for Cyber Security". Computers & Security. 128 103123. doi:10.1016/j.cose.2023.103123. ISSN 0167-4048.

    vte

Domain name speculation and parking
General	

    Reverse domain hijacking Cybersquatting Domain name drop list Domain name speculation Domain sniping Domain parking Domain tasting Domain name warehousing Doppelganger domain Type-in traffic Typosquatting IDN homograph attack Domain name front running Drop catching
        drop registrar

Legal	

    Uniform Domain-Name Dispute-Resolution Policy Anticybersquatting Consumer Protection Act PROTECT Act of 2003

Technical	

    Domain hack Wildcard DNS record Fast flux

Categories:

    Internationalized domain namesNonstandard spellingUnicodeDeceptionObfuscationWeb security exploitsOrthography

    This page was last edited on 22 November 2025, at 16:11 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.



Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents
(Top)
Duplicate vs. derived character

Compatibility issues

    CJK fullwidth forms

Letterlike symbols

    Greek
    Roman numerals
    Arabic presentation forms
    Hebrew presentation forms

List

        One-to-one mappings
        One-to-two mappings
        One-to-three mappings
        One-to-four mappings
    See also
    References

Duplicate characters in Unicode

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
icon
    
This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.
Find sources: "Duplicate characters in Unicode" – news · newspapers · books · scholar · JSTOR (March 2022) (Learn how and when to remove this message)

Unicode has a certain amount of duplication of characters. These are pairs of single Unicode code points that are canonically equivalent. The reason for this are compatibility issues with legacy systems.

Unless two characters are canonically equivalent, they are not "duplicate" in the narrow sense. There is, however, room for disagreement on whether two Unicode characters really encode the same grapheme in cases such as the U+00B5 µ MICRO SIGN versus U+03BC μ GREEK SMALL LETTER MU.

This should be clearly distinguished from Unicode characters that are rendered as identical glyphs or near-identical glyphs (homoglyphs), either because they are historically cognate (such as Greek Η vs. Latin H) or because of coincidental similarity (such as Greek Ρ vs. Latin P, or Greek Η vs. Cyrillic Н, or the following homoglyph septuplet: astronomical symbol for "Sun" ☉, "circled dot operator" ⊙, the Gothic letter 𐍈, the IPA symbol for a bilabial click ʘ, the Osage letter 𐓃, the Tifinagh letter ⵙ, and the archaic Cyrillic letter Ꙩ).
Duplicate vs. derived character
Further information: Character (computing) and Grapheme

Unicode aims at encoding graphemes, not individual "meanings" ("semantics") of graphemes, and not glyphs. It is a matter of case-by-case judgement whether such characters should receive separate encoding when used in technical contexts, e.g. Greek letters used as mathematical symbols: thus, the choice to have a "micro- sign" µ separate from Greek μ, but not a "Mega sign" separate from Latin M, was a pragmatic decision by The Unicode Consortium for historical reasons (namely, compatibility with Latin-1, which includes a micro sign). Technically µ and μ are not duplicate characters in that the consortium viewed these symbols as distinct characters (while it regarded M for "Mega" and Latin M as one and the same character).

Note that merely having different "meanings" is not sufficient grounds to split a grapheme into several characters. Thus, the acute accent may represent word accent in Welsh or Swedish, it may express vowel quality in French, and it may express vowel length in Hungarian, Icelandic or Irish. Since all these languages are written in the same script, namely Latin script, the acute accent in its various meanings is considered one and the same combining diacritic character U+0301 ́ COMBINING ACUTE ACCENT, and so the accented letter é is the same character in French and Hungarian. There is a separate "combining diacritic acute tone mark" at U+0341 ́ COMBINING ACUTE TONE MARK for the romanization of tone languages, one important difference from the acute accent being that in a language like French, the acute accent can replace the dot over the lowercase i, whereas in a language like Vietnamese, the acute tone mark is added above the dot. Diacritic signs for alphabets considered independent may be encoded separately, such as the acute ("tonos") for the Greek alphabet at U+0384 ΄ GREEK TONOS, and for the Armenian alphabet at U+055B ՛ ARMENIAN EMPHASIS MARK. Some Cyrillic-based alphabets (such as Russian) also use the acute accent, but there is no "Cyrillic acute" encoded separately and U+0301 should be used for Cyrillic as well as Latin (see Cyrillic characters in Unicode). The point that the same grapheme can have many "meanings" is even more obvious considering e.g. the letter U, which has entirely different phonemic referents in the various languages that use it in their orthographies (English /juː/, /ʊ/, /ʌ/ etc., French /y/, German /uː/, /u/, etc., not to mention various uses of U as a symbol).
Compatibility issues
Further information: Unicode compatibility characters
CJK fullwidth forms
Main article: Fullwidth form

In traditional Chinese character encodings, characters usually took either a single byte (known as halfwidth) or two bytes (known as fullwidth). Characters that took a single byte were generally displayed at half the width of those that took two bytes. Some characters such as the Latin alphabet were available in both halfwidth and fullwidth versions. As the halfwidth versions were more commonly used, they were generally the ones mapped to the standard code points for those characters. Therefore a separate section was needed for the fullwidth forms to preserve the distinction.
Letterlike symbols
Main article: Letterlike Symbols

In some cases, specific graphemes have acquired a specialized symbolic or technical meaning separate from their original function. A prominent example is the Greek letter π which is widely recognized as the symbol for the mathematical constant of a circle's circumference divided by its diameter even by people not literate in Greek.

Several variants of the entire Greek and Latin alphabets specifically for use as mathematical symbols are encoded in the Mathematical Alphanumeric Symbols range. This range disambiguates characters that would usually be considered font variants but are encoded separately because of widespread use of font variants e.g. L vs. "script L" ℒ vs. "blackletter L" 𝔏 vs. "boldface blackletter L" 𝕷) as distinctive mathematical symbols. It is intended for use only in mathematical or technical notation, not use in non-technical text.[1]
Greek

Many Greek letters are used as technical symbols. All of the Greek letters are encoded in the Greek section of Unicode but many are encoded a second time under the name of the technical symbol they represent. The "micro sign" (U+00B5 µ MICRO SIGN) is obviously inherited from ISO 8859-1, but the origin of the others is less clear.

Other Greek glyph variants encoded as separate characters include the lunate sigma Ϲ ϲ contrasting with Σ σ, final sigma ς (strictly speaking a contextual glyph variant) contrasting with σ, The Qoppa numeral symbol Ϟ ϟ contrasting with the archaic Ϙ ϙ.

Greek letters assigned separate "symbol" codepoints include the Letterlike Symbols ϐ, ϵ, ϑ, ϖ, ϱ, ϒ, and ϕ (contrasting with β, ε, θ, π, ρ, Υ, φ); the Ohm symbol Ω (contrasting with Ω); and the mathematical operators for the product ∏ and sum ∑ (contrasting with Π and Σ).
Roman numerals

Unicode has a number of characters specifically designated as Roman numerals, as part of the Number Forms range from U+2160 to U+2183. For example, Roman 1988 (MCMLXXXVIII) could alternatively be written as ⅯⅭⅯⅬⅩⅩⅩⅧ. This range includes both uppercase and lowercase numerals, as well as pre-combined glyphs for numbers up to 12 (Ⅻ for XII), mainly intended for clock faces.

The pre-combined glyphs should only be used to represent the individual numbers where the use of individual glyphs is not wanted, and not to replace compounded numbers. For example, one can combine Ⅹ with Ⅰ to produce Roman numeral 11 (ⅩⅠ), so U+216A (Ⅺ) is canonically equivalent to ⅩⅠ. Such characters are also referred to as composite compatibility characters or decomposable compatibility characters. Such characters would not normally have been included within the Unicode standard except for compatibility with other existing encodings (see Unicode compatibility characters). The goal was to accommodate simple translation from existing encodings into Unicode. This makes translations in the opposite direction complicated because multiple Unicode characters may map to a single character in another encoding. Without the compatibility concerns the only characters necessary would be: Ⅰ, Ⅴ, Ⅹ, Ⅼ, Ⅽ, Ⅾ, Ⅿ, ⅰ, ⅴ, ⅹ, ⅼ, ⅽ, ⅾ, ⅿ, ↀ, ↁ, ↂ, ↇ, ↈ, and Ↄ; all other Roman numerals can be composed from these characters.
Arabic presentation forms
Main articles: Arabic Presentation Forms-A and Arabic Presentation Forms-B

Unicode has encoded compatibility characters for contextual Arabic letter forms where its contextual forms are encoded as separate code points (isolated, final, initial, and medial). For example, U+0647 ه ARABIC LETTER HEH has its contextual forms encoded at these 4 code points:

    U+FEE9 ﻩ ARABIC LETTER HEH ISOLATED FORM
    U+FEEA ﻪ ARABIC LETTER HEH FINAL FORM
    U+FEEB ﻫ ARABIC LETTER HEH INITIAL FORM
    U+FEEC ﻬ ARABIC LETTER HEH MEDIAL FORM

The contextual-form characters are not recommended for general use. There are also compatibility Arabic ligatures encoded such as U+FDF2 ﷲ ARABIC LIGATURE ALLAH ISOLATED FORM and U+FDFD ﷽ ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM.
Hebrew presentation forms
Main article: Alphabetic Presentation Forms

Hebrew presentation forms include ligatures, several precomposed characters and wide variants of Hebrew letters. The aleph-lamed ligature is encoded as a separate character at U+FB4F ﭏ HEBREW LIGATURE ALEF LAMED. The wide variants are listed below:

    U+FB21 ﬡ HEBREW LETTER WIDE ALEF
    U+FB22 ﬢ HEBREW LETTER WIDE DALET
    U+FB23 ﬣ HEBREW LETTER WIDE HE
    U+FB24 ﬤ HEBREW LETTER WIDE KAF
    U+FB25 ﬥ HEBREW LETTER WIDE LAMED
    U+FB26 ﬦ HEBREW LETTER WIDE FINAL MEM
    U+FB27 ﬧ HEBREW LETTER WIDE RESH
    U+FB28 ﬨ HEBREW LETTER WIDE TAV

These characters are variants of ordinary Hebrew letters encoded for justification of texts written in Hebrew, such as the Torah. Unicode also encodes a stylistic variant of U+05E2 ע HEBREW LETTER AYIN at U+FB20 ﬠ HEBREW LETTER ALTERNATIVE AYIN.
List
    
This list is incomplete; you can help by adding missing items. (April 2022)
One-to-one mappings

    U+00AA ª FEMININE ORDINAL INDICATOR: U+0061 a LATIN SMALL LETTER A
    U+00B5 µ MICRO SIGN: U+03BC μ GREEK SMALL LETTER MU
    U+00BA º MASCULINE ORDINAL INDICATOR: U+006F o LATIN SMALL LETTER O
    U+017F ſ LATIN SMALL LETTER LONG S: U+0073 s LATIN SMALL LETTER S
    U+0340 ◌̀ COMBINING GRAVE TONE MARK: U+0300 ◌̀ COMBINING GRAVE ACCENT
    U+0341 ◌́ COMBINING ACUTE TONE MARK: U+0301 ◌́ COMBINING ACUTE ACCENT
    U+0343 ◌̓ COMBINING GREEK KORONIS: U+0313 ◌̓ COMBINING COMMA ABOVE
    U+0374 ʹ GREEK NUMERAL SIGN: U+02B9 ʹ MODIFIER LETTER PRIME
    U+037E ; GREEK QUESTION MARK: U+003B ; SEMICOLON
    U+0384 ΄ GREEK TONOS: U+00B4 ´ ACUTE ACCENT
    U+0387 · GREEK ANO TELEIA: U+00B7 · MIDDLE DOT
    U+03D0 ϐ GREEK BETA SYMBOL: U+03B2 β GREEK SMALL LETTER BETA
    U+03D1 ϑ GREEK THETA SYMBOL: U+03B8 θ GREEK SMALL LETTER THETA
    U+03D5 ϕ GREEK PHI SYMBOL: U+03C6 φ GREEK SMALL LETTER PHI
    U+03D6 ϖ GREEK PI SYMBOL: U+03C0 π GREEK SMALL LETTER PI
    U+03F0 ϰ GREEK KAPPA SYMBOL: U+03BA κ GREEK SMALL LETTER KAPPA
    U+03F1 ϱ GREEK RHO SYMBOL: U+03C1 ρ GREEK SMALL LETTER RHO
    U+03F2 ϲ GREEK LUNATE SIGMA SYMBOL: U+03C3 σ GREEK SMALL LETTER SIGMA
    U+03F4 ϴ GREEK CAPITAL THETA SYMBOL: U+0398 Θ GREEK CAPITAL LETTER THETA
    U+03F5 ϵ GREEK LUNATE EPSILON SYMBOL: U+03B5 ε GREEK SMALL LETTER EPSILON
    U+03F9 Ϲ GREEK CAPITAL LUNATE SIGMA SYMBOL: U+03A3 Σ GREEK CAPITAL LETTER SIGMA
    U+1FEF ` GREEK VARIA: U+0060 ` GRAVE ACCENT
    U+1FFD ´ GREEK OXIA: U+00B4 ´ ACUTE ACCENT
    U+2024 ․ ONE DOT LEADER: U+002E . FULL STOP
    U+2107 ℇ EULER CONSTANT: U+0190 Ɛ LATIN CAPITAL LETTER OPEN E
    U+210E ℎ PLANCK CONSTANT: U+0068 h LATIN SMALL LETTER H
    U+210F ℏ PLANCK CONSTANT OVER TWO PI: U+0127 ħ LATIN SMALL LETTER H WITH STROKE
    U+2126 Ω OHM SIGN: U+03A9 Ω GREEK CAPITAL LETTER OMEGA
    U+212A K KELVIN SIGN: U+004B K LATIN CAPITAL LETTER K
    U+212B Å ANGSTROM SIGN: U+00C5 Å LATIN CAPITAL LETTER A WITH RING ABOVE
    U+2135 ℵ ALEF SYMBOL: U+05D0 א HEBREW LETTER ALEF
    U+2136 ℶ BET SYMBOL: U+05D1 ב HEBREW LETTER BET
    U+2137 ℷ GIMEL SYMBOL: U+05D2 ג HEBREW LETTER GIMEL
    U+2138 ℸ DALET SYMBOL: U+05D3 ד HEBREW LETTER DALET
    U+2139 ℹ INFORMATION SOURCE: U+0069 i LATIN SMALL LETTER I
    U+2236 ∶ RATIO: U+003A : COLON
    U+FB20 ﬠ HEBREW LETTER ALTERNATIVE AYIN: U+05E2 ע HEBREW LETTER AYIN
    U+FB21 ﬡ HEBREW LETTER WIDE ALEF: U+05D0 א HEBREW LETTER ALEF
    U+FB22 ﬢ HEBREW LETTER WIDE DALET: U+05D3 ד HEBREW LETTER DALET
    U+FB23 ﬣ HEBREW LETTER WIDE HE: U+05D4 ה HEBREW LETTER HE
    U+FB24 ﬤ HEBREW LETTER WIDE KAF: U+05DB כ HEBREW LETTER KAF
    U+FB25 ﬥ HEBREW LETTER WIDE LAMED: U+05DC ל HEBREW LETTER LAMED
    U+FB26 ﬦ HEBREW LETTER WIDE FINAL MEM: U+05DD ם HEBREW LETTER FINAL MEM
    U+FB27 ﬧ HEBREW LETTER WIDE RESH: U+05E8 ר HEBREW LETTER RESH
    U+FB28 ﬨ HEBREW LETTER WIDE TAV: U+05EA ת HEBREW LETTER TAV
    U+FB29 ﬩ HEBREW LETTER ALTERNATIVE PLUS SIGN: U+002B + PLUS SIGN
    U+1F549 🕉 OM SYMBOL: U+0950 ॐ DEVANAGARI OM
    U+27EAF 𧺯 CJK UNIFIED IDEOGRAPH-27EAF: U+FA23 﨣 CJK COMPATIBILITY IDEOGRAPH-FA23

One-to-two mappings

    U+0344 ◌̈́ COMBINING GREEK DIALYTIKA TONOS: U+0308 ◌̈ COMBINING DIAERESIS, U+0301 ◌́ COMBINING ACUTE ACCENT

    U+2103 ℃ DEGREE CELSIUS: U+00B0 ° DEGREE SIGN, U+0043 C LATIN CAPITAL LETTER C
    U+2109 ℉ DEGREE FAHRENHEIT: U+00B0 ° DEGREE SIGN, U+0046 F LATIN CAPITAL LETTER F
    U+222C ∬ DOUBLE INTEGRAL: U+222B ∫ INTEGRAL, U+222B ∫ INTEGRAL

    U+2254 ≔ COLON EQUALS: U+003A : COLON, U+003D = EQUALS SIGN
    U+2255 ≕ EQUALS COLON: U+003D = EQUALS SIGN, U+003A : COLON
    U+2A75 ⩵ TWO CONSECUTIVE EQUALS SIGNS: U+003D = EQUALS SIGN, U+003D = EQUALS SIGN

One-to-three mappings

    U+222D ∭ TRIPLE INTEGRAL: U+222B ∫ INTEGRAL, U+222B ∫ INTEGRAL, U+222B ∫ INTEGRAL
    U+2A74 ⩴ DOUBLE COLON EQUAL: U+003A : COLON, U+003A : COLON, U+003D = EQUALS SIGN
    U+2A76 ⩶ THREE CONSECUTIVE EQUALS SIGNS: U+003D = EQUALS SIGN, U+003D = EQUALS SIGN, U+003D = EQUALS SIGN

One-to-four mappings

    U+2A0C ⨌ QUADRUPLE INTEGRAL OPERATOR: U+222B ∫ INTEGRAL, U+222B ∫ INTEGRAL, U+222B ∫ INTEGRAL, U+222B ∫ INTEGRAL

See also

    IDN homograph attack
    Unicode equivalence
    Homoglyph
    ASCII art

References

    "UTR #25: Unicode and Mathematics". unicode.org. Retrieved 2024-03-04.

    vte

Unicode
    


Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents
(Top)
Compatibility character types and keywords

Compatibility mappings types

        Glyph substitution and composition
        Rich text compatibility characters
        Semantically distinct characters
    Compatibility blocks
    Normalization
    See also
    References
    External links

Unicode compatibility characters

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
    
This article has multiple issues. Please help improve it or discuss these issues on the talk page. (Learn how and when to remove these messages)
This article possibly contains original research. (July 2008)
This article needs additional citations for verification. (July 2016)

In Unicode and the UCS, a compatibility character is a character that is encoded solely to maintain round-trip convertibility with other, often older standards.[1] According to the Unicode Glossary:

    A character that would not have been encoded except for compatibility and round-trip convertibility with other standards[2]

Although compatibility is used in names, it is not marked as a property. However, the definition is more complicated than the glossary reveals. One of the properties given to characters by the Unicode consortium is the characters' decomposition, or compatibility decomposition. More than five thousand characters have a compatibility decomposition mapping that compatibility character to one or more other UCS characters. By setting a character's decomposition property, Unicode establishes that character as a compatibility character. The reasons for these compatibility designations are both varied and discussed in further detail below. The term decomposition is sometimes confusing because a character's decomposition can, in some cases, be a singleton. In these cases, the decomposition of one character is simply another approximately (but not canonically) equivalent character.
Compatibility character types and keywords
    
This section is about an event or subject that may not be current but does not specify which version of Unicode is being referenced. Please help improve it to include this information. The talk page may contain suggestions. (June 2018)

The compatibility decomposition property for the 5,402 Unicode compatibility characters[when?] includes a keyword that divides the compatibility characters into 17 logical groups. Those characters with a compatibility decomposition but without a keyword are termed canonical decomposable characters and those characters are not compatibility characters. Keywords for compatibility decomposable characters include: <initial>, <medial>, <final>, <isolated>, <wide>, <narrow>, <small>, <square>, <vertical>, <circle>, <noBreak>, <fraction>, <sub>, <super>, and <compat>.These keywords provide some indication of the relation between the compatibility character and its compatibility decomposition character sequence. Compatibility characters fall in three basic categories:

    Characters corresponding to multiple alternate glyph forms and precomposed diacritics to support software and font implementations that do not include complete Unicode text layout capabilities.
    Characters included from other character sets or otherwise added to the UCS that constitute rich text rather than the plain text goals of Unicode.
    Some other characters that are semantically distinct, but visually similar.

Because these semantically distinct characters may be displayed with glyphs similar to the glyphs of other characters, text processing software should try to address possible confusion for the sake of end users. When comparing and collating (sorting) text strings, different forms and rich text variants of characters should not alter the text processing results. For example, software users may be confused when performing a find on a page for a capital Latin letter 'I' and their software application fails to find the visually similar Roman numeral 'Ⅰ'.
Compatibility mappings types
Glyph substitution and composition

Some compatibility characters are completely dispensable for text processing and display software that conforms to the Unicode standard. These include:

Ligatures
    Ligatures such as 'ﬃ' in the Latin script were often encoded as a separate character in legacy character sets. Unicode's approach to ligatures is to treat them as rich text and, if turned on, handle them through glyph substitution.
Precomposed Roman numerals
    For example, U+216B Ⅻ ROMAN NUMERAL TWELVE can be decomposed into U+2169 Ⅹ ROMAN NUMERAL TEN and two U+2160 Ⅰ ROMAN NUMERAL ONE characters. Precomposed characters are in the Number Forms block.
Precomposed fractions
    These decomposition have the keyword <fraction>. A fully conforming text handler should[3] display U+00BC ¼ VULGAR FRACTION ONE QUARTER identically to the composed fraction 1⁄4 (numeral 1 with U+2044 ⁄ FRACTION SLASH and numeral 4). Precomposed characters are in the Number Forms block.
Contextual glyphs or forms
    These arise primarily in the Arabic script. Using fonts with glyph substitution capabilities such as OpenType and TrueTypeGX, Unicode conforming software can substitute the proper glyphs for the same character depending on whether that character appears at the beginning, end, middle of a word or in isolation. Such glyph substitution is also necessary for vertical (top to bottom) text layout for some East Asian languages. In this case glyphs must be substituted or synthesized for wide, narrow, small and square glyph forms. Non-conforming software or software using other character sets instead use multiple separate character for the same letter depending on its position: further complicating text processing.

The UCS, Unicode character properties and the Unicode algorithms provide software implementations with everything needed to properly display these characters from their decomposition equivalents. Therefore, these decomposable compatibility characters become redundant and unnecessary. Their existence in the character set requires extra text processing to ensure text is properly compared and collated (see Unicode normalization). Moreover, these compatibility characters provide no additional or distinct semantics. Nor do these characters provide any visually distinct rendering provided the text layout and fonts are Unicode conforming. Also, none of these characters are required for round-trip convertibility to other character sets, since the transliteration can easily map decomposed characters to precomposed counterparts in another character set. Similarly, contextual forms, such as a final Arabic letter can be mapped based on its position within a word to the appropriate legacy character set form character.

In order to dispense with these compatibility characters, text software must conform to several Unicode protocols. The software must be able to:

    Compose diacritic marked graphemes from letter characters and one or more separate combining diacritic marks.
    Substitute (at the author or reader's discretion) ligatures and contextual glyph variants.
    Lay out CJKV text vertically (at the author's or reader's discretion), substituting glyphs for small, vertical, narrow, wide square forms, either from font data or synthesized as needed.
    Combine fractions using the U+2044 ⁄ FRACTION SLASH and any other arbitrary characters.
    Combine a U+0338 ̸ COMBINING LONG SOLIDUS OVERLAY with other symbols: for example ∄ or ∄ for U+2204 ∄ THERE DOES NOT EXIST.

All together these compatibility characters included for incomplete Unicode implementations total 3,779 of the 5,402 designated compatibility characters. These include all of the compatibility characters marked with the keywords <initial>, <medial>, <final>, <isolated>, <fraction>, <wide>, <narrow>, <small>, <vertical>, <square>. Also it includes nearly all of the canonical and most of the <compat> keyword compatibility characters (the exceptions include those <compat> keyword characters for enclosed alphanumerics, enclosed ideographs and those discussed in § Semantically distinct characters).
Rich text compatibility characters

Many other compatibility characters constitute what Unicode considers rich text and therefore outside the goals of Unicode and UCS. In some sense even compatibility characters discussed in the previous section—those that aid legacy software in displaying ligatures and vertical text—constitute a form of rich text, since the rich text protocols determine whether text is displayed in one way or another. However, the choice to display text with or without ligatures or vertically versus horizontally are both non-semantic rich text. They are simply style differences. This is in contrast to other rich text such as italics, superscripts and subscripts, or list markers where the styling of the rich text implies certain semantics along with it.

For comparing, collating, handling and storing plain text, rich text variants are semantically redundant. For example, using a superscript character for the numeral 4 is likely indistinguishable from using the standard character for a numeral 4 and then using rich text protocols to make it superscript. Such alternate rich text characters therefore create ambiguity because they appear visually the same as their plain text counterpart characters with rich text formatting applied. These rich text compatibility characters include:

Mathematical Alphanumeric Symbols
    These symbols are simply clones of the Latin and Greek alphabets and Indic-Arabic decimal digits repeated in 15 various typefaces. They are intended as an arbitrary palette for mathematical notation. However, they tend to undermine the distinction between encoding characters versus encoding visual glyphs as well as Unicode's goals of supporting only plain text characters. Such alternate styling for a mathematical symbol palette could be easily created through rich text protocols instead.
Enclosed Alphanumerics and ideographs (markers)
    These are characters included primarily for list markers. They do not constitute plain text characters. Moreover, the use of other rich text protocols is more appropriate since, the set of enclosed alphanumerics or ideographs provisioned in the UCS is limited.
Circled alphanumerics and ideographs
    The circled forms are also likely for use as markers. Again, using characters along with rich text protocols to encircle characters strings is more flexible.
Spaces and no-break spaces of varying widths
    These characters are simply rich text variants of U+0020   SPACE and U+00A0   NO-BREAK SPACE. Other rich text protocols should be used instead such as tracking, kerning or word-spacing attributes.
Some subscript and superscript form characters
    Many of the subscript and superscript characters are actually semantically distinct characters from the International Phonetic Alphabet and other writing systems and do not really fall in the category of rich text. However, others simply constitute rich text presentation forms of other Greek, Latin and numeral characters. These rich text superscript and subscript characters therefore properly belong to this category of rich text compatibility characters. Most of these are in the "Superscripts and Subscripts" or the "Basic Latin" blocks.

For all of these rich text compatibility characters the display of glyphs is typically distinct from their compatibility decomposition (related) characters. However, these are considered compatibility characters and discouraged for use by the Unicode consortium because they are not plain text characters, which is what Unicode seeks to support with its UCS and associated protocols. Rich text should be handled through non-Unicode protocols such as HTML, CSS, RTF and other such protocols.

The rich text compatibility characters comprise 1,451[citation needed] of the 5,402 compatibility characters. These include all of the compatibility characters marked with keywords <circle> and <font> (except three listed in the semantically distinct below); 11 spaces variants from the <compat> and canonical characters; and some of the keyword <superscript> and <subscript> from the "Superscripts and Subscripts" block.
Semantically distinct characters

Many compatibility characters are semantically distinct characters, though they may share representational glyphs with other characters. Some of these characters may have been included because most other characters sets that focused on one script or writing system.[sentence fragment] So for example, the ISO and other Latin character sets likely included a character for π (pi) since, when focusing on primarily one writing system or script, those character sets would not have otherwise had characters for the common mathematical symbol π;. However, with Unicode, mathematicians are free to use characters from any known script in the World to stand in for a mathematical set or mathematical constant. To date, Unicode has only added specific semantic support for a few such mathematical constants (for example U+210E ℎ PLANCK CONSTANT, and U+2107 ℇ EULER CONSTANT, both of which Unicode considers to be compatibility characters). Therefore, Unicode designates several mathematical symbols based on letters from Greek and Hebrew as compatibility characters. These include:

    Hebrew letter based symbols (4): U+2135 ℵ ALEF SYMBOL, U+2136 ℶ BET SYMBOL, U+2137 ℷ GIMEL SYMBOL and U+2138 ℸ DALET SYMBOL
    Greek letter based symbols (7): U+03D0 ϐ GREEK BETA SYMBOL, U+03D1 ϑ GREEK THETA SYMBOL, U+03D5 ϕ GREEK PHI SYMBOL, U+03D6 ϖ GREEK PI SYMBOL, U+03F0 ϰ GREEK KAPPA SYMBOL, U+03F1 ϱ GREEK RHO SYMBOL, U+03F4 ϴ GREEK CAPITAL THETA SYMBOL

While these compatibility characters are distinguished from their compatibility decomposition characters only by adding the word "symbol" to their name, they do represent long-standing distinct meanings in written mathematics. However, for all practical purposes they share the same semantics as their compatibility equivalent Greek or Hebrew letter. These may be considered border-line semantically distinguishable characters so they are not included in the total.

Though not the intention of Unicode to encode such measuring units the repertoire includes six (6) such symbols that should not be used by authors: the characters' decompositions should be used instead.[4][5]

    Unit symbols (6): U+212B Å ANGSTROM SIGN: use U+00C5 Å LATIN CAPITAL LETTER A WITH RING ABOVE instead), Ohm (U+2126 Ω : use U+03A9 instead), (U+212A K KELVIN SIGN: use U+004B instead), (U+2109 ℉ DEGREE FAHRENHEIT: use U+00B0 and U+0046 instead), (U+2103 ℃ DEGREE CELSIUS: use U+00B0 ° DEGREE SIGN and U+0043 C LATIN CAPITAL LETTER C instead), U+00B5 µ MICRO SIGN (use U+03BC μ GREEK SMALL LETTER MU instead)

Unicode also designates 22 other letter-like symbols as compatibility characters.[5]

    Other Greek letter-based symbols (3): U+03F5 ϵ GREEK LUNATE EPSILON SYMBOL, U+03F2 ϲ GREEK LUNATE SIGMA SYMBOL, U+03F9 Ϲ GREEK CAPITAL LUNATE SIGMA SYMBOL
    Mathematical constants (3): U+2107 ℇ EULER CONSTANT, U+210E ℎ PLANCK CONSTANT, U+210F ℏ PLANCK CONSTANT OVER TWO PI
    Currency symbols (2): U+20A8 ₨ RUPEE SIGN, U+FDFC ﷼ RIAL SIGN
    Punctuation (4): U+2024 ․ ONE DOT LEADER, U+00A0   NO-BREAK SPACE, U+2011 ‑ NON-BREAKING HYPHEN, U+0F0C ༌ TIBETAN MARK DELIMITER TSHEG BSTAR
    Other letter-like symbols (10): U+2139 ℹ INFORMATION SOURCE, U+2100 ℀ ACCOUNT OF, U+2101 ℁ ADDRESSED TO THE SUBJECT, U+2105 ℅ CARE OF, U+2106 ℆ CADA UNA, U+2116 № NUMERO SIGN, U+2121 ℡ TELEPHONE SIGN, U+213B ℻ FACSIMILE SIGN, U+2122 ™ TRADE MARK SIGN, U+2120 ℠ SERVICE MARK

In addition, several scripts use glyph position such as superscripts and subscripts to differentiate semantics. In these cases subscripts and superscripts are not merely rich text, but constitute a distinct character in the writing system (130 total).

    112 characters representing abstract phonemes from phonetic alphabets such as the International Phonetic Alphabet use such positional glyphs to represent semantic differences (U+1D2C – U+1D6A, U+1D78, U+1D9B – U+1DBF, U+02B0 – U+02B8, U+02E0 – U+02E4)
    14 characters from the Kanbun block (U+3192 – U+319F)
    1 character from the Tifinagh script: U+2D6F ⵯ TIFINAGH MODIFIER LETTER LABIALIZATION MARK
    1 character from the Georgian script: U+10FC ჼ MODIFIER LETTER GEORGIAN NAR
    2 ordinal characters U+00AA ª FEMININE ORDINAL INDICATOR and U+00BA º MASCULINE ORDINAL INDICATOR included in the Latin-1 Supplement[citation needed] block

Finally, Unicode designates Roman numerals as compatibility equivalence to the Latin letters that share the same glyphs.[citation needed]

    Capital Roman numerals (7): U+2160 Ⅰ ROMAN NUMERAL ONE, U+2164 Ⅴ ROMAN NUMERAL FIVE, U+2169 Ⅹ ROMAN NUMERAL TEN, U+216C Ⅼ ROMAN NUMERAL FIFTY, U+216D Ⅽ ROMAN NUMERAL ONE HUNDRED, U+216E Ⅾ ROMAN NUMERAL FIVE HUNDRED, U+216F Ⅿ ROMAN NUMERAL ONE THOUSAND
    and lower case variants (7): U+2170 ⅰ SMALL ROMAN NUMERAL ONE, U+2174 ⅴ SMALL ROMAN NUMERAL FIVE, U+2179 ⅹ SMALL ROMAN NUMERAL TEN, U+217C ⅼ SMALL ROMAN NUMERAL FIFTY, U+217D ⅽ SMALL ROMAN NUMERAL ONE HUNDRED, U+217E ⅾ SMALL ROMAN NUMERAL FIVE HUNDRED, U+217F ⅿ SMALL ROMAN NUMERAL ONE THOUSAND
    18 precomposed Roman numerals in uppercase and lowercase variants (2–4, 6–9 and 11–12)

Roman numeral One Thousand actually has a third character representing a third form or glyph for the same semantic unit: U+2180 ↀ ROMAN NUMERAL ONE THOUSAND C D. From this glyph, one can see where the practice of using a Latin M may have arisen. Strangely, though Unicode unifies the sign-value Roman numerals with the very different[citation needed] (though visually similar) Latin letters, the Indic Arabic place-value (positional) decimal digit numerals are repeated 24 times (a total of 240 code points for 10 numerals) throughout the UCS without any relational or decomposition mapping between them.

The presence of these 167 semantically distinct though visually similar characters (plus the borderline 11 Hebrew and Greek letter based symbols and the 6 measurement unit symbols) among the decomposable characters complicates the topic of compatibility characters. The Unicode standard discourages the use of compatibility characters by content authors. However, in certain specialized areas, these characters are important and quite similar to other characters that have not been included among the compatibility characters. For example, in certain academic circles the use of Roman numerals as distinct from Latin letters that share the same glyphs would be no different from the use of Cuneiform numerals or ancient Greek numerals. Collapsing the Roman numeral characters to Latin letter characters eliminates a semantic distinction. A similar situation exists for phonetic alphabet characters that use subscript or superscript positioned glyphs. In the specialized circles that use phonetic alphabets, authors should be able to do so without resorting to rich text protocols. As another example the keyword 'circle' compatibility characters are often used for describing the game Go. However, these uses of the compatibility characters constitute exceptions where the author has a special reason to use the otherwise discouraged characters.
Compatibility blocks

Several blocks of Unicode characters include either entirely or almost entirely all compatibility characters (U+F900–U+FFEF except for the noncharacters). The compatibility blocks contain none of the semantically distinct compatibility characters with only one exception: the currency symbol U+FDFC ﷼ RIAL SIGN so the compatibility decomposable characters in the compatibility blocks fall unambiguously into the set of discouraged characters. Unicode recommends authors use the plain text compatibility decomposition equivalents instead and complement those characters with rich text markup. This approach is much more flexible and open-ended than using the finite set of circled or enclosed alphanumerics to give just one example.

There are a small number of characters even within the compatibility blocks that themselves are not compatibility characters and therefore may confuse authors. The Enclosed CJK Letters and Months block contains a single non-compatibility character: the U+327F ㉿ KOREAN STANDARD SYMBOL. That symbol and 12 other characters have been included in the blocks for unknown reasons. The CJK Compatibility Ideographs block contains these incorrectly called compatibility unified Han ideographs:

    U+FA0E 﨎 CJK COMPATIBILITY IDEOGRAPH-FA0E
    U+FA0F 﨏 CJK COMPATIBILITY IDEOGRAPH-FA0F
    U+FA11 﨑 CJK COMPATIBILITY IDEOGRAPH-FA11
    U+FA13 﨓 CJK COMPATIBILITY IDEOGRAPH-FA13
    U+FA14 﨔 CJK COMPATIBILITY IDEOGRAPH-FA14
    U+FA1F 﨟 CJK COMPATIBILITY IDEOGRAPH-FA1F
    U+FA21 﨡 CJK COMPATIBILITY IDEOGRAPH-FA21
    U+FA23 﨣 CJK COMPATIBILITY IDEOGRAPH-FA23
    U+FA24 﨤 CJK COMPATIBILITY IDEOGRAPH-FA24
    U+FA27 﨧 CJK COMPATIBILITY IDEOGRAPH-FA27
    U+FA28 﨨 CJK COMPATIBILITY IDEOGRAPH-FA28
    U+FA29 﨩 CJK COMPATIBILITY IDEOGRAPH-FA29

These thirteen characters are not compatibility characters, and their use is not discouraged in any way. However, U+27EAF 𧺯 , the same as U+FA23 﨣 , is mistakenly encoded in CJK Unified Ideographs Extension B.[6] In any event, a normalized text should never contain both U+27EAF 𧺯 and U+FA23 﨣 ; these code points represent the same character, encoded twice.

Several other characters in these blocks have no compatibility mapping but are clearly intended for legacy support:[citation needed]

Alphabetic Presentation Forms (1)

    U+FB1E ﬞ HEBREW POINT JUDEO-SPANISH VARIKA. This is a glyph variant of U+05BF ֿ HEBREW POINT RAFE, though Unicode provides no compatibility mapping.

Arabic Presentation Forms (4)

    U+FD3E ﴾ ORNATE LEFT PARENTHESIS. A glyph variant of U+0028 ( LEFT PARENTHESIS
    U+FD3F ﴿ ORNATE RIGHT PARENTHESIS. A glyph variant of U+0029 ) RIGHT PARENTHESIS
    U+FDFD ﷽ ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM is a ligature for Beh (U+0628), Seen (U+0633), Meem (U+0645), Space (U+0020), Alef (U+0627), Lam (U+0644), Lam (U+0644), Heh (U+0647), Space (U+0020), Alef (U+0627), Lam (U+0644), Reh (U+0631), Hah (U+062D), Meem (U+0645), Alef (U+0627), Noon (U+0646), Space (U+0020), Alef (U+0627), Lam (U+0644), Reh (U+0631), Hah (U+062D), Yeh (U+064A), Meem (U+0645) i.e. بسم الله الرحمان الرحيم [7] (Similarly, U+FDFA and U+FDFB code for two other Arabic ligatures, of 21 and 9 characters respectively.)
    U+FE73 ﹳ ARABIC TAIL FRAGMENT for supporting text systems without contextual glyph handling

CJK Compatibility Forms (2 that are both related to CJK Unified Ideograph: U+4E36 丶)

    U+FE45 ﹅ SESAME DOT
    U+FE46 ﹆ WHITE SESAME DOT

Enclosed Alphanumerics (21 rich text variants)

    11 Negative Circled Numbers (0 and 11 through 20) (U+24FF and U+24EB through U+24F4): ⓿, ⓫ – ⓴
    10 Double Circled Numbers (0 through 10) (U+24F5 through U+24FE): ⓵ – ⓾

Normalization
Main article: Unicode normalization

Normalization is the process by which Unicode conforming software first performs full compatibility decomposition (or composition) before making comparisons or collating text strings.
See also

    CJK Compatibility
    CJK Compatibility Forms
    CJK Compatibility Ideographs

References

"Chapter 2.3: Compatibility characters" (PDF). The Unicode Standard 6.0.0.
Unicode consortium Unicode Glossary
The Unicode Consortium (2010). The Unicode Standard, Version 6.0.0 (PDF). Addison-Wesley Professional. p. 212. ISBN 978-0321480910.
Omega, mu, Angstrom, Kelvin: Unicode Consortium (2017-05-30). "Unicode Technical Report #25 / Unicode Support for Mathematics". p. 11.
≈ designates compatibility decomposition according to https://www.unicode.org/versions/Unicode15.0.0/ch24.pdf and is shown in code charts at https://www.unicode.org/charts/nameslist/n_2100.html
IRGN 1218

    Unicode chart FB50-FDFF (PDF).

External links

    Normalization (Chinese Text Project) - Unicode normalization issues in classical Chinese, with list of normalized CJK codepoints

    vte

Unicode
    

    

    
    

    

    
    

    


    

    

    

    


    

    


    

    

    

Category:

    Unicode

    This page was last edited on 7 December 2025, at 10:19 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.



Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents

    (Top)
    Rationale
    In Unicode
    In OpenType
    See also
    Notes
    References
    External links

Halfwidth and fullwidth forms

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
(Redirected from Fullwidth form)
For the Unicode block, see Halfwidth and Fullwidth Forms (Unicode block).
A command prompt (cmd.exe) with Korean localisation, showing halfwidth and fullwidth characters

In CJK (Chinese, Japanese, and Korean) computing, graphic characters are traditionally classed into fullwidth[a] and halfwidth[b] characters. Unlike monospaced fonts, a halfwidth character occupies half the width of a fullwidth character, hence the name.

Halfwidth and Fullwidth Forms is also the name of a Unicode block U+FF00–FFEF, provided so that older encodings containing both halfwidth and fullwidth characters can have lossless translation to and from Unicode.
Rationale
icon
    
This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources in this section. Unsourced material may be challenged and removed. (April 2021) (Learn how and when to remove this message)
Characters which appear in both JIS X 0201 (single byte) and JIS X 0208 / JIS X 0213 (double byte) have both a halfwidth and a fullwidth form in Shift JIS.

In the days of text mode computing, Western characters were normally laid out in a grid on the screen, often 80 columns by 24 or 25 lines. Each character was displayed as a small dot matrix, often about 8 pixels wide, and an SBCS (single-byte character set) was generally used to encode characters of Western languages.

For aesthetic reasons and readability, it is preferable for Chinese characters to be approximately square-shaped, therefore twice as wide as these fixed-width SBCS characters. As these were typically encoded in a DBCS (double-byte character set), this also meant that their width on screen in a duospaced font was proportional to their byte length. Some terminals and editing programs could not deal with double-byte characters starting at odd columns, only even ones (some could not even put double-byte and single-byte characters in the same line). So the DBCS sets generally included Roman characters and digits also, for use alongside the CJK characters in the same line.

On the other hand, early Japanese computing used a single-byte code page called JIS X 0201 for katakana. These would be rendered at the same width as the other single-byte characters, making them half-width kana characters rather than normally proportioned kana. Although the JIS X 0201 standard itself did not specify half-width display for katakana, this became the visually distinguishing feature in Shift JIS between the single-byte JIS X 0201 and double-byte JIS X 0208 katakana. Some IBM code pages used a similar treatment for Korean jamo,[1] based on the N-byte Hangul code and its EBCDIC translation.
In Unicode
See also: Halfwidth and Fullwidth Forms (Unicode block)

For compatibility with existing character sets that contained both half- and fullwidth versions of the same character, Unicode allocated a single block at U+FF00–FFEF containing the necessary "alternative width" characters. This includes a fullwidth version of all the ASCII characters and some non-ASCII punctuation such as the Yen sign, halfwidth versions of katakana and hangul, and halfwidth versions of some other symbols such as circles. Only characters needed for lossless round trip to existing character sets were allocated, rather than (for instance) making a fullwidth version of every Latin accented character.

Unicode assigns every code point an "East Asian width" property. This may be:[2]
Unicode character properties based on width Abbreviation    Name    Description
W   Wide    Naturally wide character, e.g. Hiragana.
Na  Narrow  Naturally narrow character, e.g. ISO Basic Latin alphabet.
F   Fullwidth   Wide variant with compatibility normalisation to naturally narrow character, e.g. fullwidth Latin script.
H   Halfwidth   Narrow variant with compatibility normalisation to naturally wide character, e.g. half-width kana. Includes U+20A9 (₩) as an exception.
A   Ambiguous   Characters included in East Asian DBCS codes but also in European SBCS codes, e.g. Greek alphabet. Duospaced behaviour can consequently vary.
N   Neutral     Characters which do not appear in East Asian DBCS codes, e.g. Devanagari.

Terminal emulators can use this property to decide whether a character should consume one or two "columns" when figuring out tabs and cursor position.
In OpenType

OpenType has the fwid, halt, hwid, and vhal feature tags to be used to reproduce fullwidth or halfwidth form of a character. CSS provides control over these features using font-variant-east-asian and font-feature-settings properties.[3]
See also

    East Asian punctuation
    Em size – full width forms
    Enclosed Alphanumerics – bullet point sequences; some appear as fullwidth (e.g. ⒈, ⓵, ⑴, ⒜, ⓐ)
    Han unification
    Hangul Jamo (Unicode block)
    Katakana (Unicode block)
    Latin script in Unicode

Notes

In Taiwan and Hong Kong: 全形; in CJK: 全角.

    In Taiwan and Hong Kong: 半形; in CJK: 半角.

References

"ICU Demonstration - Converter Explorer". demo.icu-project.org. Retrieved 7 May 2018.
Lunde, Ken (2019-01-25). "Unicode® Standard Annex #11: East Asian Width". Unicode Consortium.

    "Syntax for OpenType features in CSS". Adobe. Retrieved 2023-09-20.

External links

    East Asian Width Unicode Standard Annex #11

    vte

Unicode
    

    

    
    

    

    
    

    


    

    

    

    


    

    


    

    

    

Categories:

    East Asian typographyKanaHangul jamo

    This page was last edited on 12 June 2025, at 03:28 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.



Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents
(Top)
Symbols

        Glyph variants
    Block
    Emoji
    History
    See also
    References

Letterlike Symbols

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
See also: Number Forms (Unicode block)
Letterlike Symbols
Range   U+2100..U+214F
(80 code points)
Plane   BMP
Scripts Greek (1 char.)
Latin (4 char.)
Common (75 char.)
Symbol sets Mathematics
abbreviations
Assigned    80 code points
Unused  0 reserved code points
Unicode version history
1.0.0 (1991)    57 (+57)
3.0 (1999)  59 (+2)
3.2 (2002)  74 (+15)
4.0 (2003)  75 (+1)
4.1 (2005)  77 (+2)
5.0 (2006)  79 (+2)
5.1 (2008)  80 (+1)
Unicode documentation
Code chart ∣ Web page
Note: [1][2]
This article contains special characters. Without proper rendering support, you may see question marks, boxes, or other symbols.

Letterlike Symbols is a Unicode block containing 80 characters which are constructed mainly from the glyphs of one or more letters. In addition to this block, Unicode includes full styled mathematical alphabets, although Unicode does not explicitly categorize these characters as being "letterlike."
Symbols
Unicode Letterlike Symbols[3] Char  Image   Simulation  Name    Unicode
U+
℀       a⁄c     Account Of  2100
℁       a⁄s     Addressed to the Subject (i.e., care of)    2101
ℂ           Double-struck Capital C     2102
℃       °C  Degree Celsius  2103
℄           Center Line Symbol  2104
℅       c⁄o     Care Of     2105
℆       c⁄u     Cada Una[4]     2106
ℇ       Ɛ   Euler Constant[5]   2107
℈       Э   Scruple     2108
℉       °F  Degree Fahrenheit   2109
ℊ           Script Small G  210A
ℋ           Script Capital H    210B
ℌ           Black-letter Capital H  210C
ℍ           Double-struck Capital H     210D
ℎ       h   Planck Constant     210E
ℏ       ħ   Reduced Planck Constant (Planck Constant over 2π)   210F
ℐ           Script Capital I    2110
ℑ           Black-letter Capital I  2111
ℒ           Script Capital L    2112
ℓ           Script Small L (LaTeX: \ell)    2113
℔           L B Bar Symbol  2114
ℕ           Double-struck Capital N     2115
№       No or No.   Numero Sign     2116
℗       Ⓟ   Sound Recording Copyright Symbol    2117
℘           Script Capital P
alias: Weierstrass Elliptic Function    2118
ℙ           Double-struck Capital P     2119
ℚ           Double-struck Capital Q     211A
ℛ           Script Capital R    211B
ℜ           Black-letter Capital R  211C
ℝ           Double-struck Capital R     211D
℞           Prescription Take   211E
℟           Response    211F
℠       SM  Service Mark    2120
℡       TEL     Telephone Sign  2121
™       TM  Trademark Sign  2122
℣           Versicle    2123
ℤ           Double-struck Capital Z     2124
℥           Ounce Sign  2125
Ω       Ω   Ohm Sign    2126
℧       Ʊ   Inverted ohm Sign   2127
ℨ           Black-letter Capital Z  2128
℩           Turned Greek Small Letter iota  2129
K       K   Kelvin Sign     212A
Å       Å   Angstrom Sign   212B
ℬ           Script capital B    212C
ℭ           Black-letter capital C  212D
℮           Estimated symbol    212E
ℯ           Script small E  212F
ℰ           Script capital E    2130
ℱ           Script capital F    2131
Ⅎ           Turned capital F    2132
ℳ           Script capital M    2133
ℴ           Script small O  2134
ℵ       א   Alef symbol     2135
ℶ       ב   Bet symbol  2136
ℷ       ג   Gimel symbol    2137
ℸ       ד   Dalet symbol    2138
ℹ       i   Information source  2139
℺           Rotated capital Q   213A
℻       FAX     Fax sign    213B
ℼ           Double-struck small pi  213C
ℽ           Double-struck small gamma   213D
ℾ           Double-struck capital gamma     213E
ℿ           Double-struck capital pi    213F
⅀           Double-struck n-ary summation   2140
⅁           Turned sans-serif capital G     2141
⅂           Turned sans-serif capital L     2142
⅃           Reversed sans-serif capital L   2143
⅄           Turned sans-serif capital Y     2144
ⅅ       𝔻   Double-struck italic capital D  2145
ⅆ       𝕕   Double-struck italic small D    2146
ⅇ       𝕖   Double-struck italic small E    2147
ⅈ       𝕚   Double-struck italic small I    2148
ⅉ       𝕛   Double-struck italic small J    2149
⅊           Property line   214A
⅋           Turned ampersand    214B
⅌           Per sign    214C
⅍       A⁄S     Aktieselskab    214D
ⅎ           Turned small F  214E
⅏           Symbol for Samaritan source     214F
Glyph variants

Variation selectors may be used to specify chancery (U+FE00) vs roundhand (U+FE01) forms, if the font supports them:
Code point  Plain   FE00    FE01
U+212C  ℬ   ℬ︀  ℬ︁
U+2130  ℰ   ℰ︀  ℰ︁
U+2131  ℱ   ℱ︀  ℱ︁
U+210B  ℋ   ℋ︀  ℋ︁
U+2110  ℐ   ℐ︀  ℐ︁
U+2112  ℒ   ℒ︀  ℒ︁
U+2133  ℳ   ℳ︀  ℳ︁
U+211B  ℛ   ℛ︀  ℛ︁

The remainder of the set is at Mathematical Alphanumeric Symbols.
Block
Letterlike Symbols[1]
Official Unicode Consortium code chart (PDF)
    0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F
U+210x  ℀   ℁   ℂ   ℃   ℄   ℅   ℆   ℇ   ℈   ℉   ℊ   ℋ   ℌ   ℍ   ℎ   ℏ
U+211x  ℐ   ℑ   ℒ   ℓ   ℔   ℕ   №   ℗   ℘   ℙ   ℚ   ℛ   ℜ   ℝ   ℞   ℟
U+212x  ℠   ℡   ™   ℣   ℤ   ℥   Ω   ℧   ℨ   ℩   K   Å   ℬ   ℭ   ℮   ℯ
U+213x  ℰ   ℱ   Ⅎ   ℳ   ℴ   ℵ   ℶ   ℷ   ℸ   ℹ   ℺   ℻   ℼ   ℽ   ℾ   ℿ
U+214x  ⅀   ⅁   ⅂   ⅃   ⅄   ⅅ   ⅆ   ⅇ   ⅈ   ⅉ   ⅊   ⅋   ⅌   ⅍   ⅎ   ⅏
Notes

    1.^ As of Unicode version 17.0

Emoji

The Letterlike Symbols block contains two emoji: U+2122 and U+2139.[6][7]

The block has four standardized variants defined to specify emoji-style (U+FE0F VS16) or text presentation (U+FE0E VS15) for the two emoji, both of which default to a text presentation.[8]
Emoji variation sequences U+    2122    2139
base character  ™   ℹ
base+VS15 (text)    ™︎  ℹ︎
base+VS16 (emoji)   ™️  ℹ️
History

The following Unicode-related documents record the purpose and process of defining specific characters in the Letterlike Symbols block:
Version     Final code points[a]    Count   UTC ID  L2 ID   WG2 ID  Document
                        
            
            
            
            
            ""
            
            ""
            
            
            
            
            ""
                        
            
            
            
            
            
            
            
            
            
            
                    
            
            
            
            
            
            
            
                        
            
            
            
            ""
            
            
            
                    
            
            
            
            
                        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                        
            
                        
                    
            
            
            
            
            
            
            
                        
            
            

See also

    Greek in Unicode
    Latin script in Unicode
    Unicode symbols
    Mathematical operators and symbols in Unicode
    Mathematical Alphanumeric Symbols (Unicode block)
    Currency Symbols (Unicode block)

References

"Unicode character database". The Unicode Standard. Retrieved 2023-07-26.
"Enumerated Versions of The Unicode Standard". The Unicode Standard. Retrieved 2023-07-26.
Unicode chart (PDF)
Spanish for "each one."
It is unknown which constant this is supposed to be. Xerox standard XCCS 353/046 just says "Euler's".
"UTR #51: Unicode Emoji". Unicode Consortium. 2023-09-05.
"UCD: Emoji Data for UTR #51". Unicode Consortium. 2023-02-01.

    "UTS #51 Emoji Variation Sequences". The Unicode Consortium.

    vte

Unicode
    

    

    
    

    

    
    

    


    

    

    

    


    

    


    

    

    

    vte

Common mathematical notation, symbols, and formulas

    

    

    

    

    

    

    

    

    

Categories:

    Unicode blocksTypographical symbolsLatin-script letters

    This page was last edited on 7 December 2025, at 16:45 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.


    

    
    

    

    
    

    


    

    

    

    


    

    


    

    

    

Category:

    Unicode

    This page was last edited on 21 November 2025, at 17:23 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

Letterlike Symbols is a Unicode block containing 80 characters which are constructed mainly from the glyphs of one or more letters. In addition to this block, Unicode includes full styled mathematical alphabets, although Unicode does not explicitly categorize these characters as being "letterlike."



Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents
(Top)
Sources of equivalence

    Character duplication
    Combining and precomposed characters
        Example
    Typographical non-interaction
    Typographic conventions
    Encoding errors

Normalization

        Algorithms
        Normal forms
        Canonical ordering
    Errors due to normalization differences
    See also
    Notes
    References
    External links

Unicode equivalence

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
icon
    
This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.
Find sources: "Unicode equivalence" – news · newspapers · books · scholar · JSTOR (November 2014) (Learn how and when to remove this message)

Unicode equivalence is the specification by the Unicode character encoding standard that some sequences of code points represent essentially the same character. This feature was introduced in the standard to allow compatibility with pre-existing standard character sets, which often included similar or identical characters.

Unicode provides two such notions, canonical equivalence and compatibility. Code point sequences that are defined as canonically equivalent are assumed to have the same appearance and meaning when printed or displayed. For example, the code point U+006E n LATIN SMALL LETTER N followed by U+0303 ◌̃ COMBINING TILDE is defined by Unicode to be canonically equivalent to the single code point U+00F1 ñ LATIN SMALL LETTER N WITH TILDE of the Spanish alphabet). Therefore, those sequences should be displayed in the same manner, should be treated in the same way by applications such as alphabetizing names or searching, and may be substituted for each other. Similarly, each Hangul syllable block that is encoded as a single character may be equivalently encoded as a combination of a leading conjoining jamo, a vowel conjoining jamo, and, if appropriate, a trailing conjoining jamo.

Sequences that are defined as compatible are assumed to have possibly distinct appearances, but the same meaning in some contexts. Thus, for example, the code point U+FB00 (the typographic ligature "ﬀ") is defined to be compatible—but not canonically equivalent—to the sequence U+0066 U+0066 (two Latin "f" letters). Compatible sequences may be treated the same way in some applications (such as sorting and indexing), but not in others; and may be substituted for each other in some situations, but not in others. Sequences that are canonically equivalent are also compatible, but the opposite is not necessarily true.

The standard also defines a text normalization procedure, called Unicode normalization, that replaces equivalent sequences of characters so that any two texts that are equivalent will be reduced to the same sequence of code points, called the normalization form or normal form of the original text. For each of the two equivalence notions, Unicode defines two normal forms, one fully composed (where multiple code points are replaced by single points whenever possible), and one fully decomposed (where single points are split into multiple ones).
Sources of equivalence
Character duplication
Main article: Duplicate characters in Unicode

For compatibility or other reasons, Unicode sometimes assigns two different code points to entities that are essentially the same character. For example, the letter "A with a ring diacritic above" is encoded as U+00C5 Å LATIN CAPITAL LETTER A WITH RING ABOVE (a letter of the alphabet in Swedish and several other languages) or as U+212B Å ANGSTROM SIGN. Yet the symbol for angstrom is defined to be that Swedish letter, and most other symbols that are letters (such as ⟨V⟩ for volt) do not have a separate code point for each usage. In general, the code points of truly identical characters are defined to be canonically equivalent.
Combining and precomposed characters

For consistency with some older standards, Unicode provides single code points for many characters that could be viewed as modified forms of other characters (such as U+00F1 for "ñ" or U+00C5 for "Å") or as combinations of two or more characters (such as U+FB00 for the ligature "ﬀ" or U+0132 for the Dutch letter "ĳ")

For consistency with other standards, and for greater flexibility, Unicode also provides codes for many elements that are not used on their own, but are meant instead to modify or combine with a preceding base character. Examples of these combining characters are U+0303 ◌̃ COMBINING TILDE and the Japanese diacritic dakuten (U+3099 ◌゙ COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK).

In the context of Unicode, character composition is the process of replacing the code points of a base letter followed by one or more combining characters into a single precomposed character; and character decomposition is the opposite process.

In general, precomposed characters are defined to be canonically equivalent to the sequence of their base letter and subsequent combining diacritic marks, in whatever order these may occur.
Example
Amélie with its two canonically equivalent Unicode forms (NFC and NFD) NFC character    A   m   é   l   i   e
NFC code point  0041    006d    00e9    006c    0069    0065
NFD code point  0041    006d    0065    0301    006c    0069    0065
NFD character   A   m   e   ◌́  l   i   e
Typographical non-interaction

Some scripts regularly use multiple combining marks that do not, in general, interact typographically, and do not have precomposed characters for the combinations. Pairs of such non-interacting marks can be stored in either order. These alternative sequences are, in general, canonically equivalent. The rules that define their sequencing in the canonical form also define whether they are considered to interact.
Typographic conventions

Unicode provides code points for some characters or groups of characters which are modified only for aesthetic reasons (such as ligatures, the half-width katakana characters, or the full-width Latin letters for use in Japanese texts), or to add new semantics without losing the original one (such as digits in subscript or superscript positions, or the circled digits (such as "①") inherited from some Japanese fonts). Such a sequence is considered compatible with the sequence of original (individual and unmodified) characters, for the benefit of applications where the appearance and added semantics are not relevant. However, the two sequences are not declared canonically equivalent, since the distinction has some semantic value and affects the rendering of the text.
Encoding errors

UTF-8 and UTF-16 (and also some other Unicode encodings) do not allow all possible sequences of code units. Different software will convert invalid sequences into Unicode characters using varying rules, some of which are very lossy (e.g., turning all invalid sequences into the same character). This can be considered a form of normalization and can lead to the same difficulties as others.
Normalization

A text processing software implementing the Unicode string search and comparison functionality must take into account the presence of equivalent code points. In the absence of this feature, users searching for a particular code point sequence would be unable to find other visually indistinguishable glyphs that have a different, but canonically equivalent, code point representation.
Algorithms

Unicode provides standard normalization algorithms that produce a unique (normal) code point sequence for all sequences that are equivalent; the equivalence criteria can be either canonical (NF) or compatibility (NFK). Since one can arbitrarily choose the representative element of an equivalence class, multiple canonical forms are possible for each equivalence criterion. Unicode provides two normal forms that are semantically meaningful for each of the two compatibility criteria: the composed forms NFC and NFKC, and the decomposed forms NFD and NFKD. Both the composed and decomposed forms impose a canonical ordering on the code point sequence, which is necessary for the normal forms to be unique.

In order to compare or search Unicode strings, software can use either composed or decomposed forms; this choice does not matter as long as it is the same for all strings involved in a search, comparison, etc. On the other hand, the choice of equivalence criteria can affect search results. For instance, some typographic ligatures like U+FB03 (ﬃ), Roman numerals like U+2168 (Ⅸ) and even subscripts and superscripts, e.g. U+2075 (⁵) have their own Unicode code points. Canonical normalization (NF) does not affect any of these, but compatibility normalization (NFK) will decompose the ffi ligature into the constituent letters, so a search for U+0066 (f) as substring would succeed in an NFKC normalization of U+FB03 but not in NFC normalization of U+FB03. Likewise when searching for the Latin letter I (U+0049) in the precomposed Roman numeral Ⅸ (U+2168). Similarly, the superscript ⁵ (U+2075) is transformed to 5 (U+0035) by compatibility mapping.

Transforming superscripts into baseline equivalents may not be appropriate, however, for rich text software, because the superscript information is lost in the process. To allow for this distinction, the Unicode character database contains compatibility formatting tags that provide additional details on the compatibility transformation.[1] In the case of typographic ligatures, this tag is simply <compat>, while for the superscript it is <super>. Rich text standards like HTML take into account the compatibility tags. For instance, HTML uses its own markup to position a U+0035 in a superscript position.[2]
Normal forms

The four Unicode normalization forms and the algorithms (transformations) for obtaining them are listed in the table below.
NFD
Normalization Form Canonical Decomposition  Characters are decomposed by canonical equivalence, and multiple combining characters are arranged in a specific order.
NFC
Normalization Form Canonical Composition    Characters are decomposed and then recomposed by canonical equivalence.
NFKD
Normalization Form Compatibility Decomposition  Characters are decomposed by compatibility, and multiple combining characters are arranged in a specific order.
NFKC
Normalization Form Compatibility Composition    Characters are decomposed by compatibility, then recomposed by canonical equivalence.

All these algorithms are idempotent transformations, meaning that a string that is already in one of these normalized forms will not be modified if processed again by the same algorithm.

The normal forms are not closed under string concatenation.[3] For defective Unicode strings starting with a Hangul vowel or trailing conjoining jamo, concatenation can break Composition.

However, they are not injective (they map different original glyphs and sequences to the same normalized sequence) and thus also not bijective (cannot be restored). For example, the distinct Unicode strings "U+212B" (the angstrom sign "Å") and "U+00C5" (the Swedish letter "Å") are both expanded by NFD (or NFKD) into the sequence "U+0041 U+030A" (Latin letter "A" and combining ring above "°") which is then reduced by NFC (or NFKC) to "U+00C5" (the Swedish letter "Å").

A single character (other than a Hangul syllable block) that will get replaced by another under normalization can be identified in the Unicode tables for having a non-empty compatibility field but lacking a compatibility tag.
Canonical ordering

The canonical ordering is mainly concerned with the ordering of a sequence of combining characters. For the examples in this section we assume these characters to be diacritics, even though in general some diacritics are not combining characters, and some combining characters are not diacritics.

Unicode assigns each character a combining class, which is identified by a numerical value. Non-combining characters have class number 0, while combining characters have a positive combining class value. To obtain the canonical ordering, every substring of characters having non-zero combining class value must be sorted by the combining class value using a stable sorting algorithm. Stable sorting is required because combining characters with the same class value are assumed to interact typographically, thus the two possible orders are not considered equivalent.

For example, the character U+1EBF (ế), used in Vietnamese, has both an acute and a circumflex accent. Its canonical decomposition is the three-character sequence U+0065 (e) U+0302 (circumflex accent) U+0301 (acute accent). The combining classes for the two accents are both 230, thus U+1EBF is not equivalent to U+0065 U+0301 U+0302.

Since not all combining sequences have a precomposed equivalent (the last one in the previous example can only be reduced to U+00E9 U+0302), even the normal form NFC is affected by combining characters' behavior.
Errors due to normalization differences

When two applications share Unicode data, but normalize them differently, errors and data loss can result. In one specific instance, OS X normalized Unicode filenames sent from the Netatalk and Samba file- and printer-sharing software. Netatalk and Samba did not recognize the altered filenames as equivalent to the original, leading to data loss.[4][5] Resolving such an issue is non-trivial, as normalization is not losslessly invertible.
See also

    Complex text layout
    Diacritic
    IDN homograph attack
    ISO/IEC 14651
    Ligature (typography)
    Precomposed character
    The uconv tool can convert to and from NFC and NFD Unicode normalization forms.
    Unicode
    Unicode compatibility characters

Notes

"UAX #44: Unicode Character Database". Unicode.org. Retrieved 20 November 2014.
"Unicode in XML and other Markup Languages". Unicode.org. Retrieved 20 November 2014.
Per What should be done about concatenation
"netatalk / Bugs / #349 volcharset:UTF8 doesn't work from Mac". SourceForge. Retrieved 20 November 2014.

    "rsync, samba, UTF8, international characters, oh my!". 2009. Archived from the original on January 9, 2010.

References

    Unicode Standard Annex #15: Unicode Normalization Forms

External links

    Unicode.org FAQ - Normalization
    Charlint - a character normalization tool written in Perl

    vte

Unicode
    

    

    
    

    

    
    

    


    

    

    

    


    

    


    

    

    

Category:

    Unicode algorithms

    This page was last edited on 11 August 2025, at 04:01 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.



Wikipedia The Free Encyclopedia

    Donate
    Create account
    Log in

Contents
(Top)
Origin and development

Architecture and terminology

Adoption

Issues

    See also
    Notes
    References
    Further reading
    External links

Unicode

    Article
    Talk

    Read
    Edit
    View history

Tools

Appearance
Text

    Small
    Standard
    Large

Width

    Standard
    Wide

Color (beta)

    Automatic
    Light
    Dark

From Wikipedia, the free encyclopedia
Unicode
Logo of the Unicode Consortium
Alias(es)   

    Universal Coded Character Set (UCS)ISO/IEC 10646

Languages   168 scripts (list)
Standard    Unicode Standard
Encoding formats    

    UTF-8UTF-16GB18030

    UTF-32BOCUSCSUUTF-EBCDIC

(uncommon)

    UTF-7UTF-1

(obsolete)
Preceded by ISO/IEC 8859, among others

    Official websiteTechnical website

This article contains uncommon Unicode characters. Without proper rendering support, you may see question marks, boxes, or other symbols.

Unicode (also known as The Unicode Standard and TUS[1][2]) is a character encoding standard maintained by the Unicode Consortium designed to support the use of text in all of the world's writing systems that can be digitized. Version 17.0[A] defines 159,801 characters and 172 scripts[3] used in various ordinary, literary, academic, and technical contexts.

Unicode has largely supplanted the previous environment of myriad incompatible character sets used within different locales and on different computer architectures. The entire repertoire of these sets, plus many additional characters, were merged into the single Unicode set. Unicode is used to encode the vast majority of text on the Internet, including most web pages, and relevant Unicode support has become a common consideration in contemporary software development. Unicode is ultimately capable of encoding more than 1.1 million characters.

The Unicode character repertoire is synchronized with ISO/IEC 10646, each being code-for-code identical with one another. However, The Unicode Standard is more than just a repertoire within which characters are assigned. To aid developers and designers, the standard also provides charts and reference data, as well as annexes explaining concepts germane to various scripts, providing guidance for their implementation. Topics covered by these annexes include character normalization, character composition and decomposition, collation, and directionality.[4]

Unicode encodes 3,790 emoji, with the continued development thereof conducted by the Consortium as a part of the standard.[5] The widespread adoption of Unicode was in large part responsible for the initial popularization of emoji outside of Japan.[citation needed]

Unicode text is processed and stored as binary data using one of several encodings, which define how to translate the standard's abstracted codes for characters into sequences of bytes. The Unicode Standard itself defines three encodings: UTF-8, UTF-16,[a] and UTF-32, though several others exist. UTF-8 is the most widely used by a large margin, in part due to its backwards-compatibility with ASCII.
Origin and development

Unicode was originally designed with the intent of transcending limitations present in all text encodings designed up to that point: each encoding was relied upon for use in its own context, but with no particular expectation of compatibility with any other. Indeed, any two encodings chosen were often totally unworkable when used together, with text encoded in one interpreted as garbage characters by the other. Most encodings had only been designed to facilitate interoperation between a handful of scripts—often primarily between a given script and Latin characters—not between a large number of scripts, and not with all of the scripts supported being treated in a consistent manner.

The philosophy that underpins Unicode seeks to encode the underlying characters—graphemes and grapheme-like units—rather than graphical distinctions considered mere variant glyphs thereof, that are instead best handled by the typeface, through the use of markup, or by some other means. In particularly complex cases, such as the treatment of orthographical variants in Han characters, there is considerable disagreement regarding which differences justify their own encodings, and which are only graphical variants of other characters.

At the most abstract level, Unicode assigns a unique number called a code point to each character. Many issues of visual representation—including size, shape, and style—are intended to be up to the discretion of the software actually rendering the text, such as a web browser or word processor. However, partially with the intent of encouraging rapid adoption, the simplicity of this original model has become somewhat more elaborate over time, and various pragmatic concessions have been made over the course of the standard's development.

The first 256 code points mirror the ISO/IEC 8859-1 standard, with the intent of trivializing the conversion of text already written in Western European scripts. To preserve the distinctions made by different legacy encodings, therefore allowing for conversion between them and Unicode without any loss of information, many characters nearly identical to others, in both appearance and intended function, were given distinct code points. For example, the Halfwidth and Fullwidth Forms block encompasses a full semantic duplicate of the Latin alphabet, because legacy CJK encodings contained both "fullwidth" (matching the width of CJK characters) and "halfwidth" (matching ordinary Latin script) characters.
History

The origins of Unicode can be traced back to the 1980s, to a group of individuals with connections to Xerox's Character Code Standard (XCCS).[6] In 1987, Xerox employee Joe Becker, along with Apple employees Lee Collins and Mark Davis, started investigating the practicalities of creating a universal character set.[7] With additional input from Peter Fenwick and Dave Opstad,[6] Becker published a draft proposal for an "international/multilingual text character encoding system in August 1988, tentatively called Unicode". He explained that "the name 'Unicode' is intended to suggest a unique, unified, universal encoding".[6]

In this document, entitled Unicode 88, Becker outlined a scheme using 16-bit characters:[6]

    Unicode is intended to address the need for a workable, reliable world text encoding. Unicode could be roughly described as "wide-body ASCII" that has been stretched to 16 bits to encompass the characters of all the world's living languages. In a properly engineered design, 16 bits per character are more than sufficient for this purpose.

This design decision was made based on the assumption that only scripts and characters in "modern" use would require encoding:[6]

    Unicode gives higher priority to ensuring utility for the future than to preserving past antiquities. Unicode aims in the first instance at the characters published in the modern text (e.g. in the union of all newspapers and magazines printed in the world in 1988), whose number is undoubtedly far below 214 = 16,384. Beyond those modern-use characters, all others may be defined to be obsolete or rare; these are better candidates for private use registration than for congesting the public list of generally useful Unicode.

In early 1989, the Unicode working group expanded to include Ken Whistler and Mike Kernaghan of Metaphor, Karen Smith-Yoshimura and Joan Aliprand of Research Libraries Group, and Glenn Wright of Sun Microsystems. In 1990, Michel Suignard and Asmus Freytag of Microsoft and NeXT's Rick McGowan had also joined the group. By the end of 1990, most of the work of remapping existing standards had been completed, and a final review draft of Unicode was ready.

The Unicode Consortium was incorporated in California on 3 January 1991,[8] and the first volume of The Unicode Standard was published that October. The second volume, now adding Han ideographs, was published in June 1992.

In 1996, a surrogate character mechanism was implemented in Unicode 2.0, so that Unicode was no longer restricted to 16 bits. This increased the Unicode codespace to over a million code points, which allowed for the encoding of many historic scripts, such as Egyptian hieroglyphs, and thousands of rarely used or obsolete characters that had not been anticipated for inclusion in the standard. Among these characters are various rarely used CJK characters—many mainly being used in proper names, making them far more necessary for a universal encoding than the original Unicode architecture envisioned.[9]
Unicode Consortium
Main article: Unicode Consortium

The Unicode Consortium is a non-profit organization that coordinates Unicode's development. Full members include most of the main computer software and hardware companies (and few others) with any interest in text-processing standards, including Adobe, Apple, Google, IBM, Meta (previously as Facebook), Microsoft, Netflix, and SAP.[10]

Over the years several countries or government agencies have been members of the Unicode Consortium.[10]

The Consortium has the ambitious goal of eventually replacing existing character encoding schemes with Unicode and its standard Unicode Transformation Format (UTF) schemes, as many of the existing schemes are limited in size and scope and are incompatible with multilingual environments.

The Unicode Bulldog Award is given to people deemed to be influential in Unicode's development, with recipients including Tatsuo Kobayashi, Thomas Milo, Roozbeh Pournader, Ken Lunde, and Michael Everson.[11]
Scripts covered
Main article: Script (Unicode)
Many modern applications can render a substantial subset of the many scripts in Unicode, as demonstrated by this screenshot from the OpenOffice.org application.

As of September 2025, a total of 172[12] scripts (alphabets, abugidas and syllabaries) are included in Unicode, covering most major writing systems in use today.[13][14] There are still scripts that are not yet encoded, particularly those mainly used in historical, liturgical, and academic contexts. Further additions of characters to the already encoded scripts, as well as symbols, in particular for mathematics and music also occur.
Proposals for adding scripts

The Unicode Roadmap Committee (Michael Everson, Rick McGowan, Ken Whistler, V.S. Umamaheswaran)[15] maintain the list of scripts that are candidates or potential candidates for encoding and their tentative code block assignments on the Unicode Roadmap[16] page of the Unicode Consortium website. For some scripts on the Roadmap, such as Jurchen and Khitan large script, encoding proposals have been made and they are working their way through the approval process. For other scripts, such as Numidian and Rongorongo, no proposal has yet been made, and they await agreement on character repertoire and other details from the user communities involved.

Some modern invented scripts which have not yet been included in Unicode (e.g., Tengwar) or which do not qualify for inclusion in Unicode due to lack of real-world use (e.g., Klingon) are listed in the ConScript Unicode Registry, along with unofficial but widely used private use area code assignments.

There is also a Medieval Unicode Font Initiative focused on special Latin medieval characters. Part of these proposals has been already included in Unicode.

The Script Encoding Initiative (SEI),[17] a project created by Deborah Anderson at the University of California, Berkeley, was founded in 2002 with the goal of funding proposals for scripts not yet encoded in the standard. Now run by Anushah Hossain, SEI has become a major source of proposed additions to the standard in recent years.[18] Although SEI collaborates with the Unicode Consortium and the ISO/IEC 10646 standards process, it operates independently, supporting the technical, linguistic, and historical research needed to prepare formal proposals. SEI maintains a database of scripts that have yet to be encoded in the Unicode Standard on the project's website.[19]
Versions

The Unicode Consortium together with the ISO have developed a shared repertoire following the initial publication of The Unicode Standard: Unicode and the ISO's Universal Coded Character Set (UCS) use identical character names and code points. However, the Unicode versions do differ from their ISO equivalents in two significant ways.

While the UCS is a simple character map, Unicode specifies the rules, algorithms, and properties necessary to achieve interoperability between different platforms and languages. Thus, The Unicode Standard includes more information, covering in-depth topics such as bitwise encoding, collation, and rendering. It also provides a comprehensive catalog of character properties, including those needed for supporting bidirectional text, as well as visual charts and reference data sets to aid implementers. Previously, The Unicode Standard was sold as a print volume containing the complete core specification, standard annexes,[note 1] and code charts. However, version 5.0, published in 2006, was the last version printed this way. Starting with version 5.2, only the core specification, published as a print-on-demand paperback, may be purchased.[20] The full text, on the other hand, is published as a free PDF on the Unicode website.

A practical reason for this publication method highlights the second significant difference between the UCS and Unicode—the frequency with which updated versions are released and new characters added. The Unicode Standard has regularly released annual expanded versions, occasionally with more than one version released in a calendar year and with rare cases where the scheduled release had to be postponed. For instance, in April 2020, a month after version 13.0 was published, the Unicode Consortium announced they had changed the intended release date for version 14.0, pushing it back six months to September 2021 due to the COVID-19 pandemic.

Thus far, the following versions of The Unicode Standard have been published. Update versions, which do not include any changes to character repertoire, are signified by the third number (e.g., "version 4.0.1") and are omitted in the table below.[21]
Unicode version history and notable changes to characters and scripts Ver­sion  Date    Publication
(book, text)    UCS edition     Total   Details
Scripts     Characters[b]
1.0.0[22]   October 1991    ISBN 0-201-56788-1 (vol. 1)     —   24  7129    Initial scripts covered: Arabic, Armenian, Bengali, Bopomofo, Cyrillic, Devanagari, Georgian, Greek and Coptic, Gujarati, Gurmukhi, Hangul, Hebrew, Hiragana, Kannada, Katakana, Lao, Latin, Malayalam, Odia, Tamil, Telugu, Thai, and Tibetan
1.0.1[23]   June 1992   ISBN 0-201-60845-6 (vol. 2)     25  28327+21204
−6  The initial 20,902 CJK Unified Ideographs
1.1[24]     June 1993   —   ISO/IEC 10646-1:1993

[c]
    24  34168+5963
−9  33 reclassified as control characters. 4,306 Hangul syllables, Tibetan removed
2.0[25]     July 1996   ISBN 0-201-48345-9  25  38885+11373
−6656   Original set of Hangul syllables removed, new set of 11,172 Hangul syllables added at new location, Tibetan added back in a new location and with a different character repertoire, Surrogate character mechanism defined, Plane 15 and Plane 16 private use area allocated
2.1[26]     May 1998    —   38887+2
    U+20AC € EURO SIGN, U+FFFC ￼ OBJECT REPLACEMENT CHARACTER[26]
3.0[27]     September 1999  ISBN 0-201-61633-5  ISO/IEC 10646-1:2000    38  49194+10307
    Cherokee, Geʽez, Khmer, Mongolian, Burmese, Ogham, runes, Sinhala, Syriac, Thaana, Canadian Aboriginal syllabics, and Yi Syllables, Braille patterns
3.1[28]     March 2001  —   ISO/IEC 10646-1:2000[d]ISO/IEC 10646-2:2001     41  94140+44946
    Deseret, Gothic and Old Italic, sets of symbols for Western and Byzantine music, 42,711 additional CJK Unified Ideographs
3.2[29]     March 2002  45  95156+1016
    Philippine scripts (Buhid, Hanunoo, Tagalog, and Tagbanwa), mathematical symbols
4.0[30]     April 2003  ISBN 0-321-18578-1  ISO/IEC 10646:2003

[e]
    52  96382+1226
    Cypriot syllabary, Limbu, Linear B, Osmanya, Shavian, Tai Le, and Ugaritic, Hexagram symbols
4.1[31]     March 2005  —   59  97655+1273
    Buginese, Glagolitic, Kharosthi, New Tai Lue, Old Persian, Sylheti Nagri, and Tifinagh, Coptic disunified from Greek, ancient Greek numbers and musical symbols, first named character sequences were introduced.[32]
5.0[33]     July 2006   ISBN 0-321-48091-0  64  99024+1369
    Balinese, cuneiform, N'Ko, ʼPhags-pa, Phoenician[34]
5.1[35]     April 2008  —   75  100648+1624
    Carian, Cham, Kayah Li, Lepcha, Lycian, Lydian, Ol Chiki, Rejang, Saurashtra, Sundanese, and Vai, sets of symbols for the Phaistos Disc, Mahjong tiles, Domino tiles, additions to Burmese, Scribal abbreviations, U+1E9E ẞ LATIN CAPITAL LETTER SHARP S
5.2[36]     October 2009    ISBN 978-1-936213-00-9  90  107296+6648
    Avestan, Bamum, Gardiner's sign list of Egyptian hieroglyphs, Imperial Aramaic, Inscriptional Pahlavi, Inscriptional Parthian, Javanese, Kaithi, Lisu, Meetei Mayek, Old South Arabian, Old Turkic, Samaritan, Tai Tham and Tai Viet, additional CJK Unified Ideographs, Jamo for Old Hangul, Vedic Sanskrit
6.0[37]     October 2010    ISBN 978-1-936213-01-6  ISO/IEC 10646:2010

[f]
    93  109384+2088
    Batak, Brahmi, Mandaic, playing card symbols, transport and map symbols, alchemical symbols, emoticons and emoji,[38] additional CJK Unified Ideographs
6.1[39]     January 2012    ISBN 978-1-936213-02-3  ISO/IEC 10646:2012

[g]
    100     110116+732
    Chakma, Meroitic cursive, Meroitic hieroglyphs, Miao, Sharada, Sora Sompeng, and Takri
6.2[40]     September 2012  ISBN 978-1-936213-07-8  110117+1
    U+20BA ₺ TURKISH LIRA SIGN
6.3[41]     September 2013  ISBN 978-1-936213-08-5  110122+5
    5 bidirectional formatting characters
7.0[42]     June 2014   ISBN 978-1-936213-09-2  123     112956+2834
    Bassa Vah, Caucasian Albanian, Duployan, Elbasan, Grantha, Khojki, Khudawadi, Linear A, Mahajani, Manichaean, Mende Kikakui, Modi, Mro, Nabataean, Old North Arabian, Old Permic, Pahawh Hmong, Palmyrene, Pau Cin Hau, Psalter Pahlavi, Siddham, Tirhuta, Warang Citi, and dingbats
8.0[43]     June 2015   ISBN 978-1-936213-10-8  ISO/IEC 10646:2014

[h]
    129     120672+7716
    Ahom, Anatolian hieroglyphs, Hatran, Multani, Old Hungarian, SignWriting, additional CJK Unified Ideographs, lowercase letters for Cherokee, 5 emoji skin tone modifiers
9.0[46]     June 2016   ISBN 978-1-936213-13-9  135     128172+7500
    Adlam, Bhaiksuki, Marchen, Newa, Osage, Tangut, 72 emoji[47]
10.0[48]    June 2017   ISBN 978-1-936213-16-0  ISO/IEC 10646:2017

[i]
    139     136690+8518
    Zanabazar Square, Soyombo, Masaram Gondi, Nüshu, hentaigana, 7,494 CJK Unified Ideographs, 56 emoji, U+20BF ₿ BITCOIN SIGN
11.0[49]    June 2018   ISBN 978-1-936213-19-1  146     137374+684
    Dogra, Georgian Mtavruli capital letters, Gunjala Gondi, Hanifi Rohingya, Indic Siyaq Numbers, Makasar, Medefaidrin, Old Sogdian and Sogdian, Maya numerals, 5 CJK Unified Ideographs, symbols for xiangqi and star ratings, 145 emoji
12.0[50]    March 2019  ISBN 978-1-936213-22-1  150     137928+554
    Elymaic, Nandinagari, Nyiakeng Puachue Hmong, Wancho, Miao script, hiragana and katakana small letters, Tamil historic fractions and symbols, Lao letters for Pali, Latin letters for Egyptological and Ugaritic transliteration, hieroglyph format controls, 61 emoji
12.1[51]    May 2019    ISBN 978-1-936213-25-2  137929+1
    U+32FF ㋿ SQUARE ERA NAME REIWA
13.0[52]    March 2020  ISBN 978-1-936213-26-9  ISO/IEC 10646:2020

[53]
    154     143859+5930
    Chorasmian, Dhives Akuru, Khitan small script, Yezidi, 4,969 CJK ideographs, Arabic script additions used to write Hausa, Wolof, and other African languages, additions used to write Hindko and Punjabi in Pakistan, Bopomofo additions used for Cantonese, Creative Commons license symbols, graphic characters for compatibility with teletext and home computer systems, 55 emoji
14.0[54]    September 2021  ISBN 978-1-936213-29-0  159     144697+838
    Toto, Cypro-Minoan, Vithkuqi, Old Uyghur, Tangsa, extended IPA, Arabic script additions for use in languages across Africa and in Iran, Pakistan, Malaysia, Indonesia, Java, and Bosnia, additions for honorifics and Quranic use, additions to support languages in North America, the Philippines, India, and Mongolia, U+20C0 ⃀ SOM SIGN, Znamenny musical notation, 37 emoji
15.0[55]    September 2022  ISBN 978-1-936213-32-0  161     149186+4489
    Kawi and Mundari, 20 emoji, 4,192 CJK ideographs, control characters for Egyptian hieroglyphs
15.1[56]    September 2023  ISBN 978-1-936213-33-7  149813+627
    Additional CJK ideographs
16.0[57]    September 2024  ISBN 978-1-936213-34-4      168     154998+5185
    Garay, Gurung Khema, Kirat Rai, Ol Onal, Sunuwar, Todhri, Tulu-Tigalari, 7 emoji, 3,995 Egyptian Hieroglyphs
17.0[58]    September 2025  ISBN 978-1-936213-35-1      172     159801+4803
    Beria Erfe, Tai Yo, Sidetic, Tolong Siki, U+20C1 ⃁ SAUDI RIYAL SIGN, 7 emoji, 4,316 CJK unified ideographs

A large amount of documentation for Windows incorrectly uses the term "Unicode" to mean only the UTF-16 encoding.
The total number of graphic and format characters, excluding private use characters, control characters, noncharacters, and surrogate code points).

    2.0 added Amendments 5, 6, and 72.1 added two characters from Amendment 18.

3.2 added Amendment 1.

    4.1 added Amendment 15.0 added Amendment 2 as well as four characters from Amendment 35.1 added Amendment 45.2 added Amendments 5 and 6

Plus the Indian rupee sign

    6.2 added the Turkish lira sign6.3 added five additional characters7.0 added Amendments 1 and 2 as well as the ruble sign

Plus Amendment 1, as well as the Lari sign, nine CJK unified ideographs, and 41 emoji;[44]
9.0 added Amendment 2, as well as Adlam, Newa, Japanese TV symbols, and 74 emoji and symbols.[45]

        Plus 56 emoji, 285 hentaigana characters, and 3 Zanabazar Square characters11.0 added 46 Mtavruli Georgian capital letters, 5 CJK unified ideographs, and 66 emoji12.0 added 62 additional characters.

Architecture and terminology
See also: Universal Character Set characters

Codespace and code points

The Unicode Standard defines a codespace:[59] a sequence of integers called code points[60] in the range from 0 to 1114111, notated according to the standard as U+0000–U+10FFFF.[61] The codespace is a systematic, architecture-independent representation of The Unicode Standard; actual text is processed as binary data via one of several Unicode encodings, such as UTF-8.

In this normative notation, the two-character prefix U+ always precedes a written code point, and the code points themselves are written as hexadecimal numbers.[note 2] At least four hexadecimal digits are always written, with leading zeros prepended as needed. For example, the code point U+00F7 ÷ DIVISION SIGN is padded with two leading zeros, but U+13254 𓉔 EGYPTIAN HIEROGLYPH O004 () is not padded.[63]

There are a total of 1112064 valid code points within the codespace.[64] This number arises from the limitations of the UTF-16 character encoding, which can encode the 216 code points in the range U+0000 through U+FFFF except for the 211 code points in the range U+D800 through U+DFFF, which are used as surrogate pairs to encode the 220 code points in the range U+10000 through U+10FFFF.
Code planes and blocks
Main article: Plane (Unicode)

The Unicode codespace is divided into 17 planes, numbered 0 to 16. Plane 0 is the Basic Multilingual Plane (BMP), and contains the most commonly used characters. All code points in the BMP are accessed as a single code unit in UTF-16 encoding and can be encoded in one, two or three bytes in UTF-8. Code points in planes 1 through 16 (the supplementary planes) are accessed as surrogate pairs in UTF-16 and encoded in four bytes in UTF-8.

Within each plane, characters are allocated within named blocks of related characters. The size of a block is always a multiple of 16, and is often a multiple of 128, but is otherwise arbitrary. Characters required for a given script may be spread out over several different, potentially disjunct blocks within the codespace.
General Category property

Each code point is assigned a classification, listed as the code point's General Category property. Here, at the uppermost level code points are categorized as one of Letter, Mark, Number, Punctuation, Symbol, Separator, or Other. Under each category, each code point is then further subcategorized. In most cases, other properties must be used to adequately describe all the characteristics of any given code point.
General Category (Unicode Character Property)[a]

    vte

Value   Category Major, minor   Basic type[b]   Character assigned[b]   Count[c]
(as of 17.0)    Remarks
                    
L, Letter; LC, Cased Letter (Lu, Ll, and Lt only)[d]
Lu  Letter, uppercase   Graphic     Character   1,886   
Ll  Letter, lowercase   Graphic     Character   2,283   
Lt  Letter, titlecase   Graphic     Character   31  Digraphs consisting of an uppercase letter followed by a lowercase letter (e.g., ǅ, ǈ, ǋ, and ǲ)
Lm  Letter, modifier    Graphic     Character   410     A modifier letter
Lo  Letter, other   Graphic     Character   141,062     An ideograph or a letter in a unicase alphabet
M, Mark
Mn  Mark, nonspacing    Graphic     Character   2,059   
Mc  Mark, spacing combining     Graphic     Character   471     
Me  Mark, enclosing     Graphic     Character   13  
N, Number
Nd  Number, decimal digit   Graphic     Character   770     All these, and only these, have Numeric Type = De[e]
Nl  Number, letter  Graphic     Character   239     Numerals composed of letters or letterlike symbols (e.g., Roman numerals)
No  Number, other   Graphic     Character   915     E.g., vulgar fractions, superscript and subscript digits, vigesimal digits
P, Punctuation
Pc  Punctuation, connector  Graphic     Character   10  Includes spacing underscore characters such as "_", and other spacing tie characters. Unlike other punctuation characters, these may be classified as "word" characters by regular expression libraries.[f]
Pd  Punctuation, dash   Graphic     Character   27  Includes several hyphen characters
Ps  Punctuation, open   Graphic     Character   79  Opening bracket characters
Pe  Punctuation, close  Graphic     Character   77  Closing bracket characters
Pi  Punctuation, initial quote  Graphic     Character   12  Opening quotation mark. Does not include the ASCII "neutral" quotation mark. May behave like Ps or Pe depending on usage
Pf  Punctuation, final quote    Graphic     Character   10  Closing quotation mark. May behave like Ps or Pe depending on usage
Po  Punctuation, other  Graphic     Character   641     
S, Symbol
Sm  Symbol, math    Graphic     Character   960     Mathematical symbols (e.g., +, −, =, ×, ÷, √, ∊, ≠). Does not include parentheses and brackets, which are in categories Ps and Pe. Also does not include !, *, -, or /, which despite frequent use as mathematical operators, are primarily considered to be "punctuation".
Sc  Symbol, currency    Graphic     Character   64  Currency symbols
Sk  Symbol, modifier    Graphic     Character   125     
So  Symbol, other   Graphic     Character   7,468   
Z, Separator
Zs  Separator, space    Graphic     Character   17  Includes the space, but not TAB, CR, or LF, which are Cc
Zl  Separator, line     Format  Character   1   Only U+2028 LINE SEPARATOR (LSEP)
Zp  Separator, paragraph    Format  Character   1   Only U+2029 PARAGRAPH SEPARATOR (PSEP)
C, Other
Cc  Other, control  Control     Character   65 (will never change)[e]   No name,[g] <control>
Cf  Other, format   Format  Character   170     Includes the soft hyphen, joining control characters (ZWNJ and ZWJ), control characters to support bidirectional text, and language tag characters
Cs  Other, surrogate    Surrogate   Not (only used in UTF-16)   2,048 (will never change)[e]    No name,[g] <surrogate>
Co  Other, private use  Private-use     Character (but no interpretation specified)     137,468 total (will never change)[e] (6,400 in BMP, 131,068 in Planes 15–16)    No name,[g] <private-use>
Cn  Other, not assigned     Noncharacter    Not     66 (will not change unless the range of Unicode code points is expanded)[e]     No name,[g] <noncharacter>
Reserved    Not     814,664     No name,[g] <reserved>

"Table 4-4: General Category". The Unicode Standard. Unicode Consortium. September 2025.
"Table 2-3: Types of code points". The Unicode Standard. Unicode Consortium. September 2025.
"DerivedGeneralCategory.txt". The Unicode Consortium. 2025-07-24.
"5.7.1 General Category Values". UTR #44: Unicode Character Database. Unicode Consortium. 2024-08-27.
Unicode Character Encoding Stability Policies: Property Value Stability Stability policy: Some gc groups will never change. gc=Nd corresponds with Numeric Type=De (decimal).
"Annex C: Compatibility Properties (§ word)". Unicode Regular Expressions. Version 23. Unicode Consortium. 2022-02-08. Unicode Technical Standard #18.

    "Table 4-9: Construction of Code Point Labels". The Unicode Standard. Unicode Consortium. September 2025. A Code Point Label may be used to identify a nameless code point. E.g. <control-hhhh>, <control-0088>. The Name remains blank, which can prevent inadvertently replacing, in documentation, a Control Name with a true Control code. Unicode also uses <not a character> for <noncharacter>.

The 1024 points in the range U+D800–U+DBFF are known as high-surrogate code points, and code points in the range U+DC00–U+DFFF (1024 code points) are known as low-surrogate code points. A high-surrogate code point followed by a low-surrogate code point forms a surrogate pair in UTF-16 in order to represent code points greater than U+FFFF. In principle, these code points cannot otherwise be used, though in practice this rule is often ignored, especially when not using UTF-16.

A small set of code points are guaranteed never to be assigned to characters, although third-parties may make independent use of them at their discretion. There are 66 of these noncharacters: U+FDD0–U+FDEF and the last two code points in each of the 17 planes (e.g. U+FFFE, U+FFFF, U+1FFFE, U+1FFFF, ..., U+10FFFE, U+10FFFF). The set of noncharacters is stable, and no new noncharacters will ever be defined.[65] Like surrogates, the rule that these cannot be used is often ignored, although the operation of the byte order mark assumes that U+FFFE will never be the first code point in a text. The exclusion of surrogates and noncharacters leaves 1111998 code points available for use.

Private use code points are considered to be assigned, but they intentionally have no interpretation specified by The Unicode Standard[66] such that any interchange of such code points requires an independent agreement between the sender and receiver as to their interpretation. There are three private use areas in the Unicode codespace:

    Private Use Area: U+E000–U+F8FF (6400 characters),
    Supplementary Private Use Area-A: U+F0000–U+FFFFD (65534 characters),
    Supplementary Private Use Area-B: U+100000–U+10FFFD (65534 characters).

Graphic characters are those defined by The Unicode Standard to have particular semantics, either having a visible glyph shape or representing a visible space. As of Unicode 17.0, there are 159629 graphic characters.

Format characters are characters that do not have a visible appearance but may have an effect on the appearance or behavior of neighboring characters. For example, U+200C ZERO WIDTH NON-JOINER and U+200D ZERO WIDTH JOINER may be used to change the default shaping behavior of adjacent characters (e.g. to inhibit ligatures or request ligature formation). There are 172 format characters in Unicode 17.0.

65 code points, the ranges U+0000–U+001F and U+007F–U+009F, are reserved as control codes, corresponding to the C0 and C1 control codes as defined in ISO/IEC 6429. U+0009 TAB, U+000A LINE FEED, and U+000D CARRIAGE RETURN are widely used in texts using Unicode. In a phenomenon known as mojibake, the C1 code points are improperly decoded according to the Windows-1252 codepage, previously widely used in Western European contexts.

Together, graphic, format, control code, and private use characters are collectively referred to as assigned characters. Reserved code points are those code points that are valid and available for use, but have not yet been assigned. As of Unicode 17.0, there are 814664 reserved code points.
Abstract characters
Further information: Universal Character Set characters § Characters, grapheme clusters and glyphs

The set of graphic and format characters defined by Unicode does not correspond directly to the repertoire of abstract characters representable under Unicode. Unicode encodes characters by associating an abstract character with a particular code point.[67] However, not all abstract characters are encoded as a single Unicode character, and some abstract characters may be represented in Unicode by a sequence of two or more characters. For example, a Latin small letter "i" with an ogonek, a dot above, and an acute accent, which is required in Lithuanian, is represented by the character sequence U+012F; U+0307; U+0301. Unicode maintains a list of uniquely named character sequences for abstract characters that are not directly encoded in Unicode.[68]

All assigned characters have a unique and immutable name by which they are identified. This immutability has been guaranteed since version 2.0 of The Unicode Standard by its Name Stability policy.[65] In cases where a name is seriously defective and misleading, or has a serious typographical error, a formal alias may be defined that applications are encouraged to use in place of the official character name. For example, U+A015 ꀕ YI SYLLABLE WU has the formal alias YI SYLLABLE ITERATION MARK, and U+FE18 ︘ PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET (sic) has the formal alias PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRACKET.[69]
Ready-made versus composite characters

Unicode includes a mechanism for modifying characters that greatly extends the supported repertoire of glyphs. This covers the use of combining diacritical marks that may be added after the base character by the user. Multiple combining diacritics may be simultaneously applied to the same character. Unicode also contains precomposed versions of most letter/diacritic combinations in normal use. These make the conversion to and from legacy encodings simpler, and allow applications to use Unicode as an internal text format without having to implement combining characters. For example, é can be represented in Unicode as U+0065 e LATIN SMALL LETTER E followed by U+0301 ◌́ COMBINING ACUTE ACCENT), and equivalently as the precomposed character U+00E9 é LATIN SMALL LETTER E WITH ACUTE. Thus, users often have multiple equivalent ways of encoding the same character. The mechanism of canonical equivalence within The Unicode Standard ensures the practical interchangeability of these equivalent encodings.

An example of this arises with the Korean alphabet Hangul: Unicode provides a mechanism for composing Hangul syllables from their individual Hangul Jamo subcomponents. However, it also provides 11172 combinations of precomposed syllables made from the most common jamo.

CJK characters presently only have codes for uncomposable radicals and precomposed forms. Most Han characters have either been intentionally composed from, or reconstructed as compositions of, simpler orthographic elements called radicals, so in principle Unicode could have enabled their composition as it did with Hangul. While this could have greatly reduced the number of required code points, as well as allowing the algorithmic synthesis of many arbitrary new characters, the complexities of character etymologies and the post-hoc nature of radical systems add immense complexity to the proposal. Indeed, attempts to design CJK encodings on the basis of composing radicals have been met with difficulties resulting from the reality that Chinese characters do not decompose as simply or as regularly as Hangul does.

The CJK Radicals Supplement block is assigned to the range U+2E80–U+2EFF, and the Kangxi radicals are assigned to U+2F00–U+2FDF. The Ideographic Description Sequences block covers the range U+2FF0–U+2FFB, but The Unicode Standard warns against using its characters as an alternate representation for characters encoded elsewhere:

    This process is different from a formal encoding of an ideograph. There is no canonical description of unencoded ideographs; there is no semantic assigned to described ideographs; there is no equivalence defined for described ideographs. Conceptually, ideographic descriptions are more akin to the English phrase "an 'e' with an acute accent on it" than to the character sequence <U+0065, U+0301>.

Ligatures
The Devanāgarī ddhrya-ligature (द् + ध् + र् + य = द्ध्र्य) of JanaSanskritSans[70]
The Arabic lām-alif ligature (ل ‎+‎ ا ‎=‎ لا)

Many scripts, including Arabic and Devanāgarī, have special orthographic rules that require certain combinations of letterforms to be combined into special ligature forms. The rules governing ligature formation can be quite complex, requiring special script-shaping technologies such as ACE (Arabic Calligraphic Engine by DecoType in the 1980s and used to generate all the Arabic examples in the printed editions of The Unicode Standard), which became the proof of concept for OpenType (by Adobe and Microsoft), Graphite (by SIL International), or AAT (by Apple).

Instructions are also embedded in fonts to tell the operating system how to properly output different character sequences. A simple solution to the placement of combining marks or diacritics is assigning the marks a width of zero and placing the glyph itself to the left or right of the left sidebearing (depending on the direction of the script they are intended to be used with). A mark handled this way will appear over whatever character precedes it, but will not adjust its position relative to the width or height of the base glyph; it may be visually awkward and it may overlap some glyphs. Real stacking is impossible but can be approximated in limited cases (for example, Thai top-combining vowels and tone marks can just be at different heights to start with). Generally, this approach is only effective in monospaced fonts but may be used as a fallback rendering method when more complex methods fail.
Standardized subsets

Several subsets of Unicode are standardized: Microsoft Windows since Windows NT 4.0 supports WGL-4 with 657 characters, which is considered to support all contemporary European languages using the Latin, Greek, or Cyrillic script. Other standardized subsets of Unicode include the Multilingual European Subsets:[71] MES-1 (Latin scripts only; 335 characters), MES-2 (Latin, Greek, and Cyrillic; 1062 characters)[72] and MES-3A & MES-3B (two larger subsets, not shown here). MES-2 includes every character in MES-1 and WGL-4.

The standard DIN 91379[73] specifies a subset of Unicode letters, special characters, and sequences of letters and diacritic signs to allow the correct representation of names and to simplify data exchange in Europe. This standard supports all of the official languages of all European Union countries, as well as the German minority languages and the official languages of Iceland, Liechtenstein, Norway, and Switzerland. To allow the transliteration of names in other writing systems to the Latin script according to the relevant ISO standards, all necessary combinations of base letters and diacritic signs are provided.
WGL-4, MES-1 and MES-2 Row  Cells   Range(s)
00  20–7E   Basic Latin (00–7F)
A0–FF   Latin-1 Supplement (80–FF)
01  00–13, 14–15, 16–2B, 2C–2D, 2E–4D, 4E–4F, 50–7E, 7F     Latin Extended-A (00–7F)
8F, 92, B7, DE-EF, FA–FF    Latin Extended-B (80–FF ...)
02  18–1B, 1E–1F    Latin Extended-B (... 00–4F)
59, 7C, 92  IPA Extensions (50–AF)
BB–BD, C6, C7, C9, D6, D8–DB, DC, DD, DF, EE    Spacing Modifier Letters (B0–FF)
03  74–75, 7A, 7E, 84–8A, 8C, 8E–A1, A3–CE, D7, DA–E1   Greek (70–FF)
04  00–5F, 90–91, 92–C4, C7–C8, CB–CC, D0–EB, EE–F5, F8–F9  Cyrillic (00–FF)
1E  02–03, 0A–0B, 1E–1F, 40–41, 56–57, 60–61, 6A–6B, 80–85, 9B, F2–F3   Latin Extended Additional (00–FF)
1F  00–15, 18–1D, 20–45, 48–4D, 50–57, 59, 5B, 5D, 5F–7D, 80–B4, B6–C4, C6–D3, D6–DB, DD–EF, F2–F4, F6–FE   Greek Extended (00–FF)
20  13–14, 15, 17, 18–19, 1A–1B, 1C–1D, 1E, 20–22, 26, 30, 32–33, 39–3A, 3C, 3E, 44, 4A     General Punctuation (00–6F)
7F, 82  Superscripts and Subscripts (70–9F)
A3–A4, A7, AC, AF   Currency Symbols (A0–CF)
21  05, 13, 16, 22, 26, 2E  Letterlike Symbols (00–4F)
5B–5E   Number Forms (50–8F)
90–93, 94–95, A8    Arrows (90–FF)
22  00, 02, 03, 06, 08–09, 0F, 11–12, 15, 19–1A, 1E–1F, 27–28, 29, 2A, 2B, 48, 59, 60–61, 64–65, 82–83, 95, 97  Mathematical Operators (00–FF)
23  02, 0A, 20–21, 29–2A    Miscellaneous Technical (00–FF)
25  00, 02, 0C, 10, 14, 18, 1C, 24, 2C, 34, 3C, 50–6C   Box Drawing (00–7F)
80, 84, 88, 8C, 90–93   Block Elements (80–9F)
A0–A1, AA–AC, B2, BA, BC, C4, CA–CB, CF, D8–D9, E6  Geometric Shapes (A0–FF)
26  3A–3C, 40, 42, 60, 63, 65–66, 6A, 6B    Miscellaneous Symbols (00–FF)
F0  (01–02)     Private Use Area (00–FF ...)
FB  01–02   Alphabetic Presentation Forms (00–4F)
FF  FD  Specials

Rendering software that cannot process a Unicode character appropriately often displays it as an open rectangle, or as U+FFFD to indicate the position of the unrecognized character. Some systems have made attempts to provide more information about such characters. Apple's Last Resort font will display a substitute glyph indicating the Unicode range of the character, and the SIL International's Unicode fallback font will display a box showing the hexadecimal scalar value of the character.
Mapping and encodings

Several mechanisms have been specified for storing a series of code points as a series of bytes.

Unicode defines two mapping methods: the Unicode Transformation Format (UTF) encodings, and the Universal Coded Character Set (UCS) encodings. An encoding maps (possibly a subset of) the range of Unicode code points to sequences of values in some fixed-size range, termed code units. All UTF encodings map code points to a unique sequence of bytes.[74] The numbers in the names of the encodings indicate the number of bits per code unit (for UTF encodings) or the number of bytes per code unit (for UCS encodings and UTF-1). UTF-8 and UTF-16 are the most commonly used encodings. UCS-2 is an obsolete subset of UTF-16; UCS-4 and UTF-32 are functionally equivalent.

UTF encodings include:

    UTF-8, which uses one to four 8-bit units per code point,[note 3] and has maximal compatibility with ASCII
    UTF-16, which uses one 16-bit unit per code point below U+010000, and a surrogate pair of two 16-bit units per code point in the range U+010000 to U+10FFFF
    UTF-32, which uses one 32-bit unit per code point
    UTF-EBCDIC, not specified as part of The Unicode Standard, which uses one to five 8-bit units per code point, intended to maximize compatibility with EBCDIC

UTF-8 uses one to four 8-bit units (bytes) per code point and, being compact for Latin scripts and ASCII-compatible, provides the de facto standard encoding for the interchange of Unicode text. It is used by FreeBSD and most recent Linux distributions as a direct replacement for legacy encodings in general text handling.

The UCS-2 and UTF-16 encodings specify the Unicode byte order mark (BOM) for use at the beginnings of text files, which may be used for byte-order detection (or byte endianness detection). The BOM, encoded as U+FEFF ZERO WIDTH NO-BREAK SPACE, has the important property of unambiguity on byte reorder, regardless of the Unicode encoding used; U+FFFE (the result of byte-swapping U+FEFF) does not equate to a legal character, and U+FEFF in places other than the beginning of text conveys the zero-width non-break space.

The same character converted to UTF-8 becomes the byte sequence EF BB BF. The Unicode Standard allows the BOM "can serve as a signature for UTF-8 encoded text where the character set is unmarked".[75] Some software developers have adopted it for other encodings, including UTF-8, in an attempt to distinguish UTF-8 from local 8-bit code pages. However RFC 3629, the UTF-8 standard, recommends that byte order marks be forbidden in protocols using UTF-8, but discusses the cases where this may not be possible. In addition, the large restriction on possible patterns in UTF-8 (for instance there cannot be any lone bytes with the high bit set) means that it should be possible to distinguish UTF-8 from other character encodings without relying on the BOM.

In UTF-32 and UCS-4, one 32-bit code unit serves as a fairly direct representation of any character's code point (although the endianness, which varies across different platforms, affects how the code unit manifests as a byte sequence). In the other encodings, each code point may be represented by a variable number of code units. UTF-32 is widely used as an internal representation of text in programs (as opposed to stored or transmitted text), since every Unix operating system that uses the GCC compilers to generate software uses it as the standard "wide character" encoding. Recent versions of the Python programming language (beginning with 2.2) may also be configured to use UTF-32 as the representation for Unicode strings, effectively disseminating such encoding in high-level coded software.

Punycode, another encoding form, enables the encoding of Unicode strings into the limited character set supported by the ASCII-based Domain Name System (DNS). The encoding is used as part of IDNA, which is a system enabling the use of Internationalized Domain Names in all scripts that are supported by Unicode. Earlier and now historical proposals include UTF-5 and UTF-6.

GB18030 is another encoding form for Unicode, from the Standardization Administration of China. It is the official character set of the People's Republic of China (PRC). BOCU-1 and SCSU are Unicode compression schemes. The April Fools' Day RFC of 2005 specified two parody UTF encodings, UTF-9 and UTF-18.
Adoption
See also: UTF-8 § Implementations and adoption
Wikibooks has a book on the topic of: Unicode/Versions

Unicode, in the form of UTF-8, has been the most common encoding for the World Wide Web since 2008.[76] It has near-universal adoption, and much of the non-UTF-8 content is found in other Unicode encodings, e.g. UTF-16. As of 2024, UTF-8 accounts for on average 98.3% of all web pages (and 983 of the top 1,000 highest-ranked web pages).[77] Although many pages only use ASCII characters to display content, UTF-8 was designed with 8-bit ASCII as a subset and almost no websites now declare their encoding to only be ASCII instead of UTF-8.[78] Over a third of the languages tracked have 100% UTF-8 use.

All internet protocols maintained by Internet Engineering Task Force, e.g. File Transfer Protocol (FTP),[79] have required support for UTF-8 since the publication of RFC 2277 in 1998, which specified that all IETF protocols "MUST be able to use the UTF-8 charset".[80]
Operating systems

Unicode has become the dominant scheme for the internal processing and storage of text. Although a great deal of text is still stored in legacy encodings, Unicode is used almost exclusively for building new information processing systems. Early adopters tended to use UCS-2 (the fixed-length two-byte obsolete precursor to UTF-16) and later moved to UTF-16 (the variable-length current standard), as this was the least disruptive way to add support for non-BMP characters. The best known such system is Windows NT (and its descendants, 2000, XP, Vista, 7, 8, 10, and 11), which uses UTF-16 as the sole internal character encoding. The Java and .NET bytecode environments, macOS, and KDE also use it for internal representation. Partial support for Unicode can be installed on Windows 9x through the Microsoft Layer for Unicode.

UTF-8 (originally developed for Plan 9)[81] has become the main storage encoding on most Unix-like operating systems (though others are also used by some libraries) because it is a relatively easy replacement for traditional extended ASCII character sets. UTF-8 is also the most common Unicode encoding used in HTML documents on the World Wide Web.

Multilingual text-rendering engines which use Unicode include Uniscribe and DirectWrite for Microsoft Windows, ATSUI and Core Text for macOS, and Pango for GTK+ and the GNOME desktop.
Input methods
Main article: Unicode input

Because keyboard layouts cannot have simple key combinations for all characters, several operating systems provide alternative input methods that allow access to the entire repertoire.

ISO/IEC 14755,[82] which standardises methods for entering Unicode characters from their code points, specifies several methods. There is the Basic method, where a beginning sequence is followed by the hexadecimal representation of the code point and the ending sequence. There is also a screen-selection entry method specified, where the characters are listed in a table on a screen, such as with a character map program.

Online tools for finding the code point for a known character include Unicode Lookup[83] by Jonathan Hedley and Shapecatcher[84] by Benjamin Milde. In Unicode Lookup, one enters a search key (e.g. "fractions"), and a list of corresponding characters with their code points is returned. In Shapecatcher, based on Shape context, one draws the character in a box and a list of characters approximating the drawing, with their code points, is returned.
Email
Main article: Unicode and email

MIME defines two different mechanisms for encoding non-ASCII characters in email, depending on whether the characters are in email headers (such as the "Subject:"), or in the text body of the message; in both cases, the original character set is identified as well as a transfer encoding. For email transmission of Unicode, the UTF-8 character set and the Base64 or the Quoted-printable transfer encoding are recommended, depending on whether much of the message consists of ASCII characters. The details of the two different mechanisms are specified in the MIME standards and generally are hidden from users of email software.

The IETF has defined[85][86] a framework for internationalized email using UTF-8, and has updated[87][88][89][90] several protocols in accordance with that framework.

The adoption of Unicode in email has been very slow.[citation needed] Some East Asian text is still encoded in encodings such as ISO-2022, and some devices, such as mobile phones,[citation needed] still cannot correctly handle Unicode data. Support has been improving, however. Many major free mail providers such as Yahoo! Mail, Gmail, and Outlook.com support it.
Web
Main article: Unicode and HTML

All W3C recommendations have used Unicode as their document character set since HTML 4.0. Web browsers have supported Unicode, especially UTF-8, for many years. There used to be display problems resulting primarily from font related issues; e.g. v6 and older of Microsoft Internet Explorer did not render many code points unless explicitly told to use a font that contains them.[91]

Although syntax rules may affect the order in which characters are allowed to appear, XML (including XHTML) documents, by definition,[92] comprise characters from most of the Unicode code points, with the exception of:

    FFFE or FFFF.
    most of the C0 control codes,
    the permanently unassigned code points D800–DFFF,

HTML characters manifest either directly as bytes according to the document's encoding, if the encoding supports them, or users may write them as numeric character references based on the character's Unicode code point. For example, the references &#916;, &#1049;, &#1511;, &#1605;, &#3671;, &#12354;, &#21494;, &#33865;, and &#47568; (or the same numeric values expressed in hexadecimal, with &#x as the prefix) should display on all browsers as Δ, Й, ק ,م, ๗, あ, 叶, 葉, and 말.

When specifying URIs, for example as URLs in HTTP requests, non-ASCII characters must be percent-encoded.
Fonts
Main article: Unicode font

Unicode is not in principle concerned with fonts per se, seeing them as implementation choices.[93] Any given character may have many allographs, from the more common bold, italic and base letterforms to complex decorative styles. A font is "Unicode compliant" if the glyphs in the font can be accessed using code points defined in The Unicode Standard.[94] The standard does not specify a minimum number of characters that must be included in the font; some fonts have quite a small repertoire.

Free and retail fonts based on Unicode are widely available, since TrueType and OpenType support Unicode (and Web Open Font Format (WOFF and WOFF2) is based on those). These font formats map Unicode code points to glyphs, but OpenType and TrueType font files are restricted to 65,535 glyphs. Collection files provide a "gap mode" mechanism for overcoming this limit in a single font file. (Each font within the collection still has the 65,535 limit, however.) A TrueType Collection file would typically have a file extension of ".ttc".

Thousands of fonts exist on the market, but fewer than a dozen fonts—sometimes described as "pan-Unicode" fonts—attempt to support the majority of Unicode's character repertoire. Instead, Unicode-based fonts typically focus on supporting only basic ASCII and particular scripts or sets of characters or symbols. Several reasons justify this approach: applications and documents rarely need to render characters from more than one or two writing systems; fonts tend to demand resources in computing environments; and operating systems and applications show increasing intelligence in regard to obtaining glyph information from separate font files as needed, i.e., font substitution. Furthermore, designing a consistent set of rendering instructions for tens of thousands of glyphs constitutes a monumental task; such a venture passes the point of diminishing returns for most typefaces.
Newlines

Unicode partially addresses the newline problem that occurs when trying to read a text file on different platforms. Unicode defines a large number of characters that conforming applications should recognize as line terminators.

In terms of the newline, Unicode introduced U+2028 LINE SEPARATOR and U+2029 PARAGRAPH SEPARATOR. This was an attempt to provide a Unicode solution to encoding paragraphs and lines semantically, potentially replacing all of the various platform solutions. In doing so, Unicode does provide a way around the historical platform-dependent solutions. Nonetheless, few if any Unicode solutions have adopted these Unicode line and paragraph separators as the sole canonical line ending characters. However, a common approach to solving this issue is through newline normalization. This is achieved with the Cocoa text system in macOS and also with W3C XML and HTML recommendations. In this approach, every possible newline character is converted internally to a common newline (which one does not really matter since it is an internal operation just for rendering). In other words, the text system can correctly treat the character as a newline, regardless of the input's actual encoding.
Issues
Character unificationHan unification
Main article: Han unification

The Ideographic Research Group (IRG) is tasked with advising the Consortium and ISO regarding Han unification, or Unihan, especially the further addition of CJK unified and compatibility ideographs to the repertoire. The IRG is composed of experts from each region that has historically used Chinese characters. However, despite the deliberation within the committee, Han unification has consistently been one of the most contested aspects of The Unicode Standard since the genesis of the project.[95]

Existing character set standards such as the Japanese JIS X 0208 (encoded by Shift JIS) defined unification criteria, meaning rules for determining when a variant Chinese character is to be considered a handwriting/font difference (and thus unified), versus a spelling difference (to be encoded separately). Unicode's character model for CJK characters was based on the unification criteria used by JIS X 0208, as well as those developed by the Association for a Common Chinese Code in China.[96]

Due to the standard's principle of encoding semantic instead of stylistic variants, Unicode has received criticism for not assigning code points to certain rare and archaic kanji variants, possibly complicating processing of ancient and uncommon Japanese names. Since it places particular emphasis on Chinese, Japanese and Korean sharing many characters in common, Han unification is also sometimes perceived as treating the three as the same thing.[97] Regional differences in the expected forms of characters, in terms of typographical conventions and curricula for handwriting, do not always fall along language boundaries: although Hong Kong and Taiwan both write Chinese languages using Traditional Chinese characters, the preferred forms of characters differ between Hong Kong and Taiwan in some cases.[98]

Less-frequently-used alternative encodings exist, often predating Unicode, with character models differing from this paradigm, aimed at preserving the various stylistic differences between regional and/or nonstandard character forms. One example is the TRON Code favored by some users for handling historical Japanese text, though not widely adopted among the Japanese public. Another is the CCCII encoding adopted by library systems in Hong Kong, Taiwan and the United States. These have their own drawbacks in general use, leading to the Big5 encoding (introduced in 1984, four years after CCCII) having become more common than CCCII outside of library systems.[99] Although work at Apple based on Research Libraries Group's CJK Thesaurus, which was used to maintain the EACC variant of CCCII, was one of the direct predecessors of Unicode's Unihan set, Unicode adopted the JIS-style unification model.[96]

The earliest version of Unicode had a repertoire of fewer than 21,000 Han characters, largely limited to those in relatively common modern usage. As of version 17.0, the standard now encodes more than 101,000 Han characters, and work is continuing to add thousands more—largely historical and dialectal variant characters used throughout the Sinosphere.

Modern typefaces provide a means to address some of the practical issues in depicting unified Han characters with various regional graphical representations. The 'locl' OpenType table allows a renderer to select a different glyph for each code point based on the text locale.[100] The Unicode variation sequences can also provide in-text annotations for a desired glyph selection; this requires registration of the specific variant in the Ideographic Variation Database.
Italic or cursive characters in Cyrillic
Various Cyrillic characters shown with upright, oblique, and italic alternate forms

If the appropriate glyphs for characters in the same script differ only in the italic, Unicode has generally unified them, as can be seen in the comparison among a set of seven characters' italic glyphs as typically appearing in Russian, traditional Bulgarian, Macedonian, and Serbian texts at right, meaning that the differences are displayed through smart font technology or manually changing fonts. The same OpenType 'locl' technique is used.[101]
Localised case pairs

For use in the Turkish alphabet and Azeri alphabet, Unicode includes a separate dotless lowercase I (ı) and a dotted uppercase I (İ). However, the usual ASCII letters are used for the lowercase dotted i and the uppercase dotless I, matching how they are handled in the earlier ISO 8859-9. As such, case-insensitive comparisons for those languages have to use different rules than case-insensitive comparisons for other languages using the Latin script.[102][103] This can have security implications if, for example, sanitization code or access control relies on case-insensitive comparison.[103]

By contrast, the Icelandic eth (ð), the barred D (đ) and the retroflex D (ɖ), which usually[note 4] look the same in uppercase (Đ), are given the opposite treatment, and encoded separately in both letter-cases (in contrast to the earlier ISO 6937, which unifies the uppercase forms). Although it allows for case-insensitive comparison without needing to know the language of the text, this approach also has issues, requiring security measures relating to homoglyph attacks.[104]
Diacritics on lowercase I
Localised forms of the letter í (I with acute accent)

Whether the lowercase letter I is expected to retain its tittle when a diacritic applies also depends on local conventions.
Security

Unicode has a large number of homoglyphs, many of which look very similar or identical to ASCII letters. Substitution of these can make an identifier or URL that looks correct, but directs to a different location than expected.[105] Additionally, homoglyphs can also be used for manipulating the output of natural language processing (NLP) systems.[106] Mitigation requires disallowing these characters, displaying them differently, or requiring that they resolve to the same identifier;[107] all of this is complicated due to the huge and constantly changing set of characters.[108][109]

A security advisory was released in 2021 by two researchers, one from the University of Cambridge and the other from the University of Edinburgh, in which they assert that the BiDi marks can be used to make large sections of code do something different from what they appear to do. The problem was named "Trojan Source".[110] In response, code editors started highlighting marks to indicate forced text-direction changes.[111]

The UTF-8 and UTF-16 encodings do not accept all possible sequences of code units. Implementations vary in what they do when reading an invalid sequence, which has led to security bugs.[112][113]
Mapping to legacy character sets

Unicode was designed to provide code-point-by-code-point round-trip format conversion to and from any preexisting character encodings, so that text files in older character sets can be converted to Unicode and then back and get back the same file, without employing context-dependent interpretation. That has meant that inconsistent legacy architectures, such as combining diacritics and precomposed characters, both exist in Unicode, giving more than one method of representing some text. This is most pronounced in the three different encoding forms for Korean Hangul. Since version 3.0, any precomposed characters that can be represented by a combined sequence of already existing characters can no longer be added to the standard to preserve interoperability between software using different versions of Unicode.

Injective mappings must be provided between characters in existing legacy character sets and characters in Unicode to facilitate conversion to Unicode and allow interoperability with legacy software. Lack of consistency in various mappings between earlier Japanese encodings such as Shift-JIS or EUC-JP and Unicode led to round-trip format conversion mismatches, particularly the mapping of the character JIS X 0208 '～' (1-33, WAVE DASH), heavily used in legacy database data, to either U+FF5E ～ FULLWIDTH TILDE (in Microsoft Windows) or U+301C 〜 WAVE DASH (other vendors).[114]

Some Japanese computer programmers objected to Unicode because it requires them to separate the use of U+005C \ REVERSE SOLIDUS (backslash) and U+00A5 ¥ YEN SIGN, which was mapped to 0x5C in JIS X 0201, and a lot of legacy code exists with this usage.[115] (This encoding also replaces tilde '~' 0x7E with macron '¯', now 0xAF.) The separation of these characters exists in ISO 8859-1, from long before Unicode.
Indic scripts
Further information: Tamil All Character Encoding

Indic scripts such as Tamil and Devanagari are each allocated only 128 code points, matching the ISCII standard. The correct rendering of Unicode Indic text requires transforming the stored logical order characters into visual order and the forming of ligatures (also known as conjuncts) out of components. Some local scholars argued in favor of assignments of Unicode code points to these ligatures, going against the practice for other writing systems, though Unicode contains some Arabic and other ligatures for backward compatibility purposes only.[116][117][118] Encoding of any new ligatures in Unicode will not happen, in part, because the set of ligatures is font-dependent, and Unicode is an encoding independent of font variations. The same kind of issue arose for the Tibetan script in 2003 when the Standardization Administration of China proposed encoding 956 precomposed Tibetan syllables,[119] but these were rejected for encoding by the relevant ISO committee (ISO/IEC JTC 1/SC 2).[120]

Thai alphabet support has been criticized for its ordering of Thai characters. The vowels เ, แ, โ, ใ, ไ that are written to the left of the preceding consonant are in visual order instead of phonetic order, unlike the Unicode representations of other Indic scripts. This complication is due to Unicode inheriting the Thai Industrial Standard 620, which worked in the same way, and was the way in which Thai had always been written on keyboards. This ordering problem complicates the Unicode collation process slightly, requiring table lookups to reorder Thai characters for collation.[97] Even if Unicode had adopted encoding according to spoken order, it would still be problematic to collate words in dictionary order. E.g., the word แสดง [sa dɛːŋ] "perform" starts with a consonant cluster "สด" (with an inherent vowel for the consonant "ส"), the vowel แ-, in spoken order would come after the ด, but in a dictionary, the word is collated as it is written, with the vowel following the ส.
Combining characters
Main article: Combining character
See also: Unicode normalization § Normalization

Characters with diacritical marks can generally be represented either as a single precomposed character or as a decomposed sequence of a base letter plus one or more non-spacing marks. For example, ḗ (precomposed e with macron and acute above) and ḗ (e followed by the combining macron above and combining acute above) should be rendered identically, both appearing as an e with a macron (◌̄) and acute accent (◌́), but in practice, their appearance may vary depending upon what rendering engine and fonts are being used to display the characters. Similarly, underdots, as needed in the romanization of Indic languages, will often be placed incorrectly.[citation needed] Unicode characters that map to precomposed glyphs can be used in many cases, thus avoiding the problem, but where no precomposed character has been encoded, the problem can often be solved by using a specialist Unicode font such as Charis SIL that uses Graphite, OpenType ('gsub'), or AAT technologies for advanced rendering features.
Anomalies
Main article: Unicode alias names and abbreviations

The Unicode Standard has imposed rules intended to guarantee stability.[121] Depending on the strictness of a rule, a change can be prohibited or allowed. For example, a "name" given to a code point cannot and will not change. But a "script" property is more flexible, by Unicode's own rules. In version 2.0, Unicode changed many code point "names" from version 1. At the same moment, Unicode stated that, thenceforth, an assigned name to a code point would never change. This implies that when mistakes are published, these mistakes cannot be corrected, even if they are trivial (as happened in one instance with the spelling BRAKCET for BRACKET in a character name). In 2006 a list of anomalies in character names was first published, and, as of June 2021, there were 104 characters with identified issues,[122] for example:

    U+034F ͏ COMBINING GRAPHEME JOINER: Does not join graphemes.[122]
    U+2118 ℘ SCRIPT CAPITAL P: This is a small letter. The capital is U+1D4AB 𝒫 MATHEMATICAL SCRIPT CAPITAL P.[123]
    U+A015 ꀕ YI SYLLABLE WU: This is not a Yi syllable, but a Yi iteration mark.
    U+FE18 ︘ PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET: bracket is spelled incorrectly.[124] (Spelling errors are resolved by using Unicode alias names.)

While Unicode defines the script designator (name) to be "Phags_Pa", in that script's character names, a hyphen is added: U+A840 ꡀ PHAGS-PA LETTER KA.[125][126] This, however, is not an anomaly, but the rule: hyphens are replaced by underscores in script designators.[125]
See also

    Comparison of Unicode encodings
    International Components for Unicode (ICU), now as ICU-TC a part of Unicode
    List of binary codes
    List of Unicode characters
    List of XML and HTML character entity references
    Lotus Multi-Byte Character Set (LMBCS), a parallel development with similar intentions
    Open-source Unicode typefaces
    Religious and political symbols in Unicode
    Standards related to Unicode
    Unicode symbol
    Universal Coded Character Set

Notes

"A Unicode Standard Annex (UAX) forms an integral part of The Unicode Standard, but is published as a separate document."[1]
The two-character prefix U+ was chosen as an ASCII approximation of U+228E ⊎ MULTISET UNION.[62]
a code point is an abstract representation of an UCS character by an integer between 0 and 1,114,111 (1,114,112 = 220 + 216 or 17 × 216 = 0x110000 code points)

    Rarely, the uppercase Icelandic eth may instead be written in an insular style (Ꝺ) with the crossbar positioned on the stem, particularly if it needs to be distinguished from the uppercase retroflex D (see African Reference Alphabet).

References

    The Unicode Standard, Version 17.0.0. South San Francisco, California: The Unicode Consortium. 2025-09-09. ISBN 978-1-936213-35-1.

"Unicode Technical Report #28: Unicode 3.2". Unicode Consortium. 2002-03-27. Retrieved 2022-06-23.
Jenkins, John H. (2021-08-26). "Unicode Standard Annex #45: U-source Ideographs". Unicode Consortium. §2.2 The Source Field. Retrieved 2022-06-23.

    "Unicode Character Count V17.0". The Unicode Consortium. 2025-09-10.
    "Unicode 17.0 Versioned Charts Index". The Unicode Consortium. 2025-09-10.
    "Supported Scripts". The Unicode Consortium. 2025-09-10. Retrieved 2025-09-10.

"The Unicode Standard: A Technical Introduction". 2019-08-22. Retrieved 2024-09-11.
"Emoji Counts, v16.0". The Unicode Consortium. Retrieved 2024-09-10.
Becker, Joseph D. (1998-09-10) [1988-08-29]. "Unicode 88" (PDF). Unicode Consortium. Archived (PDF) from the original on 2016-11-25. Retrieved 2016-10-25. "In 1978, the initial proposal for a set of "Universal Signs" was made by Bob Belleville at Xerox PARC. Many persons contributed ideas to the development of a new encoding design. Beginning in 1980, these efforts evolved into the Xerox Character Code Standard (XCCS) by the present author, a multilingual encoding that has been maintained by Xerox as an internal corporate standard since 1982, through the efforts of Ed Smura, Ron Pellar, and others.
Unicode arose as the result of eight years of working experience with XCCS. Its fundamental differences from XCCS were proposed by Peter Fenwick and Dave Opstad (pure 16-bit codes) and by Lee Collins (ideographic character unification). Unicode retains the many features of XCCS whose utility has been proved over the years in an international line of communication multilingual system products."
"Summary Narrative". Unicode. 2006-08-31. Retrieved 2010-03-15.
"History of Unicode Release and Publication Dates". Unicode. Retrieved 2023-03-20.
Searle, Stephen J. "Unicode Revisited". Retrieved 2013-01-18.
"The Unicode Consortium Members". Retrieved 2024-02-12.
"Unicode Bulldog Award". Unicode. Archived from the original on 2023-11-11.
"Supported Scripts". Unicode. Retrieved 2025-09-09.
Otung, Ifiok (2021-01-28). Communication Engineering Principles. John Wiley & Sons. p. 12. ISBN 978-1-119-27407-0.
"Unicode FAQ". Retrieved 2020-04-02.
"Roadmap to the BMP". Unicode Consortium. Retrieved 2018-07-30.
"Roadmaps to Unicode". Unicode. Archived from the original on 2023-12-08.
"Script Encoding Initiative". Script Encoding Initiative. Archived from the original on 2023-03-25.
"About The Script Encoding Initiative". The Unicode Consortium. Retrieved 2012-06-04.
"Scripts to Encode".
"Unicode 6.1 Paperback Available". announcements_at_unicode.org. Retrieved 2012-05-30.
"Enumerated Versions of The Unicode Standard". Retrieved 2025-09-12.

    The Unicode Standard, Version 1.0.0. Mountain View, California: The Unicode Consortium. October 1991.
    "1.0.0/UnicodeData.txt (reconstructed)". 2004. Retrieved 2010-03-16.

    The Unicode Standard, Version 1.0.1. Mountain View, California: The Unicode Consortium. June 1992.
    "Unicode Data 1.0.1". Retrieved 2010-03-16.

    The Unicode Standard, Version 1.1.5. Mountain View, California: The Unicode Consortium. July 1995.
    "Unicode Data 1995". Retrieved 2010-03-16.

    The Unicode Standard, Version 2.0.0. Mountain View, California: The Unicode Consortium. July 1996.
    "Unicode Data-2.0.14". Retrieved 2010-03-16.

    The Unicode Standard, Version 2.1.2. Mountain View, California: The Unicode Consortium. May 1998.
    "Unicode Data-2.1.2". Retrieved 2010-03-16.

    The Unicode Standard, Version 3.0.0. Mountain View, California: The Unicode Consortium. September 1999.
    "Unicode Data-3.0.0". Retrieved 2023-10-02.

    The Unicode Standard, Version 3.1.0. Mountain View, California: The Unicode Consortium. March 2001.
    "Unicode Data-3.1.0". Retrieved 2023-10-02.

    The Unicode Standard, Version 3.2.0. Mountain View, California: The Unicode Consortium. March 2002.
    "Unicode Data-3.2.0". Retrieved 2023-10-02.

    The Unicode Standard, Version 4.0.0. Mountain View, California: The Unicode Consortium. April 2003. ISBN 0-321-18578-1.
    "Unicode Data-4.0.0". Retrieved 2023-10-02.

    The Unicode Standard, Version 4.1.0. Mountain View, California: The Unicode Consortium. March 2004. ISBN 0-321-18578-1.
    "Unicode Data-4.1.0". Retrieved 2010-03-16.

"Named Sequences-4.1.0". Unicode. 2005. Retrieved 2010-03-16.
The Unicode Standard, Version 5.0.0. Mountain View, California: The Unicode Consortium. 2006-07-14. ISBN 0-321-48091-0.
"Unicode Data 5.0.0". Retrieved 2010-03-17.

    The Unicode Standard, Version 5.1.0. Mountain View, California: The Unicode Consortium. 2008-04-04. ISBN 0-321-48091-0.
    "Unicode Data 5.1.0". Retrieved 2010-03-17.

    The Unicode Standard, Version 5.2.0. Mountain View, California: The Unicode Consortium. 2009-10-01. ISBN 978-1-936213-00-9.
    "Unicode Data 5.2.0". Retrieved 2010-03-17.

    The Unicode Standard, Version 6.1.0. Mountain View, California: The Unicode Consortium. 2012-01-31. ISBN 978-1-936213-02-3.
    "Unicode Data 6.0.0". Retrieved 2010-10-11.

"Unicode 6.0 Emoji List". emojipedia.org. Retrieved 2022-09-21.

    The Unicode Standard, Version 6.1.0. Mountain View, California: The Unicode Consortium. 2012-01-31. ISBN 978-1-936213-02-3.
    "Unicode Data 6.1.0". Retrieved 2012-01-31.

    The Unicode Standard, Version 6.2.0. Mountain View, California: The Unicode Consortium. 2012-09-26. ISBN 978-1-936213-07-8.
    "Unicode Data 6.2.0". Retrieved 2012-09-26.

    The Unicode Standard, Version 6.3.0. Mountain View, California: The Unicode Consortium. 2013-09-30. ISBN 978-1-936213-08-5.
    "Unicode Data 6.3.0". Retrieved 2013-09-30.

    The Unicode Standard, Version 7.0.0. Mountain View, California: The Unicode Consortium. 2014-06-16. ISBN 978-1-936213-09-2.
    "Unicode Data 7.0.0". Retrieved 2014-06-15.

    The Unicode Standard, Version 8.0.0. Mountain View, California: The Unicode Consortium. 2015-06-17. ISBN 978-1-936213-10-8.
    "Unicode Data 8.0.0". Retrieved 2015-06-17.

The Unicode Standard, Version 8.0.0. Mountain View, California: The Unicode Consortium. 2015-06-17. ISBN 978-1-936213-10-8.
The Unicode Standard, Version 9.0.0. Mountain View, California: The Unicode Consortium. 2016-06-21. ISBN 978-1-936213-13-9.

    The Unicode Standard, Version 9.0.0. Mountain View, California: The Unicode Consortium. 2016-06-21. ISBN 978-1-936213-13-9.
    "Unicode Data 9.0.0". Retrieved 2016-06-21.

Lobao, Martim (2016-06-07). "These Are The Two Emoji That Weren't Approved For Unicode 9 But Which Google Added To Android Anyway". Android Police. Retrieved 2016-09-04.
The Unicode Standard, Version 10.0.0. Mountain View, California: The Unicode Consortium. 2017-06-20. ISBN 978-1-936213-16-0.
The Unicode Standard, Version 11.0.0. Mountain View, California: The Unicode Consortium. 2018-06-05. ISBN 978-1-936213-19-1.
The Unicode Standard, Version 12.0.0. Mountain View, California: The Unicode Consortium. 2019-03-05. ISBN 978-1-936213-22-1.
"Unicode Version 12.1 released in support of the Reiwa Era". The Unicode Blog. Retrieved 2019-05-07.

    The Unicode Standard, Version 13.0.0. Mountain View, California: The Unicode Consortium. 2020-03-10. ISBN 978-1-936213-26-9.
    "Announcing The Unicode Standard, Version 13.0". The Unicode Blog. Retrieved 2020-03-11.

"The Unicode Standard, Version 13.0– Core Specification Appendix C" (PDF). Unicode Consortium. Retrieved 2020-03-11.

    The Unicode Standard, Version 14.0.0. Mountain View, California: The Unicode Consortium. 2021-09-14. ISBN 978-1-936213-29-0.
    "Announcing The Unicode Standard, Version 14.0".

The Unicode Standard, Version 15.0.0. Mountain View, California: The Unicode Consortium. 2022-09-13. ISBN 978-1-936213-32-0.

    The Unicode Standard, Version 15.1.0. South San Francisco, California: The Unicode Consortium. 2023-09-12. ISBN 978-1-936213-33-7.

The Unicode Standard, Version 16.0.0. South San Francisco, California: The Unicode Consortium. 2024-09-10. ISBN 978-1-936213-34-4.
The Unicode Standard, Version 17.0.0. South San Francisco, California: The Unicode Consortium. 2025-09-09. ISBN 978-1-936213-35-1.
"Glossary of Unicode Terms". Retrieved 2010-03-16.
"2.4 Code Points and Characters". The Unicode Standard Version 16.0 – Core Specification. 2024.
"3.4 Characters and Encoding". The Unicode Standard, Version 16.0. 2024.
"Re: Origin of the U+nnnn notation". Unicode Mail List Archive (Mailing list). 2005-11-08.
"Appendix A: Notational Conventions". The Unicode Standard. Unicode Consortium. September 2024.
"Conformance". The Unicode Standard (6.0 ed.). Mountain View, California, US: The Unicode Consortium. 3.9 Unicode Encoding Forms. ISBN 978-1-936213-01-6. "Each encoding form maps the Unicode code points U+0000..U+D7FF and U+E000..U+10FFFF"
"Unicode Character Encoding Stability Policy". Retrieved 2010-03-16.
"Properties". Retrieved 2025-09-21.
"Unicode Character Encoding Model". Retrieved 2023-09-12.
"Unicode Named Sequences". Retrieved 2025-09-21.
"Unicode Name Aliases". Retrieved 2025-09-21.
"JanaSanskritSans". Archived from the original on 2011-07-16.
CWA 13873:2000 – Multilingual European Subsets in ISO/IEC 10646-1 CEN Workshop Agreement 13873
Kuhn, Markus (1998). "Multilingual European Character Set 2 (MES-2) Rationale". University of Cambridge. Retrieved 2023-03-20.
"DIN 91379:2022-08: Characters and defined character sequences in Unicode for the electronic processing of names and data exchange in Europe, with CD-ROM". Beuth Verlag. Retrieved 2022-08-21.
"UTF-8, UTF-16, UTF-32 & BOM". Unicode.org FAQ. Retrieved 2016-12-12.
The Unicode Standard, Version 6.2. The Unicode Consortium. 2013. p. 561. ISBN 978-1-936213-08-5.
Davis, Mark (2008-05-05). "Moving to Unicode 5.1". Official Google Blog. Archived from the original on 2025-04-01. Retrieved 2025-04-12.
"Usage Survey of Character Encodings broken down by Ranking". W3Techs. Retrieved 2025-04-12.
"Usage statistics of US-ASCII for websites". W3Techs. Retrieved 2020-11-01.
B. Curtin (July 1999). Internationalization of the File Transfer Protocol. doi:10.17487/RFC2640. RFC 2640. Retrieved 2025-04-12.
H. Alvestrand (January 1998). IETF Policy on Character Sets and Languages. doi:10.17487/RFC2277. BCP 18. RFC 2277. Archived from the original on 2023-01-23. Retrieved 2025-04-12.
Pike, Rob (2003-04-30). "UTF-8 history".
"ISO/IEC JTC1/SC 18/WG 9 N" (PDF). Archived (PDF) from the original on 2025-01-22. Retrieved 2025-04-12.
Hedley, Jonathan (2009). "Unicode Lookup". Archived from the original on 2025-03-30. Retrieved 2025-04-12.
Milde, Benjamin (2025). "Unicode Character Recognition". Archived from the original on 2025-04-02.
J. Klensin; Y. Ko (July 2007). Overview and Framework for Internationalized Email. doi:10.17487/RFC4952. RFC 4952. Retrieved 2022-08-17.
J. Klensin; Y. Ko (February 2012). Overview and Framework for Internationalized Email. doi:10.17487/RFC6530. RFC 6530. Retrieved 2022-08-17.
J. Yao; W. Mao (February 2012). SMTP Extension for Internationalized Email. doi:10.17487/RFC6531. RFC 6531. Retrieved 2022-08-17.
A. Yang; S. Steele; N. Freed (February 2012). Internationalized Email Headers. doi:10.17487/RFC6532. RFC 6532. Retrieved 2022-08-17.
C. Newman; A. Gulbrandsen; A. Melnikov (June 2008). Internet Message Access Protocol Internationalization. doi:10.17487/RFC5255. RFC 5255. Retrieved 2022-08-17.
R. Gellens; C. Newman (February 2010). POP3 Support for UTF-8. doi:10.17487/RFC5721. RFC 5721. Retrieved 2022-08-17.
Wood, Alan (2005-09-13). "Setting up Windows Internet Explorer 5, 5.5 and 6 for Multilingual and Unicode Support: Options for enabling Unicode in Internet Explorer 5, 5.5 and 6: Fonts (IE 5, 5.5 and 6)". Alan Wood. Archived from the original on 2025-01-20. Retrieved 2025-04-12.
"Extensible Markup Language (XML) 1.1 (Second Edition)". World Wide Web Consortium. 2006-09-29. Archived from the original on 2025-04-05. Retrieved 2025-04-12.
Bigelow, Charles; Holmes, Kris (September 1993). "The design of a Unicode font" (PDF). Electronic Publishing. 6 (3): 292. ISSN 0894-3982. Archived (PDF) from the original on 2025-02-16. Retrieved 2025-04-12.
"FAQs: Fonts and keyboards: Fonts and Unicode". Unicode Consortium. Archived from the original on 2025-03-06. Retrieved 2025-04-12.
A Brief History of Character Codes, Steven J. Searle, originally written 1999, last updated 2004
"Appendix E: Han Unification History". The Unicode Standard Version 16.0 – Core Specification. Unicode Consortium. 2024.
Topping, Suzanne (2013-06-25). "The secret life of Unicode". IBM. Archived from the original on 2013-06-25. Retrieved 2023-03-20.
Lu, Qin (2015-06-08). "The Proposed Hong Kong Character Set" (PDF). ISO/IEC JTC1/SC2/WG2/IRG N2074.
Wittern, Christian (1995-05-01). "Chinese character codes: an update". International Research Institute for Zen Buddhism / Hanazono University. Archived from the original on 2004-10-12.
"Noto CJK fonts". Noto Fonts. 2023-02-18. "Select this deployment format if your system supports variable fonts and you prefer to use only one language, but also want full character coverage or the ability to language-tag text to use glyphs that are appropriate for the other languages (this requires an app that supports language tagging and the OpenType 'locl' GSUB feature)."
Preuss, Ingo. "OpenType Feature: locl – Localized Forms". preusstype.com.
"Case Folding Properties". Unicode Character Database. Unicode Consortium. 2025-07-30.
"Regular expression options § Compare using the invariant culture". .NET fundamentals documentation. Microsoft. 2023-05-12.
"confusablesSummary.txt". Unicode Security Mechanisms for UTS #39. Unicode Consortium. 2023-08-11.
"UTR #36: Unicode Security Considerations". Unicode.
Boucher, Nicholas; Shumailov, Ilia; Anderson, Ross; Papernot, Nicolas (2022). "Bad Characters: Imperceptible NLP Attacks". 2022 IEEE Symposium on Security and Privacy (SP). San Francisco, CA, US: IEEE. pp. 1987–2004. arXiv:2106.09898. doi:10.1109/SP46214.2022.9833641. ISBN 978-1-66541-316-9. S2CID 235485405.
Engineering, Spotify (2013-06-18). "Creative usernames and Spotify account hijacking". Spotify Engineering. Retrieved 2023-04-15.
Wheeler, David A. (2020). Initial Analysis of Underhanded Source Code (Technical report). p. 4–1–4–10. JSTOR resrep25332.7.
"UTR #36: Unicode Security Considerations". Unicode. Retrieved 2022-06-27.
Boucher, Nicholas; Anderson, Ross. "Trojan Source: Invisible Vulnerabilities" (PDF). Retrieved 2021-11-02.
"Visual Studio Code October 2021". code.visualstudio.com. Retrieved 2021-11-11.
Dittert, Dominique (2024-09-06). "From Unicode to Exploit: The Security Risks of Overlong UTF-8 Encodings". Retrieved 2024-12-26.
Boone, Kevin. "UTF-8 and the problem of over-long characters". Retrieved 2024-12-26.
AFII contribution about WAVE DASH, "An Unicode vendor-specific character table for japanese". 2011-04-22. Archived from the original on 2011-04-22. Retrieved 2019-05-20.
ISO 646-* Problem Archived 2019-04-23 at the Wayback Machine, Section 4.4.3.5 of Introduction to I18n, Tomohiro Kubota, 2001
"Arabic Presentation Forms-A" (PDF). Retrieved 2010-03-20.
"Arabic Presentation Forms-B" (PDF). Retrieved 2010-03-20.
"Alphabetic Presentation Forms" (PDF). Retrieved 2010-03-20.
"Proposal on Tibetan BrdaRten Characters Encoding for ISO/IEC 10646 in BMP" (PDF). 2002-12-02.
Umamaheswaran, V. S. (2003-11-07). "Resolutions of WG 2 meeting 44" (PDF). Resolution M44.20.
"Character Encoding Stability". Unicode. Archived from the original on 2024-01-01.
"Unicode Technical Note #27: Known Anomalies in Unicode Character Names". Unicode. 2021-06-14.
"Unicode chart: "actually this has the form of a lowercase calligraphic p, despite its name"" (PDF).
"Misspelling of BRACKET in character name is a known defect" (PDF).
"Unicode Standard Annex #24: Unicode Script Property". The Unicode Consortium. 2021. 2.2 Relation to ISO 15924 Codes. Retrieved 2022-04-29.

    "Scripts.txt". The Unicode Consortium. 2025. Retrieved 2025-09-21.

Further reading

    Julie D. Allen. The Unicode Standard, Version 6.0, The Unicode Consortium, Mountain View, 2011, ISBN 9781936213016, (Unicode 6.0.0).
    The Complete Manual of Typography, James Felici, Adobe Press; 1st edition, 2002. ISBN 0-321-12730-7
    The Unicode Standard, Version 3.0, The Unicode Consortium, Addison-Wesley Longman, Inc., April 2000. ISBN 0-201-61633-5
    The Unicode Standard, Version 4.0, The Unicode Consortium, Addison-Wesley Professional, 27 August 2003. ISBN 0-321-18578-1
    The Unicode Standard, Version 5.0, Fifth Edition, The Unicode Consortium, Addison-Wesley Professional, 27 October 2006. ISBN 0-321-48091-0
    Unicode Demystified: A Practical Programmer's Guide to the Encoding Standard, Richard Gillam, Addison-Wesley Professional; 1st edition, 2002. ISBN 0-201-70052-2
    Unicode Explained, Jukka K. Korpela, O'Reilly; 1st edition, 2006. ISBN 0-596-10121-X
    Unicode: A Primer, Tony Graham, M&T books, 2000. ISBN 0-7645-4625-2.

    Haralambous, Yannis; Martin Dürst (2019). "Unicode from a Linguistic Point of View". In Haralambous, Yannis (ed.). Proceedings of Graphemics in the 21st Century, Brest 2018. Brest: Fluxus Editions. pp. 167–183. doi:10.36824/2018-graf-hara1. ISBN 978-2-9570549-1-6.

External links
Unicode
at Wikipedia's sister projects

    Media from Commons
    Textbooks from Wikibooks

    Unicode, Inc.
        Unicode Technical Site
            The Unicode Standard
                Unicode Character Code Charts
                Unicode Character Name Index
    Alan Wood's Unicode Resources – contains lists of word processors with Unicode capability; fonts and characters are grouped by type; characters are presented in lists, not grids.
    Unicode BMP Fallback Font – displays the Unicode 6.1 value of any character in a document, including in the Private Use Area, rather than the glyph itself.
    The World's Writing Systems, all 293 known writing systems with their Unicode status (128 not yet encoded as of June 2024)

    vte

Unicode
Unicode 

    Unicode Consortium ISO/IEC 10646 (Universal Character Set) Versions

Code points 

    Block
        List Universal Character Set Character charts Character property Plane Private Use Area

Characters  
Special purpose 

    BOM Combining grapheme joiner Left-to-right mark / Right-to-left mark Soft hyphen Variant form Word joiner Zero-width joiner Zero-width non-joiner Zero-width space

Lists   

    Characters CJK Unified Ideographs Combining character Duplicate characters Numerals Scripts Spaces Symbols Halfwidth and fullwidth Alias names and abbreviations Whitespace characters

Processing  
Algorithms  

    Bidirectional text Collation
        ISO/IEC 14651 Equivalence Variation sequences International Ideographs Core

Comparison of encodings 

    BOCU-1 CESU-8 Punycode SCSU UTF-1 UTF-7 UTF-8 UTF-16/UCS-2 UTF-32/UCS-4 UTF-EBCDIC

On pairs of
code points 

    Combining character Compatibility characters Duplicate characters Equivalence Homoglyph Precomposed character
        list Z-variant Variation sequences Regional indicator symbol Emoji skin color

Usage   

    Domain names (IDN) Email Fonts HTML
        entity references numeric references Input International Ideographs Core

Related standards   

    Common Locale Data Repository (CLDR) GB 18030 ISO/IEC 8859 DIN 91379 ISO 15924

Related topics  

    Anomalies ConScript Unicode Registry Ideographic Research Group International Components for Unicode People involved with Unicode Han unification

Scripts and symbols in Unicode
Common and
inherited scripts   

    Combining marks Diacritics Punctuation marks Spaces Numbers

Modern scripts  

    Adlam Arabic Armenian Balinese Bamum Batak Bengali Beria Erfe Bopomofo Braille Buhid Burmese Canadian Aboriginal Chakma Cham Cherokee CJK Unified Ideographs (Han) Cyrillic Deseret Devanagari Garay Geʽez Georgian Greek Gujarati Gunjala Gondi Gurmukhi Gurung Khema Hangul Hanifi Rohingya Hanja Hanunuoo Hebrew Hiragana Javanese Kanji Kannada Katakana Kayah Li Khmer Kirat Rai Lao Latin Lepcha Limbu Lisu (Fraser) Lontara Malayalam Masaram Gondi Mende Kikakui Medefaidrin Miao (Pollard) Mongolian Mru N'Ko Nag Mundari New Tai Lue Nüshu Nyiakeng Puachue Hmong Odia Ol Chiki Ol Onal Osage Osmanya Pahawh Hmong Pau Cin Hau Pracalit (Newa) Ranjana Rejang Samaritan Saurashtra Shavian Sinhala Sorang Sompeng Sundanese Sunuwar Syriac Tagbanwa Tai Le Tai Tham Tai Viet Tai Yo Tamil Tangsa Telugu Thaana Thai Tibetan Tifinagh Tirhuta Tolong Siki Toto Vai Wancho Warang Citi Yi

Ancient and
historic scripts    

    Ahom Anatolian hieroglyphs Ancient North Arabian Avestan Bassa Vah Bhaiksuki Brāhmī Carian Caucasian Albanian Coptic Cuneiform Cypriot Cypro-Minoan Dives Akuru Dogra Egyptian hieroglyphs Elbasan Elymaic Glagolitic Gothic Grantha Hatran Imperial Aramaic Inscriptional Pahlavi Inscriptional Parthian Kaithi Kawi Kharosthi Khitan small script Khojki Khudawadi Khwarezmian (Chorasmian) Linear A Linear B Lycian Lydian Mahajani Makasar Mandaic Manichaean Marchen Meetei Mayek Meroitic Modi Multani Nabataean Nandinagari Ogham Old Hungarian Old Italic Old Permic Old Persian cuneiform Old Sogdian Old Turkic Old Uyghur Palmyrene ʼPhags-pa Phoenician Psalter Pahlavi Runic Sharada Siddham Sidetic Sogdian South Arabian Soyombo Sylheti Nagri Tagalog (Baybayin) Takri Tangut Todhri Tulu Tigalari Ugaritic Vithkuqi Yezidi Zanabazar Square

Notational scripts  

    Duployan SignWriting

Symbols, emojis 

    Cultural, political, and religious symbols Currency Control Pictures Mathematical operators and symbols
        Glossary Phonetic symbols (including IPA) Emoji

     Category: Unicode  Category: Unicode blocks

    vte

Character encodings
    

    

    

    

    


    

    

    

    

    

    

    

    

    

    

    

    

Authority control databases Edit this at Wikidata
    

    

    

Categories:

    UnicodeCharacter encodingDigital typography

    This page was last edited on 5 December 2025, at 15:07 (UTC).
    Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

