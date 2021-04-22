var minimumTotal = function(triangle) 
{
    var row = triangle.length
    var col = triangle[row - 1].length
    var memo = {}
    
    function minVal(r = 0, c = 0)
    {   
        var key = r.toString() + ',' + c.toString()
        if (key in memo)
        {
          return memo[key]   
        }
        if (r === row - 1)
            
        {  
            memo[key] = triangle[r][c]
            return memo[key]
        }
        else
            {
                memo[key] = triangle[r][c] + Math.min(minVal(r + 1, c), minVal(r + 1, c+ 1))
                return memo[key]
            }
    }
        
    return minVal()
    
};