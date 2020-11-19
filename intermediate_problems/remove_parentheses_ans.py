# Automate Everything from @codecaviar
# Level: Intermediate
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

# As you progress and problems get harder, there will be many ways of
# producing the correct results. Keep in mind that the answers to
# practice problems should be used as a reference, but are by no means
# the only ways of answering the questions.

import re # use regular expressions

def remove_parentheses(input_str):
    """
    Given a string, remove everything inside parentheses and themselves.
    Don't worry about other brackets such as "[]" or "{}".
    There can be multiple parentheses. The parentheses can be nested.

    Parameters
    ----------
    input_str: {str} initial string with parentheses

    Returns
    -------
    {str}: output string without parentheses or content inside

    Example
    -------
    >>> remove_parentheses("uFvCDQeePDvJlmjEYVtLTP royuXM(taRDOsmdcttKNoDdCWIHU SOj)(oye(qCsYDaM(RllBHJjEWld)cXiw)x(qPRls IemsVRkwk)MmxfIO(KD(dHJGSuduAPtVv(mvEBYmpJ URA)YjhnMoS)fMqkIqsiUbhaWBnEuvPv)TlpQ)BswaBjjyNs(ZATFprKUO(ZgjWA)LAx BAAtAvWQs jg)IADyDt((AIMwtNCtw mdlaDRQ)OGUX(ZtyS(WDhpX)J BD(zx Crpl uqS(vOQKiuBizDBM guWZmGnh)YqEjaArqC F(zExOi)gV)EQSGk x QfbtZaS)p )rRkgB(RLa)Vs GwhBsR lL(tIU(YahkMcpHjUMWf VgtiOEATE)k jOTM b vLT)(cQQvCfhA)xdSXIdUJo")
    'uFvCDQeePDvJlmjEYVtLTP royuXMBswaBjjyNsIADyDtrRkgBVs GwhBsR lLxdSXIdUJo'
    >>> remove_parentheses("((I fZNRUZUhLiRqn d)KoRBZNt)xq j(iXDJ(WHRexBUn Xy zFA cp(ejIWFCkYKXUxfYx)Lve)z (kdHEtWNwIeDACIPxG)m mkihWEg)E(HMDZiRM(zye itdvDTarWOZUlZGmX)YFnvWTUoTTmTjFc)JVeZcMa ()Chgh LDPRmcnyKOgfHhP(ZrzoB(mDw(EMzqj)BgSPnIHQe(qvlu RbFsLuAKnWT)(H PtRJYnNLOpJJSBGz uVXU)bIZCJv)TDrE)Vil((IpZ()LKdp VwxpSSRIGf)eH)d(vHcqUhfQf)(eybnPiggHlJiSS)iYhkww")
    'xq jEJVeZcMa Chgh LDPRmcnyKOgfHhPVildiYhkww'
    >>> remove_parentheses("MKTnoXuzvF(s Mk)ffy wJS pnTStMQpfgjuNJJCD ovPGMjtaLCCp iOvUFp(njtnpUS ZCwmEejTNFZCIM)Uk(VWfsC)ckkEMqzciF ZClBU(GEWdoCwjlayRBDwpDgC k)dQbiVttctXtFSuzSgCvKHIUIQoLpzfqOWwstlNL(JWhWWK HdSAFSMP)GeSXzoSEIScEl xLuStECzTYRz SwrtxqF(RIGQuCAo QyWLCRlMO)(PNZlKCRgAEKIFyMXhxCLt owt)cIvDRxmQgdPGvfu(oTTPv UsoAsKDzBggZyrhJqCU)F(tckwpzc(xnpsSKWqGGFgmHiqMbqe)(DMihpGT)kGlE sREl EO)FTd(F(ZaRzntV JOtzLgUutmj(osQibQzdjeODosmsu)n)NWCAWIeYanUMYq( NI SFDH CxuUyXIdOrFdma)zYXvKvMGn)qqLWb(XUCVJKTHR)HLQsfCMeTkhHmgT(MZfexMNkwiVLGvX mTfxpL)esLDvAtIhqznW XIU ugOcL SbJroHxc(tVchMBlAlsr)lmQSPsywHZSUoQTDxA rx sODJoAxIG CqmoWqZVZQSZVbajWkex(SFQTWSeZgYdZWsTXv)XnMqe ycTSWCXAGzDHWgxPmXOBVSgbjjQZViSFKoiWnKb pyAJzgqAoBcwTw pfd j oxXOYeYBlagTQlb ArEGZzGKZhOcARbB(eemsJfSAlPCxQlzK(FFkGI ))RlorRvdZhzd(GbL AjimGRZBMllUkogy)WVFqwfXHSA(YFHlJ)M")
    'MKTnoXuzvFffy wJS pnTStMQpfgjuNJJCD ovPGMjtaLCCp iOvUFpUkckkEMqzciF ZClBUdQbiVttctXtFSuzSgCvKHIUIQoLpzfqOWwstlNLGeSXzoSEIScEl xLuStECzTYRz SwrtxqFcIvDRxmQgdPGvfuFFTdqqLWbHLQsfCMeTkhHmgTesLDvAtIhqznW XIU ugOcL SbJroHxclmQSPsywHZSUoQTDxA rx sODJoAxIG CqmoWqZVZQSZVbajWkexXnMqe ycTSWCXAGzDHWgxPmXOBVSgbjjQZViSFKoiWnKb pyAJzgqAoBcwTw pfd j oxXOYeYBlagTQlb ArEGZzGKZhOcARbBRlorRvdZhzdWVFqwfXHSAM'
    >>> remove_parentheses("1(1))23456)789")
    '123456789'
    >>> remove_parentheses("))12345()")
    '12345'
    >>> remove_parentheses(")678910(")
    '678910'
    """

    # Use re.finditer(), all occurrences of substring in string
    start_sub = "\("
    end_sub = "\)"
    start = [i.start() for i in re.finditer(start_sub, input_str)]
    end = [i.end() for i in re.finditer(end_sub, input_str)]

    s = start[0] # set index of first open parentheses
    e = end[0] # set index of first close parentheses
    sub_str = [] # find all substrings to remove

    for i in range(1, len(start)): # use start for complete ()

        if s < start[i] and start[i] >= e: # no nesting
            sub_str.append(input_str[s:e])
            s = start[i]
            e = end[i]
        elif s < start[i] and start[i] <= e: # with nesting
            e = end[i] # update end of nest until start of next ()
        else:
            s = start[i] # update start of next set of ()

    sub_str.append(input_str[s:e]) # remove only/final nested ()
    sub_str.append("(") # remove any remaining open parentheses
    sub_str.append(")") # remove any remaining close parentheses
    # Use sorted to remove any nested () before removing single
    # open or close parentheses
    result = input_str
    for j in sorted(sub_str, key=lambda x: len(x), reverse=True):
        result = result.replace(j, "")

    return result
