class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        
        combined = []
        
        for i in range(len(val)):
            combined.append((val[i], wt[i], val[i]/wt[i]))
            
        combined.sort(key = lambda x: (x[2], x[1], x[0]), reverse=True)
        total_price = 0
        
        for i in range(len(combined)):
            value, weight, valueperweight = combined[i]
            
            if weight <= capacity:
                total_price += value
                capacity -= weight
            else:
                total_price += capacity * valueperweight
                break
            
        return total_price