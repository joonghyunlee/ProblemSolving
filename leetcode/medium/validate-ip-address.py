class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def leadingZerosOf(part):
            cnt = 0
            for c in part[:-1]:
                if c != '0':
                    break
                cnt += 1
            return cnt

        def convertAndValidate(part, base = 10):
            if not part:
                return False
                
            num = 0
            for c in part:
                if (base == 10 and c in '0123456789') or \
                    (base == 16 and c.lower() in '0123456789abcdef'):
                    num *= base
                    num += int(c, base)
                else:
                    return False
                
            maxValue = 0xFFFF if base == 16 else 255
            if num < 0 or num > maxValue:
                return False
                
            return True
            
        def valid(parts, base):
            for part in parts:
                if not convertAndValidate(part, base):
                    return False
                zeros = leadingZerosOf(part)
                if base == 10 and zeros > 0:
                    return False
                elif base == 16 and len(part) > 4 and zeros > 0:
                    return False
                    
            return True
            
        tokens = IP.split('.')
        if len(tokens) == 4 and valid(tokens, 10):
            return "IPv4"
        tokens = IP.split(':')
        if len(tokens) == 8 and valid(tokens, 16):
            return "IPv6"
        return "Neither"
        
        
if __name__ == '__main__':
    s = Solution()
    r = s.validIPAddress('172,16,254,1')
    print(r)
    r = s.validIPAddress('172.16.254.1')
    print(r)
    r = s.validIPAddress('172.16.254.01')
    print(r)
    r = s.validIPAddress('256.256.256.256')
    print(r)
    r = s.validIPAddress('00.0.0.0')
    print(r)
    r = s.validIPAddress('0.0.0.-0')
    print(r)
    r = s.validIPAddress('1.0.1.')
    print(r)
    r = s.validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334')
    print(r)
    r = s.validIPAddress('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    print(r)
    r = s.validIPAddress('2001:0db8:85a3::8A2E:0370:7334')
    print(r)
    r = s.validIPAddress('02001:0db8:85a3:0000:0000:8a2e:0370:7334')
    print(r)
    