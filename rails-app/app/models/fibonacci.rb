class Fibonacci
  def self.fibonacci(n)
    if (n < 2) 
      return 2
    else
      return fibonacci(n-1) + fibonacci(n-2)
    end
  end
end