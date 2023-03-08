import java.util.Arrays;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    private static final int ONE = 1 << 7, TWO = ONE + (1 << 6);
    public boolean validUtf8(int[] data) {
        int n = data.length;
        int index = 0;
        while (index < n) {
            int bytes = get_bytes(data[index]);
            if (bytes == -1 || (bytes + index > n)) return false;
            for (int i=1; i<bytes; i++){
                if (!isValid(data[index+i])) return false;
            }
            index += bytes;
        }
        return true;
    }

    public boolean isValid(int datax){
        return (datax & TWO) == ONE;
    }

    public int get_bytes(int data0){
        if ((data0 & ONE) == 0) return 1;
        int bytes = 0;
        while ((data0 & ONE) != 0) {
            bytes ++;
            if (bytes>4) return -1;
            data0 <<= 1;
        }
        return bytes >=2 ? bytes : -1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
