def caesar_decipher(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 2 if key == 25 else 5
            shifted_char = chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 - shift) % 26) + 97)
            decrypted_text += shifted_char
            key = 2 if key == 25 else 25
        else:
            decrypted_text += char
    return decrypted_text

def main():
    text = """Vmg Yjjqwa th yjj Ofvwkc wsxjkqu f etphguvzcq nfpiuhcug bjjtj tjcqkya gnztx ynvm kqnzunqs, ymgwg yjj hfdwkh qk gckxvjphg nu bqags hwqr nnpju th hqig fpi dnpftd fninvx. Ky kx c ujnntutrmkhcq nfddtnpyj yjfv hjfnqgsiju yjj xjtd gxujphg th bjfv nv rgfpx vt rjthgnxj, vt wsfjtxvfpi, csf yq gg.
Np yjnu iklkycq vfrjuytd, vmg Rcytnz jojtlgx cx c hqsuytzey—c xkrwqcygi tjcqkya rgykhwqqzuqa htfhygi vt fjejkag yjj ujpxgx csf jpxpftj vmg rksf. Bkyjnp nvx etpkksgx, jzofpx 
cwg gwy wsynvyksi ucwvnenrfpyu, yjjkw etpxenqzusgxu ygyjjtjf yq f etnqghvnxj kqnzunqs, ymkqg yjjkw dtfngx nng iqwofpy ks vmg wgfnr qk vmg wgfn.
Dgy, djatpi vmg agnn th yjj Ofvwkc nngx c igjrjt ytzvm—c ytzvm qguhwwgi dd nfajtx qk fjejryktp fpi qghzuhcyktp. Nv nu yjj tjcqkecyktp yjfv wgfnnvd kyujnk kx dzv f etpxvwwhv, f rwqiwhv th ugwejryktp fpi ksvjtutjvfvnqs, umcugi dd vmg npygwrqcd qk onpi csf rcyvjt.
Fu yjj vmgttd wshtniu, nv gghmtpx wx vt szgxvnqs vmg scywwg th jznuygsej, vt rwqgg yjj dtwsfftngx qk etpxenqzusgxu, fpi vt etpkttpy vmg uqxundnnnvd vmcy qzt wgfnnvd ofa gg sqyjnpl ottj vmcs cs gqcgqwcyg nnqwxktp. Nv hjfnqgsiju zu yq qqtm ggdqsf yjj etpkksgx qk qzt ugwejkagi tjcqkya fpi vt iqkrrxg yjj kshnpnvj rtuxkgkqkykju yjfv qkj djatpi.     
Dzv yjj Vmgttd qk vmg Rcytnz nu rqwg yjfp rgwg xrjeznfvnqs; ky kx c wgknjeyktp th tww fjgugxv kgftx csf igxkwgx, qzt dgftsksi kqw vwwyj np f yttqf th ighguvnqs csf zphgwvfksvd. Ky ksxnvju zu yq jogtfej vmg zppptys, vt xjpywwg npyq yjj fjryjx qk vmg zppptys, csf yq xgjm fpxyjtx vt vmg kwsffojpycq szgxvnqsu yjfv mcag unfizgi jzofpnvd unphg ykrg norgrqwkfn.
Np yjj gsf, yjj Vmgttd qk vmg Rcytnz nu f ltwwpja—f ltwwpja npyq yjj wsmsqbp, npyq yjj fjryjx qk etpxenqzusgxu, fpi ksvt vmg agwa mgfty qk gckxvjphg nvxgqh. Nv nu f szgxv kqw vwwyj, kqw wsfjtxvfpiksi, fpi htt jpqkljygsojpy ks c bqwni umttwigi ks oduygwa fpi kqnzunqs.
Vmg Yjjqwa th yjj Ofvwkc wsxjkqu f etphguvzcq nfpiuhcug bjjtj tjcqkya gnztx ynvm kqnzunqs, ymgwg yjj hfdwkh qk gckxvjphg nu bqags hwqr nnpju th hqig fpi dnpftd fninvx. Ky kx c ujnntutrmkhcq nfddtnpyj yjfv hjfnqgsiju yjj xjtd gxujphg th bjfv nv rgfpx vt rjthgnxj, vt wsfjtxvfpi, csf yq gg.
Np yjnu iklkycq vfrjuytd, vmg Rcytnz jojtlgx cx c hqsuytzey—c xkrwqcygi tjcqkya rgykhwqqzuqa htfhygi vt fjejkag yjj ujpxgx csf jpxpftj vmg rksf. Bkyjnp nvx etpkksgx, jzofpx 
cwg gwy wsynvyksi ucwvnenrfpyu, yjjkw etpxenqzusgxu ygyjjtjf yq f etnqghvnxj kqnzunqs, ymkqg yjjkw dtfngx nng iqwofpy ks vmg wgfnr qk vmg wgfn.
Dgy, djatpi vmg agnn th yjj Ofvwkc nngx c igjrjt ytzvm—c ytzvm qguhwwgi dd nfajtx qk fjejryktp fpi qghzuhcyktp. Nv nu yjj tjcqkecyktp yjfv wgfnnvd kyujnk kx dzv f etpxvwwhv, f rwqiwhv th ugwejryktp fpi ksvjtutjvfvnqs, umcugi dd vmg npygwrqcd qk onpi csf rcyvjt.
Fu yjj vmgttd wshtniu, nv gghmtpx wx vt szgxvnqs vmg scywwg th jznuygsej, vt rwqgg yjj dtwsfftngx qk etpxenqzusgxu, fpi vt etpkttpy vmg uqxundnnnvd vmcy qzt wgfnnvd ofa gg sqyjnpl ottj vmcs cs gqcgqwcyg nnqwxktp. Nv hjfnqgsiju zu yq qqtm ggdqsf yjj etpkksgx qk qzt ugwejkagi tjcqkya fpi vt iqkrrxg yjj kshnpnvj rtuxkgkqkykju yjfv qkj djatpi.     
Dzv yjj Vmgttd qk vmg Rcytnz nu rqwg yjfp rgwg xrjeznfvnqs; ky kx c wgknjeyktp th tww fjgugxv kgftx csf igxkwgx, qzt dgftsksi kqw vwwyj np f yttqf th ighguvnqs csf zphgwvfksvd. Ky ksxnvju zu yq jogtfej vmg zppptys, vt xjpywwg npyq yjj fjryjx qk vmg zppptys, csf yq xgjm fpxyjtx vt vmg kwsffojpycq szgxvnqsu yjfv mcag unfizgi jzofpnvd unphg ykrg norgrqwkfn.
Np yjj gsf, yjj Vmgttd qk vmg Rcytnz nu f ltwwpja—f ltwwpja npyq yjj wsmsqbp, npyq yjj fjryjx qk etpxenqzusgxu, fpi ksvt vmg agwa mgfty qk gckxvjphg nvxgqh. Nv nu f szgxv kqw vwwyj, kqw wsfjtxvfpiksi, fpi htt jpqkljygsojpy ks c bqwni umttwigi ks oduygwa fpi kqnzunqs."""
    decrypted_text = caesar_decipher(text, 25) # assuming the key is 25 as given in the example
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
