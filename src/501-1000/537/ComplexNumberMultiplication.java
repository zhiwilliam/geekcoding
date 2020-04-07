class Solution {
    public String complexNumberMultiply(String a, String b) {
        int[] factorA = getRealAndComplexFactor(a);
        int[] factorB = getRealAndComplexFactor(b);
        int real = factorA[0] * factorB[0] - factorA[1] * factorB[1];
        int complex = factorA[0] * factorB[1] + factorA[1] * factorB[0];
        return String.valueOf(real) + "+" + String.valueOf(complex) + "i";
    }

    private int[] getRealAndComplexFactor(String str) {

        String[] array = str.split("\\+");
        int real = Integer.parseInt(array[0]);
        int com = Integer.parseInt(array[1].substring(0, array[1].length() - 1));
        return new int[]{real, com};
    }
}