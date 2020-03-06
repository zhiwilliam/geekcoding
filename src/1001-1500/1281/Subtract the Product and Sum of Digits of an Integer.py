# From fish117


        
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        produc_sum = 1
        sum_digit = 0
        while n != 0:
            t = n % 10
            n = n // 10
            produc_sum = produc_sum * t
            sum_digit += t
        return produc_sum - sum_digit
    
    product_sum=1
    sum_digit=0
    while n!=0:
        t=n%10
        n=n//10
        product_sum=product_sum*t
        sum_digit+=t
        return product_sum-sum_digit
