# Automate Everything from @codecaviar
# Level: Basic
# Updated: 2020-11-07

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

def letter_removal(input_string, remove_count):
    """
    Given lower case string, remove a specific number of characters:
    First remove all letter 'a', followed by letter 'b', then 'c',
    etc...remove the leftmost character first.

    Parameters
    ----------
    input_string: {string} lower case string
    remove_count: {int} integer of characters to remove

    Returns
    -------
    {string}: output after removing specific number of characters

    Example
    -------
    >>> letter_removal('hxehmvkybeklnj', 5)
    xmvkyklnj
    >>> letter_removal('cccaabababaccbc', 9)
    cccccc
    >>> letter_removal('mtapctrsrnrcjhdqfprvsfzgyhovglvovueyegygcrknjvwnaojkvuxpiyjwrfljfllixxhdxruouzkkyvpzertomryvughzbzwfijjinzfhxjrxcpvqmmpfpijfqwznvijxzhysdbphfklvfzwrebmlvcmalifckfzjprkktyojfnaxiallldfjnuarzljdoqyusgjcgoiticqnbftbvslgmgaosbkrizajmczuibhbguqgxbnshxpfnfpayogdlhylsrobyiwlzgedirrptafwwglhvneuruexsukalwdhdnlffygsdkcpqqsjoenvddgfpzhgsjegsxeuifdfaywkyhzdyxolvqbchxmjoxpylqlawwmgesqjultgzaealnslitoyxusuykizjxzwpzkkfpgjmhohhwjgmbekxhuxsynxktrlwnogrsxshhofzqtsbbutwuhflezksljjyyzoqohmwlsgclcggxkvfdspsoyoamgkpkldhyoofcdnfbrytjqnrhcxnevositqpruiwdcnexzijftddxjctlgwntceuyaufznlhiipwdxbaukbeftzjjytddweudpwwvbxohtfgjlvlnjhketgcyldatcsndopldvgsdtwuilffuwpzzxczirtagtecbsfhshwhpwoxcscaagkfbmcqoiptermprnchahjamaedgedavriycpfviiezhpfgwsjucksjvdbmzkwaudvgjdctlywvqvrjlfoneebzdmodmkpljhsvpkhgbbwtzcstdkgtezkxxjlpejumwkdlctaujljlwqawgzglmohvrdlvfkxclcgsegwaszkixjcxkdaybkzasizautlryrfcuetesulgkpxixfnbbbejdvqdxflflvchbnqtkmarkdwezaocssjarzanzxdtzyhbyhlljqbvyyvgmsitfcwhesgwtzoeqlflklxltruddohknalxtasawwutcrlnvriuchljyiqsahjteqrbakhxiokokhylmvhdbfdvgopkcrdzmnigstbaiehiwnrjgoqfjpinkgtxxkkxvlxmdamlxdmpulodoyujyfcvtiefqwhlcvlaltrqhpplfclvnaccebrxfeziursuigvuercgunsqzwsvskbordmrdvlupayublwtrnxhystlqakhzuztqcvlwqxhphzsmjsnutacgxazxbumtmglngivkdmqaxocjhsxvotynomtrzwhaydlwvskqivqhchvucchifsumydpumsyfmrwombaufzemosxsobtnfukatsgqypvvfunfcuzhdjmtndbvejscspmcbjhrokwagbhytqiibfwpbwvjjilbuhpdiiluyiajqdmxxsgmvdoahfpclfxbtcfeyxxjynfrcdjdxxxonioxxvvwabqhcrdvenqsrzylaprxlyxbwefyfabfnomhzhteaeqxeokdlnieniamuvejoazupmenqaynkoyrmaliojrdhvpirfrzobfafxokqqagujnigzbzvdwtwygrwjryzdbhmewisirbasncvzqsmliohmixbartuelizmlkyexxdopgsfhhzcszqfgqjrwbuyecanuhxptbltmrbxfiqntnbjpyriwpsajoocctjrkqqdpfztighvvqyriwqtreoqgfhfvfjtoexibojylcpvymbacjuadmrkaugcecacufcqavbjwhqaoohglrfwdpdaizyvrhblzopittojyohtjyhxuykzvwxszyqlclobtyygzvmyasfsxyowyminljxoiwlanijegsrssuoijjtchxtnawkqrkladlmshiwcyedhwpgxbwqeqsjxpsmrxznqrqhwudzbrbglnwyqjpjitupdbvuzocitktgqnhaxkiyfhrwthhwihhxhiiiaheaficfgfjyqiiqprgbxksfqxipifdjnjtfkaklfibgrkixpcbzkutysclmsmdwxlczjzltgnomxkvcdhhhqwifdebjkieuzfntulttvutjusgbiolegndlegadosvlhymqafjcezdnxyeunjwiylomxlrohbzhqvrlisqviggnxsesubksvnoanpltqahdbteelnmkqjqsuuwluvblhjfbehyrwqoghqqhxksvuavynhgtkwrncgcwwnmigqthbxoyuoqsxrmqurcwqaonugqvosvnuaelgolpnhlwqwnpvjznfahvthwvornuxgkkbjdgdnqsbokvqfdfzqtjrovtlpvvygzziqxnsjlwjoyugwibmkptpwxlhbrjrqczgogelolpvrraycrjxghxfevhunxdxddkqrdyizjqdzuudnmlllleqbdqgrvfgpkmkwnyklhvgsmvxbnaoyaxssmnzaaqqqzmxqxbtpqonbgkeujybxbhhsycvoyeavsvshvmjuusvnafvjmjsxymiwgnpldokogswzpmowgmbzxyjhfyjfyporgkvcubvzyiwznynlvvlqbvofyebrsjngsmgjgxypolzquyxgrkbikyfqwbakmuoyizezrxjduecqsjvqgkdzltwdesiqxervybiauglfofowyaldvgoivobfkjpatnvjmhewularungifhkrgqxfquernvlizsehhdnxbklkiscnaekomlnakkrakloygkflgmcjnygjkrjyvusrtwoekfnqkztwfpjtcfzrkwnexrdvgrdjpwynzvmgkgycukohflskixewjuijjhrbhskjnbvfglqwkwlfjpqylvecqyfafbetztzwyeruabvyxxcwibgcuuqtxpxgqojxlpxfrpvdmlrdifvmkxubxgjnvrmxtprofvudrziaivgxslziezfbgeenyevpplkomkzoaoxetvefeatwalsdrmwwzdzeejbjxjghiaebfrmqtriepgauvrhymvmcfhwvjmpjsutioglnbqxtpzzexcrsbbugrkjllydjhcbqrirolgkdvfpmfvuhuldmirjtkhpxgiacsumqmrcjmnugvwgmfjpbktgyovfngczxvigmorjxixaszcdsyfgfxecxljiyxvwgkrijlwmtjcwoxkqeupkmtcnbydoqwkvvodrmrwnsytzwyvafwisffjwhifvurorlievhlmdxqsjtqxezykteegljdnvyrclyyhqybarcflvoughiqabkdyswhzbekdrrtsgnnzdtnbprugccpapzufzktmaszvsccqpqgiwjzbocazqvjogebuvrsnorgmfquwpsdmscllptxpdtkbuujusitxlmryoxdovfhnuqvmgiiocqzizkcmnnhmbyjqebkmfzfnxsjaeszlywnfrwuvmxtjybzzxxtpntrnsyawmdwagevdmzduqotryovzlumidveoflazlelsquhstimmfcesyvqckesntwkfhsdfqkgjxbgtartztbinyopboxcyentkqyytoqrsiafbmehteijvjjubillnhjlidxfvgzoagdjfzwdiryoiswbrpmtzecuemyxjruxquyemcjvchiprliynqjpmuzbzqwbrbnkmniyrzxglqovieklxffymahdvebrbbxojnwyephljflmrutcnnqeehypvlxcyrrhmvictjtfnlmtndcgpkfzzafsmgvhjbkeqpiwnvhiuhldyqzdekxknvjliejhjllgaqkibdpishnutdxmjeovqzercegwbaouvxgxdianrkveihcczgxqxxvntxwodtnkmejuvmtuacwjecllhehoxupycoqoezwoefravmgumbghpbfmavepotsokyvmtjrydhqkdkdnrdrtbwqfyvhcuuytjgescvwhcnpbmzbrodhayehnaklkctiebxdkahdipdlrzndnkosqezpcfklvtzqjspkzzkjgbxedarsngwtirvhpobasfwwacizqplobgtlmnphcwarrqjyztaaamtvsmwilb', 2652)
    ttsvszyvvvuyyvwvuxywxxxuuzyvztyvuzzwzxxvwzvxzysvzwvztyxuzyusttvsszzuuxsxyysywztwwvuuxsuwyssvzssxuywyzyxvxxywwsutzstyxusuyzxzwzwxuxsyxtwsxsztsutwuzsyyzwsxvssyyytxvstuwxztxtwtuyuzwxutzytwuwwvxtvtytsvstwuuwzzxzttsswwxstvyvzwsusvzwuvtywvvzsvwtzsttzxxuwtuwwzvvxswszxxyzszutyutsuxxvxvtwzsszzxtzyyvyyvstwswtzxtuxtswwutvuystxyvvzstwtxxxvxxuyuyvtwvtvxzusuvuuszwsvsvuyuwtxystzuztvwxzssutxzxutvxsxvtytzwywvsvvusuyusywuzsxstutsyvvuuztvsswytwwvuuyxxsvxtyxxyxxxxxvvwvszyxyxwyztxuvzuyyrrvrrzxuzzvwtwyrwryzwsrsvzsxrtuzyxxszszrwuyuxttrxtyrwstrztvvyrwtrvtxyvyuruuvwrwzyvrzttytyxuyzvwxszytyyzvyssxywyxwsrssutxtwrswywxwsxsrxzrwuzrwytuvuzttxyrwtwxyrxsxtrxzutysswxzztxvwuztuttvutussvyzxyuwyxrzvrsvxssusvttsuuwuvyrwxsvuvytwrwwtxyusxrurwuvsvuwwvzvtwvruxsvztrvtvvyzzxswyuwtwxrrzvrryrxxvuxxryzzuurvwyvsvxyxsszzxxtuyxsyvyvsvsvuusvvsxywswzwzxyyyrvuvzywzyvvvyrssxyzuyxrywuyzzrxusvztwsxrvyuwyvvtvwururxurvzsxsryyryvusrtwztwtzrwxrvrwyzvyusxwursvwwyvytztzwyruvyxxwuutxxxxrvrvxuxvrxtrvurzvxszzyvzxtvtwsrwwzzxrtruvryvwvsutxtzzxrsuryrrvvuurtxsuruvwtyvzxvrxxszsyxxyxvwrwtwxutywvvrrwsytzwyvwswvurrvxstxzytvyryyyrvuyswzrrtsztruzuztszvswzzvuvrsruwsstxtuuustxryxvuvzzyzxsszywrwuvxtyzzxxttrsywwvzutryvzuvzsustsyvstwsxtrtztyxytyytrstvuxvzzwryswrtzuyxruxuyvryuzzwryrzxvxyvrxwyrutyvxyrrvtttzzsvwvuyzxvsutxvzrwuvxxrvzxxxvtxwtuvtuwxuyzwrvuvtsyvtryrrtwyvuuytsvwzrytxrzszvtzszzxrswtrvswwztwrryzttvsw
    """

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
