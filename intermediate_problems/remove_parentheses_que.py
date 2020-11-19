# Automate Everything from @codecaviar
# Level: Intermediate
# Updated: 2020-11-18

# Fill each function stub according to the docstring
# Run tests with this command: "python3 -m doctest [filename].py -v"

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

    # Optional: use try...except block to handle error conditions

    pass # null operation, placeholder when a statement is required
